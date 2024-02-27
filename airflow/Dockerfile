FROM apache/airflow:2.6.3-python3.9

USER root

COPY --chown=airflow:root dags/ /opt/airflow/dags
USER airflow

