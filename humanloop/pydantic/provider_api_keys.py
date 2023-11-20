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


class ProviderApiKeys(BaseModel):
    openai: typing.Optional[str] = Field(None, alias='openai')

    ai21: typing.Optional[str] = Field(None, alias='ai21')

    mock: typing.Optional[str] = Field(None, alias='mock')

    anthropic: typing.Optional[str] = Field(None, alias='anthropic')

    cohere: typing.Optional[str] = Field(None, alias='cohere')

    openai_azure: typing.Optional[str] = Field(None, alias='openai_azure')

    openai_azure_endpoint: typing.Optional[str] = Field(None, alias='openai_azure_endpoint')
