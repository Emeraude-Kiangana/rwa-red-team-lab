import hashlib, json, sys
from pathlib import Path

def canonical(data):
    return json.dumps(data, sort_keys=True, separators=(",", ":")).encode()

def expected_hash(bundle):
    body={"asset_id":bundle["asset_id"],"evidence":bundle["evidence"]}
    return "sha256:"+hashlib.sha256(canonical(body)).hexdigest()

def check(bundle):
    issues=[]
    ids=[x.get("evidence_id") for x in bundle.get("evidence",[]) if isinstance(x,dict)]
    if len(ids)!=len(set(ids)):
        issues.append("DUPLICATE_EVIDENCE_ID")
    times=[x.get("captured_at") for x in bundle.get("evidence",[]) if isinstance(x,dict)]
    if any(b<a for a,b in zip(times,times[1:]) if a and b):
        issues.append("TIMESTAMP_CONFLICT")
    if bundle.get("payload_hash")!=expected_hash(bundle):
        issues.append("PAYLOAD_HASH_MISMATCH")
    return issues

if __name__=="__main__":
    data=json.loads(Path(sys.argv[1]).read_text())
    issues=check(data)
    print("VERIFIED" if not issues else "REJECTED")
    for issue in issues: print(issue)
    raise SystemExit(0 if not issues else 1)
