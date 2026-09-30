# Fonts of the HTML documentation and the logo

**Rethink Sans** (variable, weights 400–800) by the Rethink Sans Project Authors, based on DM Sans by
Colophon Foundry. Licensed under the SIL Open Font License 1.1 (`OFL.txt`).

| File | Use |
|---|---|
| `RethinkSans-VariableFont_wght.ttf` | the original font file; `tools/build_logo.py` converts the wordmark to outlines with it |
| `RethinkSans.woff2` | a Latin subset of the same font (Basic Latin, Latin-1, Latin Extended-A, common punctuation and arrows) that `tools/build_html.py` embeds in the style sheet, so the pages need no font download |

The body text of the documentation uses the reader's system serif (New York, Iowan Old Style, Charter or
Georgia), nothing is fetched from a font service.
