<div align="center">

<h1>decentralized-identifiers-governance-pack</h1>

<p>
  <a href="https://pypi.org/project/decentralized-identifiers-governance-pack/"><img alt="PyPI version" src="https://img.shields.io/pypi/v/decentralized-identifiers-governance-pack.svg"></a>
  <a href="https://pepy.tech/projects/decentralized-identifiers-governance-pack"><img alt="Downloads" src="https://static.pepy.tech/badge/decentralized-identifiers-governance-pack"></a>
  <a href="https://hits.sh/github.com/groupsum/decentralized-identifiers-governance-pack/"><img alt="Hits" src="https://hits.sh/github.com/groupsum/decentralized-identifiers-governance-pack.svg"></a>
  <a href="https://pypi.org/project/decentralized-identifiers-governance-pack/"><img alt="Python versions" src="https://img.shields.io/pypi/pyversions/decentralized-identifiers-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/pypi/l/decentralized-identifiers-governance-pack.svg"></a>
  <a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/groupsum/decentralized-identifiers-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master"></a>
</p>

<p>
  <a href="https://github.com/groupsum/decentralized-identifiers-governance-pack"><img alt="GitHub repo" src="https://img.shields.io/badge/GitHub-groupsum%2Fdecentralized--identifiers--governance--pack-181717?logo=github"></a>
</p>

</div>

`decentralized-identifiers-governance-pack` is an SSOT Registry pack for DID Core, DID documents, DID URLs, DID resolution and dereferencing, DID method support, domain linkage, DIDComm adjacency, trust establishment, and DID use in VC/OpenID4VC profiles.

It gives product, platform, identity, resolver, wallet, messaging, and compliance teams a reusable ADR/SPEC starting point for repositories that need to govern DID syntax, DID document processing, verification methods, verification relationships, service endpoints, method support, resolution behavior, domain linkage, DIDComm adjacency, and optional VC/OpenID4VC integration.

## What Is An SSOT Registry Pack?

