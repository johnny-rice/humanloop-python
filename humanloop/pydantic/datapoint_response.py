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
from humanloop.pydantic.datapoint_response_inputs import DatapointResponseInputs
from humanloop.pydantic.datapoint_response_target import DatapointResponseTarget

class DatapointResponse(BaseModel):
    id: str = Field(alias='id')

    dataset_id: typing.Optional[str] = Field(None, alias='dataset_id')

    inputs: typing.Optional[DatapointResponseInputs] = Field(None, alias='inputs')

    messages: typing.Optional[typing.List[ChatMessageWithToolCall]] = Field(None, alias='messages')

    target: typing.Optional[DatapointResponseTarget] = Field(None, alias='target')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
