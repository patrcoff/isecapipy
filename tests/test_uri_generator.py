import pytest
from isecapipy import generate_uri, NonUniqueFilter, NoURIsFound


def test_get_agents_all():
    assert (
        generate_uri(endpoint="AGENTS", mult=True, method="get")
        == "https://<consoleFQDN:port>/st/console/api/v1.0/agents"
    )


def test_get_agents_all():
    assert (
        generate_uri(endpoint="AGENTS", mult=False, method="get")
        == "https://<consoleFQDN:port>/st/console/api/v1.0/agents/{agentID}"
    )


def test_raises_non_unique_url_with_no_args_or_kwargs():
    with pytest.raises(NonUniqueFilter):
        generate_uri()


def test_raises_non_unique_url_with_arbitrary_kwargs():
    with pytest.raises(NonUniqueFilter):
        generate_uri(fake_kwarg="some data")


def test_raises_non_unique_url_with_count_only_in_kwargs():
    with pytest.raises(NonUniqueFilter):
        generate_uri(count=1)


def test_url_parameters_added_to_uri():
    assert (
        generate_uri(method="get", endpoint="AGENTS", count=5, name="example")
        == "https://<consoleFQDN:port>/st/console/api/v1.0/agents?count=5&name=example"
    )
    # this test requires python>=3.7 due to odered dicts - we won't support pre 3.9
