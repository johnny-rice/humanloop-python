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


class RequiredImageUrl(TypedDict):
    # Either a URL of the image or the base64 encoded image data.
    url: str

class OptionalImageUrl(TypedDict, total=False):
    # Specify the detail level of the image provided to the model. For more details see: https://platform.openai.com/docs/guides/vision/low-or-high-fidelity-image-understanding
    detail: str

class ImageUrl(RequiredImageUrl, OptionalImageUrl):
    pass
