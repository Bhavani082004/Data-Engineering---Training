from datetime import datetime, timedelta

from airflow import DAG

from airflow.providers.standard.operators.python import (
    PythonOperator,
    BranchPythonOperator
)

from airflow.utils.trigger_rule import TriggerRule


def load_incident():

    incident = {
        "ticket_id": "INC-402",
        "service": "Email",
        "severity": "High",
        "reported_by": "Operations"
    }

    print("Incident loaded:", incident)

    return incident


def choose_response(**context):

    incident = context["ti"].xcom_pull(
        task_ids="load_incident"
    )

    severity = incident["severity"]

    print("Incident severity:", severity)

    if severity in ["High", "Critical"]:
        return "urgent_response"

    else:
        return "standard_response"


def urgent_response(**context):

    ti = context["ti"]

    print("Urgent response started")

    if ti.try_number == 1:
        print("Simulating temporary failure")
        raise Exception("Temporary failure. Retrying...")

    print("Urgent incident successfully escalated")


def standard_response():

    print("Standard service desk assignment")

    print("Incident assigned to normal support team")


def write_audit(**context):

    incident = context["ti"].xcom_pull(
        task_ids="load_incident"
    )

    print("Incident ID:", incident["ticket_id"])

    print("Incident processing completed")

    print("Audit record written successfully")


with DAG(
    dag_id="it_incident_routing",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    load_incident_task = PythonOperator(
        task_id="load_incident",
        python_callable=load_incident
    )

    choose_response_task = BranchPythonOperator(
        task_id="choose_response",
        python_callable=choose_response
    )

    urgent_response_task = PythonOperator(
        task_id="urgent_response",
        python_callable=urgent_response,
        retries=1,
        retry_delay=timedelta(seconds=10)
    )

    standard_response_task = PythonOperator(
        task_id="standard_response",
        python_callable=standard_response
    )

    write_audit_task = PythonOperator(
        task_id="write_audit",
        python_callable=write_audit,
        trigger_rule=TriggerRule.NONE_FAILED_MIN_ONE_SUCCESS
    )

    load_incident_task >> choose_response_task

    choose_response_task >> [
        urgent_response_task,
        standard_response_task
    ]

    [
        urgent_response_task,
        standard_response_task
    ] >> write_audit_task

