# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from humanloop.pydantic.chat_message_with_tool_call import ChatMessageWithToolCall
from humanloop.pydantic.feedback import Feedback
from humanloop.pydantic.model_config_request import ModelConfigRequest
from humanloop.pydantic.tool_config_request import ToolConfigRequest

class LogRequest(BaseModel):
    # Unique project name. If no project exists with this name, a new project will be created.
    project: typing.Optional[str] = Field(None, alias='project')

    # Unique ID of a project to associate to the log. Either this or `project` must be provided.
    project_id: typing.Optional[str] = Field(None, alias='project_id')

    # ID of the session to associate the datapoint.
    session_id: typing.Optional[str] = Field(None, alias='session_id')

    # A unique string identifying the session to associate the datapoint to. Allows you to log multiple datapoints to a session (using an ID kept by your internal systems) by passing the same `session_reference_id` in subsequent log requests. Specify at most one of this or `session_id`.
    session_reference_id: typing.Optional[str] = Field(None, alias='session_reference_id')

    # ID associated to the parent datapoint in a session.
    parent_id: typing.Optional[str] = Field(None, alias='parent_id')

    # A unique string identifying the previously-logged parent datapoint in a session. Allows you to log nested datapoints with your internal system IDs by passing the same reference ID as `parent_id` in a prior log request. Specify at most one of this or `parent_id`. Note that this cannot refer to a datapoint being logged in the same request.
    parent_reference_id: typing.Optional[str] = Field(None, alias='parent_reference_id')

    # The inputs passed to the prompt template.
    inputs: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='inputs')

    # Identifies where the model was called from.
    source: typing.Optional[str] = Field(None, alias='source')

    # Any additional metadata to record.
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    # Whether the request/response payloads will be stored on Humanloop.
    save: typing.Optional[bool] = Field(None, alias='save')

    # ID of the source datapoint if this is a log derived from a datapoint in a dataset.
    source_datapoint_id: typing.Optional[str] = Field(None, alias='source_datapoint_id')

    # A unique string to reference the datapoint. Allows you to log nested datapoints with your internal system IDs by passing the same reference ID as `parent_id` in a subsequent log request.
    reference_id: typing.Optional[str] = Field(None, alias='reference_id')

    # The messages passed to the to provider chat endpoint.
    messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = Field(None, alias='messages')

    # Generated output from your model for the provided inputs. Can be `None` if logging an error, or if logging a parent datapoint with the intention to populate it later
    output: typing.Optional[str] = Field(None, alias='output')

    judgment: typing.Optional[typing.Union[bool, typing.Union[int, float], typing.List[str], str]] = Field(None, alias='judgment')

    # Unique ID of a config to associate to the log.
    config_id: typing.Optional[str] = Field(None, alias='config_id')

    # The model config used for this generation. Required unless `config_id` is provided.
    config: typing.Optional[typing.Union[ModelConfigRequest, ToolConfigRequest]] = Field(None, alias='config')

    # The environment name used to create the log.
    environment: typing.Optional[str] = Field(None, alias='environment')

    # Optional parameter to provide feedback with your logged datapoint.
    feedback: typing.Optional[typing.Union[Feedback, typing.List[Feedback]]] = Field(None, alias='feedback')

    # User defined timestamp for when the log was created. 
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    # Error message if the log is an error.
    error: typing.Optional[str] = Field(None, alias='error')

    # Captured log and debug statements.
    stdout: typing.Optional[str] = Field(None, alias='stdout')

    # Duration of the logged event in seconds.
    duration: typing.Optional[typing.Union[int, float]] = Field(None, alias='duration')

    # The message returned by the provider.
    output_message: typing.Optional[ChatMessageWithToolCall] = Field(None, alias='output_message')

    # Number of tokens in the prompt used to generate the output.
    prompt_tokens: typing.Optional[int] = Field(None, alias='prompt_tokens')

    # Number of tokens in the output generated by the model.
    output_tokens: typing.Optional[int] = Field(None, alias='output_tokens')

    # Cost in dollars associated to the tokens in the prompt.
    prompt_cost: typing.Optional[typing.Union[int, float]] = Field(None, alias='prompt_cost')

    # Cost in dollars associated to the tokens in the output.
    output_cost: typing.Optional[typing.Union[int, float]] = Field(None, alias='output_cost')

    # Raw request sent to provider.
    provider_request: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='provider_request')

    # Raw response received the provider.
    provider_response: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='provider_response')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
