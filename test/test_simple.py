# coding: utf-8

"""
    Humanloop API

    The Humanloop API allows you to interact with Humanloop from your product or service.  You can do this through HTTP requests from any language or via our official Python SDK.  To install the official Python SDK, run the following command:  ```bash pip install humanloop ```  ---  Guides and further details about key concepts can be found in [our docs](https://humanloop.gitbook.io/humanloop-docs/).

    The version of the OpenAPI document: 4.0.0
    Generated by: https://konfigthis.com
"""

import unittest
from humanloop.api_response import AsyncGeneratorResponse
import pytest
from unittest.mock import MagicMock, call

from humanloop import Humanloop
from humanloop.exceptions import MissingRequiredParametersError
from humanloop.client_custom import _parse_sse_chunk

import os

from humanloop.model.completion_request import CompletionRequest


class TestSimple(unittest.TestCase):
    def setUp(self):
        self.humanloop = Humanloop(
            # host="https://neostaging.humanloop.ml/v4",
            host="http://127.0.0.1:4010",
            api_key=os.environ["HUMANLOOP_API_KEY"],
            openai_api_key=os.environ["OPENAI_API_KEY"],
        )
        pass

    def tearDown(self):
        pass

    def test_pydantic_with_string_type_hints(self):
        logs_response = self.humanloop.logs.list(project_id="id")
        self.assertIsNotNone(logs_response)

    def test_deserialize_and_register(self):
        prompt = """
        ---
        model: gpt-3.5-turbo-16k
        temperature: 0.0
        max_tokens: -1
        top_p: 1.0
        presence_penalty: 0.0
        frequency_penalty: 0.0
        provider: openai
        endpoint: chat
        tools: []
        ---

        <system>
        You are a helpful assistant.
        </system>

        <user>
        Hello there!
        </user>
        """
        result = self.humanloop.model_configs.deserialize(prompt)
        model_config = result.model_dump()
        PROJECT_NAME = "test"
        PROJECT_ID = "test"
        model_config["name"] = PROJECT_NAME
        for key in [
            "id",
            "tool_configs",
            "tools",
            "type",
        ]:
            model_config.pop(key)

        is_chat = model_config["endpoint"] == "chat"
        if is_chat:
            for template_message in model_config["chat_template"]:
                # THIS SHOULD NOT BE NECESSARY
                # for k in ["tool_call"]:
                #     template_message.pop(k)
                pass
        else:
            for key in ["chat_template"]:
                model_config.pop(key)

        project_config_response = self.humanloop.model_configs.register(
            project_id=PROJECT_ID, **model_config
        )

    @pytest.mark.skip(reason="moving target so not a consistent test")
    def test_complete_arguments(self):
        # assert that "self.humanloop.generate()" throws a "MissingRequiredParametersError" error
        with self.assertRaises(TypeError) as context:
            self.humanloop.complete()
        self.assertTrue(
            "complete() missing 3 required positional arguments: 'project', 'inputs', and 'model_config'"
            in str(context.exception)
        )

    def test_unexpected_keyword_argument_is_not_raised(self):
        self.humanloop.model_configs.register(
            project="project_id",
            model="gpt-4",
            name="Entity extractor v0",
            chat_template=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Read the user's message and "
                    "extract any features or issues mentioned in json format.",
                }
            ],
        )

    def test_parse_sse_chunk(self):
        payload = '{"username": "phoenix", "time": "01:23:45", "text": "Hey hey hey. Here is some cool data: Venus is the only planet to spin clockwise!"}'
        data = ('data: ' + payload).encode("utf-8")
        parsed = _parse_sse_chunk(data)
        self.assertEqual(parsed, payload)

    def test_log_delete(self):
        response = self.humanloop.logs.delete(id=["test"])
        self.assertIsNone(response)

    def test_log_delete_raw(self):
        response = self.humanloop.logs.raw.delete(id=["test"])
        self.assertIsNotNone(response)

    def test_sessions_list(self):
        response = self.humanloop.sessions.list("test")
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.page)

    def test_chat(self):
        response = self.humanloop.chat(
            project="konfig-dev-001",
            messages=[
                {
                    "role": "system",
                    "content": "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
                },
                {"role": "user", "content": "Hello!"},
            ],
            model_config={
                "model": "gpt-3.5-turbo",
                "max_tokens": 1000,
                "temperature": 1,
            },
        )
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data[0].id)

    def test_datapoints_delete(self):
        response = self.humanloop.datapoints.delete(["test"])
        self.assertIsNone(response)

    def test_datapoints_get(self):
        response = self.humanloop.datapoints.get("test")
        self.assertIsNotNone(response)
        self.assertIsNotNone(response.id)
        self.assertIsNotNone(response.messages[0].content)

    def test_datasets_list_for_all_projects(self):
        response = self.humanloop.datasets.list_all_for_project("test")
        self.assertIsNotNone(response)
        self.assertIsNotNone(response[0].id)

    def test_complete(self):
        response: AsyncGeneratorResponse = self.humanloop.complete(
            project="konfig-dev-001",
            inputs={"question": "How should I think about competition for my startup?"},
            model_config={
                "model": "text-davinci-003",
                "prompt_template": "{{question}}",
            },
        )  # type: ignore

    def test_experiment_create(self):
        response = self.humanloop.experiments.create(
            name='test',
            positive_labels=[{"type": 'test', "value": 'test'}],
            project_id="test"
        )
        self.assertIsNotNone(response.id)

    def test_experiment_delete(self):
        response = self.humanloop.experiments.delete(
            experiment_id="test"
        )
        self.assertIsNone(response)

    def test_chat_model_config(self):
        response = self.humanloop.chat_model_config(
            model_config_id="test",
            messages=[
                {"role": "system"}
            ]
        )
        self.assertIsNotNone(response.provider_responses)

    @pytest.mark.skip(reason="circular reference is not supported for mock server")
    def test_projects_create(self):
        response = self.humanloop.projects.create("test")
        self.assertIsNotNone(response.id)

    @pytest.mark.skip(reason="circular reference is not supported for mock server")
    def test_projects_list(self):
        self.humanloop.projects.list(page=1, size=10)

    def test_generate_kwargs(self):
        self.humanloop.completions.create(
            model_config={"model": "test", "prompt_template": "{{question}}"},
            inputs={},
            project="test",
        )

    def test_projects_update_feedback_type(self):
        self.humanloop.projects.update_feedback_types(
            body=[{"class": "text", "type": "test"}], id="test"
        )
        self.humanloop.projects.update_feedback_types([], id="test")


