# -*- coding: utf-8 -*-
"""Tests for py3.6+ annotation type hint casting."""

from __future__ import unicode_literals

import pytest

import typingplus.types as tp


def test_typed_object():
    """TODO"""
    class X(tp.TypedObject):
        x: str = None
        y = 1
    x = X()
    x.x = 'hello'
    assert isinstance(x.x, str)
    assert x.x == 'hello'
    with pytest.raises(TypeError):
        x.x = 5


def test_cast_object():
    """TODO"""
    class X(tp.CastObject):
        x: str = None
    x = X()
    x.x = 5
    assert isinstance(x.x, str)
    assert x.x == '5'


def test_cast_object_failure():
    """TODO"""
    class X(tp.CastObject):
        x: int = None
    x = X()
    x.x = None
    with pytest.raises(TypeError):
        x.x = 'not an integer'
