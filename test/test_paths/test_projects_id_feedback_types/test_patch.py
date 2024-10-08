# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python or TypeScript SDK.  To install the official [Python SDK](https://pypi.org/project/humanloop/), run the following command:  ```bash pip install humanloop ```  To install the official [TypeScript SDK](https://www.npmjs.com/package/humanloop), run the following command:  ```bash npm i humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://docs.humanloop.com/).

    The version of the OpenAPI document: 4.0.1
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import humanloop
from humanloop.paths.projects_id_feedback_types import patch
from humanloop import configuration, schemas, api_client

from .. import ApiTestMixin


class TestProjectsIdFeedbackTypes(ApiTestMixin, unittest.TestCase):
    """
    ProjectsIdFeedbackTypes unit test stubs
        Update Feedback Types
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
