# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.completion.post import Create
from humanloop.paths.completion_deployed.post import CreateDeployed
from humanloop.paths.completion_experiment.post import CreateExperiment
from humanloop.paths.completion_model_config.post import CreateModelConfig
from humanloop.apis.tags.completions_api_raw import CompletionsApiRaw


class CompletionsApi(
    Create,
    CreateDeployed,
    CreateExperiment,
    CreateModelConfig,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: CompletionsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = CompletionsApiRaw(api_client)
