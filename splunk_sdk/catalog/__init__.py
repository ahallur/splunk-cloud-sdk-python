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

############# This file is auto-generated.  Do not edit! #############

"""
    SDC Service: Metadata Catalog

    With the Metadata Catalog you can create and manage knowledge objects such as datasets, fields, rules, actions, dashboards, and workflows.

    OpenAPI spec version: v2beta1.4
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import apis into sdk package
from splunk_sdk.catalog.gen_metadata_catalog_api import MetadataCatalog

# import models into sdk package
from splunk_sdk.catalog.gen_models import Action, \
    ActionPATCH, \
    ActionPOST, \
    AliasAction, \
    AliasActionKind, \
    AliasActionPATCH, \
    AliasActionPOST, \
    Annotation, \
    AnnotationPOST, \
    AutoKVAction, \
    AutoKVActionKind, \
    AutoKVActionPATCH, \
    AutoKVActionPOST, \
    Dashboard, \
    DashboardPATCH, \
    DashboardPOST, \
    Dataset, \
    DatasetImportedBy, \
    DatasetPATCH, \
    FieldPOST, \
    FieldDataType, \
    FieldType, \
    FieldPrevalence, \
    DatasetPOST, \
    EvalAction, \
    EvalActionKind, \
    EvalActionPATCH, \
    EvalActionPOST, \
    Field, \
    FieldPATCH, \
    ImportDataset, \
    ImportDatasetPOST, \
    ImportDatasetKind, \
    ImportDatasetByIdPOST, \
    ImportDatasetByNamePOST, \
    ImportDatasetPATCH, \
    IndexDataset, \
    IndexDatasetKind, \
    IndexDatasetPATCH, \
    IndexDatasetPOST, \
    JobDatasetPropertiesTimelineMetadata, \
    JobDatasetPropertiesTimelineMetadataAuto, \
    JobDatasetEventSummaryAvailableStatus, \
    JobDatasetFieldSummaryAvailableStatus, \
    JobDatasetTimeBucketsAvailableStatus, \
    JobDataset, \
    JobDatasetKind, \
    JobDatasetPATCH, \
    JobDatasetPOST, \
    KVCollectionDataset, \
    KVCollectionDatasetKind, \
    KVCollectionDatasetPATCH, \
    KVCollectionDatasetPOST, \
    LookupAction, \
    LookupActionKind, \
    LookupActionPATCH, \
    LookupActionPOST, \
    LookupDatasetExternalKind, \
    LookupDataset, \
    LookupDatasetKind, \
    LookupDatasetPATCH, \
    LookupDatasetPOST, \
    MetricDataset, \
    MetricDatasetKind, \
    MetricDatasetPATCH, \
    MetricDatasetPOST, \
    Module, \
    RegexAction, \
    RegexActionKind, \
    RegexActionPATCH, \
    RegexActionPOST, \
    RelationshipField, \
    RelationshipFieldKind, \
    RelationshipKind, \
    Relationship, \
    RelationshipFieldPOST, \
    RelationshipPATCH, \
    RelationshipPOST, \
    Rule, \
    RulePATCH, \
    RulePOST, \
    Task, \
    TaskPOST, \
    ViewDataset, \
    ViewDatasetKind, \
    ViewDatasetPATCH, \
    ViewDatasetPOST, \
    Workflow, \
    WorkflowBuild, \
    WorkflowBuildPATCH, \
    WorkflowBuildPOST, \
    WorkflowPATCH, \
    WorkflowPOST, \
    WorkflowRun, \
    WorkflowRunPATCH, \
    WorkflowRunPOST
