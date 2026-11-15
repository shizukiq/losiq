"""Public API for structured Elyx plugins.

Plugin code should import supported symbols from ``elyx``::

    from elyx import Asset, Assets, SettingsController, Strings

Plugin-bound values are resolved at runtime and remain available in the same
facade::

    from elyx import assets, metainfo, refmap, settings, strings

Runtime modules whose names start with an underscore are implementation details
and may change without preserving import compatibility.
"""

from __future__ import annotations
_qPQiM = lambda EzvxrqS: "".join(chr(x ^ 177) for x in EzvxrqS)

import java

from typing import Any

View = java.jclass(_qPQiM([208, 223, 213, 195, 222, 216, 213, 159, 199, 216, 212, 198, 159, 231, 216, 212, 198]))
JavaRunnable = java.jclass(_qPQiM([219, 208, 199, 208, 159, 221, 208, 223, 214, 159, 227, 196, 223, 223, 208, 211, 221, 212]))
Utilities = java.jclass(_qPQiM([222, 195, 214, 159, 197, 212, 221, 212, 214, 195, 208, 220, 159, 220, 212, 194, 194, 212, 223, 214, 212, 195, 159, 228, 197, 216, 221, 216, 197, 216, 212, 194]))

from elyxcore.assets import (
    Asset,
    AssetNotFoundException,
    Assets,
    AssetsDirNotFoundException,
)
from elyxcore.localization import Strings
from elyxcore.settings import SettingsController
from elyxcore.utils import LazyDict, gen, gen2, mvel_execute


OnClickListener = gen(View.OnClickListener, _qPQiM([222, 223, 242, 221, 216, 210, 218]))
Runnable = gen(JavaRunnable, "run")
Callback = gen(Utilities.Callback, "run")
Callback2 = gen(Utilities.Callback2, "run")
Callback3 = gen(Utilities.Callback3, "run")
CallbackReturn = gen(Utilities.CallbackReturn, "run", True)


def get_environment() -> dict[str, Any]:
    """Return assets, settings, strings and metadata for the calling plugin."""
    from elyxcore._importer import importer

    plugin = importer.get_caller_plugin()
    if plugin is None:
        raise RuntimeError(_qPQiM([244, 221, 200, 201, 145, 212, 223, 199, 216, 195, 222, 223, 220, 212, 223, 197, 145, 216, 194, 145, 222, 223, 221, 200, 145, 208, 199, 208, 216, 221, 208, 211, 221, 212, 145, 215, 195, 222, 220, 145, 193, 221, 196, 214, 216, 223, 145, 210, 222, 213, 212]))
    return plugin.get_environment_vars()


def import_module(name: str, package: str | None = None):
    """Import a module relative to the calling plugin when it exists locally."""
    from elyxcore._importer import importer

    return importer.import_module(name, package)


__all__ = (
    _qPQiM([240, 194, 194, 212, 197]),
    _qPQiM([240, 194, 194, 212, 197, 255, 222, 197, 247, 222, 196, 223, 213, 244, 201, 210, 212, 193, 197, 216, 222, 223]),
    _qPQiM([240, 194, 194, 212, 197, 194]),
    _qPQiM([240, 194, 194, 212, 197, 194, 245, 216, 195, 255, 222, 197, 247, 222, 196, 223, 213, 244, 201, 210, 212, 193, 197, 216, 222, 223]),
    _qPQiM([242, 208, 221, 221, 211, 208, 210, 218]),
    _qPQiM([242, 208, 221, 221, 211, 208, 210, 218, 131]),
    _qPQiM([242, 208, 221, 221, 211, 208, 210, 218, 130]),
    _qPQiM([242, 208, 221, 221, 211, 208, 210, 218, 227, 212, 197, 196, 195, 223]),
    _qPQiM([253, 208, 203, 200, 245, 216, 210, 197]),
    _qPQiM([254, 223, 242, 221, 216, 210, 218, 253, 216, 194, 197, 212, 223, 212, 195]),
    _qPQiM([227, 196, 223, 223, 208, 211, 221, 212]),
    _qPQiM([226, 212, 197, 197, 216, 223, 214, 194, 242, 222, 223, 197, 195, 222, 221, 221, 212, 195]),
    _qPQiM([226, 197, 195, 216, 223, 214, 194]),
    "gen",
    _qPQiM([214, 212, 223, 131]),
    _qPQiM([214, 212, 197, 238, 212, 223, 199, 216, 195, 222, 223, 220, 212, 223, 197]),
    _qPQiM([216, 220, 193, 222, 195, 197, 238, 220, 222, 213, 196, 221, 212]),
    _qPQiM([220, 199, 212, 221, 238, 212, 201, 212, 210, 196, 197, 212]),
)


def _public_api() -> dict[str, Any]:
    return {name: globals()[name] for name in __all__}


def _setup():
    from elyxcore._engine import _setup as setup_engine

    return setup_engine()


def _stop():
    from elyxcore._engine import _stop as stop_engine

    return stop_engine()
