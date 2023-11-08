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
from typing_extensions import TypedDict, Literal
from pydantic import BaseModel, Field, RootModel

from humanloop.pydantic.chat_message import ChatMessage
from humanloop.pydantic.chat_role import ChatRole
from humanloop.pydantic.create_datapoint_request import CreateDatapointRequest
from humanloop.pydantic.create_datapoint_request_inputs import CreateDatapointRequestInputs
from humanloop.pydantic.create_datapoint_request_target import CreateDatapointRequestTarget
from humanloop.pydantic.create_datapoints_by_logs_request import CreateDatapointsByLogsRequest
from humanloop.pydantic.create_datapoints_by_logs_request_log_ids import CreateDatapointsByLogsRequestLogIds
from humanloop.pydantic.tool_call import ToolCall

DatasetsCreateDatapointRequest = typing.Union[CreateDatapointsByLogsRequest,CreateDatapointRequest,typing.List[CreateDatapointRequest]]
