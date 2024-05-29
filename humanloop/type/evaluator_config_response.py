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

from humanloop.type.evaluator_arguments_type import EvaluatorArgumentsType
from humanloop.type.evaluator_return_type_enum import EvaluatorReturnTypeEnum
from humanloop.type.model_config_response import ModelConfigResponse
from humanloop.type.user_response import UserResponse

class RequiredEvaluatorConfigResponse(TypedDict):
    # String ID of config. Starts with `config_`.
    id: str

    type: str

    # Whether the config is committed or not.
    status: str

    # Name of config.
    name: str

    # Type of evaluator.
    evaluator_type: str


class OptionalEvaluatorConfigResponse(TypedDict, total=False):
    # Description of config.
    description: str

    # Other parameters that define the config.
    other: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

    # The user who created the config.
    created_by: UserResponse

    # The model config defining the LLM evaluator.
    model_config: ModelConfigResponse

    # The code for the evaluator. This code will be executed in a sandboxed environment.
    code: str

    # Whether this evaluator is target-free or target-required.
    arguments_type: EvaluatorArgumentsType

    # The type of the return value of the evaluator.
    return_type: EvaluatorReturnTypeEnum

class EvaluatorConfigResponse(RequiredEvaluatorConfigResponse, OptionalEvaluatorConfigResponse):
    pass