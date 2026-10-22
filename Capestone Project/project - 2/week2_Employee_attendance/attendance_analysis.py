import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

attendance_file = BASE_DIR / "attendance.csv"
tasks_file = BASE_DIR / "tasks.csv"

attendance = pd.read_csv(attendance_file)
tasks = pd.read_csv(tasks_file)

attendance.columns = attendance.columns.str.strip().str.lower()
tasks.columns = tasks.columns.str.strip().str.lower()

attendance["attendance_status"] = (
    attendance["attendance_status"].fillna("Unknown").astype(str).str.strip().str.title()
)
attendance["attendance_date"] = pd.to_datetime(attendance["attendance_date"], errors="coerce")
attendance["clock_in_dt"] = pd.to_datetime(
    attendance["attendance_date"].dt.strftime("%Y-%m-%d") + " " +
    attendance["clock_in"].fillna("").astype(str),
    errors="coerce"
)
attendance["clock_out_dt"] = pd.to_datetime(
    attendance["attendance_date"].dt.strftime("%Y-%m-%d") + " " +
    attendance["clock_out"].fillna("").astype(str),
    errors="coerce"
)

attendance["break_minutes"] = pd.to_numeric(attendance["break_minutes"], errors="coerce").fillna(0)
attendance.loc[attendance["break_minutes"] < 0, "break_minutes"] = 0

valid_times = (
    attendance["clock_in_dt"].notna()
    & attendance["clock_out_dt"].notna()
    & (attendance["clock_out_dt"] >= attendance["clock_in_dt"])
    & (attendance["attendance_status"] == "Present")
)

elapsed_hours = (
    attendance["clock_out_dt"] - attendance["clock_in_dt"]
).dt.total_seconds() / 3600

attendance["work_hours"] = np.where(
    valid_times,
    np.maximum(elapsed_hours - attendance["break_minutes"] / 60, 0),
    0
)
attendance["break_hours"] = attendance["break_minutes"] / 60
attendance["attendance_status"] = np.where(
    attendance["attendance_status"].isin(["Present", "Absent", "Leave"]),
    attendance["attendance_status"],
    np.where(valid_times, "Present", "Absent")
)

tasks["report_date"] = pd.to_datetime(tasks["report_date"], errors="coerce")
tasks["tasks_assigned"] = pd.to_numeric(tasks["tasks_assigned"], errors="coerce")
tasks["tasks_completed"] = pd.to_numeric(tasks["tasks_completed"], errors="coerce")
tasks["tasks_assigned"] = tasks["tasks_assigned"].fillna(0).clip(lower=0)
tasks["tasks_completed"] = tasks["tasks_completed"].fillna(0).clip(lower=0)
tasks["tasks_completed"] = np.minimum(tasks["tasks_completed"], tasks["tasks_assigned"])

attendance.to_csv(BASE_DIR / "cleaned_attendance.csv", index=False)

task_summary = tasks.groupby(
    ["employee_id", "employee_name", "department"], as_index=False
).agg(
    total_tasks_assigned=("tasks_assigned", "sum"),
    total_tasks_completed=("tasks_completed", "sum")
)

attendance_summary = attendance.groupby(
    ["employee_id", "employee_name", "department"], as_index=False
).agg(
    days_recorded=("attendance_status", "count"),
    days_present=("attendance_status", lambda s: (s == "Present").sum()),
    days_absent=("attendance_status", lambda s: (s == "Absent").sum()),
    total_work_hours=("work_hours", "sum"),
    average_work_hours=("work_hours", "mean"),
    total_break_hours=("break_hours", "sum")
)

report = attendance_summary.merge(
    task_summary,
    on=["employee_id", "employee_name", "department"],
    how="outer"
)

numeric_columns = [
    "days_recorded", "days_present", "days_absent", "total_work_hours",
    "average_work_hours", "total_break_hours", "total_tasks_assigned",
    "total_tasks_completed"
]
for column in numeric_columns:
    report[column] = pd.to_numeric(report[column], errors="coerce").fillna(0)

report["task_completion_rate_pct"] = np.where(
    report["total_tasks_assigned"] > 0,
    report["total_tasks_completed"] / report["total_tasks_assigned"] * 100,
    0
)
report["productivity_score"] = np.where(
    report["total_work_hours"] > 0,
    report["total_tasks_completed"] / report["total_work_hours"],
    0
)
report["productivity_score"] = report["productivity_score"].round(2)
report["task_completion_rate_pct"] = report["task_completion_rate_pct"].round(2)
report["total_work_hours"] = report["total_work_hours"].round(2)
report["average_work_hours"] = report["average_work_hours"].round(2)
report["total_break_hours"] = report["total_break_hours"].round(2)

report["performance_category"] = np.select(
    [
        report["task_completion_rate_pct"] >= 80,
        report["task_completion_rate_pct"] >= 50
    ],
    ["High", "Moderate"],
    default="Needs Review"
)

report = report.sort_values(
    ["productivity_score", "task_completion_rate_pct"],
    ascending=[False, False]
)
report.to_csv(BASE_DIR / "employee_performance_report.csv", index=False)

department_report = report.groupby("department", as_index=False).agg(
    employees=("employee_id", "nunique"),
    total_days_absent=("days_absent", "sum"),
    total_work_hours=("total_work_hours", "sum"),
    tasks_assigned=("total_tasks_assigned", "sum"),
    tasks_completed=("total_tasks_completed", "sum"),
    average_productivity_score=("productivity_score", "mean")
)
department_report["task_completion_rate_pct"] = np.where(
    department_report["tasks_assigned"] > 0,
    department_report["tasks_completed"] / department_report["tasks_assigned"] * 100,
    0
)
department_report["average_productivity_score"] = department_report["average_productivity_score"].round(2)
department_report["task_completion_rate_pct"] = department_report["task_completion_rate_pct"].round(2)
department_report.to_csv(BASE_DIR / "productivity_report.csv", index=False)

print("Week 2 analysis completed successfully.")
print("\nTop performers:")
print(report[["employee_name", "department", "productivity_score", "task_completion_rate_pct"]].head(3).to_string(index=False))
print("\nFrequent absentees (2 or more absent days):")
absentees = report.loc[report["days_absent"] >= 2, ["employee_name", "department", "days_absent"]]
if absentees.empty:
    print("No employees meet this threshold.")
else:
    print(absentees.to_string(index=False))
print("\nCreated output files:")
print("cleaned_attendance.csv")
print("productivity_report.csv")
print("employee_performance_report.csv")
