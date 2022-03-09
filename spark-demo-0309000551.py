from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "spark-demo-0309000551",
}

dag = DAG(
    "spark-demo-0309000551",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using spark-demo.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_c94ef0f1_83be_49aa_8c98_e34b70a3ade3 = NotebookOp(
    name="ml_workshop_improved_airflow_deploy_spark_jobs_spark_demo.py",
    namespace="ml-workshop",
    task_id="ml_workshop_improved_airflow_deploy_spark_jobs_spark_demo.py",
    notebook="ml-workshop-improved/airflow/deploy_spark_jobs/spark-demo.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="spark-demo-0309000551",
    cos_dependencies_archive="spark-demo-c94ef0f1-83be-49aa-8c98-e34b70a3ade3.tar.gz",
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

notebook_op_c94ef0f1_83be_49aa_8c98_e34b70a3ade3.image_pull_policy = "IfNotPresent"
