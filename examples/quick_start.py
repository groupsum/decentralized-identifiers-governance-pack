"""Inspect the installed pack identity."""

from decentralized_identifiers_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:decentralized-identifiers-governance"
print(metadata["origin"]["id"])
