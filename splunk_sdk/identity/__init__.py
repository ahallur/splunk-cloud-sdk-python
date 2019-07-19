# coding: utf-8

# flake8: noqa

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


__version__ = "1.0.0"

# import apis into sdk package
from splunk_sdk.identity.gen_identity_and_access_control_api import IdentityAndAccessControl

# import models into sdk package
from splunk_sdk.identity.gen_models import AddGroupMemberBody, \
    AddGroupRoleBody, \
    AddMemberBody, \
    AddRolePermissionBody, \
    CreateGroupBody, \
    CreateRoleBody, \
    Group, \
    GroupMember, \
    GroupRole, \
    PrincipalProfile, \
    Member, \
    PrincipalKind, \
    Principal, \
    Role, \
    RolePermission, \
    TenantStatus, \
    Tenant, \
    ValidateInfo
