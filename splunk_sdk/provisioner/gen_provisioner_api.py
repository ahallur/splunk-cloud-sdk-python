# coding: utf-8

# Copyright © 2019 Splunk, Inc.
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

############# This file is auto-generated.  Do not edit! #############

"""
    SDC Service: Provisioner

    With the Provisioner Service, you can provision your tenant and manage it

    OpenAPI spec version: v1beta1.1
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.provisioner.gen_models import CreateProvisionJobBody
from splunk_sdk.provisioner.gen_models import Error
from splunk_sdk.provisioner.gen_models import ProvisionJobInfo
from splunk_sdk.provisioner.gen_models import TenantInfo


class Provisioner(BaseService):
    """
    Provisioner
    Version: v1beta1.1
    With the Provisioner Service, you can provision your tenant and manage it
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def create_provision_job(self, create_provision_job_body: CreateProvisionJobBody) -> ProvisionJobInfo:
        """
        Creates a new job that provisions a new tenant and subscribes apps to the tenant
        """
        query_params = {}

        path_params = {
        }

        path = Template("/system/provisioner/v1beta1/jobs/tenants/provision").substitute(path_params)
        url = self.base_client.build_url(path)
        data = create_provision_job_body.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, ProvisionJobInfo)

    def get_provision_job(self, job_id: str) -> ProvisionJobInfo:
        """
        Gets details of a specific provision job
        """
        query_params = {}

        path_params = {
            "jobId": job_id,
        }

        path = Template("/system/provisioner/v1beta1/jobs/tenants/provision/${jobId}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, ProvisionJobInfo)

    def get_tenant(self, tenant_name: str) -> TenantInfo:
        """
        Gets a specific tenant
        """
        query_params = {}

        path_params = {
            "tenantName": tenant_name,
        }

        path = Template("/system/provisioner/v1beta1/tenants/${tenantName}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, TenantInfo)

    def list_provision_jobs(self) -> List[ProvisionJobInfo]:
        """
        Lists all provision jobs created by the user
        """
        query_params = {}

        path_params = {
        }

        path = Template("/system/provisioner/v1beta1/jobs/tenants/provision").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, ProvisionJobInfo)

    def list_tenants(self) -> List[TenantInfo]:
        """
        Lists all tenants that the user can read
        """
        query_params = {}

        path_params = {
        }

        path = Template("/system/provisioner/v1beta1/tenants").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, TenantInfo)

