# ruff: noqa: F401

import pytest
import isecapipy
import json


def test_agent_response_is_formatted_to_model():
    with open("./tests/dummy_data/response/agent.json", "r") as agent:
        data = json.load(agent)
        assert isinstance(isecapipy.AgentDetail(**data), isecapipy.AgentDetail)


def test_agents_response_contains_agents():
    with open("./tests/dummy_data/response/agents.json", "r") as agents:
        data = json.load(agents)
        valid = []
        for agent in data["value"]:
            valid.append(
                isinstance(isecapipy.AgentDetail(**agent), isecapipy.AgentDetail)
            )
        assert len(set(valid)) and valid[0]
