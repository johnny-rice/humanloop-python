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

from humanloop.pydantic.feedback_type import FeedbackType

class FeedbackResponse(BaseModel):
    # The type of feedback. The default feedback types available are 'rating', 'action', 'issue', 'correction', and 'comment'.
    type: typing.Union[FeedbackType, str] = Field(alias='type')

    # The feedback value to set. This would be the appropriate text for 'correction' or 'comment', or a label to apply for 'rating', 'action', or 'issue'.
    value: typing.Union[bool, typing.Union[int, float], typing.List[str], str] = Field(alias='value')

    # String ID of user feedback. Starts with `ann_`, short for annotation.
    id: str = Field(alias='id')

    # ID to associate the feedback to a previously logged datapoint.
    data_id: typing.Optional[str] = Field(None, alias='data_id')

    # A unique identifier to who provided the feedback.
    user: typing.Optional[str] = Field(None, alias='user')

    # User defined timestamp for when the feedback was created. 
    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
