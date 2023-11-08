# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from humanloop.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from humanloop.api_response import AsyncGeneratorResponse
from humanloop import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from humanloop import schemas  # noqa: F401

from humanloop.model.feedback_response import FeedbackResponse as FeedbackResponseSchema
from humanloop.model.evaluation_datapoint_snapshot_response import EvaluationDatapointSnapshotResponse as EvaluationDatapointSnapshotResponseSchema
from humanloop.model.validation_error_loc import ValidationErrorLoc as ValidationErrorLocSchema
from humanloop.model.metric_value_response import MetricValueResponse as MetricValueResponseSchema
from humanloop.model.datapoint_response_inputs import DatapointResponseInputs as DatapointResponseInputsSchema
from humanloop.model.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse as ModelConfigEvaluatorAggregateResponseSchema
from humanloop.model.chat_role import ChatRole as ChatRoleSchema
from humanloop.model.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse as ProjectModelConfigFeedbackStatsResponseSchema
from humanloop.model.chat_message import ChatMessage as ChatMessageSchema
from humanloop.model.datapoint_response import DatapointResponse as DatapointResponseSchema
from humanloop.model.config_response import ConfigResponse as ConfigResponseSchema
from humanloop.model.tool_result_response import ToolResultResponse as ToolResultResponseSchema
from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.paginated_data_evaluation_datapoint_snapshot_response import PaginatedDataEvaluationDatapointSnapshotResponse as PaginatedDataEvaluationDatapointSnapshotResponseSchema
from humanloop.model.datapoint_response_target import DatapointResponseTarget as DatapointResponseTargetSchema
from humanloop.model.evaluation_result_response import EvaluationResultResponse as EvaluationResultResponseSchema
from humanloop.model.project_config_response import ProjectConfigResponse as ProjectConfigResponseSchema
from humanloop.model.observability_status import ObservabilityStatus as ObservabilityStatusSchema
from humanloop.model.tool_call import ToolCall as ToolCallSchema
from humanloop.model.log_response import LogResponse as LogResponseSchema
from humanloop.model.feedback_type import FeedbackType as FeedbackTypeSchema
from humanloop.model.validation_error import ValidationError as ValidationErrorSchema

from humanloop.type.config_response import ConfigResponse
from humanloop.type.feedback_response import FeedbackResponse
from humanloop.type.evaluation_datapoint_snapshot_response import EvaluationDatapointSnapshotResponse
from humanloop.type.datapoint_response import DatapointResponse
from humanloop.type.observability_status import ObservabilityStatus
from humanloop.type.datapoint_response_inputs import DatapointResponseInputs
from humanloop.type.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse
from humanloop.type.evaluation_result_response import EvaluationResultResponse
from humanloop.type.validation_error_loc import ValidationErrorLoc
from humanloop.type.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse
from humanloop.type.tool_result_response import ToolResultResponse
from humanloop.type.chat_role import ChatRole
from humanloop.type.chat_message import ChatMessage
from humanloop.type.validation_error import ValidationError
from humanloop.type.feedback_type import FeedbackType
from humanloop.type.log_response import LogResponse
from humanloop.type.datapoint_response_target import DatapointResponseTarget
from humanloop.type.tool_call import ToolCall
from humanloop.type.metric_value_response import MetricValueResponse
from humanloop.type.paginated_data_evaluation_datapoint_snapshot_response import PaginatedDataEvaluationDatapointSnapshotResponse
from humanloop.type.project_config_response import ProjectConfigResponse
from humanloop.type.http_validation_error import HTTPValidationError

