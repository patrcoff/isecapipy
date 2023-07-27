# ruff: noqa: F401

import pytest
import isecapipy


def test_placeholder():
    assert isecapipy.placeholder()


def test_main():
    assert isecapipy.__main__.main() == None


def test_manage():
    assert isecapipy.manage() == None
