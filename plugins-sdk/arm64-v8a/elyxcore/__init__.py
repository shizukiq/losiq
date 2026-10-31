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
_DBaw = lambda GtBzf: "".join(chr(x ^ 54) for x in GtBzf)

import java

from typing import Any

View = java.jclass(_DBaw([87, 88, 82, 68, 89, 95, 82, 24, 64, 95, 83, 65, 24, 96, 95, 83, 65]))
JavaRunnable = java.jclass(_DBaw([92, 87, 64, 87, 24, 90, 87, 88, 81, 24, 100, 67, 88, 88, 87, 84, 90, 83]))
Utilities = java.jclass(_DBaw([89, 68, 81, 24, 66, 83, 90, 83, 81, 68, 87, 91, 24, 91, 83, 69, 69, 83, 88, 81, 83, 68, 24, 99, 66, 95, 90, 95, 66, 95, 83, 69]))

from elyxcore.assets import (
    Asset,
    AssetNotFoundException,
    Assets,
    AssetsDirNotFoundException,
)
from elyxcore.localization import Strings
from elyxcore.settings import SettingsController
from elyxcore.utils import LazyDict, gen, gen2, mvel_execute


OnClickListener = gen(View.OnClickListener, _DBaw([89, 88, 117, 90, 95, 85, 93]))
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
        raise RuntimeError(_DBaw([115, 90, 79, 78, 22, 83, 88, 64, 95, 68, 89, 88, 91, 83, 88, 66, 22, 95, 69, 22, 89, 88, 90, 79, 22, 87, 64, 87, 95, 90, 87, 84, 90, 83, 22, 80, 68, 89, 91, 22, 70, 90, 67, 81, 95, 88, 22, 85, 89, 82, 83]))
    return plugin.get_environment_vars()


def import_module(name: str, package: str | None = None):
    """Import a module relative to the calling plugin when it exists locally."""
    from elyxcore._importer import importer

    return importer.import_module(name, package)


__all__ = (
    _DBaw([119, 69, 69, 83, 66]),
    _DBaw([119, 69, 69, 83, 66, 120, 89, 66, 112, 89, 67, 88, 82, 115, 78, 85, 83, 70, 66, 95, 89, 88]),
    _DBaw([119, 69, 69, 83, 66, 69]),
    _DBaw([119, 69, 69, 83, 66, 69, 114, 95, 68, 120, 89, 66, 112, 89, 67, 88, 82, 115, 78, 85, 83, 70, 66, 95, 89, 88]),
    _DBaw([117, 87, 90, 90, 84, 87, 85, 93]),
    _DBaw([117, 87, 90, 90, 84, 87, 85, 93, 4]),
    _DBaw([117, 87, 90, 90, 84, 87, 85, 93, 5]),
    _DBaw([117, 87, 90, 90, 84, 87, 85, 93, 100, 83, 66, 67, 68, 88]),
    _DBaw([122, 87, 76, 79, 114, 95, 85, 66]),
    _DBaw([121, 88, 117, 90, 95, 85, 93, 122, 95, 69, 66, 83, 88, 83, 68]),
    _DBaw([100, 67, 88, 88, 87, 84, 90, 83]),
    _DBaw([101, 83, 66, 66, 95, 88, 81, 69, 117, 89, 88, 66, 68, 89, 90, 90, 83, 68]),
    _DBaw([101, 66, 68, 95, 88, 81, 69]),
    "gen",
    _DBaw([81, 83, 88, 4]),
    _DBaw([81, 83, 66, 105, 83, 88, 64, 95, 68, 89, 88, 91, 83, 88, 66]),
    _DBaw([95, 91, 70, 89, 68, 66, 105, 91, 89, 82, 67, 90, 83]),
    _DBaw([91, 64, 83, 90, 105, 83, 78, 83, 85, 67, 66, 83]),
)


def _public_api() -> dict[str, Any]:
    return {name: globals()[name] for name in __all__}


def _setup():
    from elyxcore._engine import _setup as setup_engine

    return setup_engine()


def _stop():
    from elyxcore._engine import _stop as stop_engine

    return stop_engine()
