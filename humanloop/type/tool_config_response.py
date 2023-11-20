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


class RequiredToolConfigResponse(TypedDict):
    # String ID of config. Starts with `config_`.
    id: str

    type: str

    # Name for the tool referenced by the model
    name: str

class OptionalToolConfigResponse(TypedDict, total=False):
    # Description of the tool referenced by the model
    description: str

    # Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/
    parameters: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Other parameters that define the config.
    other: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # Code source of the tool.
    source: str

    # Definition of parameters needed to run the tool. Provided in jsonschema format: https://json-schema.org/
    setup_schema: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The function signature of the tool when being called.
    signature: str

    # Whether the tool is one where Humanloop defines runtime or not.
    is_preset: bool

    # If is_preset = true, this is the name of the preset tool on Humanloop. This is used as the key to lookup the Humanloop runtime of the tool
    preset_name: str

class ToolConfigResponse(RequiredToolConfigResponse, OptionalToolConfigResponse):
    pass
