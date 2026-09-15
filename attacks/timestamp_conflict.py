from __future__ import annotations

from attacks.common import clone


def attack(bundle):
    forged = clone(bundle)
    forged["evidence"].append({
        "evidence_id": "EVD-0002",
        "type": "field_observation",
        "captured_at": "2026-09-14T09:00:00Z",
        "data": {"note": "Earlier timestamp appended after a later observation."}
    })
    return forged
