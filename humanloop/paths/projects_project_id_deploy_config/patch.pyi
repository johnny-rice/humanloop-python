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

from humanloop.model.projects_deploy_config_to_environments_response import ProjectsDeployConfigToEnvironmentsResponse as ProjectsDeployConfigToEnvironmentsResponseSchema
from humanloop.model.environment_request import EnvironmentRequest as EnvironmentRequestSchema
from humanloop.model.http_validation_error import HTTPValidationError as HTTPValidationErrorSchema
from humanloop.model.environment_project_config_request import EnvironmentProjectConfigRequest as EnvironmentProjectConfigRequestSchema

from humanloop.type.projects_deploy_config_to_environments_response import ProjectsDeployConfigToEnvironmentsResponse
from humanloop.type.environment_request import EnvironmentRequest
from humanloop.type.http_validation_error import HTTPValidationError
from humanloop.type.environment_project_config_request import EnvironmentProjectConfigRequest

from ...api_client import Dictionary
from humanloop.pydantic.environment_project_config_request import EnvironmentProjectConfigRequest as EnvironmentProjectConfigRequestPydantic
from humanloop.pydantic.http_validation_error import HTTPValidationError as HTTPValidationErrorPydantic
from humanloop.pydantic.environment_request import EnvironmentRequest as EnvironmentRequestPydantic
from humanloop.pydantic.projects_deploy_config_to_environments_response import ProjectsDeployConfigToEnvironmentsResponse as ProjectsDeployConfigToEnvironmentsResponsePydantic

# Path params
ProjectIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'project_id': typing.Union[ProjectIdSchema, str, ],
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


request_path_project_id = api_client.PathParameter(
    name="project_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ProjectIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = EnvironmentProjectConfigRequestSchema


request_body_environment_project_config_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = ProjectsDeployConfigToEnvironmentsResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ProjectsDeployConfigToEnvironmentsResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ProjectsDeployConfigToEnvironmentsResponse


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

    def _deploy_config_mapped_args(
        self,
        project_id: str,
        config_id: typing.Optional[str] = None,
        experiment_id: typing.Optional[str] = None,
        environments: typing.Optional[typing.List[EnvironmentRequest]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if config_id is not None:
            _body["config_id"] = config_id
        if experiment_id is not None:
            _body["experiment_id"] = experiment_id
        if environments is not None:
            _body["environments"] = environments
        args.body = _body
        if project_id is not None:
            _path_params["project_id"] = project_id
        args.path = _path_params
        return args

    async def _adeploy_config_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Deploy Config
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
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
        serialized_data = request_body_environment_project_config_request.serialize(body, content_type)
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


    def _deploy_config_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
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
        Deploy Config
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_project_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'patch'.upper()
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
        serialized_data = request_body_environment_project_config_request.serialize(body, content_type)
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


class DeployConfigRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def adeploy_config(
        self,
        project_id: str,
        config_id: typing.Optional[str] = None,
        experiment_id: typing.Optional[str] = None,
        environments: typing.Optional[typing.List[EnvironmentRequest]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._deploy_config_mapped_args(
            project_id=project_id,
            config_id=config_id,
            experiment_id=experiment_id,
            environments=environments,
        )
        return await self._adeploy_config_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def deploy_config(
        self,
        project_id: str,
        config_id: typing.Optional[str] = None,
        experiment_id: typing.Optional[str] = None,
        environments: typing.Optional[typing.List[EnvironmentRequest]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._deploy_config_mapped_args(
            project_id=project_id,
            config_id=config_id,
            experiment_id=experiment_id,
            environments=environments,
        )
        return self._deploy_config_oapg(
            body=args.body,
            path_params=args.path,
        )

class DeployConfig(BaseApi):

    async def adeploy_config(
        self,
        project_id: str,
        config_id: typing.Optional[str] = None,
        experiment_id: typing.Optional[str] = None,
        environments: typing.Optional[typing.List[EnvironmentRequest]] = None,
        validate: bool = False,
        **kwargs,
    ) -> ProjectsDeployConfigToEnvironmentsResponsePydantic:
        raw_response = await self.raw.adeploy_config(
            project_id=project_id,
            config_id=config_id,
            experiment_id=experiment_id,
            environments=environments,
            **kwargs,
        )
        if validate:
            return RootModel[ProjectsDeployConfigToEnvironmentsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ProjectsDeployConfigToEnvironmentsResponsePydantic, raw_response.body)
    
    
    def deploy_config(
        self,
        project_id: str,
        config_id: typing.Optional[str] = None,
        experiment_id: typing.Optional[str] = None,
        environments: typing.Optional[typing.List[EnvironmentRequest]] = None,
        validate: bool = False,
    ) -> ProjectsDeployConfigToEnvironmentsResponsePydantic:
        raw_response = self.raw.deploy_config(
            project_id=project_id,
            config_id=config_id,
            experiment_id=experiment_id,
            environments=environments,
        )
        if validate:
            return RootModel[ProjectsDeployConfigToEnvironmentsResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(ProjectsDeployConfigToEnvironmentsResponsePydantic, raw_response.body)


class ApiForpatch(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apatch(
        self,
        project_id: str,
        config_id: typing.Optional[str] = None,
        experiment_id: typing.Optional[str] = None,
        environments: typing.Optional[typing.List[EnvironmentRequest]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._deploy_config_mapped_args(
            project_id=project_id,
            config_id=config_id,
            experiment_id=experiment_id,
            environments=environments,
        )
        return await self._adeploy_config_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def patch(
        self,
        project_id: str,
        config_id: typing.Optional[str] = None,
        experiment_id: typing.Optional[str] = None,
        environments: typing.Optional[typing.List[EnvironmentRequest]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._deploy_config_mapped_args(
            project_id=project_id,
            config_id=config_id,
            experiment_id=experiment_id,
            environments=environments,
        )
        return self._deploy_config_oapg(
            body=args.body,
            path_params=args.path,
        )