from ...api_client import Dictionary
from humanloop.pydantic.evaluation_result_response import EvaluationResultResponse as EvaluationResultResponsePydantic
from humanloop.pydantic.validation_error_loc import ValidationErrorLoc as ValidationErrorLocPydantic
from humanloop.pydantic.observability_status import ObservabilityStatus as ObservabilityStatusPydantic
from humanloop.pydantic.chat_role import ChatRole as ChatRolePydantic
from humanloop.pydantic.config_response import ConfigResponse as ConfigResponsePydantic
from humanloop.pydantic.feedback_type import FeedbackType as FeedbackTypePydantic
from humanloop.pydantic.log_response import LogResponse as LogResponsePydantic
from humanloop.pydantic.project_model_config_feedback_stats_response import ProjectModelConfigFeedbackStatsResponse as ProjectModelConfigFeedbackStatsResponsePydantic
from humanloop.pydantic.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse as ModelConfigEvaluatorAggregateResponsePydantic
from humanloop.pydantic.project_config_response import ProjectConfigResponse as ProjectConfigResponsePydantic
from humanloop.pydantic.datapoint_response_target import DatapointResponseTarget as DatapointResponseTargetPydantic
from humanloop.pydantic.chat_message import ChatMessage as ChatMessagePydantic
from humanloop.pydantic.evaluation_datapoint_snapshot_response import EvaluationDatapointSnapshotResponse as EvaluationDatapointSnapshotResponsePydantic
from humanloop.pydantic.validation_error import ValidationError as ValidationErrorPydantic
from humanloop.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from humanloop.pydantic.feedback_response import FeedbackResponse as FeedbackResponsePydantic
from humanloop.pydantic.tool_call import ToolCall as ToolCallPydantic
from humanloop.pydantic.datapoint_response_inputs import DatapointResponseInputs as DatapointResponseInputsPydantic
from humanloop.pydantic.datapoint_response import DatapointResponse as DatapointResponsePydantic
from humanloop.pydantic.tool_result_response import ToolResultResponse as ToolResultResponsePydantic
from humanloop.pydantic.paginated_data_evaluation_datapoint_snapshot_response import PaginatedDataEvaluationDatapointSnapshotResponse as PaginatedDataEvaluationDatapointSnapshotResponsePydantic
from humanloop.pydantic.metric_value_response import MetricValueResponse as MetricValueResponsePydantic

# Query params
PageSchema = schemas.IntSchema
SizeSchema = schemas.IntSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'size': typing.Union[SizeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_size = api_client.QueryParameter(
    name="size",
    style=api_client.ParameterStyle.FORM,
    schema=SizeSchema,
    explode=True,
)
# Path params
IdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'id': typing.Union[IdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_id = api_client.PathParameter(
    name="id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=IdSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = PaginatedDataEvaluationDatapointSnapshotResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaginatedDataEvaluationDatapointSnapshotResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaginatedDataEvaluationDatapointSnapshotResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = HTTPValidationErrorSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: HTTPValidationError


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: HTTPValidationError


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _list_datapoints_mapped_args(
        self,
        id: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if page is not None:
            _query_params["page"] = page
        if size is not None:
            _query_params["size"] = size
        if id is not None:
            _path_params["id"] = id
        args.query = _query_params
        args.path = _path_params
        return args

    async def _alist_datapoints_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        List Datapoints
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _list_datapoints_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        List Datapoints
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_page,
            request_query_size,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class ListDatapointsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def alist_datapoints(
        self,
        id: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_datapoints_mapped_args(
            id=id,
            page=page,
            size=size,
        )
        return await self._alist_datapoints_oapg(
            query_params=args.query,
            path_params=args.path,
        )
    
    def list_datapoints(
        self,
        id: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_datapoints_mapped_args(
            id=id,
            page=page,
            size=size,
        )
        return self._list_datapoints_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class ListDatapoints(BaseApi):

    async def alist_datapoints(
        self,
        id: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        validate: bool = False,
    ):
        raw_response = await self.raw.alist_datapoints(
            id=id,
            page=page,
            size=size,
        )
        if validate:
            return PaginatedDataEvaluationDatapointSnapshotResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaginatedDataEvaluationDatapointSnapshotResponsePydantic, raw_response.body)
    
    
    def list_datapoints(
        self,
        id: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        validate: bool = False,
    ):
        raw_response = self.raw.list_datapoints(
            id=id,
            page=page,
            size=size,
        )
        if validate:
            return PaginatedDataEvaluationDatapointSnapshotResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(PaginatedDataEvaluationDatapointSnapshotResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        id: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._list_datapoints_mapped_args(
            id=id,
            page=page,
            size=size,
        )
        return await self._alist_datapoints_oapg(
            query_params=args.query,
            path_params=args.path,
        )
    
    def get(
        self,
        id: str,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._list_datapoints_mapped_args(
            id=id,
            page=page,
            size=size,
        )
        return self._list_datapoints_oapg(
            query_params=args.query,
            path_params=args.path,
        )

