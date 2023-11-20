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

from humanloop.pydantic.chat_data_response import ChatDataResponse
from humanloop.pydantic.chat_response_provider_responses import ChatResponseProviderResponses
from humanloop.pydantic.tool_choice import ToolChoice
from humanloop.pydantic.usage import Usage

class ChatResponse(BaseModel):
    # Array containing the chat responses.
    data: typing.List[ChatDataResponse] = Field(alias='data')

    provider_responses: ChatResponseProviderResponses = Field(alias='provider_responses')

    # Unique identifier of the parent project. Will not be provided if the request was made without providing a project name or id
    project_id: typing.Optional[str] = Field(None, alias='project_id')

    # The number of chat responses.
    num_samples: typing.Optional[int] = Field(None, alias='num_samples')

    # Include the log probabilities of the top n tokens in the provider_response
    logprobs: typing.Optional[int] = Field(None, alias='logprobs')

    # The suffix that comes after a completion of inserted text. Useful for completions that act like inserts.
    suffix: typing.Optional[str] = Field(None, alias='suffix')

    # End-user ID passed through to provider call.
    user: typing.Optional[str] = Field(None, alias='user')

    # Counts of the number of tokens used and related stats.
    usage: typing.Optional[Usage] = Field(None, alias='usage')

    # Any additional metadata to record.
    metadata: typing.Optional[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]] = Field(None, alias='metadata')

    # Controls how the model uses tools. The following options are supported: 'none' forces the model to not call a tool; the default when no tools are provided as part of the model config. 'auto' the model can decide to call one of the provided tools; the default when tools are provided as part of the model config. Providing {'type': 'function', 'function': {name': <TOOL_NAME>}} forces the model to use the named function.
    tool_choice: typing.Optional[typing.Union[str, str, ToolChoice]] = Field(None, alias='tool_choice')
