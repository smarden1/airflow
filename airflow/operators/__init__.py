'''
Imports operators dynamically while keeping the package API clean,
abstracting the underlying modules
'''
from airflow.utils import import_module_attrs as _import_module_attrs
from airflow.models import BaseOperator as _BaseOperator

_operators = {
    'bash_operator': ['BashOperator'],
    'python_operator': ['PythonOperator', 'BranchPythonOperator'],
    'hive_operator': ['HiveOperator'],
    'presto_check_operator': [
        'PrestoCheckOperator',
        'PrestoValueCheckOperator',
        'PrestoIntervalCheckOperator',
    ],
    'dummy_operator': ['DummyOperator'],
    'email_operator': ['EmailOperator'],
    'hive_to_samba_operator': ['Hive2SambaOperator'],
    'mysql_operator': ['MySqlOperator'],
    'sqlite_operator': ['SqliteOperator'],
    'mysql_to_hive': ['MySqlToHiveTransfer'],
    'postgres_operator': ['PostgresOperator'],
    'sensors': [
        'SqlSensor',
        'ExternalTaskSensor',
        'HivePartitionSensor',
        'S3KeySensor',
        'S3PrefixSensor',
        'HdfsSensor',
        'TimeSensor',
        'HttpSensor'
    ],
    'subdag_operator': ['SubDagOperator'],
    'hive_stats_operator': ['HiveStatsCollectionOperator'],
    's3_to_hive_operator': ['S3ToHiveTransfer'],
    'hive_to_mysql': ['HiveToMySqlTransfer'],
    's3_file_transform_operator': ['S3FileTransformOperator'],
    'http_operator': ['SimpleHttpOperator']
    }

_import_module_attrs(globals(), _operators)


def integrate_plugins():
    """Integrate plugins to the context"""
    from airflow.plugins_manager import operators as _operators
    for _operator in _operators:
        globals()[_operator.__name__] = _operator
