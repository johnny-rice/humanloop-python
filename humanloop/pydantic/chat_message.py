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

from humanloop.pydantic.chat_role import ChatRole
from humanloop.pydantic.function_tool import FunctionTool
from humanloop.pydantic.image_chat_content import ImageChatContent
from humanloop.pydantic.text_chat_content import TextChatContent
from humanloop.pydantic.tool_call import ToolCall

class ChatMessage(BaseModel):
    # Role of the message author.
    role: ChatRole = Field(alias='role')

    # The content of the message.
    content: typing.Optional[typing.Union[str, typing.List[typing.Union[typing.List[TextChatContent], typing.List[ImageChatContent]]]]] = Field(None, alias='content')

    # Optional name of the message author.
    name: typing.Optional[typing.Optional[str]] = Field(None, alias='name')

    # Tool call that this message is responding to.
    tool_call_id: typing.Optional[typing.Optional[str]] = Field(None, alias='tool_call_id')

    # NB: Deprecated in favour of tool_calls. A tool call requested by the assistant.
    tool_call: typing.Optional[FunctionTool] = Field(None, alias='tool_call')

    # A list of tool calls requested by the assistant.
    tool_calls: typing.Optional[typing.Optional[typing.List[ToolCall]]] = Field(None, alias='tool_calls')
