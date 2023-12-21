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


class RequiredToolResponse(TypedDict):
    # The ID of the tool. Starts with either `config_` or `oc_`.
    id: str

    # Name for the tool referenced by the model.
    name: str

class OptionalToolResponse(TypedDict, total=False):
    # Description of the tool referenced by the model
    description: str

    # Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/
    parameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The origin of the tool
    source: str

class ToolResponse(RequiredToolResponse, OptionalToolResponse):
    pass