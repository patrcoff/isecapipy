# ruff: noqa: F401

import pytest
import isecapipy


def test_placeholder():
    assert isecapipy.placeholder()
