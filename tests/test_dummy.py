# ruff: noqa: F401

import pytest
import isecapipy


def test_main():
    assert isecapipy.__main__.main() is None


def test_manage():
    assert isecapipy.manage() is None
