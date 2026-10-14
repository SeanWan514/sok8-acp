# Synthesis evidence

`sources.json` records the 66 unique sources cited in the landscape or six core synthesis claims: 40 mapped-corpus sources, five supplementary scholarly sources and 21 official specifications/documents. Each record has a retrievable locator, analytical role, claim IDs and reading scope. Mapped sources join to `taxonomy/expected/included-identifiers.csv` using `included_identifier`; source-record IDs preserve the underlying provenance.

`claims.json` contains six claim contrasts, their conditions and decisive citation keys. The broader `claim_ids` in the source ledger include contextual evidence as well as decisive examples; they do not assert that every linked source independently establishes an entire claim. `tables.json` holds the stage/function map, 27 search expressions and eligibility rules. Table 1 is calculated from the taxonomy outputs. Run the root `reproduce.py` to export all five tables and the complete source–claim edge list as CSV.

Reading scope follows the retained evidence: primary abstracts, targeted passages where recorded, and specification sections. Official snapshot notes identify the version used; a moving URL can change after that snapshot. The ledger redistributes bibliographic metadata and original analytical summaries, without source full texts or abstracts.
