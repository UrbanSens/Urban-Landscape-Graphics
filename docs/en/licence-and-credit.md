# Licence and credit

*`ulg` is free software under the MIT licence. In return UrbanSens asks for one thing: say where the style comes from.*

## Licence

The library, the catalog data (elements, palette, themes, crosswalks), the tools and this documentation are
released under the **MIT licence**. You may use them, change them and ship them in commercial products. Keep the
copyright and licence notice with the code you copy. The licence covers the software and its data files; it asks
you to add nothing to the maps and sheets you draw with it.

```text
MIT License

Copyright (c) 2026 UrbanSens

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

The same text is the file `LICENSE` in the repository.

## Please credit UrbanSens

Crediting is a request, not a condition of the licence, but it is how a small project gets found. If `ulg` or the
UrbanSens Ecological Vector Style helped with a map, a plan, a report, a tender or a paper, please say so.
The website of UrbanSens: [urbansens.de](https://urbansens.de/).

**In a map caption, a legend or the list of sources**

> Map style: UrbanSens Ecological Vector Style (ulg), urbansens.de

**In German**

> Kartenstil: UrbanSens Ecological Vector Style (ulg), urbansens.de

**In a reference list** (APA style)

> UrbanSens. (2026). *Urban Landscape Graphics (ulg): the UrbanSens Ecological Vector Style as a library* (Version 0.1.0)
> [Computer software]. https://github.com/UrbanSens/Urban-Landscape-Graphics

**In BibTeX**

```bibtex
@misc{urbansens_ulg_2026,
  author       = {{UrbanSens}},
  title        = {Urban Landscape Graphics ({ulg}): the {UrbanSens} Ecological Vector Style as a library},
  year         = {2026},
  note         = {Version 0.1.0, software},
  howpublished = {\url{https://github.com/UrbanSens/Urban-Landscape-Graphics}}
}
```

<!-- site-only
The file `CITATION.cff` in the repository holds the same reference in a machine-readable form.
-->
<!-- github-only:start -->
The file [`CITATION.cff`](../../CITATION.cff) holds the same reference in a machine-readable form; GitHub turns it
into the **Cite this repository** button at the top of the repository page.
<!-- github-only:end -->

In Python, `ulg.credit_line()` returns the caption line (`ulg.credit_line("de")` the German one), so that a script
or an agent that draws a map can put it where the sources are named:

```python
import ulg

ulg.credit_line()       # 'Style: UrbanSens Ecological Vector Style (ulg 0.1.0) · urbansens.de'
ulg.credit_line("de")   # 'Kartenstil: UrbanSens Ecological Vector Style (ulg 0.1.0) · urbansens.de'
```

## The mark on the sheets

The sheets the library draws itself carry a small UrbanSens mark (the logo with the name of the style, the version
and the website) in the lower right corner: `ulg.style_sheet()`, `ulg.catalog_sheet()` (the inventory of all
elements) and the images of this documentation. Leave the mark on when you share them. `credit=False` (or
`ulg sheet --no-credit`) draws the sheet without it. Legends go into your layouts, so `ulg.legend_svg()` adds the
mark only with `credit=True`.

Your maps are never stamped: `ulg.render_svg()`, `ulg.plot()` and the exported styles for QGIS, GeoServer, MapLibre
and design tools add nothing.

## The logos

The UrbanSens logo (`src/ulg/data/brand/urbansens-logo.png`) and the ulg logo (`docs/img/logo/`) are UrbanSens'
artwork. Use them to credit the project or to show that you work with the style; do not use them in a way that
suggests UrbanSens endorses your work. The MIT licence grants rights to the software, not trademark rights.

## Material from others

- **Fonts.** The headings of the HTML documentation and the wordmark of the ulg logo are set in Rethink Sans
  (SIL Open Font License 1.1, `tools/html/fonts/OFL.txt`).
- **Historical images** in [Origins](01-origins.md) are linked from Wikimedia Commons, not copied; each has its own
  licence, listed under *Image credits* in that chapter.
- **Standards, official colours and codes.** Class codes, colour values and coefficients of external schemes (ALKIS,
  basemap.de, BfN, OpenStreetMap Carto, CORINE, PlanZV and others) are quoted with their source in the
  [reference pages](../reference/themes.md) and in the [standards report](../research/standards-report.md). The schemes and
  their names belong to their publishers.
- **OpenStreetMap.** No OpenStreetMap data ships with `ulg`; the examples use an invented sample block. Maps you
  draw from OpenStreetMap data need OpenStreetMap's own credit: © OpenStreetMap contributors.

---

Back to the [overview](index.md)
