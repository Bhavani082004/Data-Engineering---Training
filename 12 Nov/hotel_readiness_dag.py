from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def load_rooms():
    rooms = [
        {"room": 101, "status": "Ready", "cleaning_min": 0},
        {"room": 102, "status": "Cleaning", "cleaning_min": 25},
        {"room": 103, "status": "Ready", "cleaning_min": 0},
        {"room": 104, "status": "Cleaning", "cleaning_min": 40},
        {"room": 105, "status": "Cleaning", "cleaning_min": 30}
    ]

    return rooms


def find_rooms_to_clean(**kwargs):
    ti = kwargs['ti']

    rooms = ti.xcom_pull(task_ids='load_rooms')

    cleaning_rooms = [
        room['room'] for room in rooms
        if room['status'] == 'Cleaning'
    ]

    return cleaning_rooms


def calculate_cleaning_minutes(**kwargs):
    ti = kwargs['ti']

    rooms = ti.xcom_pull(task_ids='load_rooms')

    total_minutes = sum(
        room['cleaning_min'] for room in rooms
        if room['status'] == 'Cleaning'
    )

    return total_minutes


def generate_housekeeping_report(**kwargs):
    ti = kwargs['ti']

    cleaning_rooms = ti.xcom_pull(
        task_ids='find_rooms_to_clean'
    )

    total_minutes = ti.xcom_pull(
        task_ids='calculate_cleaning_minutes'
    )

    print("HOTEL HOUSEKEEPING REPORT")
    print("-------------------------")
    print("Rooms needing cleaning:", cleaning_rooms)
    print("Total cleaning time:", total_minutes, "minutes")


with DAG(
    dag_id='hotel_readiness_dag',
    start_date=datetime(2026, 11, 12),
    schedule=None,
    catchup=False
) as dag:

    task1 = PythonOperator(
        task_id='load_rooms',
        python_callable=load_rooms
    )

    task2 = PythonOperator(
        task_id='find_rooms_to_clean',
        python_callable=find_rooms_to_clean
    )

    task3 = PythonOperator(
        task_id='calculate_cleaning_minutes',
        python_callable=calculate_cleaning_minutes
    )

    task4 = PythonOperator(
        task_id='generate_housekeeping_report',
        python_callable=generate_housekeeping_report
    )

    task1 >> [task2, task3]
    [task2, task3] >> task4

