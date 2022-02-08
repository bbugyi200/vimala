"""Tests for the vimala package."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable, List, cast

import pytest

import vimala


params = pytest.mark.parametrize


@params("lineno,commands", [(None, [])])
def test_vim(tmp_path: Path, lineno: int, commands: Iterable[str]) -> None:
    """Test the vim() function."""
    echo_proc = vimala.vim(
        tmp_path, lineno=lineno, commands=commands, vim_exe="echo"
    ).unwrap()
    assert echo_proc.popen.returncode == 0

    echo_args = cast(List[str], echo_proc.popen.args)
    echo_args = list(echo_args)
    assert echo_args.pop(0) == "echo"
    assert isinstance(echo_args.pop(0), (str, Path))
