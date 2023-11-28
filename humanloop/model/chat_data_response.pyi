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


class ChatDataResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Overwrite DataResponse for chat.
    """


    class MetaOapg:
        required = {
            "output",
            "model_config_id",
            "raw_output",
            "index",
            "id",
            "output_message",
        }
        
        class properties:
            id = schemas.StrSchema
            index = schemas.IntSchema
            output = schemas.StrSchema
            raw_output = schemas.StrSchema
            model_config_id = schemas.StrSchema
            
            
            class output_message(
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
                            ChatMessage,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'output_message':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            inputs = schemas.DictSchema
            finish_reason = schemas.StrSchema
            
            
            class tool_results(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ToolResultResponse']:
                        return ToolResultResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ToolResultResponse'], typing.List['ToolResultResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tool_results':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ToolResultResponse':
                    return super().__getitem__(i)
            
            
            class messages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ChatMessage']:
                        return ChatMessage
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ChatMessage'], typing.List['ChatMessage']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'messages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChatMessage':
                    return super().__getitem__(i)
            
            
            class tool_call(
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
                            FunctionTool,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'tool_call':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            
            
            class tool_calls(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ToolCall']:
                        return ToolCall
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ToolCall'], typing.List['ToolCall']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tool_calls':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ToolCall':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "index": index,
                "output": output,
                "raw_output": raw_output,
                "model_config_id": model_config_id,
                "output_message": output_message,
                "inputs": inputs,
                "finish_reason": finish_reason,
                "tool_results": tool_results,
                "messages": messages,
                "tool_call": tool_call,
                "tool_calls": tool_calls,
            }
    
    output: MetaOapg.properties.output
    model_config_id: MetaOapg.properties.model_config_id
    raw_output: MetaOapg.properties.raw_output
    index: MetaOapg.properties.index
    id: MetaOapg.properties.id
    output_message: MetaOapg.properties.output_message
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["index"]) -> MetaOapg.properties.index: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output"]) -> MetaOapg.properties.output: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw_output"]) -> MetaOapg.properties.raw_output: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["model_config_id"]) -> MetaOapg.properties.model_config_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output_message"]) -> MetaOapg.properties.output_message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inputs"]) -> MetaOapg.properties.inputs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finish_reason"]) -> MetaOapg.properties.finish_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tool_results"]) -> MetaOapg.properties.tool_results: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messages"]) -> MetaOapg.properties.messages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tool_call"]) -> MetaOapg.properties.tool_call: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tool_calls"]) -> MetaOapg.properties.tool_calls: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "index", "output", "raw_output", "model_config_id", "output_message", "inputs", "finish_reason", "tool_results", "messages", "tool_call", "tool_calls", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["index"]) -> MetaOapg.properties.index: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output"]) -> MetaOapg.properties.output: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw_output"]) -> MetaOapg.properties.raw_output: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["model_config_id"]) -> MetaOapg.properties.model_config_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output_message"]) -> MetaOapg.properties.output_message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inputs"]) -> typing.Union[MetaOapg.properties.inputs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finish_reason"]) -> typing.Union[MetaOapg.properties.finish_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tool_results"]) -> typing.Union[MetaOapg.properties.tool_results, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messages"]) -> typing.Union[MetaOapg.properties.messages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tool_call"]) -> typing.Union[MetaOapg.properties.tool_call, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tool_calls"]) -> typing.Union[MetaOapg.properties.tool_calls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "index", "output", "raw_output", "model_config_id", "output_message", "inputs", "finish_reason", "tool_results", "messages", "tool_call", "tool_calls", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        output: typing.Union[MetaOapg.properties.output, str, ],
        model_config_id: typing.Union[MetaOapg.properties.model_config_id, str, ],
        raw_output: typing.Union[MetaOapg.properties.raw_output, str, ],
        index: typing.Union[MetaOapg.properties.index, decimal.Decimal, int, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        output_message: typing.Union[MetaOapg.properties.output_message, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        inputs: typing.Union[MetaOapg.properties.inputs, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        finish_reason: typing.Union[MetaOapg.properties.finish_reason, str, schemas.Unset] = schemas.unset,
        tool_results: typing.Union[MetaOapg.properties.tool_results, list, tuple, schemas.Unset] = schemas.unset,
        messages: typing.Union[MetaOapg.properties.messages, list, tuple, schemas.Unset] = schemas.unset,
        tool_call: typing.Union[MetaOapg.properties.tool_call, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        tool_calls: typing.Union[MetaOapg.properties.tool_calls, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ChatDataResponse':
        return super().__new__(
            cls,
            *args,
            output=output,
            model_config_id=model_config_id,
            raw_output=raw_output,
            index=index,
            id=id,
            output_message=output_message,
            inputs=inputs,
            finish_reason=finish_reason,
            tool_results=tool_results,
            messages=messages,
            tool_call=tool_call,
            tool_calls=tool_calls,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.chat_message import ChatMessage
from humanloop.model.function_tool import FunctionTool
from humanloop.model.tool_call import ToolCall
from humanloop.model.tool_result_response import ToolResultResponse
