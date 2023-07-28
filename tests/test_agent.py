# ruff: noqa: F401

import pytest
import isecapipy
import json


def test_agent_response_is_formatted_to_model():
    with open("./tests/dummy_data/response/agent.json", "r") as agent:
        data = json.load(agent)
        assert isinstance(
            isecapipy.ResponseModels.AgentDetail(**data),
            isecapipy.ResponseModels.AgentDetail,
        )


def test_agents_response_contains_agents():
    with open("./tests/dummy_data/response/agents.json", "r") as agents:
        data = json.load(agents)
        valid = []
        for agent in data["value"]:
            valid.append(
                isinstance(
                    isecapipy.ResponseModels.AgentDetail(**agent),
                    isecapipy.ResponseModels.AgentDetail,
                )
            )
        assert len(set(valid)) and valid[0]


def test_agent_status_full_response():
    with open("./tests/dummy_data/response/agent_status.json", "r") as status:
        status = json.load(status)
        assert isinstance(
            isecapipy.ResponseModels.AgentStatus(**status),
            isecapipy.ResponseModels.AgentStatus,
        )


def test_agent_status_model():
    with open("./tests/dummy_data/response/agent_status.json", "r") as status:
        status = json.load(status)
        assert isinstance(
            isecapipy.ResponseModels.AgentStatus(**status).frameworkVersion,
            isecapipy.ResponseModels.FrameworkVersion,
        )


def test_agent_deployment():
    with open("./tests/dummy_data/response/agent_deployment.json", "r") as deployment:
        deployment = json.load(deployment)
        assert isinstance(
            isecapipy.ResponseModels.AgentDeployStatus(**deployment),
            isecapipy.ResponseModels.AgentDeployStatus,
        )
