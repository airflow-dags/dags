from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "user30-0223-10-deploy-model-0223101521",
}

dag = DAG(
    "user30-0223-10-deploy-model-0223101521",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using user30-0223-10-deploy-model.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_9717753b_c990_4c21_88ba_4a46474a32e4 = NotebookOp(
    name="ocp_deploy",
    namespace="ml-workshop",
    task_id="ocp_deploy",
    notebook="ml-workshop-improved/airflow/deploy_model/ocp/ocp_deploy.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="user30-0223-10-deploy-model-0223101521",
    cos_dependencies_archive="ocp_deploy-9717753b-c990-4c21-88ba-4a46474a32e4.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.8",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "user30-model",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)

notebook_op_9717753b_c990_4c21_88ba_4a46474a32e4.image_pull_policy = "IfNotPresent"
