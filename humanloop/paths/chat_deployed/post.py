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

from humanloop.model.tool_choice import ToolChoice as ToolChoiceSchema
from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.response_format import ResponseFormat as ResponseFormatSchema
from humanloop.model.provider_api_keys import ProviderApiKeys as ProviderApiKeysSchema
from humanloop.model.chat_response import ChatResponse as ChatResponseSchema
from humanloop.model.chat_message import ChatMessage as ChatMessageSchema
from humanloop.model.chat_deployed_request import ChatDeployedRequest as ChatDeployedRequestSchema

from humanloop.type.provider_api_keys import ProviderApiKeys
from humanloop.type.chat_message import ChatMessage
from humanloop.type.response_format import ResponseFormat
from humanloop.type.tool_choice import ToolChoice
from humanloop.type.chat_deployed_request import ChatDeployedRequest
from humanloop.type.chat_response import ChatResponse
from humanloop.type.http_validation_error import HTTPValidationError

from ...api_client import Dictionary
from humanloop.pydantic.response_format import ResponseFormat as ResponseFormatPydantic
from humanloop.pydantic.chat_message import ChatMessage as ChatMessagePydantic
from humanloop.pydantic.chat_response import ChatResponse as ChatResponsePydantic
from humanloop.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from humanloop.pydantic.chat_deployed_request import ChatDeployedRequest as ChatDeployedRequestPydantic
from humanloop.pydantic.provider_api_keys import ProviderApiKeys as ProviderApiKeysPydantic
from humanloop.pydantic.tool_choice import ToolChoice as ToolChoicePydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = ChatDeployedRequestSchema


request_body_chat_deployed_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'APIKeyHeader',
]
SchemaFor200ResponseBodyApplicationJson = ChatResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ChatResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ChatResponse


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
_status_code_to_response = {
    '200': _response_for_200,
    '422': _response_for_422,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_deployed_mapped_args(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source_datapoint_id: typing.Optional[str] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = None,
        tool_call: typing.Optional[typing.Union[str, typing.Dict[str, str]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        environment: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if project is not None:
            _body["project"] = project
        if project_id is not None:
            _body["project_id"] = project_id
        if session_id is not None:
            _body["session_id"] = session_id
        if session_reference_id is not None:
            _body["session_reference_id"] = session_reference_id
        if parent_id is not None:
            _body["parent_id"] = parent_id
        if parent_reference_id is not None:
            _body["parent_reference_id"] = parent_reference_id
        if inputs is not None:
            _body["inputs"] = inputs
        if source is not None:
            _body["source"] = source
        if metadata is not None:
            _body["metadata"] = metadata
        if source_datapoint_id is not None:
            _body["source_datapoint_id"] = source_datapoint_id
        if messages is not None:
            _body["messages"] = messages
        if provider_api_keys is not None:
            _body["provider_api_keys"] = provider_api_keys
        if num_samples is not None:
            _body["num_samples"] = num_samples
        if stream is not None:
            _body["stream"] = stream
        if user is not None:
            _body["user"] = user
        if tool_choice is not None:
            _body["tool_choice"] = tool_choice
        if tool_call is not None:
            _body["tool_call"] = tool_call
        if seed is not None:
            _body["seed"] = seed
        if response_format is not None:
            _body["response_format"] = response_format
        if environment is not None:
            _body["environment"] = environment
        args.body = _body
        return args

    async def _acreate_deployed_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Chat Deployed
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_chat_deployed_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
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


    def _create_deployed_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Chat Deployed
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_chat_deployed_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class CreateDeployedRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_deployed(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source_datapoint_id: typing.Optional[str] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = None,
        tool_call: typing.Optional[typing.Union[str, typing.Dict[str, str]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        environment: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_deployed_mapped_args(
            messages=messages,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            source_datapoint_id=source_datapoint_id,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
            tool_choice=tool_choice,
            tool_call=tool_call,
            seed=seed,
            response_format=response_format,
            environment=environment,
        )
        return await self._acreate_deployed_oapg(
            body=args.body,
            **kwargs,
        )
    
    def create_deployed(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source_datapoint_id: typing.Optional[str] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = None,
        tool_call: typing.Optional[typing.Union[str, typing.Dict[str, str]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        environment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_deployed_mapped_args(
            messages=messages,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            source_datapoint_id=source_datapoint_id,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
            tool_choice=tool_choice,
            tool_call=tool_call,
            seed=seed,
            response_format=response_format,
            environment=environment,
        )
        return self._create_deployed_oapg(
            body=args.body,
        )

class CreateDeployed(BaseApi):

    async def acreate_deployed(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source_datapoint_id: typing.Optional[str] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = None,
        tool_call: typing.Optional[typing.Union[str, typing.Dict[str, str]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        environment: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ):
        raw_response = await self.raw.acreate_deployed(
            messages=messages,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            source_datapoint_id=source_datapoint_id,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
            tool_choice=tool_choice,
            tool_call=tool_call,
            seed=seed,
            response_format=response_format,
            environment=environment,
            **kwargs,
        )
        if validate:
            return ChatResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ChatResponsePydantic, raw_response.body)
    
    
    def create_deployed(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source_datapoint_id: typing.Optional[str] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = None,
        tool_call: typing.Optional[typing.Union[str, typing.Dict[str, str]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        environment: typing.Optional[str] = None,
        validate: bool = False,
    ):
        raw_response = self.raw.create_deployed(
            messages=messages,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            source_datapoint_id=source_datapoint_id,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
            tool_choice=tool_choice,
            tool_call=tool_call,
            seed=seed,
            response_format=response_format,
            environment=environment,
        )
        if validate:
            return ChatResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ChatResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source_datapoint_id: typing.Optional[str] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = None,
        tool_call: typing.Optional[typing.Union[str, typing.Dict[str, str]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        environment: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_deployed_mapped_args(
            messages=messages,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            source_datapoint_id=source_datapoint_id,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
            tool_choice=tool_choice,
            tool_call=tool_call,
            seed=seed,
            response_format=response_format,
            environment=environment,
        )
        return await self._acreate_deployed_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        messages: typing.List[ChatMessage],
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        session_id: typing.Optional[str] = None,
        session_reference_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        parent_reference_id: typing.Optional[str] = None,
        inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        source_datapoint_id: typing.Optional[str] = None,
        provider_api_keys: typing.Optional[ProviderApiKeys] = None,
        num_samples: typing.Optional[int] = None,
        stream: typing.Optional[bool] = None,
        user: typing.Optional[str] = None,
        tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = None,
        tool_call: typing.Optional[typing.Union[str, typing.Dict[str, str]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        environment: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_deployed_mapped_args(
            messages=messages,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            source_datapoint_id=source_datapoint_id,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            stream=stream,
            user=user,
            tool_choice=tool_choice,
            tool_call=tool_call,
            seed=seed,
            response_format=response_format,
            environment=environment,
        )
        return self._create_deployed_oapg(
            body=args.body,
        )

