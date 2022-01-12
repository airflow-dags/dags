from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "test-deploy-fm-v4-0112015403",
}

dag = DAG(
    "test-deploy-fm-v4-0112015403",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using test-deploy-fm-v4.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_1c890a68_7ca6_477d_8d88_56acbaee7a17 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/chapter7/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="test-deploy-fm-v4-0112015403",
    cos_dependencies_archive="deploy_model-1c890a68-7ca6-477d-8d88-56acbaee7a17.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-aml-workshop/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "CONTAINER_REGISTRY": "quay.io",
        "CONTAINER_DETAILS": "ml-on-k8s/container-model:1.0.0",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
    },
    config_file="None",
    dag=dag,
)
