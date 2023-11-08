# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

from humanloop.paths.datapoints.delete import Delete
from humanloop.paths.datapoints_id.get import Get
from humanloop.paths.datapoints_id.patch import Update
from humanloop.apis.tags.datapoints_api_raw import DatapointsApiRaw


class DatapointsApi(
    Delete,
    Get,
    Update,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: DatapointsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = DatapointsApiRaw(api_client)
