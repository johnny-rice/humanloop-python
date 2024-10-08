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


class EvaluationResultResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "evaluator_version_id",
            "log_id",
            "updated_at",
            "evaluator_id",
            "created_at",
            "id",
        }
        
        class properties:
            id = schemas.StrSchema
            evaluator_id = schemas.StrSchema
            evaluator_version_id = schemas.StrSchema
            log_id = schemas.StrSchema
            updated_at = schemas.DateTimeSchema
            created_at = schemas.DateTimeSchema
            version = schemas.AnyTypeSchema
            evaluation_id = schemas.StrSchema
        
            @staticmethod
            def log() -> typing.Type['LogResponse']:
                return LogResponse
            version_id = schemas.StrSchema
            
            
            class value(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_0 = schemas.BoolSchema
                    any_of_1 = schemas.NumberSchema
                    items = schemas.StrSchema
                    
                    
                    class any_of_3(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_3':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    
                    @classmethod
                    @functools.lru_cache()
                    def any_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            cls.any_of_0,
                            cls.any_of_1,
                            cls.items,
                            cls.any_of_3,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'value':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            error = schemas.StrSchema
        
            @staticmethod
            def evaluator_log() -> typing.Type['LogResponse']:
                return LogResponse
            __annotations__ = {
                "id": id,
                "evaluator_id": evaluator_id,
                "evaluator_version_id": evaluator_version_id,
                "log_id": log_id,
                "updated_at": updated_at,
                "created_at": created_at,
                "version": version,
                "evaluation_id": evaluation_id,
                "log": log,
                "version_id": version_id,
                "value": value,
                "error": error,
                "evaluator_log": evaluator_log,
            }
    
    evaluator_version_id: MetaOapg.properties.evaluator_version_id
    log_id: MetaOapg.properties.log_id
    updated_at: MetaOapg.properties.updated_at
    evaluator_id: MetaOapg.properties.evaluator_id
    created_at: MetaOapg.properties.created_at
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluator_id"]) -> MetaOapg.properties.evaluator_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluator_version_id"]) -> MetaOapg.properties.evaluator_version_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log_id"]) -> MetaOapg.properties.log_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluation_id"]) -> MetaOapg.properties.evaluation_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log"]) -> 'LogResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version_id"]) -> MetaOapg.properties.version_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluator_log"]) -> 'LogResponse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "evaluator_id", "evaluator_version_id", "log_id", "updated_at", "created_at", "version", "evaluation_id", "log", "version_id", "value", "error", "evaluator_log", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluator_id"]) -> MetaOapg.properties.evaluator_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluator_version_id"]) -> MetaOapg.properties.evaluator_version_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log_id"]) -> MetaOapg.properties.log_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> typing.Union[MetaOapg.properties.version, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluation_id"]) -> typing.Union[MetaOapg.properties.evaluation_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log"]) -> typing.Union['LogResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version_id"]) -> typing.Union[MetaOapg.properties.version_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluator_log"]) -> typing.Union['LogResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "evaluator_id", "evaluator_version_id", "log_id", "updated_at", "created_at", "version", "evaluation_id", "log", "version_id", "value", "error", "evaluator_log", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        evaluator_version_id: typing.Union[MetaOapg.properties.evaluator_version_id, str, ],
        log_id: typing.Union[MetaOapg.properties.log_id, str, ],
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        evaluator_id: typing.Union[MetaOapg.properties.evaluator_id, str, ],
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        version: typing.Union[MetaOapg.properties.version, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        evaluation_id: typing.Union[MetaOapg.properties.evaluation_id, str, schemas.Unset] = schemas.unset,
        log: typing.Union['LogResponse', schemas.Unset] = schemas.unset,
        version_id: typing.Union[MetaOapg.properties.version_id, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        evaluator_log: typing.Union['LogResponse', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EvaluationResultResponse':
        return super().__new__(
            cls,
            *args,
            evaluator_version_id=evaluator_version_id,
            log_id=log_id,
            updated_at=updated_at,
            evaluator_id=evaluator_id,
            created_at=created_at,
            id=id,
            version=version,
            evaluation_id=evaluation_id,
            log=log,
            version_id=version_id,
            value=value,
            error=error,
            evaluator_log=evaluator_log,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.log_response import LogResponse
