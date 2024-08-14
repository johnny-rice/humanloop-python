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


class LogResponse(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Request model for logging a datapoint.
    """


    class MetaOapg:
        required = {
            "observability_status",
            "updated_at",
            "evaluation_results",
            "id",
            "config",
        }
        
        class properties:
            id = schemas.StrSchema
        
            @staticmethod
            def config() -> typing.Type['ConfigResponse']:
                return ConfigResponse
            
            
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
            def observability_status() -> typing.Type['ObservabilityStatus']:
                return ObservabilityStatus
            updated_at = schemas.DateTimeSchema
            project = schemas.StrSchema
            project_id = schemas.StrSchema
            session_id = schemas.StrSchema
            session_reference_id = schemas.StrSchema
            parent_id = schemas.StrSchema
            parent_reference_id = schemas.StrSchema
            inputs = schemas.DictSchema
            source = schemas.StrSchema
            metadata = schemas.DictSchema
            save = schemas.BoolSchema
            source_datapoint_id = schemas.StrSchema
            reference_id = schemas.StrSchema
            
            
            class messages(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ChatMessageWithToolCall']:
                        return ChatMessageWithToolCall
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ChatMessageWithToolCall'], typing.List['ChatMessageWithToolCall']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'messages':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ChatMessageWithToolCall':
                    return super().__getitem__(i)
            output = schemas.StrSchema
            
            
            class judgment(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    any_of_0 = schemas.BoolSchema
                    any_of_1 = schemas.NumberSchema
                    
                    
                    class any_of_2(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            items = schemas.StrSchema
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_2':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> MetaOapg.items:
                            return super().__getitem__(i)
                    items = schemas.StrSchema
                    
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
                            cls.any_of_2,
                            cls.items,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'judgment':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            config_id = schemas.StrSchema
            environment = schemas.StrSchema
            
            
            class feedback(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FeedbackResponse']:
                        return FeedbackResponse
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['FeedbackResponse'], typing.List['FeedbackResponse']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'feedback':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FeedbackResponse':
                    return super().__getitem__(i)
            created_at = schemas.DateTimeSchema
            error = schemas.StrSchema
            stdout = schemas.StrSchema
            duration = schemas.NumberSchema
        
            @staticmethod
            def output_message() -> typing.Type['ChatMessageWithToolCall']:
                return ChatMessageWithToolCall
            prompt_tokens = schemas.IntSchema
            output_tokens = schemas.IntSchema
            prompt_cost = schemas.NumberSchema
            output_cost = schemas.NumberSchema
            provider_request = schemas.DictSchema
            provider_response = schemas.DictSchema
            user = schemas.StrSchema
            provider_latency = schemas.NumberSchema
            tokens = schemas.IntSchema
            raw_output = schemas.StrSchema
            finish_reason = schemas.StrSchema
            
            
            class tools(
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
                ) -> 'tools':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ToolResultResponse':
                    return super().__getitem__(i)
            
            
            class tool_choice(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_0(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "none": "NONE",
                            }
                        
                        @schemas.classproperty
                        def NONE(cls):
                            return cls("none")
                    
                    
                    class any_of_1(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "auto": "AUTO",
                            }
                        
                        @schemas.classproperty
                        def AUTO(cls):
                            return cls("auto")
                    
                    
                    class any_of_2(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "required": "REQUIRED",
                            }
                        
                        @schemas.classproperty
                        def REQUIRED(cls):
                            return cls("required")
                    
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
                            cls.any_of_2,
                            ToolChoice,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'tool_choice':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
        
            @staticmethod
            def batch_ids() -> typing.Type['LogResponseBatchIds']:
                return LogResponseBatchIds
            __annotations__ = {
                "id": id,
                "config": config,
                "evaluation_results": evaluation_results,
                "observability_status": observability_status,
                "updated_at": updated_at,
                "project": project,
                "project_id": project_id,
                "session_id": session_id,
                "session_reference_id": session_reference_id,
                "parent_id": parent_id,
                "parent_reference_id": parent_reference_id,
                "inputs": inputs,
                "source": source,
                "metadata": metadata,
                "save": save,
                "source_datapoint_id": source_datapoint_id,
                "reference_id": reference_id,
                "messages": messages,
                "output": output,
                "judgment": judgment,
                "config_id": config_id,
                "environment": environment,
                "feedback": feedback,
                "created_at": created_at,
                "error": error,
                "stdout": stdout,
                "duration": duration,
                "output_message": output_message,
                "prompt_tokens": prompt_tokens,
                "output_tokens": output_tokens,
                "prompt_cost": prompt_cost,
                "output_cost": output_cost,
                "provider_request": provider_request,
                "provider_response": provider_response,
                "user": user,
                "provider_latency": provider_latency,
                "tokens": tokens,
                "raw_output": raw_output,
                "finish_reason": finish_reason,
                "tools": tools,
                "tool_choice": tool_choice,
                "batch_ids": batch_ids,
            }
    
    observability_status: 'ObservabilityStatus'
    updated_at: MetaOapg.properties.updated_at
    evaluation_results: MetaOapg.properties.evaluation_results
    id: MetaOapg.properties.id
    config: 'ConfigResponse'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> 'ConfigResponse': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["evaluation_results"]) -> MetaOapg.properties.evaluation_results: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["observability_status"]) -> 'ObservabilityStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
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
    def __getitem__(self, name: typing_extensions.Literal["save"]) -> MetaOapg.properties.save: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["source_datapoint_id"]) -> MetaOapg.properties.source_datapoint_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference_id"]) -> MetaOapg.properties.reference_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messages"]) -> MetaOapg.properties.messages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output"]) -> MetaOapg.properties.output: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["judgment"]) -> MetaOapg.properties.judgment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config_id"]) -> MetaOapg.properties.config_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["environment"]) -> MetaOapg.properties.environment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["feedback"]) -> MetaOapg.properties.feedback: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["error"]) -> MetaOapg.properties.error: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stdout"]) -> MetaOapg.properties.stdout: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> MetaOapg.properties.duration: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output_message"]) -> 'ChatMessageWithToolCall': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_tokens"]) -> MetaOapg.properties.prompt_tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output_tokens"]) -> MetaOapg.properties.output_tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["prompt_cost"]) -> MetaOapg.properties.prompt_cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output_cost"]) -> MetaOapg.properties.output_cost: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_request"]) -> MetaOapg.properties.provider_request: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_response"]) -> MetaOapg.properties.provider_response: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider_latency"]) -> MetaOapg.properties.provider_latency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tokens"]) -> MetaOapg.properties.tokens: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw_output"]) -> MetaOapg.properties.raw_output: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["finish_reason"]) -> MetaOapg.properties.finish_reason: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tools"]) -> MetaOapg.properties.tools: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tool_choice"]) -> MetaOapg.properties.tool_choice: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["batch_ids"]) -> 'LogResponseBatchIds': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "config", "evaluation_results", "observability_status", "updated_at", "project", "project_id", "session_id", "session_reference_id", "parent_id", "parent_reference_id", "inputs", "source", "metadata", "save", "source_datapoint_id", "reference_id", "messages", "output", "judgment", "config_id", "environment", "feedback", "created_at", "error", "stdout", "duration", "output_message", "prompt_tokens", "output_tokens", "prompt_cost", "output_cost", "provider_request", "provider_response", "user", "provider_latency", "tokens", "raw_output", "finish_reason", "tools", "tool_choice", "batch_ids", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> 'ConfigResponse': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["evaluation_results"]) -> MetaOapg.properties.evaluation_results: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["observability_status"]) -> 'ObservabilityStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
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
    def get_item_oapg(self, name: typing_extensions.Literal["save"]) -> typing.Union[MetaOapg.properties.save, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_datapoint_id"]) -> typing.Union[MetaOapg.properties.source_datapoint_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference_id"]) -> typing.Union[MetaOapg.properties.reference_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messages"]) -> typing.Union[MetaOapg.properties.messages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output"]) -> typing.Union[MetaOapg.properties.output, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["judgment"]) -> typing.Union[MetaOapg.properties.judgment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config_id"]) -> typing.Union[MetaOapg.properties.config_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["environment"]) -> typing.Union[MetaOapg.properties.environment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["feedback"]) -> typing.Union[MetaOapg.properties.feedback, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["error"]) -> typing.Union[MetaOapg.properties.error, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stdout"]) -> typing.Union[MetaOapg.properties.stdout, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> typing.Union[MetaOapg.properties.duration, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output_message"]) -> typing.Union['ChatMessageWithToolCall', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_tokens"]) -> typing.Union[MetaOapg.properties.prompt_tokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output_tokens"]) -> typing.Union[MetaOapg.properties.output_tokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["prompt_cost"]) -> typing.Union[MetaOapg.properties.prompt_cost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output_cost"]) -> typing.Union[MetaOapg.properties.output_cost, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_request"]) -> typing.Union[MetaOapg.properties.provider_request, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_response"]) -> typing.Union[MetaOapg.properties.provider_response, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> typing.Union[MetaOapg.properties.user, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider_latency"]) -> typing.Union[MetaOapg.properties.provider_latency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tokens"]) -> typing.Union[MetaOapg.properties.tokens, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw_output"]) -> typing.Union[MetaOapg.properties.raw_output, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["finish_reason"]) -> typing.Union[MetaOapg.properties.finish_reason, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tools"]) -> typing.Union[MetaOapg.properties.tools, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tool_choice"]) -> typing.Union[MetaOapg.properties.tool_choice, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["batch_ids"]) -> typing.Union['LogResponseBatchIds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "config", "evaluation_results", "observability_status", "updated_at", "project", "project_id", "session_id", "session_reference_id", "parent_id", "parent_reference_id", "inputs", "source", "metadata", "save", "source_datapoint_id", "reference_id", "messages", "output", "judgment", "config_id", "environment", "feedback", "created_at", "error", "stdout", "duration", "output_message", "prompt_tokens", "output_tokens", "prompt_cost", "output_cost", "provider_request", "provider_response", "user", "provider_latency", "tokens", "raw_output", "finish_reason", "tools", "tool_choice", "batch_ids", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        observability_status: 'ObservabilityStatus',
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, ],
        evaluation_results: typing.Union[MetaOapg.properties.evaluation_results, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        config: 'ConfigResponse',
        project: typing.Union[MetaOapg.properties.project, str, schemas.Unset] = schemas.unset,
        project_id: typing.Union[MetaOapg.properties.project_id, str, schemas.Unset] = schemas.unset,
        session_id: typing.Union[MetaOapg.properties.session_id, str, schemas.Unset] = schemas.unset,
        session_reference_id: typing.Union[MetaOapg.properties.session_reference_id, str, schemas.Unset] = schemas.unset,
        parent_id: typing.Union[MetaOapg.properties.parent_id, str, schemas.Unset] = schemas.unset,
        parent_reference_id: typing.Union[MetaOapg.properties.parent_reference_id, str, schemas.Unset] = schemas.unset,
        inputs: typing.Union[MetaOapg.properties.inputs, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        source: typing.Union[MetaOapg.properties.source, str, schemas.Unset] = schemas.unset,
        metadata: typing.Union[MetaOapg.properties.metadata, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        save: typing.Union[MetaOapg.properties.save, bool, schemas.Unset] = schemas.unset,
        source_datapoint_id: typing.Union[MetaOapg.properties.source_datapoint_id, str, schemas.Unset] = schemas.unset,
        reference_id: typing.Union[MetaOapg.properties.reference_id, str, schemas.Unset] = schemas.unset,
        messages: typing.Union[MetaOapg.properties.messages, list, tuple, schemas.Unset] = schemas.unset,
        output: typing.Union[MetaOapg.properties.output, str, schemas.Unset] = schemas.unset,
        judgment: typing.Union[MetaOapg.properties.judgment, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        config_id: typing.Union[MetaOapg.properties.config_id, str, schemas.Unset] = schemas.unset,
        environment: typing.Union[MetaOapg.properties.environment, str, schemas.Unset] = schemas.unset,
        feedback: typing.Union[MetaOapg.properties.feedback, list, tuple, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        error: typing.Union[MetaOapg.properties.error, str, schemas.Unset] = schemas.unset,
        stdout: typing.Union[MetaOapg.properties.stdout, str, schemas.Unset] = schemas.unset,
        duration: typing.Union[MetaOapg.properties.duration, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        output_message: typing.Union['ChatMessageWithToolCall', schemas.Unset] = schemas.unset,
        prompt_tokens: typing.Union[MetaOapg.properties.prompt_tokens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        output_tokens: typing.Union[MetaOapg.properties.output_tokens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        prompt_cost: typing.Union[MetaOapg.properties.prompt_cost, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        output_cost: typing.Union[MetaOapg.properties.output_cost, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        provider_request: typing.Union[MetaOapg.properties.provider_request, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        provider_response: typing.Union[MetaOapg.properties.provider_response, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        user: typing.Union[MetaOapg.properties.user, str, schemas.Unset] = schemas.unset,
        provider_latency: typing.Union[MetaOapg.properties.provider_latency, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        tokens: typing.Union[MetaOapg.properties.tokens, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        raw_output: typing.Union[MetaOapg.properties.raw_output, str, schemas.Unset] = schemas.unset,
        finish_reason: typing.Union[MetaOapg.properties.finish_reason, str, schemas.Unset] = schemas.unset,
        tools: typing.Union[MetaOapg.properties.tools, list, tuple, schemas.Unset] = schemas.unset,
        tool_choice: typing.Union[MetaOapg.properties.tool_choice, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        batch_ids: typing.Union['LogResponseBatchIds', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogResponse':
        return super().__new__(
            cls,
            *args,
            observability_status=observability_status,
            updated_at=updated_at,
            evaluation_results=evaluation_results,
            id=id,
            config=config,
            project=project,
            project_id=project_id,
            session_id=session_id,
            session_reference_id=session_reference_id,
            parent_id=parent_id,
            parent_reference_id=parent_reference_id,
            inputs=inputs,
            source=source,
            metadata=metadata,
            save=save,
            source_datapoint_id=source_datapoint_id,
            reference_id=reference_id,
            messages=messages,
            output=output,
            judgment=judgment,
            config_id=config_id,
            environment=environment,
            feedback=feedback,
            created_at=created_at,
            error=error,
            stdout=stdout,
            duration=duration,
            output_message=output_message,
            prompt_tokens=prompt_tokens,
            output_tokens=output_tokens,
            prompt_cost=prompt_cost,
            output_cost=output_cost,
            provider_request=provider_request,
            provider_response=provider_response,
            user=user,
            provider_latency=provider_latency,
            tokens=tokens,
            raw_output=raw_output,
            finish_reason=finish_reason,
            tools=tools,
            tool_choice=tool_choice,
            batch_ids=batch_ids,
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.chat_message_with_tool_call import ChatMessageWithToolCall
from humanloop.model.config_response import ConfigResponse
from humanloop.model.evaluation_result_response import EvaluationResultResponse
from humanloop.model.feedback_response import FeedbackResponse
from humanloop.model.log_response_batch_ids import LogResponseBatchIds
from humanloop.model.observability_status import ObservabilityStatus
from humanloop.model.tool_choice import ToolChoice
from humanloop.model.tool_result_response import ToolResultResponse
