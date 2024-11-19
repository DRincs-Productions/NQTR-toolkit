import builtins
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture(autouse=True)
def mock_renpy(monkeypatch):
    """This trick overrides for time of testing need to have renpy in the sys.path.

    Rationale is that we want to test NQTR library and and renpy usually is installed
    globally somewhere else in the OS.
    """
    import_orig = builtins.__import__

    def mocked_import(name, *args, **kwargs):
        if name in ("renpy.exports", "renpy.character", "renpy"):
            return MagicMock()
        return import_orig(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", mocked_import)
