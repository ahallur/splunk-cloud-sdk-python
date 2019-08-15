# coding: utf-8

# Copyright © 2019 Splunk, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"): you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
# [http://www.apache.org/licenses/LICENSE-2.0]
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

############# This file is auto-generated.  Do not edit! #############

"""
    SDC Service: Action Service

    With the Splunk Cloud Action service, you can receive incoming trigger events and use pre-defined action templates to turn these events into meaningful actions. 

    OpenAPI spec version: v1beta2.7
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.action.gen_models import Action
from splunk_sdk.action.gen_models import ActionMutable
from splunk_sdk.action.gen_models import ActionResult
from splunk_sdk.action.gen_models import ActionResultEmailDetail
from splunk_sdk.action.gen_models import PublicWebhookKey
from splunk_sdk.action.gen_models import ServiceError
from splunk_sdk.action.gen_models import TriggerEvent


class ActionService(BaseService):
    """
    Action Service
    Version: v1beta2.7
    With the Splunk Cloud Action service, you can receive incoming trigger events and use pre-defined action templates to turn these events into meaningful actions. 
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def create_action(self, action: Action) -> Action:
        """
        Creates an action template.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/action/v1beta2/actions").substitute(path_params)
        url = self.base_client.build_url(path)
        data = action.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, Action)

    def delete_action(self, action_name: str) -> SSCVoidModel:
        """
        Removes an action template.
        """
        query_params = {}

        path_params = {
            "action_name": action_name,
        }

        path = Template("/action/v1beta2/actions/${action_name}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, **query_params)
        return handle_response(response, )

    def get_action(self, action_name: str) -> Action:
        """
        Returns a specific action template.
        """
        query_params = {}

        path_params = {
            "action_name": action_name,
        }

        path = Template("/action/v1beta2/actions/${action_name}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, Action)

    def get_action_status(self, action_name: str, status_id: str) -> ActionResult:
        """
        Returns the status of a triggered action.
        """
        query_params = {}

        path_params = {
            "action_name": action_name,
            "status_id": status_id,
        }

        path = Template("/action/v1beta2/actions/${action_name}/status/${status_id}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, ActionResult)

    def get_action_status_details(self, action_name: str, status_id: str) -> List[ActionResultEmailDetail]:
        """
        Returns the status details of the triggered email action.
        """
        query_params = {}

        path_params = {
            "action_name": action_name,
            "status_id": status_id,
        }

        path = Template("/action/v1beta2/actions/${action_name}/status/${status_id}/details").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, ActionResultEmailDetail)

    def get_public_webhook_keys(self) -> List[PublicWebhookKey]:
        """
        Returns an array of one or two webhook keys. The first key is active. The second key, if present, is expired.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/system/action/v1beta2/webhook/keys").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, PublicWebhookKey)

    def list_actions(self) -> List[Action]:
        """
        Returns the list of action templates.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/action/v1beta2/actions").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, Action)

    def trigger_action(self, action_name: str, trigger_event: TriggerEvent) -> SSCVoidModel:
        """
        Triggers an action.
        """
        query_params = {}

        path_params = {
            "action_name": action_name,
        }

        path = Template("/action/v1beta2/actions/${action_name}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = trigger_event.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, )

    def update_action(self, action_name: str, action_mutable: ActionMutable) -> Action:
        """
        Modifies an action template.
        """
        query_params = {}

        path_params = {
            "action_name": action_name,
        }

        path = Template("/action/v1beta2/actions/${action_name}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = action_mutable.to_dict()
        response = self.base_client.patch(url, json=data, **query_params)
        return handle_response(response, Action)


