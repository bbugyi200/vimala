"""The vimala package's catch-all module.

You should only add code to this module when you are unable to find ANY other
module to add it to.
"""

from __future__ import annotations

import subprocess as sp
from typing import Iterable

from typist import PathLike


def vim(
    *args: PathLike, lineno: int = None, commands: Iterable[str] = ()
) -> sp.Popen:
    """Execute `vim`.."""
    extra_args: list[str] = []
    if lineno is not None:
        extra_args.append(f"+{lineno}")

    for cmd in commands:
        extra_args.extend(["-c", cmd])

    cmd_args = [str(x) for x in ["vim", *args, *extra_args]]
    popen = sp.Popen(cmd_args)
    return popen
