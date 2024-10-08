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

from humanloop.pydantic.config_type import ConfigType
from humanloop.pydantic.evaluator_response import EvaluatorResponse
from humanloop.pydantic.feedback_types import FeedbackTypes
from humanloop.pydantic.project_config_response import ProjectConfigResponse
from humanloop.pydantic.project_user_response import ProjectUserResponse

class ProjectResponse(BaseModel):
    # Project ID
    id: str = Field(alias='id')

    # Unique project name.
    name: str = Field(alias='name')

    # Users associated to the project.
    users: typing.List[ProjectUserResponse] = Field(alias='users')

    # The count of datapoints that have been logged to the project.
    data_count: int = Field(alias='data_count')

    # The feedback types that have been defined in the project.
    feedback_types: FeedbackTypes = Field(alias='feedback_types')

    # Unique ID of the team the project belongs to. Starts with `tm_`.
    team_id: str = Field(alias='team_id')

    created_at: datetime = Field(alias='created_at')

    updated_at: datetime = Field(alias='updated_at')

    # Config that has been set as the project's active deployment.
    active_config: typing.Optional[ProjectConfigResponse] = Field(None, alias='active_config')

    config_type: typing.Optional[ConfigType] = Field(None, alias='config_type')

    # Evaluators that have been set as active for the project.
    active_evaluators: typing.Optional['typing.List[EvaluatorResponse]'] = Field(None, alias='active_evaluators')

    # String ID of the directory the project belongs to. Starts with `dir_`.
    directory_id: typing.Optional[str] = Field(None, alias='directory_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
