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

from humanloop.type.create_evaluation_request_evaluator_ids import CreateEvaluationRequestEvaluatorIds
from humanloop.type.provider_api_keys import ProviderApiKeys

class RequiredCreateEvaluationRequest(TypedDict):
    # ID of the config to evaluate. Starts with `config_`.
    config_id: str

    evaluator_ids: CreateEvaluationRequestEvaluatorIds

    # ID of the dataset to use in this evaluation. Starts with `evts_`.
    dataset_id: str


class OptionalCreateEvaluationRequest(TypedDict, total=False):
    # API keys required by each provider to make API calls. The API keys provided here are not stored by Humanloop. If not specified here, Humanloop will fall back to the key saved to your organization. Ensure you provide an API key for the provider for the model config you are evaluating, or have one saved to your organization.
    provider_api_keys: ProviderApiKeys

    # Whether the log generations for this evaluation should be performed by Humanloop. If `False`, the log generations should be submitted by the user via the API.
    hl_generated: bool

    # Name of the Evaluation to help identify it.
    name: str

class CreateEvaluationRequest(RequiredCreateEvaluationRequest, OptionalCreateEvaluationRequest):
    pass
