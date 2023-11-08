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
from typing_extensions import TypedDict, Literal
from pydantic import BaseModel, Field, RootModel

from humanloop.pydantic.chat_message import ChatMessage
from humanloop.pydantic.chat_role import ChatRole
from humanloop.pydantic.tool_call import ToolCall
from humanloop.pydantic.tool_result_response import ToolResultResponse

class ChatDataResponse(BaseModel):
    # Unique ID for the model inputs and output logged to Humanloop. Use this when recording feedback later.
    id: str = Field(alias='id')

    # The index for the sampled generation for a given input. The num_samples request parameter controls how many samples are generated.
    index: int = Field(alias='index')

    # Output text returned from the provider model with leading and trailing whitespaces stripped.
    output: str = Field(alias='output')

    # Raw output text returned from the provider model.
    raw_output: str = Field(alias='raw_output')

    # The model configuration used to create the generation.
    model_config_id_: str = Field(alias='model_config_id')

    # The inputs passed to the chat template.
    inputs: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]] = Field(None, alias='inputs')

    # Why the generation ended. One of 'stop' (indicating a stop token was encountered), or 'length' (indicating the max tokens limit has been reached), or 'tool_call' (indicating that the model has chosen to call a tool - in which case the tool_call parameter of the response will be populated). It will be set as null for the intermediary responses during a stream, and will only be set as non-null for the final streamed token.
    finish_reason: str = Field(None, alias='finish_reason')

    # Results of any tools run during the generation.
    tool_results: typing.List[ToolResultResponse] = Field(None, alias='tool_results')

    # The messages passed to the to provider chat endpoint.
    messages: typing.List[ChatMessage] = Field(None, alias='messages')

    # JSON definition of the tool to call and the corresponding argument values. Will be populated when finish_reason='tool_call'.
    tool_call: ToolCall = Field(None, alias='tool_call')
