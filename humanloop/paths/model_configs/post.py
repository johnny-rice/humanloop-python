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

from humanloop.model.model_providers import ModelProviders as ModelProvidersSchema
from humanloop.model.project_model_config_request import ProjectModelConfigRequest as ProjectModelConfigRequestSchema
from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.response_format import ResponseFormat as ResponseFormatSchema
from humanloop.model.model_endpoints import ModelEndpoints as ModelEndpointsSchema
from humanloop.model.chat_message_with_tool_call import ChatMessageWithToolCall as ChatMessageWithToolCallSchema
from humanloop.model.project_config_response import ProjectConfigResponse as ProjectConfigResponseSchema
from humanloop.model.project_model_config_request_tools import ProjectModelConfigRequestTools as ProjectModelConfigRequestToolsSchema

from humanloop.type.response_format import ResponseFormat
from humanloop.type.project_model_config_request import ProjectModelConfigRequest
from humanloop.type.project_model_config_request_tools import ProjectModelConfigRequestTools
from humanloop.type.chat_message_with_tool_call import ChatMessageWithToolCall
from humanloop.type.model_providers import ModelProviders
from humanloop.type.project_config_response import ProjectConfigResponse
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.model_endpoints import ModelEndpoints

from ...api_client import Dictionary
from humanloop.pydantic.response_format import ResponseFormat as ResponseFormatPydantic
from humanloop.pydantic.project_config_response import ProjectConfigResponse as ProjectConfigResponsePydantic
from humanloop.pydantic.project_model_config_request_tools import ProjectModelConfigRequestTools as ProjectModelConfigRequestToolsPydantic
from humanloop.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from humanloop.pydantic.project_model_config_request import ProjectModelConfigRequest as ProjectModelConfigRequestPydantic
from humanloop.pydantic.model_endpoints import ModelEndpoints as ModelEndpointsPydantic
from humanloop.pydantic.model_providers import ModelProviders as ModelProvidersPydantic
from humanloop.pydantic.chat_message_with_tool_call import ChatMessageWithToolCall as ChatMessageWithToolCallPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = ProjectModelConfigRequestSchema


