from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "flights-model-0329061932",
}

dag = DAG(
    "flights-model-0329061932",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using flights-model.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_4b76ee22_35c2_4e98_b980_0fe294a10f98 = NotebookOp(
    name="build_push_image",
    namespace="ml-workshop",
    task_id="build_push_image",
    notebook="Machine-Learning-on-Kubernetes/chapter10/model_deploy_pipeline/model_build_push/build_push_image.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="flights-model-0329061932",
    cos_dependencies_archive="build_push_image-4b76ee22-35c2-4e98-b980-0fe294a10f98.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/kaniko-container-builder:1.0.0",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "flights-ontime",
        "MODEL_VERSION": "1",
        "CONTAINER_REGISTRY": "quay.io",
        "CONTAINER_REGISTRY_USER": "ml-on-k8s+model_container_builder",
        "CONTAINER_REGISTRY_PASSWORD": "SEEIL8M5A2G8LVTKMA4PIKN9GAELM24AJESY04EH29B0GP5FU10ROMVYY97UXKZR",
        "CONTAINER_DETAILS": "ml-on-k8s/container-model:2.0.0",
    },
    config_file="None",
    dag=dag,
)

notebook_op_4b76ee22_35c2_4e98_b980_0fe294a10f98.image_pull_policy = "Always"


notebook_op_a8a2be4d_dfd1_4a0a_9ce5_5477d6bf8b56 = NotebookOp(
    name="deploy_model",
    namespace="ml-workshop",
    task_id="deploy_model",
    notebook="Machine-Learning-on-Kubernetes/chapter10/model_deploy_pipeline/model_deploy/deploy_model.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="flights-model-0329061932",
    cos_dependencies_archive="deploy_model-a8a2be4d-dfd1-4a0a-9ce5-5477d6bf8b56.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "MODEL_NAME": "flights-ontime",
        "MODEL_VERSION": "1",
        "CONTAINER_DETAILS": "quay.io/ml-on-k8s/container-model:1.0.0",
        "CLUSTER_DOMAIN_NAME": "192.168.39.216.nio.io",
    },
    config_file="None",
    dag=dag,
)

notebook_op_a8a2be4d_dfd1_4a0a_9ce5_5477d6bf8b56.image_pull_policy = "IfNotPresent"

(
    notebook_op_a8a2be4d_dfd1_4a0a_9ce5_5477d6bf8b56
    << notebook_op_4b76ee22_35c2_4e98_b980_0fe294a10f98
)
