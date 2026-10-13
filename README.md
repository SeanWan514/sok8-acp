# Agentic Commerce Protocols · Research Artifacts

Offline companion for an **eight-function analysis of agentic commerce**: frozen taxonomy selections, English Method policy translations, two conditional economic models, and saved GLM decision evidence.

[![Taxonomy: Python 3.9+](https://img.shields.io/badge/Taxonomy-Python%203.9%2B-2563eb)](taxonomy/docs/reproduction.md)
[![Modeling: Python 3.12+](https://img.shields.io/badge/Modeling-Python%203.12%2B-7c3aed)](modeling/README.md)
[![Replay: offline](https://img.shields.io/badge/Replay-offline-0f766e)](#-quick-start)
[![Framework: 8 functions](https://img.shields.io/badge/Framework-8%20functions-d97706)](taxonomy/docs/analytical-codebook.md)

**Start here:** [Submission review](REVIEW.md) · [Method guide](method/README.md) · [Analytical codebook](taxonomy/docs/analytical-codebook.md) · [Data dictionary](taxonomy/docs/data-dictionary.md) · [Modeling guide](modeling/README.md)

> [!NOTE]
> Reproduction covers **five frozen taxonomy outputs, specified calculations, and saved decisions**. Live searches, AI screening, independent-work resolution, and corpus-wide function coding are not reproduced. Model results are conditional, not deployed-platform performance.

## 🧭 Repository map

| Location | Contents |
|---|---|
| [`taxonomy/`](taxonomy/README.md) | Frozen records, selection overlay, counts, analytical definitions, and standard-library reproduction code |
| [`method/`](method/README.md) | Complete English translations of source, workflow, and acceptance policies; context and external dependencies |
| [`modeling/`](modeling/README.md) | Cases A/B, numerical data, vector figures, editable code, prompts, settings, final responses, and offline checks |
| [`REVIEW.md`](REVIEW.md) | Submission-readiness review and remaining limitations |
| [`MANIFEST.json`](MANIFEST.json) · [`SHA256SUMS`](SHA256SUMS) | File sizes, SHA-256 hashes, applicable CSV schemas, and package integrity checks |
| [`PROVENANCE.json`](PROVENANCE.json) | Frozen-source lineage, translation hashes, packaging history, and publication context |

The manuscript is separate: no manuscript `.tex`, `.bib`, paper PDF, or `paper/` directory is included. Modeling figure PDFs are included. `sok8-acp` names this repository, not a new protocol or complete ACP implementation.

## 🚀 Quick start

From the repository root, use **Python 3.9+ and the standard library only**. Taxonomy reproduction needs no network, model, credentials, or dependency installation.

```sh
# Check frozen inputs and compare all five outputs byte-for-byte.
(cd taxonomy && python3 -I -S -B code/reproduce.py --check-only)

# Write the same outputs to a new or empty directory.
(cd taxonomy && python3 -I -S -B code/reproduce.py --output outputs/run)

# Verify the complete package, including Modeling.
shasum -a 256 -c SHA256SUMS
```

Generated outputs are excluded from Git. For Modeling, use **Python 3.12+** and the [pinned dependencies](modeling/README.md), then replay:

```sh
python3 -B modeling/replay.py --output outputs/modeling-replay.json
```

The Modeling guide also covers data/figure regeneration. Replay makes **zero API calls**, with no provider/model fallback.

## 🔬 Taxonomy: reproduced outputs and boundaries

Using saved identifiers and screening decisions, the code applies the **237-record administrative overlay**, groups exact typed keys, reconciles counts, and checks hashes, schemas, and structural constraints.

| Output in `taxonomy/expected/` | Reconstructed content |
|---|---|
| `final-selection-records.csv` | Scientific dispositions and final selection/bases for **5,241 source records** |
| `source-counts.csv` | Selection, standard-track, and relation-only counts for five sources |
| `identifier-selection.csv` | Source memberships and selection views for **5,208 exact typed keys** |
| `included-identifiers.csv` | **1,301 included typed keys**, derived from 1,312 included source records |
| `counts.json` | Frame, selection, and exact-key repetition arithmetic |

**Typed keys are not independent papers.** The 237 user-directed non-inclusions retain their scientific pending status. Scientific, coverage, and work/version acceptance remain **Partial or Unknown**.

Query counts, receipts, and gate scopes are frozen observations. Replay neither repeats collection, full-text retrieval, or screening nor validates inclusion judgments or resolves works/versions. The codebook supplies definitions and comparison questions, **not per-record labels, classification frequencies, saturation, or agreement measures**.

Details: [Reproduction instructions](taxonomy/docs/reproduction.md) · [Query/count table](taxonomy/data/query-counts.csv) · [Gate scopes](taxonomy/data/gate-matrix.csv) · [Method boundaries](taxonomy/docs/method-boundaries.md)

## 📊 Modeling: calculations and saved decisions

| Case | Mathematical scope | Saved GLM pilot |
|---|---|---|
| [A: Timely review](modeling/case-a/README.md) | Independent review probability `q` and autonomy cap `d`; **501 × 601 parameter pairs**. Original and optimized-cap supplements remain separate. | **23/24** decisions maximize the stipulated utility. |
| [B: Selective validation](modeling/case-b/README.md) | Exact seller-control calculation under fixed revenues and four observation policies. | **8/14** schema-valid effort choices are optimal across **15 revised attempts**; one schema error stopped the campaign, leaving **nine cells unattempted**. The initial campaign remains excluded. |

Both cases retain figures/data, prompts, decoding settings, option order, complete final outputs, and editable computation/plotting code. Success probabilities are exact model expectations, not platform effects or multi-round GLM success rates. This does not broaden the taxonomy's five-output claim.

## 📚 Method translations and source continuity

`method/` provides three complete English policy translations and a context/dependency guide. Originals remain unchanged outside the repository; [PROVENANCE](PROVENANCE.json) records both sets of hashes. Unlike redacted taxonomy projections, the translations retain explicitly requested brief decision quotations and opaque message identifiers.

Historical **NotRun** statements describe policy-approval time. Some original references point to unshipped dependencies listed in the [Method guide](method/README.md); the translations do not reproduce search execution.

## 🗂️ Publication history

Publication to **`kl41r3/sok8-acp`, public branch `main`**, was explicitly authorized. The first taxonomy/Method commit, [`cd55fb5`](https://github.com/kl41r3/sok8-acp/commit/cd55fb5aa9360fc5df7c57b6d64f86253e870ad8), was verified private before visibility changed; Modeling followed separately.

Revision **6, batch 2** incorporated the verified 104-file package from local revision 5. All **23 frozen taxonomy files and their internal seal** remain byte-identical. Root integrity records cover the combined package and are refreshed with this README.

Frozen “public candidate” and nonpublication statements describe preparation context; publication status is stated here. Claim-map manuscript locators refer to the separate paper. Originals and prior packages remain locally preserved.

## ⚖️ Rights and release scope

Public availability does not establish a redistribution license. Ownership/license coverage for new code, documents, and derived data remains unresolved; **no MIT or CC license has been assigned**. The upstream MIT notice is retained as license evidence only.

The release excludes primary full text, abstracts, screenshots, unrestricted internal conversations or hidden reasoning, raw service envelopes, credentials, original research Git, and archives. It includes the scoped research artifacts and saved final-answer evidence described above.
