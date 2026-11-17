from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import csv


def load_atms():
    with open('/opt/airflow/dags/atm_cash.csv', newline='') as file:
        records = list(csv.DictReader(file))

    print('ATM records loaded:', len(records))
    return records


def identify_low_cash(ti):
    records = ti.xcom_pull(task_ids='load_atms')

    low_cash_atms = []

    for atm in records:
        cash = int(atm['cash_available'])
        demand = int(atm['daily_demand'])

        if cash < demand:
            low_cash_atms.append(atm['atm_id'])

    print('Low cash ATMs:', low_cash_atms)
    return low_cash_atms


def calculate_total_cash(ti):
    records = ti.xcom_pull(task_ids='load_atms')

    total_cash = sum(
        int(atm['cash_available']) for atm in records
    )

    print('Total available cash:', total_cash)
    return total_cash


def generate_report(ti):
    records = ti.xcom_pull(task_ids='load_atms')
    low_cash_atms = ti.xcom_pull(task_ids='identify_low_cash')
    total_cash = ti.xcom_pull(task_ids='calculate_total_cash')

    print('========== ATM CASH REPORT ==========')
    print('Total number of ATMs:', len(records))
    print('Low cash ATM IDs:', low_cash_atms)
    print('Total available cash:', total_cash)
    print('=====================================')


with DAG(
    dag_id='atm_cash_pipeline',
    start_date=datetime(2026, 11, 17),
    schedule=None,
    catchup=False
) as dag:

    load_atms_task = PythonOperator(
        task_id='load_atms',
        python_callable=load_atms
    )

    identify_low_cash_task = PythonOperator(
        task_id='identify_low_cash',
        python_callable=identify_low_cash
    )

    calculate_total_cash_task = PythonOperator(
        task_id='calculate_total_cash',
        python_callable=calculate_total_cash
    )

    generate_report_task = PythonOperator(
        task_id='generate_report',
        python_callable=generate_report
    )

    load_atms_task >> [
        identify_low_cash_task,
        calculate_total_cash_task
    ] >> generate_report_task
