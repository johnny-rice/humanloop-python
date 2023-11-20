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

from humanloop.pydantic.feedback_class import FeedbackClass
from humanloop.pydantic.feedback_label_request import FeedbackLabelRequest

class FeedbackTypeRequest(BaseModel):
    # The type of feedback to update.
    type: str = Field(alias='type')

    # The feedback values to be available. This field should only be populated when updating a 'select' or 'multi_select' feedback class.
    values: typing.Optional[typing.List[FeedbackLabelRequest]] = Field(None, alias='values')

    # The data type associated to this feedback type; whether it is a 'text'/'select'/'multi_select'. This is optional when updating the default feedback types (i.e. when `type` is 'rating', 'action' or 'issue').
    class_: typing.Optional[FeedbackClass] = Field(None, alias='class')