humanloop = Humanloop(
    # host="https://neostaging.humanloop.ml/v4",
    host="http://127.0.0.1:4010",
    api_key=os.environ["HUMANLOOP_API_KEY"],
)


@pytest.mark.asyncio
async def test_chat_stream():
    humanloop = Humanloop(
        host="https://neostaging.humanloop.ml/v4",
        api_key=os.environ["HUMANLOOP_API_KEY"],
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )
    response: AsyncGeneratorResponse = await humanloop.chat_stream(
        project="konfig-dev-001",
        messages=[
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
            },
            {"role": "user", "content": "Write me a country song"},
        ],
        model_config={
            "model": "gpt-3.5-turbo",
            "max_tokens": 1000,
            "temperature": 1,
        },
    )  # type: ignore

    lines = []
    async for line in response.content:
        lines.append(line)
        assert "project_id" in line

    assert len(lines) > 1
    assert response.status == 200
    assert response is not None


@pytest.mark.asyncio
async def test_chat():
    humanloop = Humanloop(
        host="https://neostaging.humanloop.ml/v4",
        api_key=os.environ["HUMANLOOP_API_KEY"],
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )
    response = await humanloop.achat(
        project="konfig-dev-001",
        messages=[
            {
                "role": "system",
                "content": "You are ChatGPT, a large language model trained by OpenAI. Follow the user's instructions carefully. Respond using markdown.",
            },
            {"role": "user", "content": "Hello!"},
        ],
        model_config={
            "model": "gpt-3.5-turbo",
            "max_tokens": 1000,
            "temperature": 1,
        },
    )
    assert response is not None
    assert response.data[0].id is not None

@pytest.mark.asyncio
async def test_model_configs_register():
    humanloop = Humanloop(
        host="http://127.0.0.1:4010",
        api_key=os.environ["HUMANLOOP_API_KEY"],
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )
    response = humanloop.model_configs.register(
        project="project_id",
        model="gpt-4",
        name="Entity extractor v0",
        chat_template=[
            {
                "role": "system",
                "content": "You are a helpful assistant. Read the user's message and "
                "extract any features or issues mentioned in json format.",
            }
        ],
    )
    assert response is not None

@pytest.mark.asyncio
async def test_complete_stream():
    humanloop = Humanloop(
        host="https://neostaging.humanloop.ml/v4",
        api_key=os.environ["HUMANLOOP_API_KEY"],
        openai_api_key=os.environ["OPENAI_API_KEY"],
    )
    response: AsyncGeneratorResponse = await humanloop.complete_stream(
        project="konfig-dev-001",
        inputs={"question": "How should I think about competition for my startup?"},
        model_config={"model": "gpt-3.5-turbo", "prompt_template": "{{question}}"},
    )  # type: ignore

    lines = []
    async for line in response.content:
        assert line["id"] is not None
        assert line["output"] is not None
        lines.append(line)

    assert len(lines) > 1
    assert response.status == 200
    assert response is not None


@pytest.mark.asyncio
@pytest.mark.skip(reason="circular reference is not supported for mock server")
async def test_projects_list_async():
    response = await humanloop.projects.alist(page=1, size=10)
    assert response.records is not None


@pytest.mark.asyncio
@pytest.mark.skip(reason="circular reference is not supported for mock server")
async def test_projects_update_async():
    response = await humanloop.projects.aupdate(id="project_id")
    assert response.id is not None


@pytest.mark.asyncio
@pytest.mark.skip(reason="circular reference is not supported for mock server")
async def test_projects_delete_async():
    response = await humanloop.projects.adeactivate_experiment(id="project_id")
    assert response is not None


@pytest.mark.asyncio
async def test_log_async():
    response = humanloop.log(output="example", project="test")
    response = await humanloop.alog(output="example", project="test")
    assert response is not None


if __name__ == "__main__":
    unittest.main()
