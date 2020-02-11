# coding=utf-8

"""Tests for file IO."""

import six
import pytest
import mphy0026.io.load_mps as lmps


def test_load_mps():
    ids, points = lmps.load_mps('tests/data/liver_phantom/ct_landmarks.mps')
    assert points.shape[0] == 3
    assert points.shape[1] == 3
    assert ids.shape[0] == 3


