import copy, json
from pathlib import Path
from verifier.check import check

BASE=Path("assets/PLOT-001/evidence.json")
def load(): return json.loads(BASE.read_text())

def test_baseline(): assert check(load())==[]
def test_measurement_change():
    x=load(); x["evidence"][0]["data"]["soil_carbon_percent"]=4.9
    assert "PAYLOAD_HASH_MISMATCH" in check(x)
def test_duplicate_id():
    x=load(); x["evidence"].append(copy.deepcopy(x["evidence"][0]))
    assert "DUPLICATE_EVIDENCE_ID" in check(x)
def test_timestamp_order():
    x=load(); y=copy.deepcopy(x["evidence"][0]); y["evidence_id"]="EVD-0002"; y["captured_at"]="2026-09-14T09:00:00Z"; x["evidence"].append(y)
    assert "TIMESTAMP_CONFLICT" in check(x)
