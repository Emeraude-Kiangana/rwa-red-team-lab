from __future__ import annotations

from attacks.common import clone


def attack(bundle):
    forged = clone(bundle)
    forged["evidence"][0]["data"]["soil_carbon_percent"] = 4.90
    return forged
