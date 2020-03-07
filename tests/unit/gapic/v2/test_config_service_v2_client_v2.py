# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests."""

import mock
import pytest

from google.cloud import logging_v2
from google.cloud.logging_v2.proto import logging_config_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2


class MultiCallableStub(object):
    """Stub for the grpc.UnaryUnaryMultiCallable interface."""

    def __init__(self, method, channel_stub):
        self.method = method
        self.channel_stub = channel_stub

    def __call__(self, request, timeout=None, metadata=None, credentials=None):
        self.channel_stub.requests.append((self.method, request))

        response = None
        if self.channel_stub.responses:
            response = self.channel_stub.responses.pop()

        if isinstance(response, Exception):
            raise response

        if response:
            return response


class ChannelStub(object):
    """Stub for the grpc.Channel interface."""

    def __init__(self, responses=[]):
        self.responses = responses
        self.requests = []

    def unary_unary(self, method, request_serializer=None, response_deserializer=None):
        return MultiCallableStub(method, self)


class CustomException(Exception):
    pass


class TestConfigServiceV2Client(object):
    def test_list_buckets(self):
        # Setup Expected Response
        next_page_token = ""
        buckets_element = {}
        buckets = [buckets_element]
        expected_response = {"next_page_token": next_page_token, "buckets": buckets}
        expected_response = logging_config_pb2.ListBucketsResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        parent = "parent-995424086"

        paged_list_response = client.list_buckets(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.buckets[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.ListBucketsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_buckets_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        parent = "parent-995424086"

        paged_list_response = client.list_buckets(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_bucket(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        description = "description-1724546052"
        retention_days = 1544391896
        expected_response = {
            "name": name_2,
            "description": description,
            "retention_days": retention_days,
        }
        expected_response = logging_config_pb2.LogBucket(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        name = "name3373707"

        response = client.get_bucket(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.GetBucketRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_bucket_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        name = "name3373707"

        with pytest.raises(CustomException):
            client.get_bucket(name)

    def test_update_bucket(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        description = "description-1724546052"
        retention_days = 1544391896
        expected_response = {
            "name": name_2,
            "description": description,
            "retention_days": retention_days,
        }
        expected_response = logging_config_pb2.LogBucket(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        name = "name3373707"
        bucket = {}
        update_mask = {}

        response = client.update_bucket(name, bucket, update_mask)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.UpdateBucketRequest(
            name=name, bucket=bucket, update_mask=update_mask
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_bucket_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        name = "name3373707"
        bucket = {}
        update_mask = {}

        with pytest.raises(CustomException):
            client.update_bucket(name, bucket, update_mask)

    def test_list_sinks(self):
        # Setup Expected Response
        next_page_token = ""
        sinks_element = {}
        sinks = [sinks_element]
        expected_response = {"next_page_token": next_page_token, "sinks": sinks}
        expected_response = logging_config_pb2.ListSinksResponse(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        parent = client.project_path("[PROJECT]")

        paged_list_response = client.list_sinks(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.sinks[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.ListSinksRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_sinks_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        parent = client.project_path("[PROJECT]")

        paged_list_response = client.list_sinks(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_sink(self):
        # Setup Expected Response
        name = "name3373707"
        destination = "destination-1429847026"
        filter_ = "filter-1274492040"
        description = "description-1724546052"
        disabled = True
        writer_identity = "writerIdentity775638794"
        include_children = True
        expected_response = {
            "name": name,
            "destination": destination,
            "filter": filter_,
            "description": description,
            "disabled": disabled,
            "writer_identity": writer_identity,
            "include_children": include_children,
        }
        expected_response = logging_config_pb2.LogSink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        sink_name = "sinkName-1391757129"

        response = client.get_sink(sink_name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.GetSinkRequest(sink_name=sink_name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_sink_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        sink_name = "sinkName-1391757129"

        with pytest.raises(CustomException):
            client.get_sink(sink_name)

    def test_create_sink(self):
        # Setup Expected Response
        name = "name3373707"
        destination = "destination-1429847026"
        filter_ = "filter-1274492040"
        description = "description-1724546052"
        disabled = True
        writer_identity = "writerIdentity775638794"
        include_children = True
        expected_response = {
            "name": name,
            "destination": destination,
            "filter": filter_,
            "description": description,
            "disabled": disabled,
            "writer_identity": writer_identity,
            "include_children": include_children,
        }
        expected_response = logging_config_pb2.LogSink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        parent = client.project_path("[PROJECT]")
        sink = {}

        response = client.create_sink(parent, sink)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.CreateSinkRequest(
            parent=parent, sink=sink
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_sink_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        parent = client.project_path("[PROJECT]")
        sink = {}

        with pytest.raises(CustomException):
            client.create_sink(parent, sink)

    def test_update_sink(self):
        # Setup Expected Response
        name = "name3373707"
        destination = "destination-1429847026"
        filter_ = "filter-1274492040"
        description = "description-1724546052"
        disabled = True
        writer_identity = "writerIdentity775638794"
        include_children = True
        expected_response = {
            "name": name,
            "destination": destination,
            "filter": filter_,
            "description": description,
            "disabled": disabled,
            "writer_identity": writer_identity,
            "include_children": include_children,
        }
        expected_response = logging_config_pb2.LogSink(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        sink_name = "sinkName-1391757129"
        sink = {}

        response = client.update_sink(sink_name, sink)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.UpdateSinkRequest(
            sink_name=sink_name, sink=sink
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_sink_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        sink_name = "sinkName-1391757129"
        sink = {}

        with pytest.raises(CustomException):
            client.update_sink(sink_name, sink)

    def test_delete_sink(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        sink_name = "sinkName-1391757129"

        client.delete_sink(sink_name)

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.DeleteSinkRequest(sink_name=sink_name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_sink_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        sink_name = "sinkName-1391757129"

        with pytest.raises(CustomException):
            client.delete_sink(sink_name)

    def test_list_exclusions(self):
        # Setup Expected Response
        next_page_token = ""
        exclusions_element = {}
        exclusions = [exclusions_element]
        expected_response = {
            "next_page_token": next_page_token,
            "exclusions": exclusions,
        }
        expected_response = logging_config_pb2.ListExclusionsResponse(
            **expected_response
        )

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        parent = client.project_path("[PROJECT]")

        paged_list_response = client.list_exclusions(parent)
        resources = list(paged_list_response)
        assert len(resources) == 1

        assert expected_response.exclusions[0] == resources[0]

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.ListExclusionsRequest(parent=parent)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_list_exclusions_exception(self):
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        parent = client.project_path("[PROJECT]")

        paged_list_response = client.list_exclusions(parent)
        with pytest.raises(CustomException):
            list(paged_list_response)

    def test_get_exclusion(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        description = "description-1724546052"
        filter_ = "filter-1274492040"
        disabled = True
        expected_response = {
            "name": name_2,
            "description": description,
            "filter": filter_,
            "disabled": disabled,
        }
        expected_response = logging_config_pb2.LogExclusion(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        name = "name3373707"

        response = client.get_exclusion(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.GetExclusionRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_exclusion_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        name = "name3373707"

        with pytest.raises(CustomException):
            client.get_exclusion(name)

    def test_create_exclusion(self):
        # Setup Expected Response
        name = "name3373707"
        description = "description-1724546052"
        filter_ = "filter-1274492040"
        disabled = True
        expected_response = {
            "name": name,
            "description": description,
            "filter": filter_,
            "disabled": disabled,
        }
        expected_response = logging_config_pb2.LogExclusion(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        parent = client.project_path("[PROJECT]")
        exclusion = {}

        response = client.create_exclusion(parent, exclusion)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.CreateExclusionRequest(
            parent=parent, exclusion=exclusion
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_create_exclusion_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        parent = client.project_path("[PROJECT]")
        exclusion = {}

        with pytest.raises(CustomException):
            client.create_exclusion(parent, exclusion)

    def test_update_exclusion(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        description = "description-1724546052"
        filter_ = "filter-1274492040"
        disabled = True
        expected_response = {
            "name": name_2,
            "description": description,
            "filter": filter_,
            "disabled": disabled,
        }
        expected_response = logging_config_pb2.LogExclusion(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        name = "name3373707"
        exclusion = {}
        update_mask = {}

        response = client.update_exclusion(name, exclusion, update_mask)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.UpdateExclusionRequest(
            name=name, exclusion=exclusion, update_mask=update_mask
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_exclusion_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        name = "name3373707"
        exclusion = {}
        update_mask = {}

        with pytest.raises(CustomException):
            client.update_exclusion(name, exclusion, update_mask)

    def test_delete_exclusion(self):
        channel = ChannelStub()
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        name = "name3373707"

        client.delete_exclusion(name)

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.DeleteExclusionRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_delete_exclusion_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        name = "name3373707"

        with pytest.raises(CustomException):
            client.delete_exclusion(name)

    def test_get_cmek_settings(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        kms_key_name = "kmsKeyName2094986649"
        service_account_id = "serviceAccountId-111486921"
        expected_response = {
            "name": name_2,
            "kms_key_name": kms_key_name,
            "service_account_id": service_account_id,
        }
        expected_response = logging_config_pb2.CmekSettings(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        name = "name3373707"

        response = client.get_cmek_settings(name)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.GetCmekSettingsRequest(name=name)
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_get_cmek_settings_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        name = "name3373707"

        with pytest.raises(CustomException):
            client.get_cmek_settings(name)

    def test_update_cmek_settings(self):
        # Setup Expected Response
        name_2 = "name2-1052831874"
        kms_key_name = "kmsKeyName2094986649"
        service_account_id = "serviceAccountId-111486921"
        expected_response = {
            "name": name_2,
            "kms_key_name": kms_key_name,
            "service_account_id": service_account_id,
        }
        expected_response = logging_config_pb2.CmekSettings(**expected_response)

        # Mock the API response
        channel = ChannelStub(responses=[expected_response])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup Request
        name = "name3373707"
        cmek_settings = {}

        response = client.update_cmek_settings(name, cmek_settings)
        assert expected_response == response

        assert len(channel.requests) == 1
        expected_request = logging_config_pb2.UpdateCmekSettingsRequest(
            name=name, cmek_settings=cmek_settings
        )
        actual_request = channel.requests[0][1]
        assert expected_request == actual_request

    def test_update_cmek_settings_exception(self):
        # Mock the API response
        channel = ChannelStub(responses=[CustomException()])
        patch = mock.patch("google.api_core.grpc_helpers.create_channel")
        with patch as create_channel:
            create_channel.return_value = channel
            client = logging_v2.ConfigServiceV2Client()

        # Setup request
        name = "name3373707"
        cmek_settings = {}

        with pytest.raises(CustomException):
            client.update_cmek_settings(name, cmek_settings)
