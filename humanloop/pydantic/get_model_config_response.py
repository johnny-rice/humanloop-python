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

from humanloop.pydantic.config_response import ConfigResponse
from humanloop.pydantic.model_config_evaluator_aggregate_response import ModelConfigEvaluatorAggregateResponse

class GetModelConfigResponse(BaseModel):
    # String ID of project the model config belongs to. Starts with `pr_`.
    project_id: str = Field(alias='project_id')

    # Name of the project the model config belongs to.
    project_name: str = Field(alias='project_name')

    created_at: datetime = Field(alias='created_at')

    updated_at: datetime = Field(alias='updated_at')

    last_used: datetime = Field(alias='last_used')

    config: ConfigResponse = Field(alias='config')

    # Number of datapoints associated with this project model config.
    num_datapoints: typing.Optional[int] = Field(None, alias='num_datapoints')

    # Aggregates of evaluators for the model config.
    evaluation_aggregates: typing.Optional[typing.List[ModelConfigEvaluatorAggregateResponse]] = Field(None, alias='evaluation_aggregates')

    # ID of environment to reference in subsequent log calls.
    environment_id: typing.Optional[str] = Field(None, alias='environment_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
