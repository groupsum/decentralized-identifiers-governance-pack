# decentralized-identifiers-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>decentralized-identifiers-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for DID Core, DID documents, DID URLs, DID resolution, DID methods, domain linkage, DIDComm adjacency, and DID use in VC/OpenID4VC profiles.</p>
<p align="center">
<a href="https://pypi.org/project/decentralized-identifiers-governance-pack/"><img alt="pypi: decentralized-identifiers-governance-pack unpublished" src="https://img.shields.io/static/v1?label=pypi&amp;message=decentralized-identifiers-governance-pack%20unpublished&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.1.1.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.1.1.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/decentralized-identifiers-governance-pack/"><img alt="pypi downloads: decentralized-identifiers-governance-pack: unpublished" src="https://img.shields.io/static/v1?label=pypi%20downloads&amp;message=decentralized-identifiers-governance-pack%3A%20unpublished&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/README.md"><img alt="README hits: decentralized-identifiers-governance-pack" src="https://hits.sh/github.com/groupsum/decentralized-identifiers-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/decentralized-identifiers-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for DID Core, DID documents, DID URLs, DID resolution, DID methods, domain linkage, DIDComm adjacency, and DID use in VC/OpenID4VC profiles.

### Why This Package

The pack supplies versioned, source-linked ADR and SPEC templates for Decentralized Identifiers Governance.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Decentralized Identifiers Governance.

### Features

**Included ADRs**

- [`adr:did-core-is-the-identifier-document-and-url-authority`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1100-did-core-is-the-identifier-document-and-url-authority.yaml) — DID Core Is The Identifier Document And URL Authority
- [`adr:did-method-support-must-be-explicitly-declared`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1101-did-method-support-must-be-explicitly-declared.yaml) — DID Method Support Must Be Explicitly Declared
- [`adr:did-resolution-and-dereferencing-are-separate-from-method-lifecycle`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1102-did-resolution-and-dereferencing-are-separate-from-method-lifecycle.yaml) — DID Resolution And Dereferencing Are Separate From Method Lifecycle
- [`adr:did-documents-govern-verification-methods-relationships-and-services`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1103-did-documents-govern-verification-methods-relationships-and-services.yaml) — DID Documents Govern Verification Methods Relationships And Services
- [`adr:did-domain-linkage-is-a-separate-trust-signal`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1104-did-domain-linkage-is-a-separate-trust-signal.yaml) — DID Domain Linkage Is A Separate Trust Signal
- [`adr:didcomm-and-trust-establishment-are-adjacent-protocols-not-did-core`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1105-didcomm-and-trust-establishment-are-adjacent-protocols-not-did-core.yaml) — DIDComm And Trust Establishment Are Adjacent Protocols Not DID Core
- [`adr:did-use-in-vc-and-openid4vc-is-optional-profile-integration`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/adr/ADR-1106-did-use-in-vc-and-openid4vc-is-optional-profile-integration.yaml) — DID Use In VC And OpenID4VC Is Optional Profile Integration

**Included SPECs**

- [`spc:did-core-data-model-and-syntax-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2100-did-core-data-model-and-syntax-contract.yaml) — DID Core Data Model And Syntax Contract
- [`spc:did-url-and-did-document-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2101-did-url-and-did-document-contract.yaml) — DID URL And DID Document Contract
- [`spc:did-resolution-and-dereferencing-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2102-did-resolution-and-dereferencing-contract.yaml) — DID Resolution And Dereferencing Contract
- [`spc:did-method-registry-and-method-support-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2103-did-method-registry-and-method-support-contract.yaml) — DID Method Registry And Method Support Contract
- [`spc:did-web-method-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2104-did-web-method-contract.yaml) — DID Web Method Contract
- [`spc:did-key-and-did-jwk-method-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2105-did-key-and-did-jwk-method-contract.yaml) — DID Key And DID JWK Method Contract
- [`spc:did-peer-method-boundary-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2106-did-peer-method-boundary-contract.yaml) — DID Peer Method Boundary Contract
- [`spc:did-webvh-ion-ethr-pkh-method-boundary-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2107-did-webvh-ion-ethr-pkh-method-boundary-contract.yaml) — DID WebVH ION ETHR PKH Method Boundary Contract
- [`spc:well-known-did-configuration-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2108-well-known-did-configuration-contract.yaml) — Well-Known DID Configuration Contract
- [`spc:didcomm-boundary-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2109-didcomm-boundary-contract.yaml) — DIDComm Boundary Contract
- [`spc:did-trust-establishment-boundary-contract`](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates/specs/SPEC-2110-did-trust-establishment-boundary-contract.yaml) — DID Trust Establishment Boundary Contract

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

#### uv

<!-- readme-standards:begin installation.uv -->
`decentralized-identifiers-governance-pack` is not declared published. From the source checkout:

```bash
uv pip install .
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
`decentralized-identifiers-governance-pack` is not declared published. From the source checkout:

```bash
python -m pip install .
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
`decentralized-identifiers-governance-pack` is not declared published. From a separate Poetry project, replace the path with your checkout:

```bash
poetry add /path/to/decentralized-identifiers-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from decentralized_identifiers_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:decentralized-identifiers-governance"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:decentralized-identifiers-governance` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/examples/usage.py).

```python
"""Resolve and read a packaged specification without synchronizing it."""

from decentralized_identifiers_governance_pack import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:did-core-data-model-and-syntax-contract")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `decentralized-identifiers-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect decentralized_identifiers_governance_pack
uv run ssot pack preflight . decentralized_identifiers_governance_pack --all
uv run ssot pack sync . decentralized_identifiers_governance_pack --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `decentralized_identifiers_governance_pack` in SSOT Registry. Review reservation owner `extension-pack:decentralized-identifiers-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

The pack owns the Decentralized Identifiers Governance ADRs and SPECs listed under Features.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `decentralized_identifiers_governance_pack` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/decentralized-identifiers-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/decentralized-identifiers-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/src/decentralized_identifiers_governance_pack/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/decentralized-identifiers-governance-pack)
- [Issues](https://github.com/groupsum/decentralized-identifiers-governance-pack/issues)
- [Repository](https://github.com/groupsum/decentralized-identifiers-governance-pack)
- [pypi: decentralized-identifiers-governance-pack](https://pypi.org/project/decentralized-identifiers-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/decentralized-identifiers-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs. Update the PyPI publication setting after the first successful upload.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:decentralized-identifiers-governance`. The pack's reservation owner is `extension-pack:decentralized-identifiers-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

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

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/decentralized-identifiers-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
