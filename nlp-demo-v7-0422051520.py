from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "nlp-demo-v7-0422051520",
}

dag = DAG(
    "nlp-demo-v7-0422051520",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using nlp-demo-v7.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_4464fe94_a958_4cb2_b8b8_b080f87ff679 = NotebookOp(
    name="ocp_deploy",
    namespace="ml-workshop",
    task_id="ocp_deploy",
    notebook="anz_ml_project/deploy/text_classification/ocp_deploy.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="nlp-demo-v7-0422051520",
    cos_dependencies_archive="ocp_deploy-4464fe94-a958-4cb2-b8b8-b080f87ff679.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.8",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "nlp",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_4464fe94_a958_4cb2_b8b8_b080f87ff679.image_pull_policy = "IfNotPresent"
