from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "testsdfsdfs-0112030734",
}

dag = DAG(
    "testsdfsdfs-0112030734",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using testsdfsdfs.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_05b9ddfb_efc7_4c37_843b_8bcdc8f6e0a9 = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/chapter7/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="testsdfsdfs-0112030734",
    cos_dependencies_archive="build_push_image-05b9ddfb-efc7-4c37-843b-8bcdc8f6e0a9.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "CONTAINER_REGISTRY": "quay.io",
        "CONTAINER_DETAILS": "ml-on-k8s/container-model:1.0.0",
        "MODEL_NAME": "mlflowdemo",
        "MODEL_VERSION": "1",
        "CONTAINER_REGISTRY_USER": "ml-on-k8s+model_container_builder",
        "CONTAINER_REGISTRY_PASSWORD": "SEEIL8M5A2G8LVTKMA4PIKN9GAELM24AJESY04EH29B0GP5FU10ROMVYY97UXKZR",
    },
    config_file="None",
    dag=dag,
)

notebook_op_05b9ddfb_efc7_4c37_843b_8bcdc8f6e0a9.image_pull_policy = "Always"
