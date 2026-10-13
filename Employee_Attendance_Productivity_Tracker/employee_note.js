use("employee_tracker");

db.employee_notes.insertMany([
    {
        employee_id: 1,
        department: "IT",
        task_name: "Develop login page",
        feedback: "Completed the task successfully.",
        note: "Good collaboration with team members.",
        created_at: new Date()
    },
    {
        employee_id: 2,
        department: "HR",
        task_name: "Prepare HR report",
        feedback: "Report needs a few corrections.",
        note: "Review the report before submission.",
        created_at: new Date()
    },
    {
        employee_id: 3,
        department: "Finance",
        task_name: "Review financial data",
        feedback: "Completed the assigned analysis.",
        note: "Verify figures before final approval.",
        created_at: new Date()
    }
]);

db.employee_notes.createIndex({ employee_id: 1 });
db.employee_notes.createIndex({ department: 1 });

db.employee_notes.find();
db.employee_notes.getIndexes();
