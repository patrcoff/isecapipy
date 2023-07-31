import pytest
from isecapipy import select_uri


def test_get_agents_all():
    assert (
        select_uri(endpoint="AGENTS", mult=True, method="get")
        == "https://<consoleFQDN:port>/st/console/api/v1.0/agents"
    )


def test_get_agents_all():
    assert (
        select_uri(endpoint="AGENTS", mult=False, method="get")
        == "https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentID}"
    )
