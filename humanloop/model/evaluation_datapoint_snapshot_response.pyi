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


class EvaluationDatapointSnapshotResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "datapoint",
            "evaluation_results",
        }
        
        class properties:
        
            @staticmethod
            def datapoint() -> typing.Type['DatapointResponse']:
                return DatapointResponse
            
            
            class evaluation_results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['EvaluationResultResponse']:
                        return EvaluationResultResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['EvaluationResultResponse'], typing.List['EvaluationResultResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'evaluation_results':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'EvaluationResultResponse':
                    return super().__getitem__(i)
        
            @staticmethod
            def log() -> typing.Type['LogResponse']:
                return LogResponse
            __annotations__ = {
                "datapoint": datapoint,
                "evaluation_results": evaluation_results,
                "log": log,
            }
    
    datapoint: 'DatapointResponse'
    evaluation_results: MetaOapg.properties.evaluation_results
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["datapoint"]) -> 'DatapointResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluation_results"]) -> MetaOapg.properties.evaluation_results: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["log"]) -> 'LogResponse': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["datapoint", "evaluation_results", "log", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["datapoint"]) -> 'DatapointResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluation_results"]) -> MetaOapg.properties.evaluation_results: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["log"]) -> typing.Union['LogResponse', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["datapoint", "evaluation_results", "log", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        datapoint: 'DatapointResponse',
        evaluation_results: typing.Union[MetaOapg.properties.evaluation_results, list, tuple, ],
        log: typing.Union['LogResponse', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'EvaluationDatapointSnapshotResponse':
        return super().__new__(
            cls,
            *args,
            datapoint=datapoint,
            evaluation_results=evaluation_results,
            log=log,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.datapoint_response import DatapointResponse
from humanloop.model.evaluation_result_response import EvaluationResultResponse
from humanloop.model.log_response import LogResponse
