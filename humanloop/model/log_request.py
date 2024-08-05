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


class LogRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Request model for logging a datapoint.
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
            save = schemas.BoolSchema
            source_datapoint_id = schemas.StrSchema
            reference_id = schemas.StrSchema
            trial_id = schemas.StrSchema
            
            
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
            
            
            class config(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            ModelConfigRequest,
                            ToolConfigRequest,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'config':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            environment = schemas.StrSchema
            
            
            class feedback(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    
                    class any_of_1(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Feedback']:
                                return Feedback
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['Feedback'], typing.List['Feedback']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'any_of_1':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Feedback':
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
                            Feedback,
                            cls.any_of_1,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'feedback':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                        **kwargs,
                    )
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
                "save": save,
                "source_datapoint_id": source_datapoint_id,
                "reference_id": reference_id,
                "trial_id": trial_id,
                "messages": messages,
                "output": output,
                "judgment": judgment,
                "config_id": config_id,
                "config": config,
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
            }
    
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
    def __getitem__(self, name: typing_extensions.Literal["trial_id"]) -> MetaOapg.properties.trial_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messages"]) -> MetaOapg.properties.messages: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["output"]) -> MetaOapg.properties.output: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["judgment"]) -> MetaOapg.properties.judgment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config_id"]) -> MetaOapg.properties.config_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["config"]) -> MetaOapg.properties.config: ...
    
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
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["project", "project_id", "session_id", "session_reference_id", "parent_id", "parent_reference_id", "inputs", "source", "metadata", "save", "source_datapoint_id", "reference_id", "trial_id", "messages", "output", "judgment", "config_id", "config", "environment", "feedback", "created_at", "error", "stdout", "duration", "output_message", "prompt_tokens", "output_tokens", "prompt_cost", "output_cost", "provider_request", "provider_response", ], str]):
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
    def get_item_oapg(self, name: typing_extensions.Literal["save"]) -> typing.Union[MetaOapg.properties.save, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["source_datapoint_id"]) -> typing.Union[MetaOapg.properties.source_datapoint_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference_id"]) -> typing.Union[MetaOapg.properties.reference_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["trial_id"]) -> typing.Union[MetaOapg.properties.trial_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messages"]) -> typing.Union[MetaOapg.properties.messages, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["output"]) -> typing.Union[MetaOapg.properties.output, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["judgment"]) -> typing.Union[MetaOapg.properties.judgment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config_id"]) -> typing.Union[MetaOapg.properties.config_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["config"]) -> typing.Union[MetaOapg.properties.config, schemas.Unset]: ...
    
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
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["project", "project_id", "session_id", "session_reference_id", "parent_id", "parent_reference_id", "inputs", "source", "metadata", "save", "source_datapoint_id", "reference_id", "trial_id", "messages", "output", "judgment", "config_id", "config", "environment", "feedback", "created_at", "error", "stdout", "duration", "output_message", "prompt_tokens", "output_tokens", "prompt_cost", "output_cost", "provider_request", "provider_response", ], str]):
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
        save: typing.Union[MetaOapg.properties.save, bool, schemas.Unset] = schemas.unset,
        source_datapoint_id: typing.Union[MetaOapg.properties.source_datapoint_id, str, schemas.Unset] = schemas.unset,
        reference_id: typing.Union[MetaOapg.properties.reference_id, str, schemas.Unset] = schemas.unset,
        trial_id: typing.Union[MetaOapg.properties.trial_id, str, schemas.Unset] = schemas.unset,
        messages: typing.Union[MetaOapg.properties.messages, list, tuple, schemas.Unset] = schemas.unset,
        output: typing.Union[MetaOapg.properties.output, str, schemas.Unset] = schemas.unset,
        judgment: typing.Union[MetaOapg.properties.judgment, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        config_id: typing.Union[MetaOapg.properties.config_id, str, schemas.Unset] = schemas.unset,
        config: typing.Union[MetaOapg.properties.config, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        environment: typing.Union[MetaOapg.properties.environment, str, schemas.Unset] = schemas.unset,
        feedback: typing.Union[MetaOapg.properties.feedback, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
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
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LogRequest':
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
            save=save,
            source_datapoint_id=source_datapoint_id,
            reference_id=reference_id,
            trial_id=trial_id,
            messages=messages,
            output=output,
            judgment=judgment,
            config_id=config_id,
            config=config,
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
            _configuration=_configuration,
            **kwargs,
        )

from humanloop.model.chat_message_with_tool_call import ChatMessageWithToolCall
from humanloop.model.feedback import Feedback
from humanloop.model.model_config_request import ModelConfigRequest
from humanloop.model.tool_config_request import ToolConfigRequest
