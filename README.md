# RWA Red-Team Lab

Adversarial verification lab for Real-World Asset (RWA) evidence.

## Gate 0 objective

Prove that a deterministic verifier can detect three classes of tampering against a sample agricultural evidence bundle:

1. Measurement mutation
2. Duplicate evidence identifier
3. Timestamp conflict

The AI layer is intentionally out of scope for Gate 0. This repository first establishes deterministic, reproducible checks that an AI red-team agent can later invoke.

## Run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python verifier/verify.py assets/PLOT-001/evidence.json
pytest -q
```

Expected baseline verdict:

```text
VERIFIED
```

Expected test result:

```text
4 passed
```

## Security model

The bundle contains a `payload_hash` computed from canonical JSON of the `asset_id` and `evidence` fields only. Any content mutation without a valid recomputation is detected. Independent structural checks detect duplicate evidence IDs and conflicting timestamps.

This is not yet legal attestation, identity verification, blockchain anchoring, or RWA issuance.