An SSOT Registry pack is an installable package of governed Architecture Decision Records (ADRs) and Specifications (SPECs) for [`ssot-registry`](https://pypi.org/project/ssot-registry/). The pack supplies reusable decision and requirement documents that downstream repositories can synchronize into their local `.ssot` registry and link to features, tests, claims, evidence, and releases.

This makes governance portable. A project can adopt the pack, synchronize the documents, list the active requirements, and connect local implementation or test work to the shared IDs.

## Why This Pack Exists

Decentralized Identifiers governance crosses identifier syntax, DID document semantics, verification material, method-specific behavior, resolution and dereferencing, domain linkage, messaging adjacency, and downstream use by VC and OpenID4VC profiles. Teams need explicit boundaries before claiming support for a DID method, resolver behavior, verification relationship, service endpoint, or trust signal.

This pack helps teams:

- apply reviewed DID governance requirements across projects
- distinguish DID Core requirements from method-specific and adjacent protocol requirements
- keep DID resolution, dereferencing, domain linkage, DIDComm, and trust-establishment boundaries explicit
- give resolver, wallet, issuer, verifier, messaging, platform, and compliance teams stable ADR and SPEC IDs
- connect downstream features, tests, claims, evidence, and releases to shared governance records

## Pack Metadata

- Pack ID: `pack:decentralized-identifiers-governance`
- PyPI package: `decentralized-identifiers-governance-pack`
- Import package: `decentralized_identifiers_governance_pack`
- GitHub repository: [groupsum/decentralized-identifiers-governance-pack](https://github.com/groupsum/decentralized-identifiers-governance-pack)
- Reservation owner: `extension-pack:decentralized-identifiers-governance-pack`

## Domain Focus

The pack focuses on domains where DID behavior affects interoperability, resolver behavior, trust review, and release evidence:

- DID Core data model, syntax, and DID URL handling
- DID documents, verification methods, verification relationships, and service endpoints
- DID resolution and dereferencing behavior
- explicit DID method support policy and method-specific requirements
- `did:web`, `did:key`, `did:jwk`, `did:peer`, `did:webvh`, `did:ion`, `did:ethr`, and `did:pkh` boundaries
- Well-Known DID Configuration and domain linkage
- DIDComm and trust-establishment adjacency
- optional DID use in VC and OpenID4VC profiles without making those profiles baseline DID prerequisites

## Authority Sources

Core DID authorities:

- [W3C DID Core 1.0](https://www.w3.org/TR/did-core/)
- [W3C DID Extensions](https://www.w3.org/TR/did-spec-registries/)
- [W3C Controlled Identifiers](https://www.w3.org/TR/cid/)
- [DID Resolution](https://w3c-ccg.github.io/did-resolution/)

DID method authorities:

- [did:web](https://w3c-ccg.github.io/did-method-web/)
- [did:key](https://w3c-ccg.github.io/did-method-key/)
- [did:jwk](https://github.com/quartzjer/did-jwk/blob/main/spec.md)
- [did:peer](https://identity.foundation/peer-did-method-spec/)
- [did:webvh](https://identity.foundation/didwebvh/)
- [did:ion](https://identity.foundation/ion/)
- [did:ethr](https://github.com/uport-project/ethr-did-resolver)
- [did:pkh](https://github.com/w3c-ccg/did-pkh/blob/main/did-pkh-method-draft.md)

Adjacent DID specs:

- [Well-Known DID Configuration](https://identity.foundation/.well-known/resources/did-configuration/)
- [DIDComm Messaging v2.0](https://identity.foundation/didcomm-messaging/spec/)
- [DIF Trust Establishment](https://identity.foundation/trust-establishment/)

Adjacent consumer profiles:

- [W3C Verifiable Credentials Data Model v2.0](https://www.w3.org/TR/vc-data-model-2.0/)
- [W3C Verifiable Credential Data Integrity 1.0](https://www.w3.org/TR/vc-data-integrity/)
- [W3C Securing Verifiable Credentials using JOSE and COSE](https://www.w3.org/TR/vc-jose-cose/)
- [OpenID for Verifiable Credential Issuance](https://openid.net/specs/openid-4-verifiable-credential-issuance-1_0.html)
- [OpenID for Verifiable Presentations](https://openid.net/specs/openid-4-verifiable-presentations-1_0.html)
- [Self-Issued OpenID Provider v2](https://openid.net/specs/openid-connect-self-issued-v2-1_0.html)

## Included ADRs

- [`adr:did-core-is-the-identifier-document-and-url-authority`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1100-did-core-is-the-identifier-document-and-url-authority.yaml) - DID Core Is The Identifier Document And URL Authority
- [`adr:did-method-support-must-be-explicitly-declared`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1101-did-method-support-must-be-explicitly-declared.yaml) - DID Method Support Must Be Explicitly Declared
- [`adr:did-resolution-and-dereferencing-are-separate-from-method-lifecycle`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1102-did-resolution-and-dereferencing-are-separate-from-method-lifecycle.yaml) - DID Resolution And Dereferencing Are Separate From Method Lifecycle
- [`adr:did-documents-govern-verification-methods-relationships-and-services`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1103-did-documents-govern-verification-methods-relationships-and-services.yaml) - DID Documents Govern Verification Methods Relationships And Services
- [`adr:did-domain-linkage-is-a-separate-trust-signal`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1104-did-domain-linkage-is-a-separate-trust-signal.yaml) - DID Domain Linkage Is A Separate Trust Signal
- [`adr:didcomm-and-trust-establishment-are-adjacent-protocols-not-did-core`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1105-didcomm-and-trust-establishment-are-adjacent-protocols-not-did-core.yaml) - DIDComm And Trust Establishment Are Adjacent Protocols Not DID Core
- [`adr:did-use-in-vc-and-openid4vc-is-optional-profile-integration`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1106-did-use-in-vc-and-openid4vc-is-optional-profile-integration.yaml) - DID Use In VC And OpenID4VC Is Optional Profile Integration

## Included SPECs

- [`spc:did-core-data-model-and-syntax-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2100-did-core-data-model-and-syntax-contract.yaml) - DID Core Data Model And Syntax Contract
- [`spc:did-url-and-did-document-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2101-did-url-and-did-document-contract.yaml) - DID URL And DID Document Contract
- [`spc:did-resolution-and-dereferencing-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2102-did-resolution-and-dereferencing-contract.yaml) - DID Resolution And Dereferencing Contract
- [`spc:did-method-registry-and-method-support-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2103-did-method-registry-and-method-support-contract.yaml) - DID Method Registry And Method Support Contract
- [`spc:did-web-method-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2104-did-web-method-contract.yaml) - DID Web Method Contract
- [`spc:did-key-and-did-jwk-method-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2105-did-key-and-did-jwk-method-contract.yaml) - DID Key And DID JWK Method Contract
- [`spc:did-peer-method-boundary-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2106-did-peer-method-boundary-contract.yaml) - DID Peer Method Boundary Contract
- [`spc:did-webvh-ion-ethr-pkh-method-boundary-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2107-did-webvh-ion-ethr-pkh-method-boundary-contract.yaml) - DID WebVH ION ETHR PKH Method Boundary Contract
- [`spc:well-known-did-configuration-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2108-well-known-did-configuration-contract.yaml) - Well-Known DID Configuration Contract
- [`spc:didcomm-boundary-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2109-didcomm-boundary-contract.yaml) - DIDComm Boundary Contract
- [`spc:did-trust-establishment-boundary-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2110-did-trust-establishment-boundary-contract.yaml) - DID Trust Establishment Boundary Contract

## Install With uv

Install the pack into a project environment:

```bash
uv add decentralized-identifiers-governance-pack
```

Install it alongside the SSOT Registry CLI:

```bash
uv add ssot-registry decentralized-identifiers-governance-pack
```

Run without adding dependencies to a project:

```bash
uvx --from ssot-registry --with decentralized-identifiers-governance-pack ssot --help
```

## Install With The SSOT Registry Pack CLI

Pack-enabled SSOT Registry environments can inspect, preflight, and synchronize packs through the pack command surface:

```bash
uv run ssot pack inspect decentralized_identifiers_governance_pack
uv run ssot pack preflight . decentralized_identifiers_governance_pack --all
uv run ssot pack sync . decentralized_identifiers_governance_pack --all --trust --yes
```

## Use With The SSOT Registry CLI

After the pack is installed in the same environment as `ssot-registry`, validate the synchronized governance surface:

```bash
uv run ssot validate .
uv run ssot adr list .
uv run ssot spec list .
uv run ssot spec get . --id spc:pack.decentralized-identifiers-governance.did-core-data-model-and-syntax-contract
```

Use the IDs from this pack when linking project features, tests, claims, and release evidence in your local `.ssot` registry.

## Programmatic Usage

```python
from decentralized_identifiers_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")

print(adr_manifest[0]["id"])
print(spec_manifest[0]["id"])

text = read_packaged_document_text("spec", "SPEC-2100-did-core-data-model-and-syntax-contract.yaml")
print(text[:120])
```

## Resources

- GitHub repository: [groupsum/decentralized-identifiers-governance-pack](https://github.com/groupsum/decentralized-identifiers-governance-pack)
- PyPI package: [decentralized-identifiers-governance-pack](https://pypi.org/project/decentralized-identifiers-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)
