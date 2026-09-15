from __future__ import annotations

from attacks.common import clone


def attack(bundle):
    forged = clone(bundle)
    duplicate = clone(forged["evidence"][0])
    duplicate["captured_at"] = "2026-09-15T11:00:00Z"
    forged["evidence"].append(duplicate)
    return forged
