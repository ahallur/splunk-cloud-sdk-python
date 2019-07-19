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
    SDC Service: Splunk Search Service

    Use the Search service to dispatch, review, and manage searches and search jobs. You can also finalize or cancel running search jobs, retrieve search results and events, and request search-related configurations from the Metadata Catalog service.

    OpenAPI spec version: v2beta1.0
    Generated by: https://openapi-generator.tech
"""


from requests import Response
from string import Template
from typing import List, Dict

from splunk_sdk.base_client import handle_response
from splunk_sdk.base_service import BaseService
from splunk_sdk.common.sscmodel import SSCModel, SSCVoidModel

from splunk_sdk.search.gen_models import FieldsSummary
from splunk_sdk.search.gen_models import ListSearchResultsResponse
from splunk_sdk.search.gen_models import SearchJob
from splunk_sdk.search.gen_models import SearchStatus
from splunk_sdk.search.gen_models import TimeBucketsSummary
from splunk_sdk.search.gen_models import UpdateJob


class SplunkSearchService(BaseService):
    """
    Splunk Search Service
    Version: v2beta1.0
    Use the Search service to dispatch, review, and manage searches and search jobs. You can also finalize or cancel running search jobs, retrieve search results and events, and request search-related configurations from the Metadata Catalog service.
    """

    def __init__(self, base_client):
        super().__init__(base_client)

    def create_job(self, search_job: SearchJob = None) -> SearchJob:
        """
        Creates a search job.
        """
        query_params = {}

        path_params = {
        }

        path = Template("/search/v2beta1/jobs").substitute(path_params)
        url = self.base_client.build_url(path)
        data = search_job.to_dict()
        response = self.base_client.post(url, json=data, **query_params)
        return handle_response(response, SearchJob)

    def get_job(self, sid: str) -> SearchJob:
        """
        Return the search job with the specified search ID (SID).
        """
        query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, SearchJob)

    def list_events_summary(self, sid: str, count: float = None, earliest: str = None, field: str = None, latest: str = None, offset: float = None) -> ListSearchResultsResponse:
        """
        Return events summary, for search ID (SID) search.
        """
        query_params = {}
        if count is not None:
            query_params['count'] = count
        if earliest is not None:
            query_params['earliest'] = earliest
        if field is not None:
            query_params['field'] = field
        if latest is not None:
            query_params['latest'] = latest
        if offset is not None:
            query_params['offset'] = offset

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}/timeline-metadata/auto/events-summary").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, ListSearchResultsResponse)

    def list_fields_summary(self, sid: str, earliest: str = None, latest: str = None) -> FieldsSummary:
        """
        Return fields stats summary of the events to-date, for search ID (SID) search.
        """
        query_params = {}
        if earliest is not None:
            query_params['earliest'] = earliest
        if latest is not None:
            query_params['latest'] = latest

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}/timeline-metadata/auto/fields-summary").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, FieldsSummary)

    def list_jobs(self, count: float = None, status: SearchStatus = None) -> List[SearchJob]:
        """
        Return the matching list of search jobs.
        """
        query_params = {}
        if count is not None:
            query_params['count'] = count
        if status is not None:
            query_params['status'] = status

        path_params = {
        }

        path = Template("/search/v2beta1/jobs").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, SearchJob)

    def list_results(self, sid: str, count: float = None, field: str = None, offset: float = None) -> ListSearchResultsResponse:
        """
        Return the search results for the job with the specified search ID (SID).
        """
        query_params = {}
        if count is not None:
            query_params['count'] = count
        if field is not None:
            query_params['field'] = field
        if offset is not None:
            query_params['offset'] = offset

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}/results").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, ListSearchResultsResponse)

    def list_time_buckets(self, sid: str) -> TimeBucketsSummary:
        """
        Return event distribution over time of the untransformed events read to-date, for search ID(SID) search.
        """
        query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}/timeline-metadata/auto/time-buckets").substitute(path_params)
        url = self.base_client.build_url(path)
        response = self.base_client.get(url, **query_params)
        return handle_response(response, TimeBucketsSummary)

    def update_job(self, sid: str, update_job: UpdateJob = None) -> SearchJob:
        """
        Update the search job with the specified search ID (SID) with an action.
        """
        query_params = {}

        path_params = {
            "sid": sid,
        }

        path = Template("/search/v2beta1/jobs/${sid}").substitute(path_params)
        url = self.base_client.build_url(path)
        data = update_job.to_dict()
        response = self.base_client.patch(url, json=data, **query_params)
        return handle_response(response, SearchJob)


