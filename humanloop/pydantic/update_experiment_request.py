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

from humanloop.pydantic.positive_label import PositiveLabel
from humanloop.pydantic.update_experiment_request_config_ids_to_deregister import UpdateExperimentRequestConfigIdsToDeregister
from humanloop.pydantic.update_experiment_request_config_ids_to_register import UpdateExperimentRequestConfigIdsToRegister

class UpdateExperimentRequest(BaseModel):
    # Name of experiment.
    name: typing.Optional[str] = Field(None, alias='name')

    # Feedback labels to treat as positive user feedback. Used to monitor the performance of model configs in the experiment.
    positive_labels: typing.Optional[typing.List[PositiveLabel]] = Field(None, alias='positive_labels')

    config_ids_to_register: typing.Optional[UpdateExperimentRequestConfigIdsToRegister] = Field(None, alias='config_ids_to_register')

    config_ids_to_deregister: typing.Optional[UpdateExperimentRequestConfigIdsToDeregister] = Field(None, alias='config_ids_to_deregister')
