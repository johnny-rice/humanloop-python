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


class MetricValueResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "metric_id",
            "metric_name",
            "metric_value",
        }
        
        class properties:
            metric_id = schemas.StrSchema
            metric_name = schemas.StrSchema
            metric_value = schemas.NumberSchema
            __annotations__ = {
                "metric_id": metric_id,
                "metric_name": metric_name,
                "metric_value": metric_value,
            }
    
    metric_id: MetaOapg.properties.metric_id
    metric_name: MetaOapg.properties.metric_name
    metric_value: MetaOapg.properties.metric_value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metric_id"]) -> MetaOapg.properties.metric_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metric_name"]) -> MetaOapg.properties.metric_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metric_value"]) -> MetaOapg.properties.metric_value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["metric_id", "metric_name", "metric_value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metric_id"]) -> MetaOapg.properties.metric_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metric_name"]) -> MetaOapg.properties.metric_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metric_value"]) -> MetaOapg.properties.metric_value: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["metric_id", "metric_name", "metric_value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        metric_id: typing.Union[MetaOapg.properties.metric_id, str, ],
        metric_name: typing.Union[MetaOapg.properties.metric_name, str, ],
        metric_value: typing.Union[MetaOapg.properties.metric_value, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MetricValueResponse':
        return super().__new__(
            cls,
            *args,
            metric_id=metric_id,
            metric_name=metric_name,
            metric_value=metric_value,
            _configuration=_configuration,
            **kwargs,
        )
