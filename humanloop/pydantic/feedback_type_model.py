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

from humanloop.pydantic.categorical_feedback_label import CategoricalFeedbackLabel
from humanloop.pydantic.feedback_type import FeedbackType
from humanloop.pydantic.label_sentiment import LabelSentiment

class FeedbackTypeModel(BaseModel):
    # The type of feedback. The default feedback types available are 'rating', 'action', 'issue', 'correction', and 'comment'.
    type: typing.Union[FeedbackType, str] = Field(alias='type')

    # The allowed values for categorical feedback types. Not populated for `correction` and `comment`.
    values: typing.List[CategoricalFeedbackLabel] = Field(None, alias='values')
