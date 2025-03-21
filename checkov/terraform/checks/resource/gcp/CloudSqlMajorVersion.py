from checkov.terraform.checks.resource.base_resource_value_check import BaseResourceValueCheck
from checkov.common.models.enums import CheckCategories


class CloudSqlMajorVersion(BaseResourceValueCheck):
    def __init__(self):
        name = "Ensure SQL database is using latest Major version"
        id = "CKV_GCP_79"
        supported_resources = ['google_sql_database_instance']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self):
        return 'database_version'

    def get_expected_values(self):
        return ["POSTGRES_17", "MYSQL_8_0", "MYSQL_8_4", "SQLSERVER_2022_STANDARD", "SQLSERVER_2022_WEB",
                "SQLSERVER_2022_ENTERPRISE", "SQLSERVER_2022_EXPRESS"]


check = CloudSqlMajorVersion()
