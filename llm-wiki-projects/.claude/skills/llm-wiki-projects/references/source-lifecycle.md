# Source Lifecycle

Use this reference when adding, reading, validating, or promoting source material.

## Two-Layer Source Model

Every durable source gets a markdown wrapper:

```text
10-sources/<source-id>.md        # metadata, summary, claims, provenance
assets/sources/<source-id>.<ext> # raw evidence when a local copy is allowed
```

The markdown wrapper is what agents read by default. The raw file is evidence for verification.

## Source ID

Prefer stable kebab-case IDs:

- papers/books: `<lastname>-<year>-<slug>`;
- laws/standards: `<type>-<number>-<year>-<slug>`;
- repositories: `<repo-name>-repo`;
- interviews/transcripts: `interview-<person>-<date>`;
- web pages without authors: `<domain>-<slug>-<year>`.

Use a 2-4 word slug. If an ID exists, add `-2`, `-3`, etc.

## Source Wrapper Sections

Recommended sections:

- what this is;
- where it lives: wiki copy, original URL/path, DOI or identifier;
- author abstract or original summary when available;
- key claims with evidence quote or page/section;
- methods/results/limitations when relevant;
- what to use in project(s);
- citation or reuse notes;
- linked atomic notes.

## Deep Reading

Do not invent quotes, page numbers, methods, or findings. If the raw source was not read, mark the note `read-status: reading-meta-only` and keep claims modest.

When reading a long source, chunk it and record which parts were actually inspected. Promote reusable ideas into `20-notes`; leave one-off facts in the source note.

## Project Use

When a source supports a project:

1. Add the project to `used-in`.
2. Add a source line to the project dashboard.
3. Add section-specific notes under "What to use" when the project has a structure.
4. Link derived atomic notes back to the source.
