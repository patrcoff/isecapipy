import pytest
from isecapipy import select_uri, NonUniqueFilter, NoURIsFound


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


def test_raises_non_unique_url_with_no_args_or_kwargs():
    with pytest.raises(NonUniqueFilter):
        select_uri()


def test_raises_non_unique_url_with_arbitrary_kwargs():
    with pytest.raises(NonUniqueFilter):
        select_uri(fake_kwarg="some data")


def test_raises_non_unique_url_with_count_only_in_kwargs():
    with pytest.raises(NonUniqueFilter):
        select_uri(count=1)
