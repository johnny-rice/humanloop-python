# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

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


class CompletionDeployedRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Completion request using the project's active deployment.
    """


    class MetaOapg:
        
        class properties:
            project = schemas.StrSchema
            project_id = schemas.StrSchema
            session_id = schemas.StrSchema
            session_reference_id = schemas.StrSchema
            parent_id = schemas.StrSchema
            parent_reference_id = schemas.StrSchema
            inputs = schemas.DictSchema
            source = schemas.StrSchema
            metadata = schemas.DictSchema
            
            
            class provider_api_keys(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            ProviderApiKeys,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'provider_api_keys':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            num_samples = schemas.IntSchema
            logprobs = schemas.IntSchema
            stream = schemas.BoolSchema
            suffix = schemas.StrSchema
            seed = schemas.IntSchema
            user = schemas.StrSchema
            environment = schemas.StrSchema
            __annotations__ = {
                "project": project,
                "project_id": project_id,
                "session_id": session_id,
                "session_reference_id": session_reference_id,
                "parent_id": parent_id,
                "parent_reference_id": parent_reference_id,
                "inputs": inputs,
                "source": source,
                "metadata": metadata,
                "provider_api_keys": provider_api_keys,
                "num_samples": num_samples,
                "logprobs": logprobs,
                "stream": stream,
                "suffix": suffix,
                "seed": seed,
                "user": user,
                "environment": environment,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project"]) -> MetaOapg.properties.project: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["project_id"]) -> MetaOapg.properties.project_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session_id"]) -> MetaOapg.properties.session_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["session_reference_id"]) -> MetaOapg.properties.session_reference_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_id"]) -> MetaOapg.properties.parent_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parent_reference_id"]) -> MetaOapg.properties.parent_reference_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputs"]) -> MetaOapg.properties.inputs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source"]) -> MetaOapg.properties.source: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metadata"]) -> MetaOapg.properties.metadata: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_api_keys"]) -> MetaOapg.properties.provider_api_keys: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["num_samples"]) -> MetaOapg.properties.num_samples: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logprobs"]) -> MetaOapg.properties.logprobs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stream"]) -> MetaOapg.properties.stream: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suffix"]) -> MetaOapg.properties.suffix: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seed"]) -> MetaOapg.properties.seed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> MetaOapg.properties.environment: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["project"], typing_extensions.Literal["project_id"], typing_extensions.Literal["session_id"], typing_extensions.Literal["session_reference_id"], typing_extensions.Literal["parent_id"], typing_extensions.Literal["parent_reference_id"], typing_extensions.Literal["inputs"], typing_extensions.Literal["source"], typing_extensions.Literal["metadata"], typing_extensions.Literal["provider_api_keys"], typing_extensions.Literal["num_samples"], typing_extensions.Literal["logprobs"], typing_extensions.Literal["stream"], typing_extensions.Literal["suffix"], typing_extensions.Literal["seed"], typing_extensions.Literal["user"], typing_extensions.Literal["environment"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project"]) -> typing.Union[MetaOapg.properties.project, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["project_id"]) -> typing.Union[MetaOapg.properties.project_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session_id"]) -> typing.Union[MetaOapg.properties.session_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["session_reference_id"]) -> typing.Union[MetaOapg.properties.session_reference_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_id"]) -> typing.Union[MetaOapg.properties.parent_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parent_reference_id"]) -> typing.Union[MetaOapg.properties.parent_reference_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputs"]) -> typing.Union[MetaOapg.properties.inputs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source"]) -> typing.Union[MetaOapg.properties.source, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metadata"]) -> typing.Union[MetaOapg.properties.metadata, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_api_keys"]) -> typing.Union[MetaOapg.properties.provider_api_keys, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["num_samples"]) -> typing.Union[MetaOapg.properties.num_samples, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logprobs"]) -> typing.Union[MetaOapg.properties.logprobs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stream"]) -> typing.Union[MetaOapg.properties.stream, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suffix"]) -> typing.Union[MetaOapg.properties.suffix, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seed"]) -> typing.Union[MetaOapg.properties.seed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> typing.Union[MetaOapg.properties.environment, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["project"], typing_extensions.Literal["project_id"], typing_extensions.Literal["session_id"], typing_extensions.Literal["session_reference_id"], typing_extensions.Literal["parent_id"], typing_extensions.Literal["parent_reference_id"], typing_extensions.Literal["inputs"], typing_extensions.Literal["source"], typing_extensions.Literal["metadata"], typing_extensions.Literal["provider_api_keys"], typing_extensions.Literal["num_samples"], typing_extensions.Literal["logprobs"], typing_extensions.Literal["stream"], typing_extensions.Literal["suffix"], typing_extensions.Literal["seed"], typing_extensions.Literal["user"], typing_extensions.Literal["environment"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        project: typing.Union[MetaOapg.properties.project, str, schemas.Unset] = schemas.unset,
        project_id: typing.Union[MetaOapg.properties.project_id, str, schemas.Unset] = schemas.unset,
        session_id: typing.Union[MetaOapg.properties.session_id, str, schemas.Unset] = schemas.unset,
        session_reference_id: typing.Union[MetaOapg.properties.session_reference_id, str, schemas.Unset] = schemas.unset,
        parent_id: typing.Union[MetaOapg.properties.parent_id, str, schemas.Unset] = schemas.unset,
        parent_reference_id: typing.Union[MetaOapg.properties.parent_reference_id, str, schemas.Unset] = schemas.unset,
        inputs: typing.Union[MetaOapg.properties.inputs, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        provider_api_keys: typing.Union[MetaOapg.properties.provider_api_keys, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        num_samples: typing.Union[MetaOapg.properties.num_samples, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        logprobs: typing.Union[MetaOapg.properties.logprobs, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        stream: typing.Union[MetaOapg.properties.stream, bool, schemas.Unset] = schemas.unset,
        suffix: typing.Union[MetaOapg.properties.suffix, str, schemas.Unset] = schemas.unset,
        seed: typing.Union[MetaOapg.properties.seed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        environment: typing.Union[MetaOapg.properties.environment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs,
    ) -> 'CompletionDeployedRequest':
        return super().__new__(
            cls,
            *args,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            provider_api_keys=provider_api_keys,
            num_samples=num_samples,
            logprobs=logprobs,
            stream=stream,
            suffix=suffix,
            seed=seed,
            user=user,
            environment=environment,
            _configuration=_configuration,
        )

from humanloop.model.provider_api_keys import ProviderApiKeys
