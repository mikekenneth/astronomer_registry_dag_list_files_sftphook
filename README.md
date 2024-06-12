# Airflow: List files on a remote server using SFTPHook

This DAG shows how to get the **list of files** in a remote directory using the `SFTPHook`.
To be able to run this DAG you need to install the relevant provider package
for your SFTP provider and define an Airflow SFTP/SSH connection to it.

- `apache-airflow-providers-sftp>=4.8.0`

#### This was done using Airflow 2.8.0
