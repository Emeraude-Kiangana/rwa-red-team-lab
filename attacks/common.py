from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any


def load_bundle(path: str | Path) -> dict[str, Any]:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def clone(bundle: dict[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(bundle)
