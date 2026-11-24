"""Find a specification and its downstream path in the installed manifest."""

from decentralized_identifiers_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:did-core-data-model-and-syntax-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2100-did-core-data-model-and-syntax-contract.yaml"
