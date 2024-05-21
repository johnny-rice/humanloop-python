# coding: utf-8
"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.evaluations_id_evaluators.patch import AddEvaluators
from humanloop.paths.projects_project_id_evaluations.post import Create
from humanloop.paths.evaluations_id.get import Get
from humanloop.paths.evaluations.get import List
from humanloop.paths.projects_project_id_evaluations.get import ListAllForProject
from humanloop.paths.evaluations_id_datapoints.get import ListDatapoints
from humanloop.paths.evaluations_evaluation_id_log.post import Log
from humanloop.paths.evaluations_evaluation_id_result.post import Result
from humanloop.paths.evaluations_id_status.patch import UpdateStatus
from humanloop.apis.tags.evaluations_api_raw import EvaluationsApiRaw


class EvaluationsApiGenerated(
    AddEvaluators,
    Create,
    Get,
    List,
    ListAllForProject,
    ListDatapoints,
    Log,
    Result,
    UpdateStatus,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: EvaluationsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = EvaluationsApiRaw(api_client)
