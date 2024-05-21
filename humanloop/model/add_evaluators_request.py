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


class AddEvaluatorsRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def evaluator_ids() -> typing.Type['AddEvaluatorsRequestEvaluatorIds']:
                return AddEvaluatorsRequestEvaluatorIds
        
            @staticmethod
            def evaluator_version_ids() -> typing.Type['AddEvaluatorsRequestEvaluatorVersionIds']:
                return AddEvaluatorsRequestEvaluatorVersionIds
            __annotations__ = {
                "evaluator_ids": evaluator_ids,
                "evaluator_version_ids": evaluator_version_ids,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluator_ids"]) -> 'AddEvaluatorsRequestEvaluatorIds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluator_version_ids"]) -> 'AddEvaluatorsRequestEvaluatorVersionIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["evaluator_ids", "evaluator_version_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluator_ids"]) -> typing.Union['AddEvaluatorsRequestEvaluatorIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluator_version_ids"]) -> typing.Union['AddEvaluatorsRequestEvaluatorVersionIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["evaluator_ids", "evaluator_version_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        evaluator_ids: typing.Union['AddEvaluatorsRequestEvaluatorIds', schemas.Unset] = schemas.unset,
        evaluator_version_ids: typing.Union['AddEvaluatorsRequestEvaluatorVersionIds', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AddEvaluatorsRequest':
        return super().__new__(
            cls,
            *args,
            evaluator_ids=evaluator_ids,
            evaluator_version_ids=evaluator_version_ids,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.add_evaluators_request_evaluator_ids import AddEvaluatorsRequestEvaluatorIds
from humanloop.model.add_evaluators_request_evaluator_version_ids import AddEvaluatorsRequestEvaluatorVersionIds