request_body_project_model_config_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
_auth = [
    'APIKeyHeader',
]
SchemaFor200ResponseBodyApplicationJson = ProjectConfigResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ProjectConfigResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ProjectConfigResponse


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

    def _register_mapped_args(
        self,
        model: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[ModelProviders] = None,
        max_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        other: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        prompt_template: typing.Optional[str] = None,
        chat_template: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        endpoint: typing.Optional[ModelEndpoints] = None,
        tools: typing.Optional[ProjectModelConfigRequestTools] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if description is not None:
            _body["description"] = description
        if name is not None:
            _body["name"] = name
        if provider is not None:
            _body["provider"] = provider
        if model is not None:
            _body["model"] = model
        if max_tokens is not None:
            _body["max_tokens"] = max_tokens
        if temperature is not None:
            _body["temperature"] = temperature
        if top_p is not None:
            _body["top_p"] = top_p
        if stop is not None:
            _body["stop"] = stop
        if presence_penalty is not None:
            _body["presence_penalty"] = presence_penalty
        if frequency_penalty is not None:
            _body["frequency_penalty"] = frequency_penalty
        if other is not None:
            _body["other"] = other
        if seed is not None:
            _body["seed"] = seed
        if response_format is not None:
            _body["response_format"] = response_format
        if project is not None:
            _body["project"] = project
        if project_id is not None:
            _body["project_id"] = project_id
        if prompt_template is not None:
            _body["prompt_template"] = prompt_template
        if chat_template is not None:
            _body["chat_template"] = chat_template
        if endpoint is not None:
            _body["endpoint"] = endpoint
        if tools is not None:
            _body["tools"] = tools
        args.body = _body
        return args

    async def _aregister_oapg(
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
        Register
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
            path_template='/model-configs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_project_model_config_request.serialize(body, content_type)
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


    def _register_oapg(
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
        Register
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
            path_template='/model-configs',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_project_model_config_request.serialize(body, content_type)
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


class RegisterRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aregister(
        self,
        model: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[ModelProviders] = None,
        max_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        other: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        prompt_template: typing.Optional[str] = None,
        chat_template: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        endpoint: typing.Optional[ModelEndpoints] = None,
        tools: typing.Optional[ProjectModelConfigRequestTools] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._register_mapped_args(
            model=model,
            description=description,
            name=name,
            provider=provider,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            other=other,
            seed=seed,
            response_format=response_format,
            project=project,
            project_id=project_id,
            prompt_template=prompt_template,
            chat_template=chat_template,
            endpoint=endpoint,
            tools=tools,
        )
        return await self._aregister_oapg(
            body=args.body,
            **kwargs,
        )
    
    def register(
        self,
        model: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[ModelProviders] = None,
        max_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        other: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        prompt_template: typing.Optional[str] = None,
        chat_template: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        endpoint: typing.Optional[ModelEndpoints] = None,
        tools: typing.Optional[ProjectModelConfigRequestTools] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """ Register a model config to a project.  If the project name provided does not exist, a new project will be created automatically.  If the model config is the first to be associated to the project, it will be set as the active model config. """
        args = self._register_mapped_args(
            model=model,
            description=description,
            name=name,
            provider=provider,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            other=other,
            seed=seed,
            response_format=response_format,
            project=project,
            project_id=project_id,
            prompt_template=prompt_template,
            chat_template=chat_template,
            endpoint=endpoint,
            tools=tools,
        )
        return self._register_oapg(
            body=args.body,
        )

class Register(BaseApi):

    async def aregister(
        self,
        model: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[ModelProviders] = None,
        max_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        other: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        prompt_template: typing.Optional[str] = None,
        chat_template: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        endpoint: typing.Optional[ModelEndpoints] = None,
        tools: typing.Optional[ProjectModelConfigRequestTools] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProjectConfigResponsePydantic:
        raw_response = await self.raw.aregister(
            model=model,
            description=description,
            name=name,
            provider=provider,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            other=other,
            seed=seed,
            response_format=response_format,
            project=project,
            project_id=project_id,
            prompt_template=prompt_template,
            chat_template=chat_template,
            endpoint=endpoint,
            tools=tools,
            **kwargs,
        )
        if validate:
            return ProjectConfigResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectConfigResponsePydantic, raw_response.body)
    
    
    def register(
        self,
        model: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[ModelProviders] = None,
        max_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        other: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        prompt_template: typing.Optional[str] = None,
        chat_template: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        endpoint: typing.Optional[ModelEndpoints] = None,
        tools: typing.Optional[ProjectModelConfigRequestTools] = None,
        validate: bool = False,
    ) -> ProjectConfigResponsePydantic:
        raw_response = self.raw.register(
            model=model,
            description=description,
            name=name,
            provider=provider,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            other=other,
            seed=seed,
            response_format=response_format,
            project=project,
            project_id=project_id,
            prompt_template=prompt_template,
            chat_template=chat_template,
            endpoint=endpoint,
            tools=tools,
        )
        if validate:
            return ProjectConfigResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(ProjectConfigResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        model: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[ModelProviders] = None,
        max_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        other: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        prompt_template: typing.Optional[str] = None,
        chat_template: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        endpoint: typing.Optional[ModelEndpoints] = None,
        tools: typing.Optional[ProjectModelConfigRequestTools] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._register_mapped_args(
            model=model,
            description=description,
            name=name,
            provider=provider,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            other=other,
            seed=seed,
            response_format=response_format,
            project=project,
            project_id=project_id,
            prompt_template=prompt_template,
            chat_template=chat_template,
            endpoint=endpoint,
            tools=tools,
        )
        return await self._aregister_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        model: str,
        description: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        provider: typing.Optional[ModelProviders] = None,
        max_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[typing.Union[int, float]] = None,
        top_p: typing.Optional[typing.Union[int, float]] = None,
        stop: typing.Optional[typing.Union[str, typing.List[str]]] = None,
        presence_penalty: typing.Optional[typing.Union[int, float]] = None,
        frequency_penalty: typing.Optional[typing.Union[int, float]] = None,
        other: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = None,
        seed: typing.Optional[int] = None,
        response_format: typing.Optional[ResponseFormat] = None,
        project: typing.Optional[str] = None,
        project_id: typing.Optional[str] = None,
        prompt_template: typing.Optional[str] = None,
        chat_template: typing.Optional[typing.List[ChatMessageWithToolCall]] = None,
        endpoint: typing.Optional[ModelEndpoints] = None,
        tools: typing.Optional[ProjectModelConfigRequestTools] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """ Register a model config to a project.  If the project name provided does not exist, a new project will be created automatically.  If the model config is the first to be associated to the project, it will be set as the active model config. """
        args = self._register_mapped_args(
            model=model,
            description=description,
            name=name,
            provider=provider,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop,
            presence_penalty=presence_penalty,
            frequency_penalty=frequency_penalty,
            other=other,
            seed=seed,
            response_format=response_format,
            project=project,
            project_id=project_id,
            prompt_template=prompt_template,
            chat_template=chat_template,
            endpoint=endpoint,
            tools=tools,
        )
        return self._register_oapg(
            body=args.body,
        )

