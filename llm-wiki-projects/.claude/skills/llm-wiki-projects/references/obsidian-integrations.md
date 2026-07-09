# Obsidian Integrations

Use this reference when a task touches Obsidian-specific syntax or tools.

## Local Skills

- Use `obsidian-markdown` when creating or editing `.md` notes with properties, wikilinks, embeds, callouts, block references, or Obsidian-specific syntax.
- Use `obsidian-bases` when creating or editing `.base` files.
- Use `json-canvas` when creating or editing `.canvas` maps.
- Use `obsidian-cli` when the user asks to inspect or operate inside an active Obsidian vault.
- Use `defuddle` when the user provides a web page to turn into clean markdown before adding it as a source.

## Bases

Default generated Bases:

- `sources.base`: table of source notes and processing status.
- `atomic-notes.base`: table of atomic notes by status and updated date.
- `projects.base`: project and decision notes.

Keep Bases under `90-meta/bases/` so they remain operational but do not dominate the wiki root.

## Canvas

Use a `.canvas` file for high-level spatial maps, not as the only source of truth. Every important canvas node should link to a markdown note or include a short text summary that can stand alone.

## Attachments

Use `assets/` for images and media referenced by notes. Use `assets/sources/` for source files kept as evidence, with `10-sources/<id>.md` as the markdown wrapper. Prefer local media when a note depends on an image, chart, or PDF page.

## Compatibility Rules

- Keep YAML valid.
- Keep file names stable after wikilinks exist.
- Prefer wikilinks for notes and Markdown links for non-note files.
- Avoid wikilinks with aliases inside Markdown tables; use Markdown links inside tables or move wikilinks into a nearby paragraph.
- Avoid relative paths inside wikilinks when the wiki validator uses stem-based resolution.
- Avoid embedding remote images when local copies are available.
