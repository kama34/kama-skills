# Methodology

Use this reference when designing a project wiki, deciding what belongs in each layer, or explaining why the structure works.

## Core Pattern

The LLM Wiki pattern, described by Andrej Karpathy in `llm-wiki.md`, treats the wiki as a persistent, compounding artifact. Instead of only retrieving raw chunks at query time, the agent reads sources once, extracts durable knowledge, updates linked markdown pages, and keeps indexes, contradictions, and summaries current.

Use three layers:

- Raw sources: curated evidence such as articles, PDFs, transcripts, docs, images, and datasets. These should be preserved.
- Wiki: LLM-maintained markdown synthesis: source notes, entity/concept pages, maps, project notes, decisions, comparisons, and answers worth keeping.
- Schema: the project instructions that tell future agents how to maintain the wiki. In Codex projects this should live in `AGENTS.md` or `90-meta/wiki-rules.md`.

This is not a claim that markdown wikis replace RAG at every scale. It is best for small-to-medium, human-curated, slow-to-moderate change projects where maintenance quality matters more than raw ingestion volume.

## Operations

- Ingest: add one source or a batch, summarize it, record provenance, update affected notes/maps/index/log.
- Query: answer from the wiki first, then sources when evidence is needed; file valuable answers back into notes.
- Lint: periodically find broken links, stale claims, contradictions, orphan notes, missing source citations, duplicate concepts, and weak maps.

## Index and Log

Keep two navigation files:

- `90-meta/index.md`: content-oriented catalog of important pages, grouped by type or map.
- `90-meta/log.md`: append-only chronological record of ingests, migrations, queries, lint passes, and decisions.

Use consistent log headings so simple text search can recover recent activity.

## Zettelkasten Adaptation

Borrow principles, not ceremony:

- Atomicity: one durable idea per atomic note when possible.
- Connectivity: every durable note should link to related notes or a source.
- Structure notes: Maps of Content organize growing clusters without forcing rigid folder taxonomies.
- Source separation: source notes preserve what a source says; atomic notes preserve what the project now believes or can reuse.
- Anti-collector rule: clipping is not knowledge. Every stored source should eventually produce links, synthesis, or a clear "not processed" status.

## Boundary Conditions

Prefer a compact wiki over an exhaustive archive. Do not create a note for every tiny fact. Promote ideas into atomic notes when they are likely to be reused, disputed, combined with other sources, or important for future agents.

References:

- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- https://github.com/kepano/obsidian-skills
- https://zettelkasten.de/overview/
