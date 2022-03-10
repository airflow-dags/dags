from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "flights-0310134728",
}

dag = DAG(
    "flights-0310134728",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using flights.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_5d7f9e05_9f56_4669_a868_88afec62ccdb = NotebookOp(
    name="Machine_Learning_on_Kubernetes_chapter9_flights.py",
    namespace="ml-workshop",
    task_id="Machine_Learning_on_Kubernetes_chapter9_flights.py",
    notebook="Machine-Learning-on-Kubernetes/chapter9/flights.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="flights-0310134728",
    cos_dependencies_archive="flights-5d7f9e05-9f56-4669-a868-88afec62ccdb.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_5d7f9e05_9f56_4669_a868_88afec62ccdb.image_pull_policy = "IfNotPresent"
