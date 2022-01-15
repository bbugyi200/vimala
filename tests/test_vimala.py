"""Tests for the vimala package."""

from __future__ import annotations

from vimala import dummy


def test_dummy() -> None:
    """Test the dummy() function."""
    assert dummy(1, 2) == 3
