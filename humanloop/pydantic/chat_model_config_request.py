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
from pydantic import BaseModel, Field, RootModel

from humanloop.pydantic.chat_message import ChatMessage
from humanloop.pydantic.provider_api_keys import ProviderApiKeys
from humanloop.pydantic.response_format import ResponseFormat
from humanloop.pydantic.tool_choice import ToolChoice

class ChatModelConfigRequest(BaseModel):
    # The messages passed to the to provider chat endpoint.
    messages: typing.List[ChatMessage] = Field(alias='messages')

    # Identifies the model configuration used to create a chat response.
    model_config_id_: str = Field(alias='model_config_id')

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

    # API keys required by each provider to make API calls. The API keys provided here are not stored by Humanloop. If not specified here, Humanloop will fall back to the key saved to your organization.
    provider_api_keys: typing.Optional[ProviderApiKeys] = Field(None, alias='provider_api_keys')

    # The number of chat responses.
    num_samples: typing.Optional[int] = Field(None, alias='num_samples')

    # If true, tokens will be sent as data-only server-sent events. If num_samples > 1, samples are streamed back independently.
    stream: typing.Optional[bool] = Field(None, alias='stream')

    # End-user ID passed through to provider call.
    user: typing.Optional[str] = Field(None, alias='user')

    # Controls how the model uses tools. The following options are supported: 'none' forces the model to not call a tool; the default when no tools are provided as part of the model config. 'auto' the model can decide to call one of the provided tools; the default when tools are provided as part of the model config. Providing {'type': 'function', 'function': {name': <TOOL_NAME>}} forces the model to use the named function.
    tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = Field(None, alias='tool_choice')

    # NB: Deprecated with new tool_choice. Controls how the model uses tools. The following options are supported: 'none' forces the model to not call a tool; the default when no tools are provided as part of the model config. 'auto' the model can decide to call one of the provided tools; the default when tools are provided as part of the model config. Providing {'name': <TOOL_NAME>} forces the model to use the provided tool of the same name.
    tool_call: typing.Optional[typing.Union[str, typing.Dict[str, str]]] = Field(None, alias='tool_call')

    # If specified, model will make a best effort to sample deterministically, but it is not guaranteed.
    seed: typing.Optional[int] = Field(None, alias='seed')

    # The format of the response. Only type json_object is currently supported for chat.
    response_format: typing.Optional[ResponseFormat] = Field(None, alias='response_format')
