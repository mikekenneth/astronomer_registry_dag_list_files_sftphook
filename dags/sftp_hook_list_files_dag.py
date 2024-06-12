"""
## List files in remote SFTP Server using SFTPHook

This DAG shows how to get the **list of files** in a remote directory using the `SFTPHook`.
To be able to run this DAG you need to install the relevant provider package
for your SFTP provider and define an Airflow SFTP/SSH connection to it.

- `apache-airflow-providers-sftp>=4.8.0`

"""

from pendulum import datetime
from airflow.decorators import dag, task
from airflow.providers.sftp.hooks.sftp import SFTPHook

SFTP_CONN_ID = "sftp_conn_id"
REMOTE_DIRECTORY = "/"


@dag(
    schedule_interval="0 0 * * *",
    start_date=datetime(2024, 6, 1),
    catchup=False,
    doc_md=__doc__,
)
def sftp_list_remote_directory_files():
    @task
    def get_files_in_directory():
        sftp_hook = SFTPHook(ssh_conn_id=SFTP_CONN_ID)
        files_list = sftp_hook.list_directory(path=REMOTE_DIRECTORY)
        print(f"Remote Directory files: {files_list}")
        return files_list

    remote_files_list = get_files_in_directory(remote_path="/")


sftp_list_remote_directory_files()
