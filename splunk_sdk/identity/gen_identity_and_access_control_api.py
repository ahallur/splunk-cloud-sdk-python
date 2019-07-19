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

################################################################################
################################################################################
###                                                                          ###
###           This file is auto-generated.  Do not edit!                     ###
###                                                                          ###
################################################################################
################################################################################

"""
    SDC Service: Identity and Access Control

    With the Splunk Cloud Identity and Access Control (IAC) Service, you can authenticate and authorize Splunk API users.

    OpenAPI spec version: v2beta1.6
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.identity.gen_models import AddGroupMemberBody
from splunk_sdk.identity.gen_models import AddGroupRoleBody
from splunk_sdk.identity.gen_models import AddMemberBody
from splunk_sdk.identity.gen_models import CreateGroupBody
from splunk_sdk.identity.gen_models import CreateRoleBody
from splunk_sdk.identity.gen_models import Group
from splunk_sdk.identity.gen_models import GroupMember
from splunk_sdk.identity.gen_models import GroupRole
from splunk_sdk.identity.gen_models import Member
from splunk_sdk.identity.gen_models import Principal
from splunk_sdk.identity.gen_models import Role
from splunk_sdk.identity.gen_models import RolePermission
from splunk_sdk.identity.gen_models import ValidateInfo


class IdentityAndAccessControl(BaseService):
    """
    Identity and Access Control
    Version: v2beta1.6
    With the Splunk Cloud Identity and Access Control (IAC) Service, you can authenticate and authorize Splunk API users.
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def add_group_member(self, group: str, add_group_member_body: AddGroupMemberBody) -> GroupMember:
        """
        Adds a member to a given group.
        """
        query_params = {}

        path_params = {
            "group": group,
        }

        path = Template("/identity/v2beta1/groups/${group}/members").substitute(path_params)
        url = self.base_client.build_url(path)
        data = add_group_member_body.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, GroupMember)

    def add_group_role(self, group: str, add_group_role_body: AddGroupRoleBody) -> GroupRole:
        """
        Adds a role to a given group.
        """
        query_params = {}

        path_params = {
            "group": group,
        }

        path = Template("/identity/v2beta1/groups/${group}/roles").substitute(path_params)
        url = self.base_client.build_url(path)
        data = add_group_role_body.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, GroupRole)

    def add_member(self, add_member_body: AddMemberBody) -> Member:
        """
        Adds a member to a given tenant.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/identity/v2beta1/members").substitute(path_params)
        url = self.base_client.build_url(path)
        data = add_member_body.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, Member)

    def add_role_permission(self, role: str, body: str) -> RolePermission:
        """
        Adds permissions to a role in a given tenant.
        """
        query_params = {}

        path_params = {
            "role": role,
        }

        path = Template("/identity/v2beta1/roles/${role}/permissions").substitute(path_params)
        url = self.base_client.build_url(path)
        data = body
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, RolePermission)

    def create_group(self, create_group_body: CreateGroupBody) -> Group:
        """
        Creates a new group in a given tenant.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/identity/v2beta1/groups").substitute(path_params)
        url = self.base_client.build_url(path)
        data = create_group_body.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, Group)

    def create_role(self, create_role_body: CreateRoleBody) -> Role:
        """
        Creates a new authorization role in a given tenant.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/identity/v2beta1/roles").substitute(path_params)
        url = self.base_client.build_url(path)
        data = create_role_body.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, Role)

    def delete_group(self, group: str) -> SSCVoidModel:
        """
        Deletes a group in a given tenant.
        """
        query_params = {}

        path_params = {
            "group": group,
        }

        path = Template("/identity/v2beta1/groups/${group}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, **query_params)
        return handle_response(response, )

    def delete_role(self, role: str) -> SSCVoidModel:
        """
        Deletes a defined role for a given tenant.
        """
        query_params = {}

        path_params = {
            "role": role,
        }

        path = Template("/identity/v2beta1/roles/${role}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, **query_params)
        return handle_response(response, )

    def get_group(self, group: str) -> Group:
        """
        Returns information about a given group within a tenant.
        """
        query_params = {}

        path_params = {
            "group": group,
        }

        path = Template("/identity/v2beta1/groups/${group}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, Group)

    def get_group_member(self, group: str, member: str) -> GroupMember:
        """
        Returns information about a given member within a given group.
        """
        query_params = {}

        path_params = {
            "group": group,
            "member": member,
        }

        path = Template("/identity/v2beta1/groups/${group}/members/${member}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, GroupMember)

    def get_group_role(self, group: str, role: str) -> GroupRole:
        """
        Returns information about a given role within a given group.
        """
        query_params = {}

        path_params = {
            "group": group,
            "role": role,
        }

        path = Template("/identity/v2beta1/groups/${group}/roles/${role}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, GroupRole)

    def get_member(self, member: str) -> Member:
        """
        Returns a member of a given tenant.
        """
        query_params = {}

        path_params = {
            "member": member,
        }

        path = Template("/identity/v2beta1/members/${member}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, Member)

    def get_principal(self, principal: str) -> Principal:
        """
        Returns the details of a principal, including its tenant membership.
        """
        query_params = {}

        path_params = {
            "principal": principal,
        }

        path = Template("/system/identity/v2beta1/principals/${principal}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, Principal)

    def get_role(self, role: str) -> Role:
        """
        Returns a role for a given tenant.
        """
        query_params = {}

        path_params = {
            "role": role,
        }

        path = Template("/identity/v2beta1/roles/${role}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, Role)

    def get_role_permission(self, role: str, permission: str) -> RolePermission:
        """
        Gets a permission for the specified role.
        """
        query_params = {}

        path_params = {
            "role": role,
            "permission": permission,
        }

        path = Template("/identity/v2beta1/roles/${role}/permissions/${permission}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, RolePermission)

    def list_group_members(self, group: str) -> List[str]:
        """
        Returns a list of the members within a given group.
        """
        query_params = {}

        path_params = {
            "group": group,
        }

        path = Template("/identity/v2beta1/groups/${group}/members").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_group_roles(self, group: str) -> List[str]:
        """
        Returns a list of the roles that are attached to a group within a given tenant.
        """
        query_params = {}

        path_params = {
            "group": group,
        }

        path = Template("/identity/v2beta1/groups/${group}/roles").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_groups(self) -> List[str]:
        """
        List the groups that exist in a given tenant.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/identity/v2beta1/groups").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_member_groups(self, member: str) -> List[str]:
        """
        Returns a list of groups that a member belongs to within a tenant.
        """
        query_params = {}

        path_params = {
            "member": member,
        }

        path = Template("/identity/v2beta1/members/${member}/groups").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_member_permissions(self, member: str) -> List[str]:
        """
        Returns a set of permissions granted to the member within the tenant.

        """
        query_params = {}

        path_params = {
            "member": member,
        }

        path = Template("/identity/v2beta1/members/${member}/permissions").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_member_roles(self, member: str) -> List[str]:
        """
        Returns a set of roles that a given member holds within the tenant.

        """
        query_params = {}

        path_params = {
            "member": member,
        }

        path = Template("/identity/v2beta1/members/${member}/roles").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_members(self) -> List[str]:
        """
        Returns a list of members in a given tenant.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/identity/v2beta1/members").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_principals(self) -> List[str]:
        """
        Returns the list of principals known to IAC.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/system/identity/v2beta1/principals").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_role_groups(self, role: str) -> List[str]:
        """
        Gets a list of groups for a role in a given tenant.
        """
        query_params = {}

        path_params = {
            "role": role,
        }

        path = Template("/identity/v2beta1/roles/${role}/groups").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_role_permissions(self, role: str) -> List[str]:
        """
        Gets the permissions for a role in a given tenant.
        """
        query_params = {}

        path_params = {
            "role": role,
        }

        path = Template("/identity/v2beta1/roles/${role}/permissions").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def list_roles(self) -> List[str]:
        """
        Returns all roles for a given tenant.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/identity/v2beta1/roles").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, str)

    def remove_group_member(self, group: str, member: str) -> SSCVoidModel:
        """
        Removes the member from a given group.
        """
        query_params = {}

        path_params = {
            "group": group,
            "member": member,
        }

        path = Template("/identity/v2beta1/groups/${group}/members/${member}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, **query_params)
        return handle_response(response, )

    def remove_group_role(self, group: str, role: str) -> SSCVoidModel:
        """
        Removes a role from a given group.
        """
        query_params = {}

        path_params = {
            "group": group,
            "role": role,
        }

        path = Template("/identity/v2beta1/groups/${group}/roles/${role}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, **query_params)
        return handle_response(response, )

    def remove_member(self, member: str) -> SSCVoidModel:
        """
        Removes a member from a given tenant
        """
        query_params = {}

        path_params = {
            "member": member,
        }

        path = Template("/identity/v2beta1/members/${member}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, **query_params)
        return handle_response(response, )

    def remove_role_permission(self, role: str, permission: str) -> SSCVoidModel:
        """
        Removes a permission from the role.
        """
        query_params = {}

        path_params = {
            "role": role,
            "permission": permission,
        }

        path = Template("/identity/v2beta1/roles/${role}/permissions/${permission}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.delete(url, **query_params)
        return handle_response(response, )

    def validate_token(self, include: List[str] = None) -> ValidateInfo:
        """
        Validates the access token obtained from the authorization header and returns the principal name and tenant memberships.

        """
        query_params = {}
        if include is not None:
            query_params['include'] = include

        path_params = {
        }

        path = Template("/identity/v2beta1/validate").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, ValidateInfo)


