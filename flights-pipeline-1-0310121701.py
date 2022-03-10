from airflow import DAG

from airflow_notebook.pipeline import NotebookOp
from airflow.utils.dates import days_ago

# Setup default args with older date to automatically trigger when uploaded
args = {
    "project_id": "flights-pipeline-1-0310121701",
}

dag = DAG(
    "flights-pipeline-1-0310121701",
    default_args=args,
    schedule_interval="@once",
    start_date=days_ago(1),
    description="Created with Elyra 2.2.4 pipeline editor using flights-pipeline-1.pipeline.",
    is_paused_upon_creation=False,
)


notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d = NotebookOp(
    name="start_spark_cluster",
    namespace="ml-workshop",
    task_id="start_spark_cluster",
    notebook="Machine-Learning-on-Kubernetes/chapter9/pipeline-helpers/start-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="flights-pipeline-1-0310121701",
    cos_dependencies_archive="start-spark-cluster-d5009697-771e-4f71-bc20-e52d905c9f9d.tar.gz",
    pipeline_outputs=["spark-info.txt"],
    pipeline_inputs=[],
    image="quay.io/ml-on-k8s/airflow-python-runner:0.0.11",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
        "SPARK_CLUSTER": "ml-user-airflow-cluster",
        "WORKER_NODES": "2",
    },
    config_file="None",
    dag=dag,
)

notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d.image_pull_policy = "IfNotPresent"


notebook_op_5ad53c7e_c1a5_4dab_b766_cd6e3642891a = NotebookOp(
    name="merge_data",
    namespace="ml-workshop",
    task_id="merge_data",
    notebook="Machine-Learning-on-Kubernetes/chapter9/merge_data.ipynb",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="flights-pipeline-1-0310121701",
    cos_dependencies_archive="merge_data-5ad53c7e-c1a5-4dab-b766-cd6e3642891a.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info.txt"],
    image="quay.io/ml-on-k8s/elyra-spark:0.0.4",
    in_cluster=True,
    env_vars={
        "AWS_ACCESS_KEY_ID": "minio",
        "AWS_SECRET_ACCESS_KEY": "minio123",
        "ELYRA_ENABLE_PIPELINE_INFO": "True",
    },
    config_file="None",
    dag=dag,
)

notebook_op_5ad53c7e_c1a5_4dab_b766_cd6e3642891a.image_pull_policy = "IfNotPresent"

(
    notebook_op_5ad53c7e_c1a5_4dab_b766_cd6e3642891a
    << notebook_op_d5009697_771e_4f71_bc20_e52d905c9f9d
)


notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f = NotebookOp(
    name="stop_spark_cluster",
    namespace="ml-workshop",
    task_id="stop_spark_cluster",
    notebook="Machine-Learning-on-Kubernetes/chapter9/pipeline-helpers/stop-spark-cluster.py",
    cos_endpoint="http://minio-ml-workshop:9000",
    cos_bucket="airflow",
    cos_directory="flights-pipeline-1-0310121701",
    cos_dependencies_archive="stop-spark-cluster-b6d6a9d3-65b6-4ef6-9ce8-4d713bea5e2f.tar.gz",
    pipeline_outputs=[],
    pipeline_inputs=["spark-info.txt"],
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

notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f.image_pull_policy = "IfNotPresent"

(
    notebook_op_b6d6a9d3_65b6_4ef6_9ce8_4d713bea5e2f
    << notebook_op_5ad53c7e_c1a5_4dab_b766_cd6e3642891a
)
