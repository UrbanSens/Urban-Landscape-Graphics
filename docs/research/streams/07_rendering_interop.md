# 07 · Rendering techniques and style-format interoperability

Research stream for **Urban Landscape Graphics** (`ulg`, house style "UrbanSens – Ecological Vector Style").
Compiled 2026-09-30. Scope: QGIS style formats, OGC style encodings, MapLibre/Leaflet/OpenLayers/deck.gl, hand-drawn vector algorithms, design tokens, accessibility rules for map colours, agent-facing packaging.

## Evidence marks

- **V** = verified this session in a primary source (URL given).
- **S** = secondary source (blog, issue thread, search-result summary, third-party article).
- **R** = recalled from memory / not verified this session.
- **D** = my own derivation or design proposal (not a sourced fact).
- **T** = tested locally this session (Python 3.12.7, NumPy 1.26.4, SciPy 1.13.1, Shapely 2.1.2, Matplotlib 3.9.2 – older than the current releases in section 0). Test scripts: `scratchpad/s07_tests/`.

**Caveat on "V".** Pages were read through a fetch tool that extracts text with a small model. Snippets marked V were returned as verbatim quotes of the cited URL, but attribute order and whitespace can differ from the byte-exact source, and long values are abridged where noted. No style file below has been loaded into the target software in this session. Every exporter must therefore be covered by a round-trip test (load in target, save, diff).

---

## 0. Version snapshot (2026-09-30)

| Item | State | Mark · source |
|---|---|---|
| QGIS latest release | **4.2.3** (4.2.0 on 2026-07-03; 4.0.0 on 2026-03-06, first Qt6-based release, code name "Norrköping") | V roadmap + schedule.ics; code name S |
| QGIS LTR | **3.44.15** (last 3.x line; scheduled point releases up to 3.44.19 on 2027-01-22) | V |
| Next QGIS LTR | schedule.ics lists "QGIS Long-term release **4.4.0**" on **2026-10-30**; it replaces 3.44 in the LTR repositories as 4.4.4 on 2027-03-05. The blog post of 2025-10-07 had announced 4.2 as first 4.x LTR; the live schedule no longer says that. | V (ics, roadmap) / V (blog) – contradiction noted |
| QGIS style XML version | `STYLE_CURRENT_VERSION "2"`, root `<qgis_style version="2">` in `master` | V qgsstyle.cpp, symbology-style.xml |
| GeoServer | **3.0.0** released 2026-06-12 (Spring 7, Jakarta EE; data directory format unchanged from 2.28.x; docs moved to Markdown and new URLs) | V osgeo.org news |
| MapLibre GL JS | **6.11.2**; `@maplibre/maplibre-gl-style-spec` 26.4.4 | V registry.npmjs.org |
| OpenLayers | **10.10.0** | V apidoc header |
| Leaflet | reference docs are for **1.9.4**; 2.0 alpha published 2025-05, stable release date marked "unknown" in the tracking issue | V / S |
| Matplotlib | **3.11.2** (2026-09-11); 3.11.0 on 2026-06-11 | V PyPI / S |
| SciPy / NumPy / Shapely | docs at 1.18.0 / 2.5 / 2.1.2 | V |
| rough.js | 4.6.6 (deps: hachure-fill ^0.5.2, path-data-parser, points-on-curve, points-on-path) | V package.json |
| `rough` (Python port, cktlco/rough-py) | 1.6, MIT, Python ≥ 3.10, no dependencies | V PyPI JSON |
| DTCG design tokens | Format / Color / Resolver Module **2025.10** – "Final Community Group Report 28 October 2025", first stable version | V designtokens.org |
| Style Dictionary | **5.5.5**, ESM, Node ≥ 22 | V registry.npmjs.org |
| WCAG | 2.2, W3C Recommendation (edition of 12 December 2024); approved as ISO/IEC 40500:2025 on 2025-10-21 | V w3.org/TR / S search hit on w3.org news |
| EN 301 549 | **V4.1.1 published September 2026** (adopts WCAG 2.2). Not yet cited in the OJEU, so V3.2.1 (2021, WCAG 2.1 AA) remains the legal reference | V AccessibleEU |
| MCP | spec revision **2026-07-28**; Python SDK `mcp` **2.2.0** (2026-09-07); `fastmcp` **4.0.10** (2026-09-25) | V |
| Agent Skills | open spec at agentskills.io; Claude Code reads `AGENTS.md` natively since v2.1.277 | V |
| llms.txt | page titled "The /llms.txt file, v2", published 2024-09-03, modified 2026-08-10 | V llmstxt.org |

---

## 1. QGIS style formats

### 1.1 Versions and what changed with QGIS 4

- Current binaries: "LTR 3.44.15 and Latest 4.2.3". **V** https://qgis.org/resources/roadmap/
- Schedule (from https://qgis.org/schedule.ics, **V**): 4.0.0 regular release 2026-03-06; 4.2.0 regular release 2026-07-03; feature freeze 4.3 on 2026-09-18; **"Long-term release 4.4.0" 2026-10-30**; 4.6.0 on 2027-03-05. Roadmap rule: "In the first four months after its release, a new LTR is also the current LR. In this phase, the new LTR doesn't replace the previous LTR in the LTR repositories." **V**
- QGIS 4.0 is the Qt6 migration; deprecated APIs were kept where possible, but plugins written only for Qt5 are unlikely to run in 4.x. **S** (search summaries of the QGIS blog and release coverage; the 4.0 changelog itself was read, **V**, and lists no file-format change).
- Style file format: I found **no documented change** of the 2D symbology XML between 3.x and 4.x. Evidence: `master` still defines `#define STYLE_CURRENT_VERSION "2"` and writes `<qgis_style version="2">`; the 4.0 changelog lists no format break. **V** (absence of a statement, not a positive guarantee). `QgsStyle::exportXml` in `master` appends these children in order: `symbols`, `colorramps`, `textformats`, `labelsettings`, `legendpatchshapes`, `symbols3d`, `materialsettings`. **V** https://raw.githubusercontent.com/qgis/QGIS/master/src/core/symbology/qgsstyle.cpp
- Practical consequence (**D**): target both 3.44 LTR and 4.2/4.4 with one file format, but test in both.

### 1.2 Two property encodings inside `<layer>`: `<prop>` and `<Option>`

Symbol-layer properties are a flat string map. Three generations exist in real files:

1. Legacy only: `<prop k="color" v="247,247,247,255"/>` (QGIS 2.x–3.1x; still present in the default style shipped in `master`). **V** symbology-style.xml
2. Dual: `<Option type="Map">…</Option>` **and** duplicate `<prop>` elements in the same `<layer>` (symbol tagged `addedVersion="32300"`). **V** same file, "wavy line" symbol
3. `<Option>` only (a QML written by 3.18.3 shows only `<Option>`; geostyler-qgis-parser switches its writer to Option-only for versions ≥ 3.28). **V** gist / **S** parser source summary

QGIS reads both. For widest compatibility an exporter can write the dual form (**D**).

Value encodings (**V** https://raw.githubusercontent.com/qgis/QGIS/master/src/core/symbology/qgssymbollayerutils.cpp):

| Thing | Encoding |
|---|---|
| Colour | `"%1,%2,%3,%4"` = `r,g,b,a` with 0–255 integers. `decodeColor` accepts 3 or 4 comma-separated parts, otherwise falls back to `QColor(str)` |
| Map-unit scale | `3x:minScale,maxScale,minSizeMMEnabled,minSizeMM,maxSizeMMEnabled,maxSizeMM`, default `3x:0,0,0,0,0,0` |
| Point / size | `x,y` / `w,h` |
| Pen join | `bevel`, `miter`, `round` |
| Pen cap | `square`, `flat`, `round` |
| Pen style | `no`, `solid`, `dash`, `dot`, `dash dot`, `dash dot dot` |
| Brush style | `solid`, `horizontal`, `vertical`, `cross`, `b_diagonal`, `f_diagonal`, `diagonal_x`, `dense1`…`dense7`, `no` |
| Marker clip mode | `no`, `shape`, `centroid_within`, `completely_within` |
| Line clip mode | `no`, `during_render`, `before_render` |
| Coordinate reference | `feature`, `viewport` |
| Scale method | `diameter`, `area` |

Render units: the test suite enumerates `RenderMillimeters, RenderMetersInMapUnits, RenderMapUnits, RenderPixels, RenderPercentage, RenderPoints, RenderInches`; unknown strings decode to millimetres; decoding is case-insensitive and trims whitespace; aliases `Meters`, `MapUnits`, `Percent`, `Points` are accepted. **V** test_qgsunittypes.py. Encoded strings: `MM` (**V**, in every sample file), `MapUnit`, `RenderMetersInMapUnits`, `Pixel`, `Percentage`, `Point`, `Inch` (**S**: search summary of `qgsunittypes.cpp`; could not open the function body directly).

### 1.3 Style library `.xml` (Style Manager import)

Real file, default style shipped with QGIS (**V** https://raw.githubusercontent.com/qgis/QGIS/master/resources/symbology-style.xml):

```xml
<!DOCTYPE qgis_style>
<qgis_style version="2">
  <symbols>
    <symbol force_rhr="0" name="gray 1 fill" alpha="1" tags="Grayscale" type="fill" clip_to_extent="1" addedVersion="30000">
      <layer enabled="1" class="SimpleFill" locked="0" pass="0">
        <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
        <prop k="color" v="247,247,247,255"/>
        <prop k="joinstyle" v="bevel"/>
        <prop k="offset" v="0,0"/>
        <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
        <prop k="offset_unit" v="MM"/>
        <prop k="outline_color" v="82,82,82,255"/>
        <prop k="outline_style" v="solid"/>
        <prop k="outline_width" v="0.26"/>
        <prop k="outline_width_unit" v="MM"/>
        <prop k="style" v="solid"/>
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" value="" type="QString"/>
            <Option name="properties"/>
            <Option name="type" value="collection" type="QString"/>
          </Option>
        </data_defined_properties>
      </layer>
    </symbol>
  </symbols>
</qgis_style>
```

(The closing `</symbols></qgis_style>` is added by me; the file continues with many more symbols.)

Pattern layer with a nested sub-symbol, same file (**V**). Sub-symbols are named `@<parent name>@<layer index>`:

```xml
<symbol favorite="1" force_rhr="0" name="hashed black /" alpha="1" tags="Grayscale" type="fill" clip_to_extent="1" addedVersion="30000">
  <layer enabled="1" class="LinePatternFill" locked="0" pass="0">
    <prop k="angle" v="45"/>
    <prop k="color" v="55,126,184,255"/>
    <prop k="distance" v="2"/>
    <prop k="distance_map_unit_scale" v="3x:0,0,0,0,0,0"/>
    <prop k="distance_unit" v="MM"/>
    <prop k="line_width" v="0.26"/>
    <prop k="line_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
    <prop k="line_width_unit" v="MM"/>
    <prop k="offset" v="0"/>
    <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
    <prop k="offset_unit" v="MM"/>
    <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
    <prop k="outline_width_unit" v="MM"/>
    <data_defined_properties>…</data_defined_properties>
    <symbol force_rhr="0" name="@hashed black /@0" alpha="1" type="line" clip_to_extent="1">
      <layer enabled="1" class="SimpleLine" locked="0" pass="0">
        <prop k="capstyle" v="square"/>
        <prop k="customdash" v="5;2"/>
        <prop k="joinstyle" v="bevel"/>
        <prop k="line_color" v="0,0,0,255"/>
        <prop k="line_style" v="solid"/>
        <prop k="line_width" v="0.3"/>
        <prop k="line_width_unit" v="MM"/>
        <prop k="offset" v="0"/>
        <prop k="use_custom_dash" v="0"/>
        <!-- further props abridged -->
      </layer>
    </symbol>
  </layer>
  <layer enabled="1" class="SimpleLine" locked="0" pass="0">
    <!-- outline layer: same SimpleLine keys, line_width 0.46 -->
  </layer>
</symbol>
```

Colour ramps in the same root: `<colorramps><colorramp type="gradient" name="…">` with keys `color1`, `color2`, `discrete`, `stops` (format `0.25;241,182,218,255:0.5;247,247,247,255`), plus `rampType`, `spec` (`rgb|hsv|hsl`), `direction` (`cw|ccw`). A preset (discrete list) ramp uses keys `preset_color_<i>`, `preset_color_name_<i>`, `rampType`. **V** categorized.qml test file and qgscolorrampimpl.cpp. The `type` string for the preset ramp (I believe `preset`) is **R**.

Import/export: Style Manager exports selected items "to an `.XML` file… a single file containing all the selected items"; symbols can also be exported as PNG or SVG; import takes an XML file or URL; the user library lives in `symbology-style.db` in the active profile; shared styles are at https://hub.qgis.org/styles. **V** https://docs.qgis.org/latest/en/docs/user_manual/style_library/style_manager.html

### 1.4 Layer style `.qml`

Root and renderer opening tags from a file written by QGIS 3.18.3 (**V** https://gist.github.com/lymperis-e/6b17521fa6df4a00671d0b1c7caf9d47):

```xml
<qgis simplifyDrawingTol="1" simplifyMaxScale="1" maxScale="0" simplifyLocal="1" hasScaleBasedVisibilityFlag="0" version="3.18.3-Zürich" minScale="100000000" readOnly="0" labelsEnabled="1" simplifyAlgorithm="0" styleCategories="AllStyleCategories" simplifyDrawingHints="1">
  <renderer-v2 forceraster="0" enableorderby="0" symbollevels="0" type="RuleRenderer">
```

Categorized renderer, QGIS test data (**V** https://raw.githubusercontent.com/qgis/QGIS/master/tests/testdata/symbol_layer/categorized.qml):

```xml
<renderer-v2 attr="subregion" forceraster="0" symbollevels="0" type="categorizedSymbol" enableorderby="0">
  <categories>
    <category render="true" symbol="0" value="Antarctica" label="Antarctica"/>
    <category render="true" symbol="1" value="Australia and New Zealand" label="Australia and New Zealand"/>
  </categories>
  <symbols>
    <symbol alpha="1" clip_to_extent="1" type="fill" name="0">
      <layer pass="0" class="SimpleFill" locked="0">
        <prop k="color" v="208,28,139,255"/>
        <prop k="outline_color" v="0,0,0,255"/>
        <prop k="outline_width" v="0.26"/>
      </layer>
    </symbol>
    <!-- symbol name="1" … -->
  </symbols>
  <source-symbol>…</source-symbol>
  <colorramp type="gradient" name="[source]">…</colorramp>
  <invertedcolorramp value="0"/>
  <rotation/>
  <sizescale scalemethod="diameter"/>
</renderer-v2>
```

(Element order inside `<renderer-v2>` reconstructed from two extractions of the same file; `symbol="N"` refers to `<symbol name="N">`.) Current QGIS writes two more attributes on `<category>`: `type="string"` and `uuid="{…}"`, e.g. `<category symbol="0" label="11" value="11" type="string" render="true" uuid="{9ee747f8-197f-42a6-8a87-33e3377dd625}"/>`. **V** https://github.com/opengisch/QField/issues/6202 (the uuid key exists since 3.34, **S**). The issue also shows that a `type` that mismatches the field type breaks category visibility in QField, so write `type` to match the data (`string` for a class-name column).

Rule-based renderer with scale limits, QGIS test data (**V** https://raw.githubusercontent.com/qgis/QGIS/master/tests/testdata/symbol_layer/ruleBased.qml):

```xml
<renderer-v2 forceraster="0" symbollevels="0" type="RuleRenderer" enableorderby="0">
  <rules key="{318c2945-dfa9-44b8-a8d3-1b167642830a}">
    <rule scalemaxdenom="40000000" filter="POP_EST > 100000"
          key="{2302b573-a5b0-4118-9df3-bb01e802d96b}" symbol="0"
          scalemindenom="1000" label="pophigh"/>
    <rule filter="POP_EST &lt;= 100000" key="{961eba0d-523d-42c9-bc88-9d4a9704ddee}"
          symbol="1" label="popLow"/>
  </rules>
  <symbols>…</symbols>
</renderer-v2>
```

`scalemindenom="1000"` and `scalemaxdenom="40000000"` make the rule active between 1:1 000 and 1:40 000 000. Rules can be nested (child `<rule>` inside `<rule>`), which is the natural carrier for "class → LOD" trees (**R** for nesting syntax).

Not verified this session (**R**): the `<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>` prolog, the trailing `<blendMode>`, `<featureBlendMode>`, `<layerGeometryType>2</layerGeometryType>` elements, and `styleCategories="Symbology"` for a symbology-only file.

### 1.5 Symbol-layer reference for the ULG fill stack

Target stack per element: `SimpleFill` (pastel, no outline) → texture layer (`SVGFill`, `PointPatternFill`, `RandomMarkerFill` or `LinePatternFill`) → outline (`SimpleLine`, optionally wrapped in a `GeometryGenerator`).

**SimpleFill** – `layerType()` = `SimpleFill`. Keys written: `color`, `style`, `outline_color`, `outline_style`, `outline_width`, `outline_width_unit`, `border_width_map_unit_scale`, `joinstyle`, `offset`, `offset_unit`, `offset_map_unit_scale`. **V** https://raw.githubusercontent.com/qgis/QGIS/master/src/core/symbology/qgsfillsymbollayer.cpp

**SVGFill** – `layerType()` = `SVGFill`. Keys written: `svgFile` (or `data`), `width`, `angle`, `color`, `outline_color`, `outline_width`, `pattern_width_unit`, `pattern_width_map_unit_scale`, `svg_outline_width_unit`, `svg_outline_width_map_unit_scale`, `outline_width_unit`, `outline_width_map_unit_scale`, `parameters`. Legacy keys still read: `svgFillColor`, `svgOutlineColor`, `svgOutlineWidth`. **V** same source. Docs: "fills the polygon using SVG markers of a given size (Texture width)". **V** symbol_selector.html. I did not find a real file with an `SVGFill` layer in `<Option>` form; treat a hand-written one as untested.

**PointPatternFill** – real layer written before 3.24 (**V** https://raw.githubusercontent.com/Klakar/QGIS_resources/master/collections/Geosupportsystem/symbol/70s_wallpaper.xml):

```xml
<layer class="PointPatternFill" enabled="1" pass="0" locked="0">
  <prop v="0" k="displacement_x"/>
  <prop v="3x:0,0,0,0,0,0" k="displacement_x_map_unit_scale"/>
  <prop v="MM" k="displacement_x_unit"/>
  <prop v="0" k="displacement_y"/>
  <prop v="3x:0,0,0,0,0,0" k="displacement_y_map_unit_scale"/>
  <prop v="MM" k="displacement_y_unit"/>
  <prop v="10" k="distance_x"/>
  <prop v="3x:0,0,0,0,0,0" k="distance_x_map_unit_scale"/>
  <prop v="MM" k="distance_x_unit"/>
  <prop v="10" k="distance_y"/>
  <prop v="3x:0,0,0,0,0,0" k="distance_y_map_unit_scale"/>
  <prop v="MM" k="distance_y_unit"/>
  <prop v="0" k="offset_x"/>
  <prop v="3x:0,0,0,0,0,0" k="offset_x_map_unit_scale"/>
  <prop v="MM" k="offset_x_unit"/>
  <prop v="0" k="offset_y"/>
  <prop v="3x:0,0,0,0,0,0" k="offset_y_map_unit_scale"/>
  <prop v="MM" k="offset_y_unit"/>
  <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
  <prop v="MM" k="outline_width_unit"/>
  <data_defined_properties>
    <Option type="Map">
      <Option value="" type="QString" name="name"/>
      <Option name="properties"/>
      <Option value="collection" type="QString" name="type"/>
    </Option>
  </data_defined_properties>
  <symbol alpha="1" clip_to_extent="1" type="marker" force_rhr="0" name="@70's Wallpaper@1">
    <layer class="EllipseMarker" enabled="1" pass="0" locked="0">
      <!-- marker props; this file data-defines width/height with randf(3,10) -->
    </layer>
  </symbol>
</layer>
```

Keys added in QGIS 3.24 (**V** PR diff https://patch-diff.githubusercontent.com/raw/qgis/QGIS/pull/45638.diff): `random_deviation_x`, `random_deviation_y`, `random_deviation_x_unit`, `random_deviation_y_unit`, `random_deviation_x_map_unit_scale`, `random_deviation_y_map_unit_scale`, `seed` (if absent on creation, a random seed is generated), and `clip_mode` (values in 1.2). 3.24 also added a rotation angle for the whole pattern and a coordinate reference mode ("Align pattern to feature" / "Align pattern to map extent"). **V** https://qgis.org/project/visual-changelogs/visualchangelog324/ – their key names (`angle`, `coordinate_reference`) are **R**.

**RandomMarkerFill** – since QGIS 3.12 (**V** API docs). Real layer with an embedded SVG marker (**V** https://raw.githubusercontent.com/Klakar/QGIS_resources/master/collections/Geosupportsystem/symbol/crayon_fill.xml):

```xml
<layer pass="0" enabled="1" locked="0" class="RandomMarkerFill">
  <prop k="clip_points" v="0"/>
  <prop k="count_method" v="1"/>
  <prop k="density_area" v="1000"/>
  <prop k="density_area_unit" v="MM"/>
  <prop k="density_area_unit_scale" v="3x:0,0,0,0,0,0"/>
  <prop k="point_count" v="10"/>
  <prop k="seed" v="758041469"/>
  <data_defined_properties>…</data_defined_properties>
  <symbol clip_to_extent="1" force_rhr="0" name="@Crayon Fill@1" alpha="1" type="marker">
    <layer pass="0" enabled="1" locked="0" class="SvgMarker">
      <prop k="angle" v="0"/>
      <prop k="color" v="0,0,0,255"/>
      <prop k="fixedAspectRatio" v="0"/>
      <prop k="horizontal_anchor_point" v="1"/>
      <prop k="name" v="base64:PD94bWwgdmVyc2lvbj0iMS4wIi…"/>  <!-- ~12 000 chars, abridged -->
      <!-- further SvgMarker props not extracted -->
    </layer>
  </symbol>
</layer>
```

Semantics (**V** PR diffs 32241 and 32456, API docs, user manual):

- `count_method`: `0` = absolute count, `1` = density-based (`AbsoluteCount` / `DensityBasedCount`; in `master` the enum is `Qgis::PointCountMethod`). Defaults: `point_count` 10, `density_area` 250.0.
- `seed`: "the random number seed to use when generating points, or 0 if a truly random sequence will be used (causing points to appear in different locations with every map refresh)". A ULG export must always write a non-zero seed.
- `clip_points`: whether markers near the edge are clipped to the polygon boundary.
- Density area "ensures the fill density of markers remains the same on different scale/zoom levels". The original implementation counts per polygon part (**S**).
- Constructor in `master`: `QgsRandomMarkerFillSymbolLayer(int pointCount=10, Qgis::PointCountMethod method=Absolute, double densityArea=250.0, unsigned long seed=0)`.

**SimpleLine** (outline) – full key set from a symbol written by QGIS 3.23 in dual form (**V** symbology-style.xml, sub-symbol of "wavy line"): `align_dash_pattern`, `capstyle`, `customdash`, `customdash_map_unit_scale`, `customdash_unit`, `dash_pattern_offset`, `dash_pattern_offset_map_unit_scale`, `dash_pattern_offset_unit`, `draw_inside_polygon`, `joinstyle`, `line_color`, `line_style`, `line_width`, `line_width_unit`, `offset`, `offset_map_unit_scale`, `offset_unit`, `ring_filter`, `trim_distance_end`, `trim_distance_end_map_unit_scale`, `trim_distance_end_unit`, `trim_distance_start`, `trim_distance_start_map_unit_scale`, `trim_distance_start_unit`, `tweak_dash_pattern_on_corners`, `use_custom_dash`, `width_map_unit_scale`.

**GeometryGenerator** – keys `SymbolType` (`Marker`, `Line`, anything else = fill), `geometryModifier` (expression), `units`. **V** https://raw.githubusercontent.com/qgis/QGIS/master/src/core/symbology/qgsgeometrygeneratorsymbollayer.cpp. Complete real layer in dual encoding (**V** symbology-style.xml, first symbol; inner SimpleLine keys as listed above):

```xml
<symbol type="line" favorite="1" clip_to_extent="1" force_rhr="0" name="wavy line" tags="Showcase" alpha="1" addedVersion="32300">
  <data_defined_properties>
    <Option type="Map">
      <Option type="QString" name="name" value=""/>
      <Option name="properties"/>
      <Option type="QString" name="type" value="collection"/>
    </Option>
  </data_defined_properties>
  <layer locked="0" pass="0" enabled="1" class="GeometryGenerator">
    <Option type="Map">
      <Option type="QString" name="SymbolType" value="Line"/>
      <Option type="QString" name="geometryModifier" value="wave_randomized(&#xa;&#x9;$geometry,&#xa;&#x9;min_wavelength:=2,&#xa;&#x9;max_wavelength:=6,&#xa;&#x9;min_amplitude:=0,&#xa;&#x9;max_amplitude:=0.3,&#xa;&#x9;seed:=1&#xa;)"/>
      <Option type="QString" name="units" value="MM"/>
    </Option>
    <prop k="SymbolType" v="Line"/>
    <prop k="geometryModifier" v="wave_randomized(&#xa;&#x9;$geometry,&#xa;&#x9;min_wavelength:=2,&#xa;&#x9;max_wavelength:=6,&#xa;&#x9;min_amplitude:=0,&#xa;&#x9;max_amplitude:=0.3,&#xa;&#x9;seed:=1&#xa;)"/>
    <prop k="units" v="MM"/>
    <data_defined_properties>…</data_defined_properties>
    <symbol type="line" clip_to_extent="1" force_rhr="0" name="@wavy line@0" alpha="1">
      <data_defined_properties>…</data_defined_properties>
      <layer locked="0" pass="0" enabled="1" class="SimpleLine">
        <Option type="Map">
          <Option type="QString" name="capstyle" value="round"/>
          <Option type="QString" name="joinstyle" value="round"/>
          <Option type="QString" name="line_color" value="35,35,35,255"/>
          <Option type="QString" name="line_style" value="solid"/>
          <Option type="QString" name="line_width" value="0.38"/>
          <Option type="QString" name="line_width_unit" value="MM"/>
          <!-- remaining SimpleLine options as listed above, then the duplicate <prop> set -->
        </Option>
      </layer>
    </symbol>
  </layer>
</symbol>
```

This shipped symbol is the closest official prior art for a hand-drawn outline: a sine-like randomized wave with wavelength 2–6 mm and amplitude 0–0.3 mm, fixed seed 1, round caps and joins.

Marker sub-symbol keys for `SimpleMarker` (`name`, `color`, `size`, `size_unit`, `outline_color`, `outline_style`, `outline_width`, `angle`, `offset`, `scale_method`, anchor points …) are **R**; I did not extract a real `SimpleMarker` layer.

### 1.6 Embedding SVG and parameter substitution

- Embedded SVG: "Feature: SVG files can be embedded in projects and symbols – Allows SVG images for symbology, labels, etc to be directly embedded inside a project file (or QML style, or QPT print template!) by encoding the svg as a standard base64 string." → **since QGIS 3.4**. **V** https://qgis.org/project/visual-changelogs/visualchangelog34/ ; design in QEP 126 (Nyall Dawson, 2018-05-24). **V** https://github.com/qgis/QGIS-Enhancement-Proposals/issues/126
- Syntax: the path value starts with `base64:` followed by the base64 of the SVG bytes (no MIME header). Current code: `isBase64Data(path)` = `path.startsWith("base64:") || parseBase64DataUrl(path)`, so a standard `data:<mime>;base64,<data>` URL is recognised as well. **V** https://raw.githubusercontent.com/qgis/QGIS/master/src/core/qgsabstractcontentcache.cpp
- The value goes into `svgFile` for `SVGFill` and into `name` for `SvgMarker` (real example above). Raster fill gained the same URL/embed options in 3.6. **V** changelog 3.6
- Parameters: "You have to add the placeholders `param(fill)` for fill color, `param(fill-opacity)` for fill opacity, `param(outline)` and `param(outline-opacity)` for stroke color and opacity respectively, and `param(outline-width)` for stroke width." Example from the manual (**V** symbol_selector.html):

```xml
<svg width="100%" height="100%">
<rect fill="param(fill) #ff0000" fill-opacity="param(fill-opacity) 1"
stroke="param(outline) #00ff00" stroke-opacity="param(outline-opacity) 1"
stroke-width="param(outline-width) 10" width="100" height="100">
</rect>
</svg>
```

  The text after the placeholder is the default used by other SVG viewers. "More generally, SVG can be freely parametrized using `param(param_name)`. This param can either be used as an attribute value or a node text." `QgsSvgCache::replaceElemParams` handles the five built-ins and then matches custom keys from the layer's `parameters` map (`value.startsWith("param(<key>)")`); it processes both `style="…"` declarations and plain attributes. **V** https://raw.githubusercontent.com/qgis/QGIS/master/src/core/symbology/qgssvgcache.cpp
- Consequence for ULG (**D**): ship one ink-only tile SVG per texture with `param(outline)`/`param(fill)` placeholders and defaults, so a single asset is recolourable in QGIS and still valid in browsers, resvg and GeoServer. QGIS renders SVG with Qt SVG, so keep tiles to basic shapes and paths (see 4.4: no filters).

### 1.7 Units and map-unit-scaled patterns

Manual, "Unit Selector" (**V** https://raw.githubusercontent.com/qgis/QGIS-Documentation/master/docs/user_manual/introduction/general_tools.rst):

- Available: Millimeters, Points, Pixels, Inches, Percentage, Meters at Scale, Map Units.
- "Meters at Scale: This allows you to always set the size in meters, regardless of what the underlying map units are (e.g. they can be in inches, feet, geographic degrees, ...). The size in meters is calculated based on the current project ellipsoid setting and a projection of the distances in meters at the center of the current map extent."
- "Map Units: The size is scaled according to the map view scale. Because this can lead to too big or too small values, use the button next to the entry to constrain the size to a range of values based on: The Minimum scale and the Maximum scale … and/or The Minimum size and the Maximum size in mm".

Implications (**D**):

- `MM` patterns keep constant paper density at every scale. This is the right default for "sparse texture" and for legends.
- `MapUnit` / `RenderMetersInMapUnits` patterns are ground-anchored: marks grow when zooming in. Use for elements whose texture has a real-world module (paving joints, deck planks, herringbone) and clamp with the map-unit scale (`3x:min,max,1,<minMM>,1,<maxMM>`) so the pattern never collapses into noise or explodes.
- `MapUnit` in a geographic CRS means degrees; use `RenderMetersInMapUnits` when the layer CRS is not metric.

SLD export maps units like this: MapUnits → uom `http://www.opengeospatial.org/se/units/metre` with factor 0.001; MetersInMapUnits → same uom, factor 1.0; Millimeters → no uom (pixels), factor `1/0.28`. **V** `encodeSldUom` in qgssymbollayerutils.cpp

### 1.8 Geometry-generator expressions for a hand-drawn outline

Function signatures from the function-help JSON in the QGIS repo (**V** https://raw.githubusercontent.com/qgis/QGIS/master/resources/function_help/json/<name>):

| Function | Arguments and defaults | Since |
|---|---|---|
| `smooth(geometry, iterations=1, offset=0.25, min_length=-1, max_angle=180)` | offset 0–0.5 controls tightness; "By lowering the maximum angle intentionally sharp corners in the geometry can be preserved. For instance, a value of 80 degrees will retain right angles" | 3.0 (**V** changelog 3.0) |
| `simplify(geometry, tolerance)` | Douglas–Peucker | 3.0 (**V**) |
| `simplify_vw(geometry, tolerance)` | Visvalingam–Whyatt | 3.0 (**V**) |
| `offset_curve(geometry, distance, segments, join, miter_limit)` | | 3.0 (**V**) |
| `densify_by_distance(geometry, distance)` | "maximum interval distance between vertices in output geometry"; accepts (multi)linestrings and (multi)polygons | 3.24 (**V** changelog 3.24) |
| `densify_by_count(geometry, vertices)` | | 3.24 (**V**) |
| `wave_randomized(geometry, min_wavelength, max_wavelength, min_amplitude, max_amplitude, seed=0)` | "Constructs randomized curved (sine-like) waves along the boundary of a geometry." "If the seed is 0, then a completely random set of waves will be generated." | 3.24 (**V**) |
| `triangular_wave_randomized(...)`, `square_wave_randomized(...)` | same argument list | 3.24 (**V**) |
| `apply_dash_pattern(...)` | returns a MultiLineString stroked with a dash pattern | 3.24 (**V**) |
| `rand(min, max, seed=NULL)`, `randf(min, max, seed)` | "If a seed is provided, the returned will always be the same, depending on the seed." | seed argument version **R** |

Geometry generators have had selectable units since **3.22**: "Geometry generators now expose an option for users to select which units should be used for returning geometries in… Map units (default), Millimeters, Pixels, Inches, and Points." The changelog says that with non-map units the variable `@map_geometry` holds "the feature geometry in the specified units (relative to the map frame), whilst the $geometry variable remains available within the expression in the layer CRS map units". **V** https://qgis.org/project/visual-changelogs/visualchangelog322/ . The current source instead comments "convert feature geometry to painter units" before evaluating, and the shipped "wavy line" symbol uses `$geometry` with `units=MM`. **V** source / symbology-style.xml. These two statements conflict; which variable carries painter units in 3.44/4.2 must be tested.

Expressions for ULG (**D**, built only from the verified functions):

```text
-- outline wobble, paper units (layer units = MM, SymbolType = Line)
wave_randomized($geometry, 4, 12, 0.05, 0.2, $id + 1)

-- soften digitising corners but keep right angles (map units)
smooth($geometry, 1, 0.12, -1, 80)
```

Notes: never pass seed 0 (flicker on every redraw). `$id + 1` gives per-feature variation. Adjacent polygons get different waves along a shared edge, so keep the fill on the exact geometry and wobble only the line layer, with amplitude below half the stroke width (see Recommendations). Andy Woodruff's tutorial confirms this toolbox (`wave_randomized`, `simplify`/`simplify_vw`, `smooth`, `rand`/`randf` everywhere) and warns that generators "slow down map rendering" and are better baked into geometry when possible. **V** https://andywoodruff.com/posts/2024/qgis-hand-drawn-maps/

### 1.9 Scale-dependent levels of detail

- Rule-based renderer: `scalemindenom` / `scalemaxdenom` per rule (**V**, 1.4). One parent rule per class with three child rules is the cleanest mapping of ULG's three LODs.
- The expression variable `@map_scale` allows data-defined overrides per symbol layer, including enabling or disabling a layer (**R**).
- Layer-level scale visibility: `hasScaleBasedVisibilityFlag`, `minScale`, `maxScale` on the root element (**V** attribute names in the gist).

### 1.10 GPL palettes

- Format (GIMP Palette Format Version 2, **V** https://developer.gimp.org/core/standards/gpl/): first line must be `GIMP Palette`; optional second line `Name: <utf-8 name>`; optional `Columns: <0–255>`; then comment lines starting with `#`, blank lines, or colour lines `r g b [name]` with integers 0–255 in sRGB; line-feed separated; no alpha, 8 bit only.

```text
GIMP Palette
Name: UrbanSens Ecological Vector Style
Columns: 8
#
207 232 195	lawn.fill
143 176 131	lawn.outline
```

  (Layout adapted from the spec; colour values are placeholders.)
- QGIS: Settings ▸ Options ▸ Colors lets users manage palettes and "Import or Export the set of colors from/to `.gpl` file"; custom palettes can be shown in colour-button menus ("Show in Color Buttons"). **V** https://docs.qgis.org/latest/en/docs/user_manual/introduction/qgis_configuration.html . `QgsUserColorScheme`: "A color scheme which stores its colors in a gpl palette file within the 'palettes' subfolder off the user's QGIS settings folder." **V** https://qgis.org/pyqgis/master/core/QgsUserColorScheme.html
- A GPL palette gives QGIS users named swatches; it does not create symbols or colour ramps. For a ramp, add a preset `<colorramp>` to the style XML (1.3).

### 1.11 Pitfalls and open points for the QGIS exporter

- No real `SVGFill` layer in `<Option>` form and no `SimpleMarker` sub-symbol were extracted. Safest implementation (**D**): keep *golden templates* saved by QGIS 3.44 and 4.2 for each layer class and substitute values, or build symbols with PyQGIS when available (`QgsStyle.exportXml`) and keep the pure-Python writer as fallback.
- `RandomMarkerFill` density is per feature and independent of neighbours; two adjacent lawn polygons never share a texture phase. `PointPatternFill` with `coordinate_reference=viewport` is continuous across polygons but shifts when the map is panned in tiles (**R**, behaviour of viewport alignment under tiled rendering not checked).
- Random fills and geometry generators are expensive on large layers (**V** Woodruff for generators; **R** for random fills).

---

## 2. OGC style encodings, GeoServer, INSPIRE, GeoStyler

### 2.1 The standards

| Standard | Document | Status | Mark |
|---|---|---|---|
| Styled Layer Descriptor 1.0.0 | OGC 02-070 | one schema for layer binding and symbolizers, `CssParameter` | V ogc.org/standards/sld |
| SLD 1.1.0 ("SLD profile of WMS") | OGC 05-078r4 | layer/style binding only | V |
| Symbology Encoding 1.1.0 | OGC 05-077r4 | symbolizers in namespace `se`, `SvgParameter`, `uom` | V ogc.org/standards/se |
| Symbology Conceptual Model: Core Part 1.0 ("SymCore") | OGC 18-067r3, approved 2020-08-24, published 2020-10-15 | conceptual model only: "modular and extensible (one core model, many extensions), also encoding agnostic"; defines Style, Rule, Symbolizer, ParameterValue, Literal, UOM, Color, Fill, Stroke, Graphic, GraphicSize, Label, Font; no encoding | V docs.ogc.org/is/18-067r3 |
| OGC Cartographic Symbology – Part 1: Core Model & Encodings (SymCore 2.0) | draft 18-067r4 | working draft in github.com/opengeospatial/cartographic-symbology; encodings CartoSym-CSS and CartoSym-JSON; requirement classes include basic vector styling, labeling and "hatch/stipple fills"; Parts 2–4 planned | V repo README; I found no evidence of approval by 2026-09 |
| OGC API – Styles | 20-009, "1.0.0-draft.2" editor's draft | "This document is not an OGC Standard." Resources `{base}/styles`, `{base}/styles/{styleId}`; encoding classes SLD/SE 1.0 and 1.1 (`application/vnd.ogc.sld+xml`), Mapbox Style (`application/vnd.mapbox.style+json`), CartoSym-JSON (`application/vnd.ogc.cartosym+json`), CartoSym-CSS (`application/vnd.ogc.cartosym+css`) | V docs.ogc.org/DRAFTS/20-009.html |
| ISO 19117:2012 Geographic information – Portrayal | edition 2 | conceptual schema for portrayal; reviewed and confirmed 2023; no new edition or DIS found | S search results on iso.org |

Consequence (**D**): SLD 1.0 and SE 1.1 remain the only widely implemented OGC encodings in 2026. CartoSym-JSON is worth a watch item, not an export target yet.

### 2.2 Polygon fill with a repeated graphic: schema facts (SE 1.1)

From the normative schema (**V** https://schemas.opengis.net/se/1.1.0/Symbolizer.xsd and common.xsd):

- `SymbolizerType` has attributes `version` and **`uom`** (`xsd:anyURI`).
- `PolygonSymbolizer` = `Geometry?`, `Fill?`, `Stroke?`, `Displacement?`, `PerpendicularOffset?`.
- `Fill` = `GraphicFill?` + `SvgParameter*`; "The allowed SvgParameters are: 'fill' (color) and 'fill-opacity'."
- `GraphicFill` = exactly one `Graphic`; "defines repeated-graphic filling (stippling) pattern for an area geometry".
- `Graphic` = (`ExternalGraphic` | `Mark`)*, `Opacity?`, `Size?`, `Rotation?`, `AnchorPoint?`, `Displacement?`.
- `ExternalGraphic` = (`OnlineResource` | **`InlineContent`**), `Format`, `ColorReplacement*`.
- `InlineContent` has a required attribute `encoding` with values `xml` or `base64`: "XML- or base64-encoded encoded content in some externally-defined format that is included in an SE in-line."
- `Mark` = (`WellKnownName` | (`OnlineResource`|`InlineContent`), `Format`, `MarkIndex?`)?, `Fill?`, `Stroke?`.

Standard mark names: `circle`, `square`, `triangle`, `star`, `cross`, `x`. **V** GeoServer PointSymbolizer reference. There is no standard element for spacing between repeated graphics, for randomness, or for hatching; those are vendor territory.

SLD 1.0 differences (**R** except where shown in the GeoServer examples below): no `se:` namespace, `CssParameter` instead of `SvgParameter`, no `uom`, no `InlineContent`.

### 2.3 Real snippets

**SE 1.1, SVG tile as graphic fill** – as written by QGIS for an SVG fill layer (**V** https://raw.githubusercontent.com/qgis/QGIS/master/tests/testdata/symbol_layer/QgsSVGFillSymbolLayer.sld):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:ogc="http://www.opengis.net/ogc" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" version="1.1.0" xmlns:xlink="http://www.w3.org/1999/xlink" xsi:schemaLocation="http://www.opengis.net/sld http://schemas.opengis.net/sld/1.1.0/StyledLayerDescriptor.xsd" xmlns:se="http://www.opengis.net/se">
  <NamedLayer>
    <se:Name>PolygonLayer</se:Name>
    <UserStyle>
      <se:Name>PolygonLayer</se:Name>
      <se:FeatureTypeStyle>
        <se:Rule>
          <se:Name>Single symbol</se:Name>
          <se:PolygonSymbolizer>
            <se:Fill>
              <se:GraphicFill>
                <se:Graphic>
                  <se:ExternalGraphic>
                    <OnlineResource xlink:type="simple" xlink:href="file:accommodation/accommodation_camping.svg"/>
                    <Format>image/svg+xml</Format>
                  </se:ExternalGraphic>
                  <se:Size>6</se:Size>
                  <se:SvgParameter name="stroke">#000000</se:SvgParameter>
                  <se:SvgParameter name="stroke-width">3</se:SvgParameter>
                  <se:Rotation>
                    <ogc:Literal>3</ogc:Literal>
                  </se:Rotation>
                </se:Graphic>
              </se:GraphicFill>
            </se:Fill>
          </se:PolygonSymbolizer>
          <se:LineSymbolizer>
            <se:Stroke>
              <se:SvgParameter name="stroke">#000000</se:SvgParameter>
              <se:SvgParameter name="stroke-width">0.26</se:SvgParameter>
              <se:SvgParameter name="stroke-linejoin">bevel</se:SvgParameter>
              <se:SvgParameter name="stroke-linecap">square</se:SvgParameter>
              <se:SvgParameter name="stroke-dasharray">5 2</se:SvgParameter>
            </se:Stroke>
          </se:LineSymbolizer>
        </se:Rule>
      </se:FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
```

Observations: QGIS emits the outline as a separate `LineSymbolizer`; `OnlineResource` and `Format` are written without the `se:` prefix (default namespace is sld), and `SvgParameter` inside `Graphic` is outside the SE schema. It is a realistic interoperability sample, not a schema-valid model. **D**

**SE 1.1, mark as graphic fill** – QGIS point pattern fill (**V** .../QgsPointPatternFillSymbolLayer.sld), inner part:

```xml
<se:PolygonSymbolizer>
  <se:Fill>
    <se:GraphicFill>
      <se:Graphic>
        <se:Mark>
          <se:WellKnownName>triangle</se:WellKnownName>
          <se:Fill>
            <se:SvgParameter name="fill">#ffaa00</se:SvgParameter>
          </se:Fill>
          <se:Stroke>
            <se:SvgParameter name="stroke">#ff007f</se:SvgParameter>
          </se:Stroke>
        </se:Mark>
        <se:Size>3</se:Size>
        <se:Rotation>
          <ogc:Literal>5</ogc:Literal>
        </se:Rotation>
      </se:Graphic>
    </se:GraphicFill>
  </se:Fill>
  <VendorOption name="distance">15,15</VendorOption>
</se:PolygonSymbolizer>
```

QGIS encodes pattern spacing in its own `VendorOption name="distance"`, which GeoServer does not document (GeoServer uses `graphic-margin`). A QGIS-exported SLD therefore loses spacing in GeoServer; ULG should write the GeoServer options itself. **D** from the two **V** sources.

**SLD 1.0, GeoServer cookbook** (**V** https://docs.geoserver.org/main/en/user/styling/sld/cookbook/polygons/):

```xml
<PolygonSymbolizer>
  <Fill>
    <GraphicFill>
      <Graphic>
        <ExternalGraphic>
          <OnlineResource xlink:type="simple" xlink:href="colorblocks.png" />
          <Format>image/png</Format>
        </ExternalGraphic>
        <Size>93</Size>
      </Graphic>
    </GraphicFill>
  </Fill>
</PolygonSymbolizer>
```

```xml
<PolygonSymbolizer>
  <Fill>
    <GraphicFill>
      <Graphic>
        <Mark>
          <WellKnownName>shape://times</WellKnownName>
          <Stroke>
            <CssParameter name="stroke">#990099</CssParameter>
            <CssParameter name="stroke-width">1</CssParameter>
          </Stroke>
        </Mark>
        <Size>16</Size>
      </Graphic>
    </GraphicFill>
  </Fill>
</PolygonSymbolizer>
```

"Hatching is not part of the standard SLD 1.0 specification". **V**

### 2.4 GeoServer vendor options and extensions

**Random fills** – "Starting with GeoServer 2.4.2 it is possible to generate fills by randomly repeating a symbol in the polygons to be filled"; the fill is a repeated tile whose content is random; "The random distribution is stable, so it will be the same across calls and tiles, and it's controlled by the seed". **V** https://docs.geoserver.org/main/en/user/styling/sld/extensions/randomized/

| VendorOption | Default | Meaning |
|---|---|---|
| `random` | `none` | "Activates random distribution of symbol. Possible values are **none**, **free**, **grid**" |
| `random-tile-size` | `256` | "Size the texture fill tile that will contain the randomly distributed symbols" |
| `random-rotation` | `none` | `none` or `free` |
| `random-symbol-count` | `16` | "The number of symbols in the tile" |
| `random-seed` | `0` | "The 'seed' used to generate the random distribution" |

```xml
<sld:PolygonSymbolizer>
  <sld:Fill>
    <sld:GraphicFill>
      <sld:Graphic>
        <sld:Mark>
          <sld:WellKnownName>shape://slash</sld:WellKnownName>
          <sld:Stroke>
            <sld:CssParameter name="stroke">#0000ff</sld:CssParameter>
            <sld:CssParameter name="stroke-linecap">round</sld:CssParameter>
            <sld:CssParameter name="stroke-width">4</sld:CssParameter>
          </sld:Stroke>
        </sld:Mark>
        <sld:Size>8</sld:Size>
      </sld:Graphic>
    </sld:GraphicFill>
  </sld:Fill>
  <sld:VendorOption name="random-seed">5</sld:VendorOption>
  <sld:VendorOption name="random">grid</sld:VendorOption>
  <sld:VendorOption name="random-tile-size">100</sld:VendorOption>
  <sld:VendorOption name="random-rotation">free</sld:VendorOption>
  <sld:VendorOption name="random-symbol-count">50</sld:VendorOption>
</sld:PolygonSymbolizer>
```

This maps almost one-to-one to ULG's grass ticks: short `shape://slash`/`shape://vertline` marks, `random=free`, `random-rotation=free` or fixed, sparse count. The result is still a repeating tile (period = `random-tile-size`), not per-feature randomness.

**`graphic-margin`** – since GeoServer 2.3.4; pixels of empty space around the fill graphic, CSS-margin syntax with 1–4 values ("top,right,bottom,left" … "single value for all four margins"). Different margins per symbolizer let several stacked symbolizers interleave into a composite fill. **V** https://docs.geoserver.org/main/en/user/styling/sld/extensions/margins/

```xml
<PolygonSymbolizer>
  <Fill>
    <GraphicFill>
      <Graphic>
        <ExternalGraphic>
          <OnlineResource xlink:type="simple" xlink:href="./rockFillSymbol.png"/>
          <Format>image/png</Format>
        </ExternalGraphic>
      </Graphic>
    </GraphicFill>
  </Fill>
  <VendorOption name="graphic-margin">10</VendorOption>
</PolygonSymbolizer>
```

**Extended mark names** (**V** https://docs.geoserver.org/main/en/user/styling/sld/extensions/pointsymbols/): `shape://vertline`, `shape://horline`, `shape://slash`, `shape://backslash` ("suitable for hatch fills"), `shape://plus`, `shape://times` (cross-hatch), `shape://dot`, `shape://oarrow`, `shape://carrow`; families `extshape://`, `ttf://<font>#<hex>`, `wkt://<WKT>`, `windbarbs://`; custom WKT mark sets via a `.properties` file. `wkt://` allows arbitrary small ink shapes (a pebble outline, a wave dash) without any image asset. **D**

**Ground units** (**V** https://docs.geoserver.org/main/en/user/styling/sld/extensions/uom/): `uom` on a symbolizer with `http://www.opengeospatial.org/se/units/metre`, `.../foot`, `.../pixel`; supported since GeoServer 2.1.0. Example from the page:

```xml
<LineSymbolizer uom="http://www.opengeospatial.org/se/units/metre">
  <Stroke>
    <CssParameter name="stroke">#0000FF</CssParameter>
    <CssParameter name="stroke-width">5</CssParameter>
  </Stroke>
</LineSymbolizer>
```

**External graphics**: `OnlineResource xlink:href` takes a URL or a path relative to the styles directory, supports CQL in `${ }`; `Format` values include `image/png`, `image/jpeg`, `image/gif`, `image/svg+xml`. **V** PointSymbolizer reference. `InlineContent` with base64 is reported to work in GeoServer (mailing-list thread "Publish SLD with InlineContent via REST API") – **S**, untested.

Other style languages in GeoServer: CSS, YSLD and MBStyle as extensions. **V** SLD introduction page

### 2.5 INSPIRE view services

Technical Guidance for the implementation of INSPIRE View Services, version 3.3.0 of 2024-01-31 (**V** https://inspire-mif.github.io/technical-guidelines/services/view-wms/ViewServices.html):

- Basis: ISO 19128 (WMS 1.3.0), the SLD profile OGC 05-078r4 and Symbology Encoding OGC 05-077r4.
- Requirement 41: "A Style shall be composed of a Title and a Unique Identifier."
- Requirement 42: "For each harmonised layer according to [INS DS] an <inspire_common:DEFAULT> style shall be as defined in the 'Portrayal' section of the [INS DS], Article 14."
- Requirement 43: layers without a default style use the generic styles "Point: grey square, 6 pixels; Curve: black solid line, 1 pixel; Surface: black solid line, 1 pixel, grey fill."
- Requirement 44: "If no style is specified in the request or the style parameter is empty, the <inspire_common:DEFAULT> style shall be used in layer rendering."
- Requirement 45: "A legend shall be provided for each style and supported language defined in the View Service."
- Recommendation 12: "In addition to the <inspire_common:DEFAULT> style, the View Service should provide additional thematic or national styles for each layer".
- Requirement 57: `image/png` or `image/gif` must be supported.

Data specifications name the layers and default styles, for Land Use: layers `LU.ExistingLandUse`, `LU.SpatialPlan`, `LU.ZoningElement`, …; default styles follow `LU.<FeatureType>.Default` and use the HILUCS colour scheme. **V** https://inspire-mif.github.io/technical-guidelines/data/lu/dataspecification_lu.html

Consequence (**D**): a ULG style can never be the INSPIRE default style of a harmonised layer. It is an *additional* style under Recommendation 12, needs a unique Name, a Title and a legend graphic per language, and should be delivered as SLD/SE so WMS servers can register it next to `inspire_common:DEFAULT`.

### 2.6 GeoStyler and other converters

- GeoStyler parsers: SLD (`geostyler-sld-parser`), OpenLayers, ArcGIS `.lyrx`, Mapbox, MapServer mapfile, QGIS `.qml`; data parsers for GeoJSON, Shapefile, WFS. GeoStyler styles "geodata as a single dataset (layer) not a complete map appearance". **V** https://github.com/geostyler/geostyler
- `geostyler-cli`: `npx geostyler-cli -s sld -t qgis -o output.qml input.sld`; sources SLD, QML, Mapbox, Mapfile, OpenLayers flat styles; targets SLD, QML, Mapbox. **V** https://github.com/geostyler/geostyler-cli
- QML parser coverage (source read through the fetch tool, so **S**): renderers single, categorized, graduated, rule-based; symbol layers `SimpleMarker`, `SvgMarker`, `SimpleLine`, `SimpleFill`, `PointPatternFill` (mapped to `FillSymbolizer.graphicFill`). Not implemented: `LinePatternFill`, `SVGFill`, `RasterFill`, `MarkerLine`, `FontMarker`, `RandomMarkerFill`, `GeometryGenerator`, `ShapeburstFill`, `GradientFill`. Default written version string `3.28.0-Firenze`.
- Mapbox parser: sprites only work if the host application implements a sprite endpoint; source information is stashed under `metadata["mapbox:ref"]`. **V** https://github.com/geostyler/geostyler-mapbox-parser
- `bridge-style` (GeoCat, Python, on PyPI as `bridgestyle` since June 2025): converts via GeoStyler JSON to SLD, MapLibre GL, Mapfile; CLI `style2style input.geostyler output.sld`; converting *from* QGIS needs the QGIS Python API. **V** https://github.com/GeoCat/bridge-style

Consequence (**D**): none of these converters carries random fills, SVG tile fills, geometry generators or seeds. ULG must generate each target format natively from its own catalog. A GeoStyler JSON export is a cheap extra for users of that ecosystem, limited to colour, outline and a simple `graphicFill`.

---

## 3. Web map libraries

### 3.1 MapLibre GL style specification

**Pattern properties** (**V** https://maplibre.org/maplibre-style-spec/layers/):

- `fill-pattern` (type `resolvedImage`): "Name of image in sprite to use for drawing image fills. For seamless patterns, image width and height must be a factor of two (2, 4, 8, ..., 512). Note that zoom-dependent expressions will be evaluated only at integer zoom levels." Data-driven styling since GL JS 0.49.0.
- `line-pattern`: same wording for image width; data-driven since 0.49.0. `line-dasharray` is disabled by `line-pattern`.
- `background-pattern`: data-driven styling "Not supported yet".
- `fill-outline-color` is "Disabled by: fill-pattern" and requires `fill-antialias`; the outline is always 1 px. A real outline needs a separate `line` layer. **V** / **D**
- `fill-extrusion-pattern` exists with the same constraint.

**Expressions** (**V** https://maplibre.org/maplibre-style-spec/expressions/):

- "`["zoom"]` may only appear as the input to a top-level `"step"` or `"interpolate"` expression."
- `interpolate` types: linear, exponential (with base), cubic-bezier; output types number, arrays, color, projection. Images are not interpolated, so pattern switching by zoom uses `step`.
- `image`: "Returns an `image` type for use in `icon-image`, `*-pattern` entries and as a section in the `format` expression."
- There is **no random-number expression** in the specification.

LOD switch for a pattern (**D**, composed from the verified rules):

```json
{
  "id": "ulg-lawn-texture",
  "type": "fill",
  "source": "landcover",
  "filter": ["==", ["get", "ulg_class"], "lawn"],
  "minzoom": 15,
  "paint": {
    "fill-pattern": ["step", ["zoom"], "ulg:lawn-lod1", 17, "ulg:lawn-lod2"]
  }
}
```

**Zoom behaviour of patterns** (**S**, GitHub issues mapbox-gl-js #6296, #1831, #8043, #10033): patterns are tied to the tile grid, scale continuously between integer zooms (up to 200 %) and then snap back while cross-fading; there is no `fill-pattern-size` property. Mapbox issue #8020 reports that `fill-pattern` ignored an image's `pixelRatio` (**S**, state in MapLibre 6 not checked). Textures therefore never have a constant on-screen density in GL maps.

**Sprites** (**V** https://maplibre.org/maplibre-style-spec/sprite/):

- `"sprite": "https://…/sprite"` or an array `[{"id": "roadsigns", "url": "…"}, {"id": "default", "url": "…"}]`.
- The renderer loads `<url>.json` and `<url>.png`; on high-DPI devices `@2x` is appended: `sprite@2x.json`, `sprite@2x.png`.
- Index entry, required: `width`, `height`, `x`, `y`, `pixelRatio`. Optional: `content`, `stretchX`, `stretchY`, `sdf` ("If `true` then the image is handled as a signed-distance field"), `textFitWidth`, `textFitHeight`.

```json
{"poi": {"width": 32, "height": 32, "x": 0, "y": 0, "pixelRatio": 1}}
```

Images from a non-default sprite are referenced as `<id>:<name>` (**R**). Whether SDF images can be used and recoloured in `fill-pattern` is **R/unknown**; assume not and ship coloured RGBA tiles.

**Sprite build tool**: `spreet` (Rust CLI): `spreet [OPTIONS] <INPUT> <OUTPUT>` with `--ratio`, `--retina`, `--unique`, `--recursive`, `--spacing`, `--minify-index-file`, `--sdf`; e.g. `spreet --retina --unique --minify-index-file icons my_style@2x`. **V** https://github.com/flother/spreet . A sprite sheet is simple enough to write directly from Python (PNG atlas + JSON), which avoids a non-Python build dependency. **D**

**Runtime images** (**V** https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/): `addImage(id, image, options?)` accepts `HTMLImageElement`, `ImageBitmap`, `ImageData`, `{width, height, data}` or a `StyleImageInterface`; options `pixelRatio`, `sdf`, `stretchX`, `stretchY`, `content`, `textFitWidth`, `textFitHeight`; also `updateImage`, `hasImage`, `removeImage`, `listImages`, `loadImage`, `addSprite(id, url)`. A JS helper can therefore draw ULG tiles on a canvas from the JSON catalog and register them without any sprite file; the `styleimagemissing` event can create them lazily (**R**).

**Trees as circles with a radius in metres** – `circle-radius` is in pixels, supports data-driven and zoom interpolation; `circle-pitch-scale` (`map`|`viewport`, default `map`) and `circle-pitch-alignment` (`map`|`viewport`, default `viewport`). **V**. The known trick (**S**: StackOverflow 37599561, quoted in several tutorials): `metersToPixelsAtMaxZoom = meters / 0.075 / Math.cos(latitude * Math.PI / 180)` with stops `[[0, 0], [20, px]]` and `base: 2`.

Derivation (**D**): with 512-px tiles the ground resolution is `res(z, φ) = C·cos φ / (512·2^z)`, `C = 40 075 016.686 m`; at z = 20 on the equator that is 0.0746 m/px (the "0.075"). The pixel radius is `r_m / res`, proportional to `2^z`. Exponential interpolation with base 2 between two stops that both lie on `a·2^z` reproduces `a·2^z` exactly, so use two real stops rather than `0 → 0`:

```json
{
  "id": "ulg-tree-crowns",
  "type": "circle",
  "source": "trees",
  "minzoom": 14,
  "paint": {
    "circle-radius": ["interpolate", ["exponential", 2], ["zoom"],
      14, ["*", ["get", "crown_radius_m"], 0.3438],
      22, ["*", ["get", "crown_radius_m"], 88.03]
    ],
    "circle-pitch-alignment": "map",
    "circle-pitch-scale": "map",
    "circle-color": "#b9d8a8",
    "circle-stroke-color": "#5f7f55",
    "circle-stroke-width": 1
  }
}
```

The two factors are px per metre at latitude 52.5° (`512·2^z / (C·cos 52.5°)`: 0.3438 at z 14, 88.03 at z 22; computed, not taken from a source); the exporter must compute them from the data's mean latitude, or write a per-feature factor into the data for layers spanning several degrees. Limits (**R**): very large circles can be clipped at tile borders depending on the source buffer; at high zoom real crown polygons in a `fill` layer are more robust and can carry the wobbly outline.

**What cannot be done in a GL style** (**V** where derived from the spec, else **D**): no per-feature random placement or rotation (no random expression), no pattern offset per feature, no pattern size in metres, no stroke wobble, no clipping modes for marks. Everything irregular must be baked into the tile image or into the geometry.

**Fill colour plus pattern** (**R**): when `fill-pattern` is set the pattern image replaces the fill colour. Use two layers per element: a `fill` with `fill-color` and above it a `fill` with a transparent-background ink tile. One ink tile then serves any base colour.

### 3.2 Leaflet

- Path options include `fillColor`, `fillOpacity`, `fillRule`, `className` ("A custom CSS class name for the path"), `renderer`; map option `preferCanvas` switches paths to the Canvas renderer. **V** https://leafletjs.com/reference.html (1.9.4)
- The SVG renderer writes `path.setAttribute('fill', options.fillColor || options.color)` and adds `options.className` to the `<path>`. **V** https://raw.githubusercontent.com/Leaflet/Leaflet/v1.9.4/src/layer/vector/SVG.js . So `fillColor: 'url(#ulg-lawn)'` or a CSS rule `.ulg-lawn { fill: url(#ulg-lawn); }` works once a `<pattern id="ulg-lawn">` exists in a `<defs>` of the page (**D**; SVG renderer only, not Canvas).
- `Leaflet.pattern` plugin: "Requires Leaflet 0.7.0 or newer"; `L.StripePattern`, `L.Pattern` with `L.PatternPath`, `L.PatternCircle`, `L.PatternRect`; attach with `{ fillPattern: stripes, fillOpacity: 1.0 }`; BSD-2-Clause. **V** https://github.com/teastman/Leaflet.pattern . Maintenance state not checked; Leaflet 2.0 (ESM, no global `L` factories) will likely break it (**R**).
- Assets to export (**D**): `ulg-patterns.svg` (one `<pattern>` per element and LOD, `patternUnits="userSpaceOnUse"`), `ulg.css` (custom properties plus `.ulg-<element>` classes), and a small ES module that injects the defs and returns a `style(feature)` function.

### 3.3 OpenLayers (10.10.0)

- `ol/style/Fill` option `color: Color | ColorLike | PatternDescriptor | null`. `ColorLike` = `string | CanvasPattern | CanvasGradient`. `PatternDescriptor` = `{src, color, size, offset}`: "Pattern image URL", "Color to tint the pattern with", and `size`/`offset` to cut a slice out of a sprite sheet. **V** https://openlayers.org/en/latest/apidoc/module-ol_colorlike.html
- Flat styles: `fill-pattern-src` ("Fill pattern image source URI. If `fill-color` is defined as well, it will be used to tint this image. (Expressions only in Canvas)"), `fill-pattern-size`, `fill-pattern-offset`. **V** https://openlayers.org/en/latest/apidoc/module-ol_style_flat.html
- Assets (**D**): the same PNG atlas as for MapLibre is directly usable through `size`/`offset`, and the tint option allows ink-only white tiles to be coloured per class. A flat-style JSON per LOD is the natural export.

### 3.4 deck.gl

`FillStyleExtension({pattern: true})` adds (**V** https://deck.gl/docs/api-reference/extensions/fill-style-extension): `fillPatternAtlas` (image or URL), `fillPatternMapping` (object or URL; per pattern `{"x", "y", "width", "height"}`), `fillPatternMask` (default `true`: pattern used as transparency mask, coloured by `getFillColor`), `fillPatternEnabled`, `fillPatternSizeUnits` (`'meters'` default, `'common'`, `'pixels'`), `getFillPattern`, `getFillPatternScale` (default 1), `getFillPatternOffset` (default `[0, 0]`), `getFillPatternBackgroundColor`; a `proceduralPattern` constructor option generates patterns in the shader. Works with layers that render fills (GeoJsonLayer, PolygonLayer, ScatterplotLayer).

Assets (**D**): the same atlas PNG plus a mapping JSON in deck.gl's shape (no `pixelRatio`). deck.gl is the only web target where a pattern can be sized in metres and offset or scaled per feature (accessors), so per-feature variation is possible there.

### 3.5 Asset matrix for web targets

| Target | Pattern carrier | Randomness | Units | Export |
|---|---|---|---|---|
| MapLibre GL | sprite PNG + JSON (`@2x`), power-of-two tiles ≤ 512 px | baked into tile only | screen px, rescales with zoom | `style.json` fragment, `sprite.{json,png}`, `sprite@2x.{json,png}` |
| Leaflet (SVG renderer) | inline SVG `<pattern>` | baked into tile | CSS px | `ulg-patterns.svg`, `ulg.css`, helper module |
| OpenLayers | `CanvasPattern` or `PatternDescriptor`/flat style | baked into tile | CSS px | atlas PNG + flat-style JSON |
| deck.gl | atlas + mapping | per-feature offset/scale possible | metres, common or pixels | atlas PNG + mapping JSON |

---

## 4. Hand-drawn vector rendering algorithms

### 4.1 rough.js (4.6.6)

All code facts **V** from https://raw.githubusercontent.com/rough-stuff/rough/master/src/ (`renderer.ts`, `math.ts`, `generator.ts`, `fillers/*.ts`) and https://raw.githubusercontent.com/pshihn/hachure-fill/master/src/hachure.ts.

**Defaults** (`RoughGenerator.defaultOptions`):

```ts
maxRandomnessOffset: 2, roughness: 1, bowing: 1, stroke: '#000', strokeWidth: 1,
curveTightness: 0, curveFitting: 0.95, curveStepCount: 9,
fillStyle: 'hachure', fillWeight: -1, hachureAngle: -41, hachureGap: -1,
dashOffset: -1, dashGap: -1, zigzagOffset: -1, seed: 0,
disableMultiStroke: false, disableMultiStrokeFill: false,
preserveVertices: false, fillShapeRoughnessGain: 0.8,
```

**Seeded RNG** (`math.ts`):

```ts
next(): number {
  if (this.seed) {
    return ((2 ** 31 - 1) & (this.seed = Math.imul(48271, this.seed))) / 2 ** 31;
  } else {
    return Math.random();
  }
}
```

A multiplicative generator with multiplier 48271 in 32-bit wrap-around arithmetic, masked to 31 bits. Seed 0 means unseeded. It is trivially portable: a Python port returned 48271/2³¹ for seed 1, as the formula requires (**T**). The statistical quality is low; good enough for jitter, not for sampling.

**Sketchy line** (`_line`), for a segment of length ℓ:

- `roughnessGain` = 1 if ℓ < 200; 0.4 if ℓ > 500; else `−0.0016668·ℓ + 1.233334`. Long lines get proportionally less jitter.
- `offset = maxRandomnessOffset`; if `offset² · 100 > ℓ²` then `offset = ℓ / 10`. The jitter never exceeds a tenth of the segment length.
- `_offset(min, max) = roughness · roughnessGain · (rand·(max − min) + min)`; `_offsetOpt(x) = _offset(−x, x)`.
- `divergePoint = 0.2 + rand · 0.2`.
- Bowing: `midDispX = bowing · maxRandomnessOffset · (y2 − y1) / 200`, `midDispY = bowing · maxRandomnessOffset · (x1 − x2) / 200`, each then randomised with `_offsetOpt`. The displacement is perpendicular to the segment and proportional to its length.
- Output is one cubic Bézier: start point `(x1, y1) + jitter`; control points at `divergePoint` and `2·divergePoint` along the segment plus `midDisp` plus jitter; end point `(x2, y2) + jitter`.
- `preserveVertices: true` sets the start and end jitter to 0, so vertices stay exactly on the input geometry.
- **Double stroke** (`_doubleLine`): the segment is drawn twice, first with jitter amplitude `offset`, then as "overlay" with `offset/2`. `disableMultiStroke` (or `disableMultiStrokeFill` for fill lines) reduces this to a single pass.

**Curves and ellipses**: `_curveWithOffset` jitters every point by `_offsetOpt(offset)` and fits a Catmull-Rom-like cubic chain with `s = 1 − curveTightness` (control points `p[i] + (s·p[i+1] − s·p[i−1]) / 6`). Ellipses: step count `max(curveStepCount, (curveStepCount/√200) · √(2π·√((rx² + ry²)/2)))`; radii perturbed by `± r·(1 − curveFitting)`; start angle randomised; two passes with an overlap so the loop visibly does not close.

**Hachure fill**: `gap = hachureGap` or `4 · strokeWidth` if negative, rounded to an integer ≥ 0.1; angle = `hachureAngle + 90`; polygons are rotated, scanned with a classic edge-table/active-edge scan-line (`hachure-fill`), and rotated back; with `roughness ≥ 1` there is a 30 % chance of stepping the scan by `gap` instead of 1. Each hachure is drawn with `doubleLineOps`, so fills use the same sketchy line. `fillWeight` defaults to `strokeWidth / 2`. Scan-line x coordinates are rounded to integers (`Math.round(ce.x)`), so the algorithm assumes pixel-scale coordinates.

**Dot fill**: hachure lines at angle 0, then dots every `gap` with jitter `± gap/4`, drawn as ellipses of diameter `fillWeight`. The jitter uses `Math.random()` directly, so **dot fills are not reproducible even with a seed**.

Take-aways for ULG (**D**): keep the length-dependent gain and the ℓ/10 cap; use `preserveVertices` semantics; use a single stroke; do not port the integer rounding or the unseeded dot filler.

### 4.2 Matplotlib sketch and hatch

**Sketch parameters** (**V** https://raw.githubusercontent.com/matplotlib/matplotlib/main/lib/matplotlib/artist.py): `set_sketch_params(scale=None, length=None, randomness=None)` – scale: "The amplitude of the wiggle perpendicular to the source line, in pixels"; length: "The length of the wiggle along the line, in pixels (default 128.0)"; randomness: "The scale factor by which the length is shrunken or expanded (default 16.0)"; "The PGF backend uses this argument as an RNG seed and not as described above." `plt.xkcd(scale=1, length=100, randomness=2)` sets this through rcParams (`path.sketch`), needs the xkcd font or 'Humor Sans'/'Comic Neue', and does not work with `text.usetex`. **V** pyplot.xkcd docs; `path.sketch` exists, default `None` (**T**).

**Algorithm** (**V** https://raw.githubusercontent.com/matplotlib/matplotlib/main/src/path_converters.h, class `Sketch`): the path is segmented, then every vertex is moved perpendicular to the local direction by `r = sin(p · p_scale) · scale`, where `p_scale = 2π / (length · randomness)` and `p` advances per vertex by `exp(d_rand · 2·ln(randomness))`, i.e. by a factor between 1 and randomness². The random source is a linear congruential generator (`a = 214013`, `c = 2531011`) constructed with seed 0 for every path (`m_rand(0)`). Output is deterministic (**T**: two SVG renders identical after stripping ids), and two paths with equal geometry get equal wiggles.

**Backend support**: the SVG backend passes `gc.get_sketch_params()` into `_convert_path` in `draw_path` only; `draw_markers` and `draw_path_collection` do not. The PDF backend passes sketch parameters in `writePath`. **V** backend_svg.py, backend_pdf.py. Measured (**T**, Matplotlib 3.9.2): a `Polygon` patch with sketch parameters grows from 5 to 534 path commands in SVG and changes the Agg raster; the same polygon in a `PatchCollection` with `set_sketch_params` is **unchanged in both SVG and Agg**. GeoPandas plots polygons as collections, so sketch parameters do not reach a GeoDataFrame plot unless every polygon is added as its own patch.

**Why it does not fit ULG** (**D** from the above): amplitude is in device pixels, so it changes with dpi; there is no per-artist seed; fill and stroke wiggle together and independently per polygon, which opens slivers between neighbours; hatches and clip paths are not sketched.

**Hatch limitations**:

- Pattern vocabulary is fixed: `/ \ | - + x o O . *`; density only by repeating characters; "Hatching is supported in the PostScript, PDF, SVG, macosx and Agg backends only." **V** matplotlib.patches.Patch docs
- Patterns are generated in a unit square by `matplotlib.hatch.get_path(hatchpattern, density=6)` and tiled in a fixed **72-unit** cell: `HATCH_SIZE = 72` with `patternUnits="userSpaceOnUse"` in SVG, `sidelen = 72.0` with `XStep`/`YStep` in PDF. **V** backend sources; **T**: the emitted element is `<pattern … patternUnits="userSpaceOnUse" x="0" y="0" width="72" height="72">`. Hatch size is therefore tied to the page (points), not to data or map scale, and the phase is anchored to the page, not to the feature.
- One colour and one line width per artist: `hatch.linewidth` rcParam (default 1.0, **T**), `set_hatch_linewidth`, `set_hatchcolor` exist in the 3.11 docs; a `hatchcolor` parameter for patches and collections is described for 3.11 (if not given, the hatch follows the edge colour). **V** docs / **S** what's-new summary
- No API for custom hatch shapes (only the private hatch-type registry, **R**), no random placement, no clipping mode.

Conclusion (**D**): ULG should compute texture marks as geometry (Shapely) and draw them with `LineCollection`/`PathCollection`; the SVG writer and the Matplotlib renderer then consume the same coordinates and give the same picture.

**Reproducible Matplotlib SVG** (**R** except where noted): set `svg.hashsalt` (exists, default `None`, **T**) and `metadata={"Date": None}`, otherwise ids and the date differ between runs.

### 4.3 Poisson-disk sampling

- Bridson, R. (2007). "Fast Poisson Disk Sampling in Arbitrary Dimensions." SIGGRAPH sketches. Algorithm (**R**): background grid with cell size r/√n holding at most one sample; an active list; for a random active sample generate up to k (typically 30) candidates uniformly in the annulus [r, 2r]; accept a candidate if no sample lies within r (check neighbouring cells); drop the active sample when all k fail; O(N).
- `scipy.stats.qmc.PoissonDisk`: added in **SciPy 1.9.0** ("It guarantees that samples are separated from each other by a given `radius`"). **V** release notes. Signature in the 1.18.0 docs (**V**):

```python
class scipy.stats.qmc.PoissonDisk(d, *, radius=0.05, hypersphere='volume',
                                  ncandidates=30, optimization=None, rng=None,
                                  l_bounds=None, u_bounds=None, seed=None)
```

  `hypersphere='volume'` is the original Bridson annulus sampling, `'surface'` samples only on the sphere surface; `optimization` (`None`, `'random-cd'`, `'lloyd'`) since 1.10.0; `rng` replaces `seed` since 1.15.0 (SPEC 7); methods `random(n)` ("it can return fewer samples if the space is full") and `fill_space()` ("will try to add points until the space is full"). Docs warn that the algorithm suits low dimensions and moderate sample sizes.
- Measured (**T**, SciPy 1.13.1): the constructor there has **no `l_bounds`/`u_bounds`** (they arrived in a later release), so the domain is the unit square and must be scaled by the caller; `fill_space()` with r = 0.05 gives 247 points for `'volume'` (N·r² ≈ 0.62) and 347 for `'surface'` (N·r² ≈ 0.87); results are deterministic for a fixed seed.
- Missing for ULG: no periodic (toroidal) domain, no anisotropic spacing, no polygon domain. A pure-Python toroidal Bridson is about 40 lines; a 64 × 64 mm tile with r = 6 mm took 10 ms and produced 74 marks (N·r²/area = 0.65) with toroidal minimum distance 6.006 mm (**T**).
- Polygon domain (**V** functions, **D** recipe): sample the bounding box or repeat a tile, then filter with `shapely.contains_xy(geom, x, y)` after `shapely.prepare(geom)`; docs recommend preparing when testing many points. Use `geom.buffer(-inset)` as the test geometry so whole marks stay inside.

### 4.4 Seamless, non-repeating stipple: blue noise and Wang tiles

- Cohen, M. F., Shade, J., Hiller, S., Deussen, O. (2003). "Wang Tiles for Image and Texture Generation." ACM TOG 22(3), 287–294: a small set of square tiles with colour-coded edges tiles the plane non-periodically; tiles can carry textures or point sets. **S** (ACM/Konstanz listings in search results)
- Kopf, J., Cohen-Or, D., Deussen, O., Lischinski, D. (2006). "Recursive Wang Tiles for Real-Time Blue Noise." ACM TOG 25(3), 509–518: progressive, recursive blue-noise Wang tiles give unbounded non-periodic point sets at varying density and zoom. **S**
- Applicability (**D**): Wang tiling needs a renderer that chooses a tile per cell. QGIS `SVGFill`, SLD `GraphicFill`, MapLibre `fill-pattern`, Leaflet `<pattern>` and deck.gl all repeat **one** tile. Wang tiles are therefore usable only inside ULG's own renderer, where direct per-polygon sampling is simpler. For exported tiles the practical levers are: a toroidal blue-noise tile (no seams), a large period (64–128 mm on paper, 256–512 px on screen), sparse and irregular marks (repetition is far less visible than with dense patterns), and where available true randomness (QGIS `RandomMarkerFill`, `PointPatternFill` random deviation, GeoServer `random`).
- Toroidal tile rule (**D**): measure distances with wrap-around, `d² = min(|dx|, W−|dx|)² + min(|dy|, H−|dy|)²`, and draw every mark that crosses a tile edge a second time shifted by ±W or ±H.

### 4.5 SVG filters `feTurbulence` + `feDisplacementMap`

- `feDisplacementMap` moves pixels of `in` by the channel values of `in2`: `P'(x,y) ← P(x + scale·(XC(x,y) − 0.5), y + scale·(YC(x,y) − 0.5))`; attributes `in`, `in2`, `scale`, `xChannelSelector`, `yChannelSelector`; "Widely available" across browsers since July 2015. MDN example (**V** https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap):

```html
<filter id="displacementFilter">
  <feTurbulence type="turbulence" baseFrequency="0.05" numOctaves="2" result="turbulence" />
  <feDisplacementMap in2="turbulence" in="SourceGraphic" scale="50"
                     xChannelSelector="R" yChannelSelector="G" />
</filter>
```

- Qt SVG (used by QGIS for SVG markers and fills): extended features beyond SVG Tiny 1.2 since Qt 6.7 are `mask`, `symbol`, `marker`, `pattern`, `filter` with `feColorMatrix`, `feComposite`, `feFlood`, `feGaussianBlur`, `feOffset`, `feMerge`; **feTurbulence and feDisplacementMap are not listed**; extended features can be switched off with `QtSvg::Tiny12FeaturesOnly`. **V** https://doc.qt.io/qt-6/svgextensions.html . Under Qt5 (QGIS 3.x) none of these exist (**R**).
- CairoSVG: "3 filter effects are supported: feBlend, feFlood, feOffset"; "Patterns are poorly handled. Naive patterns are rendered, but simple features such as the viewBox property are ignored." **V** https://cairosvg.org/svg_support/
- resvg: the list of unsupported SVG 1.1 features contains only SVG fonts, `color-profile`, external `use` and a few text/colour attributes; filters are not on it. **V** https://raw.githubusercontent.com/linebender/resvg/main/docs/unsupported.md
- PDF has no filter primitive, so renderers rasterise filtered groups (**R**).
- Assessment (**D**): displacement filters operate on the rasterised source at device resolution. Edges become soft and resolution-dependent, the fill boundary itself moves, output differs between renderers, and the filter is dropped or rasterised in QGIS, CairoSVG and PDF. That contradicts "clean, polygon-accurate, GIS-compatible". Use geometric wobble. A paper-grain filter can be an opt-in flourish for browser-only output, never part of exported assets. Also: do not rely on `<pattern>` for the core SVG output if CairoSVG is a supported rasteriser; write explicit mark geometry or rasterise with resvg.

### 4.6 Pen-plotter tooling

- `vpype` 1.15.0 ("The Swiss Army knife of vector graphics for pen plotters"; Python ≥ 3.11, < 3.14; depends on Shapely, svgelements, svgwrite, scipy): commands `linemerge`, `linesort`, `linesimplify`, `reloop` ("Randomize the seam location of closed paths"), `multipass`, `splitall`, `filter`, `crop`, `trim`, `layout`, `scale`, `scaleto`, `read`, `write` (SVG, HPGL). **V** PyPI JSON, https://vpype.readthedocs.io/en/latest/reference.html
- `vsketch` 1.2.0 (Python ≥ 3.11, < 3.14; depends on vpype, PySide6, Shapely): layers instead of colours, `vsk.stroke()`/`vsk.fill()` per layer, vectorised Perlin `noise()` up to 3-D, `randomSeed()`, `detail()` for maximum segment length, `geometry()` accepts Shapely objects. **V** PyPI JSON, vsketch docs. Fill is emulated by hatching at pen width (**R**).
- Techniques worth borrowing (**D**): hatch = intersection of a parallel line family with the polygon (`shapely.intersection(polygon, MultiLineString(...))`); stipple = Poisson-disk points; seam randomisation for closed outlines; everything is geometry, so it is resolution-independent and exportable to GeoPackage. Their Python upper bound (< 3.14) and heavy dependencies make them unsuitable as ULG dependencies.

### 4.7 Packages

| Package | State | Use for ULG |
|---|---|---|
| `rough` (cktlco/rough-py) 1.6 | MIT, Python ≥ 3.10, no dependencies; port of Rough.js; shapes line, rectangle, circle, polygon, arc, path; fill patterns hachure, solid, zigzag, cross-hatch, dots, dashed; SVG output. First release 2025-02. **V** PyPI, README | reference implementation to read; not a dependency (canvas-oriented, pixel units) |
| `prettymaps` 1.4.2 | MIT, Python ≥ 3.11; style dict per layer with `fc`, `ec`, `lw`, `alpha`, `zorder`, `palette`, `hatch`, `hatch_c`; presets as JSON; depends on matplotlib, shapely ≥ 2, osmnx < 2, vsketch ≥ 1.0. **V** PyPI, README | prior art for a data-first style dict; textures are Matplotlib hatches |
| `drawsvg` 2.4.2 | MIT; raster output through CairoSVG (extra). **V** PyPI | optional; a minimal own SVG writer avoids the dependency |
| `svgwrite` 1.4.3 | inactive: "No new features will be added, there will be no change of behavior, just bugfixes will be merged"; last release 2022-07. **V** PyPI | avoid |
| `CairoSVG` 2.9.1 | LGPL-3.0-or-later, Python ≥ 3.10. **V** PyPI | weak patterns and filters (4.5); acceptable only for explicit geometry |
| `resvg_py` 0.5.0 | Python ≥ 3.10; `svg_to_bytes(...)` re-exposes resvg. **V** PyPI | preferred rasteriser for sprites and tests |
| Shapely 2.1.2 | `segmentize(geometry, max_segment_length)`; `buffer(geometry, distance, quad_segs=8, cap_style='round', join_style='round', mitre_limit=5.0, single_sided=False)` with `cap_style` round/square/flat and `join_style` round/mitre/bevel (keyword-only in future); `contains_xy(geom, x, y)`; `prepare`. **V** shapely docs | core geometry engine |

### 4.8 Prior art: hand-drawn styles in QGIS and ArcGIS

- **QGIS default style**: "wavy line" symbol with a `wave_randomized` geometry generator in millimetres (1.5). **V**
- **Andy Woodruff, "Hand-Drawn and Antique Styles with QGIS" (2024)**: `wave_randomized` for wobble "both inside and outside the polygon"; `simplify`/`smooth` to generalise; `rand()`/`randf()` in data-defined sizes, rotations and colours; sketchy fills from point pattern fills with randomised line markers; "painty" fills by blurring marker fills with draw effects; deliberate misalignment of fill and outline by giving them different generators; paper texture from low-opacity random marker fills with multiply/screen blending; warns about render cost. **V** https://andywoodruff.com/posts/2024/qgis-hand-drawn-maps/
- **Klas Karlsson's QGIS resource collection**: style XML files such as `crayon_fill.xml` (MarkerLine plus `RandomMarkerFill` with embedded base64 SVG crayon strokes; colours picked with `array_get(array(...), rand(0,5))`, `rand(0,360)` rotation), `crayon_polygon_outside.xml`, `RoughDrops.xml`, `edge_bleed.xml`, and a geometry-generator recipe for random points in polygons built from `generate_series`, `randf` and `intersects`. **V** https://github.com/Klakar/QGIS_resources/tree/master/collections/Geosupportsystem/symbol
- **John Nelson (Esri)**: ArcGIS Pro watercolour style (picture fills from photographed paper and watercolour textures) and a "squiggly pencil sketch hack": wave effect on lines, high transparency, several stacked duplicated symbol layers. **S** (Esri blog pages returned 403; content from search summaries)
- Pattern across all of them (**D**): raster textures and blend modes give the painterly look; stacked, randomised vector strokes give the sketch look. ULG's brief (clean, vector, polygon-accurate) sits between: one stroke, small amplitude, sparse vector marks, no blur, no raster paper.

### 4.9 Prototype check of the proposed pipeline

A throw-away prototype (**T**, `scratchpad/s07_tests/t3_proto.py`, `t4_render.py`, output `proto.png`/`proto.svg`) implemented: exact pastel fill; a toroidal Poisson-disk tile repeated over the polygon and filtered with `contains_xy` against an inward buffer; grass tufts and pebble outlines as vector marks; an outline displaced along the normal by three seeded sine components with amplitude 0.15 mm, tapered to zero at the original vertices. Results: Hausdorff distance between wobbled and true ring 0.149 mm; every original vertex lies on the wobbled ring; polygon stays valid; tile generation 10 ms. Visual finding: where two polygons share an edge, two differently seeded outlines in two colours are drawn on top of each other and read as a doubled line. Shared edges need one seed and one colour rule (see Recommendations).

---

## 5. Design tokens

### 5.1 DTCG format (Design Tokens Community Group)

- Status: **Design Tokens Format Module 2025.10 – "Final Community Group Report 28 October 2025"**; "This specification is considered stable. Further updates will be provided in superseding specifications." It "is not a W3C Standard nor is it on the W3C Standards Track". Announced 2025-10-28 as "the first stable version of the Design Tokens Specification", with a Color Module and a Resolver Module of the same version. **V** https://www.designtokens.org/tr/2025.10/format/ , https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/ . An editor's draft dated 2026-09-08 exists under `/tr/drafts/` and is marked as a preview, not for implementation. **V**
- Files: recommended extensions `.tokens` and `.tokens.json`; media type `application/design-tokens+json` (tools must also accept `application/json`). **V**
- Token: object with `$value`; `$type` on the token or inherited from a parent group; optional `$description`, `$extensions` (vendor data under reverse-domain keys), `$deprecated` (boolean or string). Groups may carry `$type`, `$description`, `$extends` (deep-merge inheritance, equivalent to a `$ref`), and a `$root` token. **V**
- Names must not start with `$` and must not contain `{`, `}` or `.`. **V**
- Types: `color`, `dimension` (`{"value": n, "unit": "px"|"rem"}`), `fontFamily`, `fontWeight`, `duration` (`ms`|`s`), `cubicBezier`, `number`; composites `strokeStyle` (keyword or `{dashArray, lineCap}`), `border`, `transition`, `shadow`, `gradient`, `typography`. **V**
- Aliases: `"{group.token}"` resolves to the target token's `$value`; JSON Pointer form `"$ref": "#/colors/blue/$value"` can address parts of a value. Circular references are errors. **V**

```json
{
  "colors": {
    "blue": {
      "$value": { "colorSpace": "srgb", "components": [0, 0.4, 0.8], "hex": "#0066cc" },
      "$type": "color"
    }
  },
  "semantic": {
    "primary": { "$value": "{colors.blue}", "$type": "color" }
  }
}
```

  (verbatim from the Format Module, **V**)
- Colour value (Color Module 2025.10, **V** https://www.designtokens.org/tr/drafts/color/): object with `colorSpace` (required), `components` (required array; numbers or the keyword `none`), `alpha` (optional, 0–1, default 1), `hex` (optional 6-digit fallback). Colour spaces: `srgb`, `srgb-linear`, `hsl`, `hwb`, `lab`, `lch`, `oklab`, `oklch`, `display-p3`, `a98-rgb`, `prophoto-rgb`, `rec2020`, `xyz-d65`, `xyz-d50`. sRGB components are 0–1.
- Resolver Module 2025.10: `.resolver.json` documents with `sets`, `modifiers` (named `contexts`, e.g. light/dark) and `resolutionOrder`. **V** https://www.designtokens.org/tr/2025.10/resolver/

Implications for ULG (**D**):

- `dimension` only knows `px` and `rem`. Millimetre and metre values (stroke widths in mm, pattern module in m) have to be `number` tokens with the unit in the name or in `$extensions`, or be duplicated as px for CSS.
- There is no token type for patterns. Texture parameters belong in `$extensions["org.urbansens.ulg"]` or, better, stay in the ULG catalog JSON, with tokens carrying only colours, stroke widths and opacities.
- The Resolver fits theme variants: `default`, `high-contrast`, `cvd-safe`, `print-greyscale`.

### 5.2 Style Dictionary

- Current major version **5** (5.5.5; ESM; Node ≥ 22.0.0). **V** registry.npmjs.org
- "first-class support for the DTCG format" since version 4; "the latest format 2025.10 does not have full support yet in Style Dictionary", work ongoing in v5; a `convertToDTCG` utility renames `value/type/description` to `$`-prefixed keys. **V** https://styledictionary.com/info/dtcg/
- Predefined formats include `css/variables` (options `showFileHeader`, `outputReferences`, `selector`), `scss/*`, `less/*`, `javascript/es6`, `javascript/esm`, `typescript/es6-declarations`, `json`, `json/nested`, `json/flat`, Android, iOS, Compose, Flutter. **There is no predefined Python format.** **V** https://styledictionary.com/reference/hooks/formats/predefined/
- References use `{path.to.token}`; the category/type/item naming is optional; token metadata `name`, `path`, `original`, `filePath`, `isSource`; `include` for overridable base files, `source` for primary files. **V** https://styledictionary.com/info/tokens/

Structure that yields CSS, JSON and Python from one source (**D**):

```text
tokens/
  primitive.tokens.json     color.green.200 … (raw pastel ramp, OKLCH + hex fallback)
  semantic.tokens.json      element.lawn.fill = {color.green.200}, element.lawn.outline = {color.green.600},
                            element.lawn.ink = {color.green.500}, map.paper = {color.neutral.50}
  themes/*.tokens.json      overrides per theme (high-contrast, cvd-safe)
  ulg.resolver.json         sets + theme modifier
```

- Primitive tokens hold values; semantic tokens hold only aliases; exports expose semantic tokens and keep primitives as an implementation layer (`outputReferences` keeps `var(--ulg-color-green-200)` indirection in CSS).
- Python constants cannot come from Style Dictionary without a custom format and a Node toolchain. Since ULG is a Python library, make the **Python catalog the source of truth** and generate `*.tokens.json`, `ulg.css`, `tokens.json` and `ulg/_tokens.py` with a small Python exporter. The DTCG files then let design tools and Style Dictionary users consume the palette; Style Dictionary stays optional. Validate the generated files in CI by running Style Dictionary once against them.
- CSS naming: `--ulg-<element>-<role>` (`--ulg-lawn-fill`), plus `--ulg-color-<hue>-<step>` for primitives.

---

## 6. Accessibility and legibility of map colours

### 6.1 Normative texts

**WCAG 2.2** (W3C Recommendation; ISO/IEC 40500:2025):

- SC 1.4.1 Use of Color (Level A): "Color is not used as the only visual means of conveying information, indicating an action, prompting a response, or distinguishing a visual element." **V** https://www.w3.org/TR/WCAG22/ . Sufficient techniques include **G111 "Using color and pattern"** and G14 (information also available in text). The Understanding document adds that a lightness difference of 3:1 or more between colours can itself serve as the non-colour distinction. **V** https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html
- SC 1.4.11 Non-text Contrast (Level AA): "The visual presentation of the following have a contrast ratio of at least 3:1 against adjacent color(s): User Interface Components …; Graphical Objects: Parts of graphics required to understand the content, except when a particular presentation of graphics is essential to the information being conveyed." **V**. Understanding notes (**V** https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html): "not every graphical object needs to contrast with its surroundings, only those that are required for a user to understand what the graphic is conveying"; a graphic is exempt when the same information is available in another form; the pie-chart example passes by adding a darker border between slices; essential exceptions are logos, flags, real-life imagery and representations such as screenshots, medical diagrams and heat maps. Techniques G207 (3:1 for icons) and G209 ("Provide sufficient contrast at the boundaries between adjoining colors").
- SC 1.4.3 Contrast (Minimum): 4.5:1 for text, 3:1 for large text. Relevant for labels on pastel fills. **V**
- Contrast ratio `(L1 + 0.05) / (L2 + 0.05)`; relative luminance `L = 0.2126·R + 0.7152·G + 0.0722·B` with `c ≤ 0.04045 ? c/12.92 : ((c + 0.055)/1.055)^2.4` (0.03928 in texts before May 2021). **V** https://www.w3.org/WAI/WCAG22/Techniques/general/G18

**EN 301 549**: V4.1.1 was published in September 2026 and "adopts WCAG 2.2 as the accessibility benchmark for websites, software and digital documents, replacing WCAG 2.1". "Until the European Commission formally cites EN 301 549 v4.1.1 in the Official Journal of the European Union, the current reference remains EN 301 549 v3.2.1 (2021), which is based on WCAG 2.1 Level AA." Once cited, conformance gives presumption of conformity with both the European Accessibility Act and the Web Accessibility Directive. **V** https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en

**BITV 2.0** (German federal public bodies; last amended by the ordinance of 24 October 2023, BGBl. 2023 I Nr. 286): § 3(1) "Die in § 2 genannten Angebote, Anwendungen und Dienste der Informationstechnik sind barrierefrei zu gestalten." § 3(2): "Die Erfüllung der Anforderungen nach Absatz 1 wird vermutet, wenn diese Angebote, Anwendungen und Dienste harmonisierten Normen oder Teilen dieser Normen entsprechen, und die harmonisierten Normen oder Teile dieser Normen im Amtsblatt der Europäischen Union genannt worden sind." **V** https://www.gesetze-im-internet.de/bitv_2_0/BJNR184300011.html . The harmonised standard cited in the OJEU is EN 301 549 V3.2.1 (**S**). The extraction of the BITV text found exemptions for cultural-heritage collections, archives and broadcasters but **no exemption for online maps** (**S**: reading by the fetch tool; check § 2 before relying on it). Länder have their own ordinances (**R**).

**Web Accessibility Directive** (EU) 2016/2102, public-sector websites and apps: Article 1(4)(d) excludes "online maps and mapping services, as long as essential information is provided in an accessible digital manner for maps intended for navigational use". **V** https://www.legislation.gov.uk/eudr/2016/2102/article/1

**European Accessibility Act** (Directive (EU) 2019/882), private-sector products and services: Article 31(2) "They shall apply those measures from 28 June 2025." Article 2(4) excludes, among other content, "online maps and mapping services, if essential information is provided in an accessible digital manner for maps intended for navigational use". **V** https://www.legislation.gov.uk/eudr/2019/882/article/31 and /article/2 . German transposition: Barrierefreiheitsstärkungsgesetz (BFSG), in force 28 June 2025 (**S**).

Reading (**D**, not legal advice): the EU exemptions concern the map service itself and presuppose an accessible alternative for essential information; legends, controls, labels and the surrounding page stay in scope, and the German federal ordinance appears not to repeat the exemption. A style library for public-sector apps should therefore be able to meet WCAG 1.4.1 and 1.4.11 on its own and should ship an accessible legend/table representation of every class.

**DIN 32975:2009-12** "Gestaltung visueller Informationen im öffentlichen Raum zur barrierefreien Nutzung": luminance contrast by the Michelson formula `K = (L1 − L2)/(L1 + L2)`; K ≥ 0.7 for text, symbols and warnings, K ≥ 0.4 for other information carriers such as guidance elements, K ≥ 0.8 recommended for black on white; "Colour can only act in a supporting role, but can never compensate for low luminance contrast." Scope is signage, timetables, displays and controls in public space. **S** https://nullbarriere.de/din32975.htm . Relevance (**D**): applies when ULG maps are printed as site plans, information boards or kiosk displays, not to web apps. Conversion: WCAG 3:1 on bright colours corresponds to roughly K ≈ 0.5.

### 6.2 What this means for pastel area fills

Computed with the WCAG formula (**T**, `scratchpad/s07_tests/t5_color.py`; colours are my placeholders, not the UrbanSens palette):

- Six sample pastel fills (L* about 88–92) have pairwise WCAG contrast between **1.01:1 and 1.11:1**, and about 1.3:1 against white paper. Pastel fills can never reach 3:1 against each other.
- For a fill with relative luminance `Lf`, an outline reaches 3:1 only if its luminance is `≤ (Lf + 0.05)/3 − 0.05`: 0.233 for Lf = 0.8, 0.200 for 0.7. Example: fill `#CFE8C3` (L = 0.749) against outline `#6F8F6A` gives 2.75:1 (fails), `#5F7F55` gives 3.43:1, `#4F6B47` gives 4.53:1. A "slightly darker" outline is usually not enough; it must be clearly mid-dark.

Interpretation (**D**, consistent with G111 and G209 but not an official ruling):

1. Class identity must not rest on fill colour alone. The ULG texture is the second visual channel (G111), the legend and labels the third (G14).
2. Boundaries between classes are "parts of graphics required to understand the content". Give every polygon an outline with ≥ 3:1 against **both** adjoining fills (G209), or offer a high-contrast theme that does.
3. Texture ink should reach 3:1 against its own fill when the texture is the only non-colour cue; otherwise it is decoration.
4. Labels need 4.5:1 against the fill (3:1 for large text), which pastel fills make easy with dark text.

### 6.3 Colour difference between classes

- Brychtová, A., & Çöltekin, A. (2016). The effect of spatial distance on the discriminability of colors in maps. *Cartography and Geographic Information Science*. https://doi.org/10.1080/15230406.2016.1140074 (published online 15 Feb 2016). **V** (author PDF read this session; print issue 44(3), 229–245, 2017 is **R**). Design: web survey with 211 volunteers plus an eye-tracking study with 32; colour distances ΔE00 = 2, 4, 6, 8, 10 (and 0); spatial distance small, medium, large; sequential schemes (six greens varying only in L) and qualitative schemes (six hues at roughly constant, very high lightness, L ≈ 94–99). Findings from the abstract: "increasing the gap between colors has a consistent negative impact on the ability to differentiate them"; "sequential schemes require larger color distances than qualitative schemes"; "for qualitative colors, the largest tested color distance ΔE00 = 10 yields considerably higher levels of accuracy in color discrimination (even when the spatial gap between the two colors is large), thus we recommend ΔE00 = 10". Note that the tested qualitative colours were pale pastels, close to the ULG use case.
- Earlier study: Brychtová, A., & Çöltekin, A. (2015). Discriminating classes of sequential and qualitative colour schemes. *International Journal of Cartography*, 1(1), 62–78. https://doi.org/10.1080/23729333.2015.1055643 . **S** (publisher listing; not read)
- CIEDE2000 is the metric in both (formulas: Sharma, Wu & Dalal 2005, cited in the paper). A 60-line pure-Python implementation reproduced the published test pair value 2.0425 (**T**).
- Sample run on six placeholder pastels (**T**): normal-vision ΔE00 between 5.9 and 24.3; under simulated protanopia lawn–sand drops from 12.8 to 1.8 and meadow–sand from 10.0 to 3.4; under tritanopia lawn–water drops from 19.6 to 4.0. A pastel land-cover palette will fail a ΔE00 ≥ 10 rule for several pairs under CVD, which is exactly where texture has to carry the distinction.

### 6.4 Colour-vision-deficiency simulation

| Method | Citation | Use | Mark |
|---|---|---|---|
| Brettel 1997 | Brettel, H., Viénot, F., & Mollon, J. D. (1997). Computerized simulation of color appearance for dichromats. *JOSA A*, 14(10), 2647–2655 | dichromacy, two half-planes in LMS; "the only solid choice" for tritanopia | V daltonlens.org review |
| Viénot 1999 | Viénot, F., Brettel, H., & Mollon, J. D. (1999). Digital video colourmaps for checking the legibility of displays by dichromats. *Color Research & Application*, 24(4), 243–252 | one 3×3 matrix for protanopia/deuteranopia; "behaves a bit better with extreme values" | V |
| Machado 2009 | Machado, G. M., Oliveira, M. M., & Fernandes, L. A. F. (2009). A physiologically-based model for simulation of color vision deficiency. *IEEE TVCG*, 15(6), 1291–1298. doi:10.1109/TVCG.2009.113 | severity 0.0–1.0 in steps of 0.1 (cone sensitivity shift up to about 20 nm), 3×3 matrices applied in **linear RGB**; principled model for anomalous trichromacy | V author page |

Severity 1.0 matrices (**V** https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html):

```text
protan:  0.152286  1.052583 -0.204868 |  0.114503 0.786281 0.099216 | -0.003882 -0.048116 1.051998
deutan:  0.367322  0.860646 -0.227968 |  0.280085 0.672501 0.047413 | -0.011820  0.042940 0.968881
tritan:  1.255528 -0.076749 -0.178779 | -0.078411 0.930809 0.147602 |  0.004733  0.691367 0.303900
```

Review advice: "For protanopia and deuteranopia Viénot 1999, Brettel 1997 and Machado 2009 are solid choices"; "Coblis V1 (ColorMatrix) should never be used"; sRGB must be linearised first. **V** https://daltonlens.org/opensource-cvd-simulation/

Python libraries:

- `colorspacious` 1.1.2 (MIT; last upload 2018): CVD space `{"name": "sRGB1+CVD", "cvd_type": "deuteranomaly"|"protanomaly"|"tritanomaly", "severity": 0–100}` using Machado 2009; `deltaE(color1, color2, input_space="sRGB1", uniform_space="CAM02-UCS")`; "has no ability to perform ΔE calculations like CIEDE2000". **V** docs, PyPI
- `colour-science` 0.4.7 (BSD-3-Clause; Python ≥ 3.11, < 3.15): `colour.blindness.matrix_cvd_Machado2009(deficiency, severity)`, `matrix_anomalous_trichromacy_Machado2009`, dataset `CVD_MATRICES_MACHADO2010`; `colour.delta_E(a, b, method='CIE 2000')` on CIE L\*a\*b\* arrays (also CIE 1976/1994, CMC, DIN99, ITP, CAM02-UCS, CAM16-LCD, HyAB). **V** docs, PyPI
- `daltonlens` 0.1.5 (MIT; Python ≥ 3.7; last upload 2021): `simulate.Simulator_Vienot1999()`, `Simulator_Brettel1997()`, `Simulator_Machado2009()`; `simulator.simulate_cvd(im, simulate.Deficiency.PROTAN, severity=0.8)`. **V** PyPI

Two of the three are unmaintained and the third is heavy. The needed maths (WCAG contrast, sRGB↔Lab, CIEDE2000, three Machado matrices, optionally Viénot/Brettel) is about 150 lines without dependencies (**T** for the first four). Keep `colour-science` as an optional cross-check in the test suite (**D**).

### 6.5 Published guidance on accessible maps and pattern fills

- **UK Government Analysis Function, "Data visualisation: colours"** (last updated 12 February 2026): restates the 3:1 rule for graphical parts against adjacent colours; categorical palette `#12436D`, `#28A197`, `#801650`, `#F46A25`, `#3D3D3D`, `#A285D1`; recommends at most four categories; sequential blues for maps `#092135`, `#12436D`, `#2073BC`, `#6BACE6`, `#ADD1F1` with `#F2F2F2` for no data; advises against hatching or textures to tell *lines* apart because they "may be misinterpreted as they are often used for projections"; for maps, provide the data table and state key messages in text. **V** https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/
- **W3C**: no normative map guidance beyond WCAG. The WAI R&D "Accessible Maps" wiki (last modified 2012) is a research collection about tactile and audio maps and says nothing on colour or pattern. **V** https://www.w3.org/WAI/RD/wiki/Accessible_Maps
- Other material found but not read in depth (**S**): Minnesota IT "Accessibility Guide for Interactive Web Maps" (Oct 2024); Ordnance Survey's colour-blind-friendly Zoomstack styles (RGS article); a 2025 systematic WCAG evaluation of map tools (PMC12094671). I found no German federal guidance specific to pattern fills in maps.

---

## 7. Agent-facing packaging conventions (2026)

### 7.1 What coding agents read

**AGENTS.md** (**V** https://agents.md/): "Think of AGENTS.md as a README for agents: a dedicated, predictable place to provide the context and instructions to help AI coding agents work on your project." Plain Markdown, no required fields; nested files in monorepos, "the closest one takes precedence"; explicit user prompts override it; "Used by over 60k open-source projects"; "Stewarded by the Agentic AI Foundation under the Linux Foundation"; supported by OpenAI Codex, Google Jules, Aider, VS Code, GitHub Copilot, JetBrains Junie, Cursor, Warp and others.

**Claude Code** (**V** https://code.claude.com/docs/en/memory): reads `CLAUDE.md` (`./CLAUDE.md` or `./.claude/CLAUDE.md`, user `~/.claude/CLAUDE.md`, local `CLAUDE.local.md`) and, since v2.1.277, "can read `AGENTS.md` as your project instructions, so a repository already set up for other coding agents works without adding a `CLAUDE.md`". Default rule: `AGENTS.md` is read only when no `CLAUDE.md`/`CLAUDE.local.md` exists in the working directory or above; otherwise import it with a line `@AGENTS.md` in `CLAUDE.md`. Not read: `AGENTS.local.md`, `AGENTS.override.md`, "or anything under a `.agents/` directory". Path-scoped rules live in `.claude/rules/*.md` with `paths:` frontmatter. Target size "under 200 lines per CLAUDE.md file".

**llms.txt** (**V** https://llmstxt.org/, "The /llms.txt file, v2", Jeremy Howard, published 2024-09-03, modified 2026-08-10): a Markdown file "at the root path `/llms.txt` of a website or at any subpath (e.g. `/docs/llms.txt`)" with, in order: optional BOM; "An H1 with the name of the project or site. This is the only required section"; a blockquote summary; free Markdown without headings; H2 sections containing "file lists" of `- [name](url): notes`; a section named `Optional` marks skippable links. Pages should also be served as Markdown (`page.html.md` or `.md`). The current page does not mention `llms-full.txt`.

**Agent Skills** (**V** https://agentskills.io/specification): a directory with `SKILL.md` plus optional `scripts/`, `references/`, `assets/`. Frontmatter:

| Field | Required | Constraint |
|---|---|---|
| `name` | yes | 1–64 chars, lowercase `a-z`, `0-9`, hyphens, no leading/trailing/double hyphen, must match the directory name |
| `description` | yes | 1–1024 chars; what the skill does and when to use it |
| `license` | no | name or bundled file |
| `compatibility` | no | ≤ 500 chars, environment requirements |
| `metadata` | no | map of string to string |
| `allowed-tools` | no | space-separated pre-approved tools (experimental) |

```markdown
---
name: pdf-processing
description: Extract PDF text, fill forms, merge files. Use when handling PDFs.
license: Apache-2.0
metadata:
  author: example-org
  version: "1.0"
---
```

Progressive disclosure: metadata (~100 tokens) at startup, the body (< 5000 tokens recommended, "Keep your main `SKILL.md` under 500 lines") on activation, other files on demand; file references one level deep; validate with `skills-ref validate ./my-skill`. Discovery convention for clients (**V** https://agentskills.io/client-implementation/adding-skills-support.md): scan `<project>/.<client>/skills/` and the cross-client `<project>/.agents/skills/`, plus `~/.<client>/skills/` and `~/.agents/skills/`; project skills override user skills; project skills may be gated on a trust check.

**Claude Code skills** (**V** https://code.claude.com/docs/en/skills): follow the Agent Skills standard and extend it. Locations: enterprise (managed settings dir), personal `~/.claude/skills/<name>/SKILL.md`, project `.claude/skills/<name>/SKILL.md`, nested `<subdir>/.claude/skills/…`, additional directories via `--add-dir`, plugins `<plugin>/skills/<name>/SKILL.md` (invoked as `/plugin-name:skill-name`). Frontmatter accepted by Claude Code: `name`, `description`, `when_to_use`, `argument-hint`, `arguments`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `disallowed-tools`, `model`, `effort`, `context` (`fork`), `agent`, `background`, `hooks`, `paths`, `shell`, `metadata`, `license`, `compatibility`. The combined `description` + `when_to_use` is truncated at 1,536 characters in the skill listing; the listing budget is 1 % of the context window. Substitutions: `$ARGUMENTS`, `$N`, `${CLAUDE_SKILL_DIR}`, `${CLAUDE_PROJECT_DIR}`, `${CLAUDE_PLUGIN_ROOT}`. Uploads to claude.ai, the Skills API and `package_skill.py` accept only the six spec fields; any other key is a hard error ("Unexpected key(s) in SKILL.md frontmatter"). A skill meant for several agents should therefore use **only** `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.

**MCP** (**V** https://modelcontextprotocol.io/specification/latest and changelog): current revision **2026-07-28**. Servers offer Resources, Prompts and Tools; JSON-RPC 2.0; this revision makes the protocol stateless (no `initialize` handshake, no `Mcp-Session-Id`; every request carries protocol version and client capabilities in `_meta`), adds `server/discover`, requires `ttlMs`/`cacheScope` on list and read results, asks servers to return tools in deterministic order, allows any JSON Schema 2020-12 in `inputSchema`/`outputSchema`, and deprecates Roots, Sampling, Logging and the old HTTP+SSE transport. Extensions: Tasks, MCP Apps, and a working group on "Skills over MCP".

Python SDK v2 (**V** https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md ; `mcp` 2.2.0 on PyPI): "This is v2 of the MCP Python SDK, the current stable release line"; v1.x gets critical fixes only (pin `mcp>=1.28,<2` to stay). Quickstart, verbatim:

```python
from mcp.server import MCPServer

mcp = MCPServer("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Greet someone by name."""
    return f"Hello, {name}!"
```

Run with `uv run mcp dev server.py` (Inspector) or `uv run mcp run server.py --transport streamable-http`; install with `pip install "mcp[cli]"`. Prompts use `@mcp.prompt()`. In SDK v1 the same API was `from mcp.server.fastmcp import FastMCP` (**R**). The standalone `fastmcp` package (4.0.10, Apache-2.0) keeps the `FastMCP("name")`, `@mcp.tool`, `mcp.run()` style. **V** PyPI, gofastmcp.com

### 7.2 Making a Python package self-describing to agents

Findings:

- An agent working in a user's project sees that project's `AGENTS.md`/`CLAUDE.md` and skills, not files inside `site-packages`, unless something points it there. Files merely shipped in a wheel are invisible by default. **D** from the discovery rules above
- One article documents the typical failure: the README advertised `AGENTS.md` and `.agents/skills/*/SKILL.md`, but neither file was in the sdist or wheel until `MANIFEST.in`/`pyproject.toml` were fixed. **S** https://mikelev.in/futureproof/agents-md-agent-skills-pypi-receipts
- Frameworks start to load skills from installed packages (Microsoft Agent Framework `AgentSkill.from_module()`, LangChain deepagents skills). **S** search summary. No cross-tool standard exists for "skills provided by a dependency".

Practice that follows (**D**): put the knowledge in places an agent reaches with one command, and give users a one-line installer for the project-level files. Concrete file list in the Recommendations.

---

## 8. Open points and known gaps

1. **QGIS files were not loaded in QGIS.** No real `SVGFill` layer in `<Option>` form and no `SimpleMarker` sub-symbol were extracted; the key names `angle` and `coordinate_reference` for pattern fills, the `type` string of the preset colour ramp, and the unit strings other than `MM` are not confirmed from source. Which variable (`$geometry` or `@map_geometry`) carries painter units in a geometry generator differs between the 3.22 changelog and the current source.
2. **QGIS 4 compatibility is inferred.** The style version constant is unchanged and the changelog shows no break, but no statement guarantees that a 3.44-written QML renders identically in 4.2/4.4. The LTR designation changed between the 2025 blog post (4.2) and the live schedule (4.4.0 on 2026-10-30).
3. **OGC drafts.** I could not confirm whether Cartographic Symbology Part 1 (18-067r4) or OGC API – Styles moved beyond draft during 2026. No ISO 19117 revision was found; that is an absence of evidence from a web search.
4. **MapLibre pattern behaviour** (scaling between integer zooms, `pixelRatio` handling, whether the 512-px limit applies to physical or logical pixels, SDF in patterns, interaction of `fill-color` with `fill-pattern`, circle clipping at tile borders) comes from issue threads and memory, not from the specification or a test.
5. **Accessibility reading is interpretive.** How WCAG 1.4.11 applies to adjacent map fills, and whether national rules exempt maps, is not settled by the sources; EN 301 549 V4.1.1 is three weeks old and not yet cited in the OJEU. Thresholds for ΔE00 under CVD simulation have no published basis; Brychtová & Çöltekin tested normal vision only.
6. **Extraction fidelity.** All web content passed through a summarising fetch tool. Long files (QGIS C++ sources, the MapLibre `v8.json`) were truncated, so several facts rest on PR diffs or documentation instead of current source. GeoStyler parser coverage is from one source-file summary.
7. **Local tests used older library versions** (Matplotlib 3.9.2, SciPy 1.13.1) than the current releases (3.11.2, 1.18.0). The finding that sketch parameters do not affect collections should be re-run on 3.11.

---

## 9. Sources

QGIS
- https://qgis.org/resources/roadmap/ · https://qgis.org/schedule.ics
- https://blog.qgis.org/2025/10/07/update-on-qgis-4-0-release-schedule-and-ltr-plans/
- https://changelog.qgis.org/en/version/4.0/
- https://qgis.org/project/visual-changelogs/visualchangelog30/ · …/visualchangelog34/ · …/visualchangelog36/ · …/visualchangelog322/ · …/visualchangelog324/
- https://raw.githubusercontent.com/qgis/QGIS/master/resources/symbology-style.xml
- https://raw.githubusercontent.com/qgis/QGIS/master/src/core/symbology/qgsstyle.cpp · …/qgsfillsymbollayer.cpp · …/qgssymbollayerutils.cpp · …/qgssvgcache.cpp · …/qgsgeometrygeneratorsymbollayer.cpp · …/src/core/qgsabstractcontentcache.cpp · …/src/core/qgscolorrampimpl.cpp
- https://raw.githubusercontent.com/qgis/QGIS/master/tests/testdata/symbol_layer/categorized.qml · …/ruleBased.qml · …/QgsSVGFillSymbolLayer.sld · …/QgsPointPatternFillSymbolLayer.sld
- https://raw.githubusercontent.com/qgis/QGIS/master/tests/src/python/test_qgsunittypes.py · …/test_qgsrandommarkersymbollayer.py
- https://patch-diff.githubusercontent.com/raw/qgis/QGIS/pull/32241.diff · …/32456.diff · …/45638.diff
- https://raw.githubusercontent.com/qgis/QGIS/master/resources/function_help/json/{wave_randomized,triangular_wave_randomized,smooth,simplify,densify_by_distance,rand}
- https://api.qgis.org/api/master/classQgsRandomMarkerFillSymbolLayer.html · https://qgis.org/pyqgis/master/core/QgsUserColorScheme.html
- https://docs.qgis.org/latest/en/docs/user_manual/style_library/symbol_selector.html · …/style_library/style_manager.html · …/introduction/qgis_configuration.html
- https://raw.githubusercontent.com/qgis/QGIS-Documentation/master/docs/user_manual/introduction/general_tools.rst
- https://github.com/qgis/QGIS-Enhancement-Proposals/issues/126
- https://gist.github.com/lymperis-e/6b17521fa6df4a00671d0b1c7caf9d47 · https://github.com/opengisch/QField/issues/6202
- https://github.com/Klakar/QGIS_resources/tree/master/collections/Geosupportsystem/symbol (crayon_fill.xml, 70s_wallpaper.xml, random_points_geometry_generator.md)
- https://andywoodruff.com/posts/2024/qgis-hand-drawn-maps/
- https://developer.gimp.org/core/standards/gpl/

OGC, GeoServer, INSPIRE, converters
- https://www.ogc.org/standards/sld/ · https://www.ogc.org/standards/se/ · https://schemas.opengis.net/se/1.1.0/Symbolizer.xsd · …/common.xsd
- https://docs.ogc.org/is/18-067r3/18-067r3.html · https://github.com/opengeospatial/cartographic-symbology · https://docs.ogc.org/DRAFTS/20-009.html
- https://docs.geoserver.org/main/en/user/styling/sld/extensions/randomized/ · …/margins/ · …/pointsymbols/ · …/uom/ · …/sld/cookbook/polygons/ · …/sld/reference/pointsymbolizer/ · …/sld/introduction/
- https://www.osgeo.org/community-news/geoserver-3-0-0-released/
- https://inspire-mif.github.io/technical-guidelines/services/view-wms/ViewServices.html · https://inspire-mif.github.io/technical-guidelines/data/lu/dataspecification_lu.html
- https://github.com/geostyler/geostyler · …/geostyler-cli · …/geostyler-mapbox-parser · https://raw.githubusercontent.com/geostyler/geostyler-qgis-parser/master/src/QGISStyleParser.ts · https://github.com/GeoCat/bridge-style

Web mapping
- https://maplibre.org/maplibre-style-spec/layers/ · …/expressions/ · …/sprite/ · https://maplibre.org/maplibre-gl-js/docs/API/classes/Map/ · https://registry.npmjs.org/maplibre-gl/latest
- https://github.com/flother/spreet
- https://github.com/mapbox/mapbox-gl-js/issues/6296 · /1831 · /8043 · /8020 · /10033 (search summaries)
- https://leafletjs.com/reference.html · https://raw.githubusercontent.com/Leaflet/Leaflet/v1.9.4/src/layer/vector/SVG.js · https://github.com/teastman/Leaflet.pattern · https://github.com/Leaflet/Leaflet/issues/9869
- https://openlayers.org/en/latest/apidoc/module-ol_colorlike.html · …/module-ol_style_flat.html · …/module-ol_style_Fill-Fill.html
- https://deck.gl/docs/api-reference/extensions/fill-style-extension

Algorithms and packages
- https://raw.githubusercontent.com/rough-stuff/rough/master/src/{renderer,math,generator}.ts · …/src/fillers/{scan-line-hachure,hachure-filler,dot-filler}.ts · …/package.json · https://raw.githubusercontent.com/pshihn/hachure-fill/master/src/hachure.ts
- https://raw.githubusercontent.com/matplotlib/matplotlib/main/lib/matplotlib/artist.py · …/backends/backend_svg.py · …/backends/backend_pdf.py · …/src/path_converters.h · https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xkcd.html · …/matplotlib.patches.Patch.html · https://matplotlib.org/stable/gallery/shapes_and_collections/hatchcolor_demo.html
- https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.qmc.PoissonDisk.html · https://docs.scipy.org/doc/scipy/release/1.9.0-notes.html · …/1.10.0-notes.html · https://raw.githubusercontent.com/scipy/scipy/main/scipy/stats/_qmc.py
- https://numpy.org/doc/stable/reference/random/compatibility.html
- https://shapely.readthedocs.io/en/stable/reference/shapely.segmentize.html · …/shapely.buffer.html · …/shapely.contains_xy.html
- https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap · https://doc.qt.io/qt-6/svgextensions.html · https://cairosvg.org/svg_support/ · https://raw.githubusercontent.com/linebender/resvg/main/docs/unsupported.md
- https://vpype.readthedocs.io/en/latest/reference.html · https://vsketch.readthedocs.io/en/latest/overview.html · https://raw.githubusercontent.com/marceloprates/prettymaps/main/README.md · https://github.com/cktlco/rough-py
- PyPI JSON: rough, prettymaps, vsketch, vpype, drawsvg, svgwrite, CairoSVG, resvg-py, shapely, colorspacious, colour-science, daltonlens, mcp, fastmcp
- ACM listings for Cohen et al. 2003 (doi 10.1145/882262.882265) and Kopf et al. 2006 (doi 10.1145/1179352.1141916)

Tokens
- https://www.designtokens.org/tr/2025.10/format/ · …/tr/2025.10/resolver/ · …/tr/drafts/format/ · …/tr/drafts/color/ · https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/
- https://styledictionary.com/info/dtcg/ · …/info/tokens/ · …/reference/hooks/formats/predefined/ · https://registry.npmjs.org/style-dictionary/latest

Accessibility
- https://www.w3.org/TR/WCAG22/ · https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html · …/non-text-contrast.html · https://www.w3.org/WAI/WCAG22/Techniques/general/G18 · https://www.w3.org/WAI/news/2025-10-21/wcag22-iso
- https://accessible-eu-centre.ec.europa.eu/content-corner/news/european-accessibility-standard-en-301-549-has-been-updated-2026-09-07_en
- https://www.gesetze-im-internet.de/bitv_2_0/BJNR184300011.html · https://www.legislation.gov.uk/eudr/2016/2102/article/1 · https://www.legislation.gov.uk/eudr/2019/882/article/2 · …/article/31
- https://nullbarriere.de/din32975.htm
- http://coltekin.net/arzu/publications/brychtova_coltekin-2016.pdf (doi 10.1080/15230406.2016.1140074) · https://www.tandfonline.com/doi/full/10.1080/23729333.2015.1055643
- https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html · https://daltonlens.org/opensource-cvd-simulation/
- https://colorspacious.readthedocs.io/en/latest/reference.html · https://colour.readthedocs.io/en/latest/colour.blindness.html · https://colour.readthedocs.io/en/latest/generated/colour.delta_E.html
- https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-colours-in-charts/ · https://www.w3.org/WAI/RD/wiki/Accessible_Maps

Agents
- https://agents.md/ · https://llmstxt.org/ · https://agentskills.io/specification · https://agentskills.io/client-implementation/adding-skills-support.md
- https://code.claude.com/docs/en/skills · https://code.claude.com/docs/en/memory
- https://modelcontextprotocol.io/specification/latest · https://modelcontextprotocol.io/specification/2026-07-28/changelog · https://raw.githubusercontent.com/modelcontextprotocol/python-sdk/main/README.md · https://pypi.org/project/mcp/ · https://pypi.org/project/fastmcp/ · https://gofastmcp.com/getting-started/welcome
- https://mikelev.in/futureproof/agents-md-agent-skills-pypi-receipts

---

## Recommendations for the library

Everything in this section is a design proposal (**D**) derived from the findings above.

### A. One canonical model, native writers per platform

1. **Source of truth**: a Python catalog (`ulg/catalog/catalog.json` with JSON Schema 2020-12). Per element: stable `id`, labels and synonyms (de/en), semantic colour tokens (fill, outline, ink), texture recipe per LOD (mark type, spacing, size, jitter, units, clip mode), and accessibility data.
2. **Canonical texture asset = a toroidal tile per element and LOD**, defined as vector marks in a 64 × 64 mm cell (≙ 256 px at 1×). Every platform can consume a tile; richer per-feature scattering is an optional mode where the platform supports it. This keeps QGIS, GeoServer, MapLibre and the Python renderer visually consistent.
3. **No converter chain.** GeoStyler, bridge-style and QGIS's own SLD export all drop random fills, SVG tiles, seeds and generators. Write each format directly.

### B. Export artefacts per platform

| Platform | Files | Content and rules |
|---|---|---|
| Neutral | `catalog.json`, `catalog.schema.json`, `tiles/<element>-lod<n>.svg`, `tiles/*.png` (1×, 2×), `legend/*.svg` | SVG tiles ink-only with `param(fill)`/`param(outline)` placeholders and defaults; basic shapes and paths only (no filters, no `<pattern>`, no CSS); PNG via resvg |
| QGIS 3.44 / 4.x | `ulg.xml` (style library), `ulg_categorized.qml`, `ulg_rules_lod.qml`, `ulg.gpl` | `<qgis_style version="2">`; one fill symbol per element and LOD, tagged `ULG`; layers: `SimpleFill` (no outline) + texture + outline. Texture mapping: tile → `SVGFill` with `svgFile="base64:…"`, `pattern_width_unit=MM`; scatter → `RandomMarkerFill` (`count_method=1`, non-zero `seed`) or `PointPatternFill` with `random_deviation_*`, `seed`, `clip_mode=completely_within`; lines (planks, herringbone) → `LinePatternFill` in `RenderMetersInMapUnits` with map-unit-scale clamp. Outline: plain `SimpleLine` at LOD 0–1; `GeometryGenerator` (`SymbolType=Line`, `units=MM`, `wave_randomized(…, seed := $id + 1)`) at LOD 2. Rule-based QML with `scalemindenom`/`scalemaxdenom` per LOD. Write properties in dual `<Option>` + `<prop>` form. Build from golden templates saved by QGIS, or through PyQGIS when present. Preset colour ramp plus GPL palette for swatches |
| OGC / GeoServer | `sld/<element>.sld` (SE 1.1 core), `sld-geoserver/<element>.sld`, tile PNG/SVG next to the SLD, `legend/*.png` | Core: `PolygonSymbolizer` with solid `Fill`, second `PolygonSymbolizer` with `GraphicFill`/`ExternalGraphic` (relative `OnlineResource`, `Format image/png` or `image/svg+xml`), `LineSymbolizer` for the outline, `MinScaleDenominator`/`MaxScaleDenominator` per LOD. GeoServer flavour adds `graphic-margin` and, for scatter textures, `random`, `random-tile-size`, `random-symbol-count`, `random-rotation`, `random-seed` with `shape://` or `wkt://` marks; `uom` metre for ground-anchored patterns. Unique style `Name`, `Title`, `Abstract`; for INSPIRE view services register as an additional style next to `inspire_common:DEFAULT` and provide a legend per language |
| MapLibre GL | `maplibre/style-fragment.json`, `sprite.json/.png`, `sprite@2x.json/.png`, `ulg-maplibre.js` | Per element three layers: `fill` (colour), `fill` (`fill-pattern`, transparent ink tile), `line` (outline). Tiles power-of-two (128 or 256 px logical). LOD via `minzoom`/`maxzoom` and `["step", ["zoom"], …]`. Trees: `circle` layer with the base-2 exponential radius expression generated for the data latitude, or crown polygons at high zoom. Helper registers tiles at runtime with `addImage` |
| Leaflet | `ulg-patterns.svg`, `ulg.css`, `ulg-leaflet.js` | `<pattern>` defs + classes; SVG renderer only |
| OpenLayers | `ol-flat-style.json`, atlas PNG | `fill-pattern-src`, `fill-pattern-size`, `fill-pattern-offset`, tint through `fill-color` |
| deck.gl | `atlas.png`, `atlas-mapping.json` | `FillStyleExtension({pattern: true})`, `fillPatternSizeUnits: 'meters'` for ground-anchored textures |
| Tokens | `tokens/*.tokens.json`, `ulg.resolver.json`, `ulg.css`, `tokens.flat.json`, `ulg/_tokens.py` | DTCG 2025.10 colour objects with `hex` fallback; primitives + semantic aliases; themes `default`, `high-contrast`, `cvd-safe`, `greyscale`; generated by Python, validated with Style Dictionary in CI |
| Baked geometry (optional) | `textures.gpkg` | outline and texture marks as real geometries for a given scale; the only route to identical marks on every platform, and usable for plotters and CAD |

### C. Rendering algorithm: hand-drawn but clean

**Units.** All style parameters in paper millimetres; convert with `map_units = mm · scale_denominator / 1000`. Ground-anchored textures (paving, planks) are specified in metres instead.

**Levels of detail** (proposal; web zooms computed for 52.5° N with 512-px tiles and 0.28 mm pixels: z 14 ≈ 1:10 400, z 15 ≈ 1:5 200, z 17 ≈ 1:1 300):

| LOD | Scale | Web zoom | Fill | Texture | Outline |
|---|---|---|---|---|---|
| 0 overview | smaller than 1:10 000 | ≤ 14 | flat pastel | none | 0.18 mm, no wobble, or none |
| 1 plan | 1:2 500 – 1:10 000 | 15–16 | flat | tile, sparse (Poisson radius 6–8 mm) | 0.25 mm, amplitude 0.08 mm |
| 2 detail | larger than 1:2 500 | ≥ 17 | flat | tile or per-feature scatter (radius 4–6 mm), richer marks, single trees | 0.35–0.40 mm, amplitude 0.15 mm |

**Fill.** Always the exact input geometry. No displacement, no smoothing, no filters.

**Outline wobble.**

1. Node all polygon boundaries once (`shapely.unary_union` of the boundaries, then `linemerge`) so every shared edge exists exactly once; draw each edge once. Colour rule for shared edges: the darker of the two outline tokens or a neutral edge token. The prototype shows a doubled line without this step and a clean result with it.
2. Densify each edge (`shapely.segmentize`, step ≈ 0.75 mm on paper).
3. Displace along the normal by a band-limited random signal with wavelengths 4–12 mm. Randomise wavelength and amplitude per half-wave (as `wave_randomized` does) or use 1-D value noise; a plain sum of three sines looked too regular in the prototype.
4. Amplitude `A = min(A_lod, w/2 − 0.02 mm, ℓ/10, local_width/4)`, with stroke width `w` and edge length `ℓ`. `A < w/2` guarantees that the ink always covers the true boundary, so the exact fill never shows a sliver and the map stays polygon-accurate; `ℓ/10` is rough.js's cap for short segments. At 1:1 000 an amplitude of 0.15 mm is 15 cm on the ground.
5. Taper the displacement to zero within `λ_min/2` of every original vertex (rough.js `preserveVertices`), so corners and junctions stay on the data.
6. One stroke, round caps and joins, no double stroke.
7. Seed per edge from its canonical coordinates (rounded, direction-normalised), so an edge looks the same whichever polygon is drawn and whatever the feature order.

**Texture sampling.**

- Tile mode (default, portable): toroidal Bridson Poisson-disk in the 64 mm cell; marks crossing a cell edge are duplicated with wrap-around; the tile is anchored to the map origin, so adjacent polygons of one class share a continuous texture and output does not depend on how features are split.
- Scatter mode (Python renderer, QGIS, GeoServer, deck.gl): per-feature sampling seeded by the feature key.
- Placement: keep marks completely inside (`contains_xy` against `polygon.buffer(−mark_radius − 0.3 mm)` with `shapely.prepare`); fall back to centroid-inside for polygons narrower than twice the inset; skip the texture for polygons smaller than about (2·radius)² on paper.
- Marks: a small parametric vocabulary (tuft of 2–3 blades, dot, open pebble, wave dash, plank line, herringbone pair), each with seeded jitter in rotation (± 8–15°), length (± 20 %) and shape; stroke ≥ 0.18 mm, single stroke.
- Regular textures (pavings, deck, herringbone) are lattices in metres with light jitter, not Poisson samples.
- Target ink coverage 2–10 % of the area so the texture stays sparse.

**Seeding and reproducibility.**

- `seed = blake2b(catalog_version | element_id | lod | key | user_seed)` reduced to a non-zero 32-bit integer. `key` is the edge key, the tile id, or a stable feature id; if no id column exists use a hash of the normalised, precision-reduced WKB. Never use Python's `hash()` or the global `random` state.
- Use one small integer PRNG specified in the docs and implemented identically in Python and in the JS helper, with published test vectors. Do not rely on `numpy.random.Generator` method streams across NumPy versions (the policy allows them to change); `BitGenerator` raw streams are the stable layer.
- Write non-zero seeds into QGIS (`seed`) and GeoServer (`random-seed`). Their generators differ from ULG's, so scatter textures match in density and style, not mark for mark. Only tile mode or baked geometry is identical everywhere.
- Deterministic output: sort by key, fixed decimal precision, no timestamps, fixed `svg.hashsalt`, and record `ulg_version`, `catalog_version`, `scale`, `lod`, `seed` in the SVG metadata. Test: same input gives byte-identical SVG.
- Matplotlib: draw computed geometry with `PatchCollection`/`LineCollection`; do not use `set_sketch_params` or hatches. The SVG writer consumes the same coordinates.

### D. Legibility checks to automate (`ulg check`)

| Check | Rule | Basis |
|---|---|---|
| Outline vs. fills | contrast ≥ 3:1 against its own fill and every fill it may adjoin; mandatory in the `high-contrast` theme, reported in the default theme | WCAG 1.4.11, G209 |
| Texture ink vs. fill | ≥ 3:1 where texture is the distinguishing cue | WCAG 1.4.1 (G111), 1.4.11 |
| Label vs. fill | ≥ 4.5:1 (≥ 3:1 large text) | WCAG 1.4.3 |
| Fill pairs, normal vision | ΔE00 ≥ 10 for every pair of classes; list violations | Brychtová & Çöltekin 2016 |
| Fill pairs under CVD | recompute ΔE00 after Machado 2009 protan/deutan/tritan (severity 1.0, linear RGB); every pair below 10 must differ in texture family and be flagged in the catalog | design rule; no published threshold |
| Greyscale | ΔL\* report for print themes | design rule |
| Texture geometry | stroke ≥ 0.18 mm, mark ≥ 1 mm on paper and ≥ 2 CSS px on screen; ink coverage within 2–10 % | design rule |
| Tile integrity | 2 × 2 seam test, power-of-two pixel size, transparent background | MapLibre spec |
| Wobble bound | Hausdorff distance between drawn outline and true boundary ≤ A; A < w/2 | design rule |
| Format validity | QGIS round trip in CI containers (LTR and latest) with PyQGIS; MapLibre style-spec validator; SLD schema validation and a GeoServer smoke test; DTCG files through Style Dictionary; `skills-ref validate` | tool docs |
| Legend completeness | every class has name, swatch, texture sample and a text description; a table export exists for non-visual use | WCAG 1.4.1 (G14), EU map exemptions presuppose an accessible alternative |

The colour maths (WCAG contrast, sRGB↔Lab, CIEDE2000, Machado matrices) fits in about 150 dependency-free lines; keep `colour-science` as an optional cross-check in tests.

### E. Agent-facing files to ship

| Where | File | Purpose |
|---|---|---|
| Wheel | `ulg/catalog/catalog.json`, `catalog.schema.json` | machine-readable truth; load with `importlib.resources`; include `schema_version`, synonyms (de/en), `use_when`/`avoid_when`, asset names per platform, contrast and ΔE data |
| Wheel | `ulg/agent/skill/urban-landscape-graphics/SKILL.md` + `references/catalog.md`, `references/platforms.md`, `scripts/` | Agent Skill using only the six spec fields (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`); description ≤ 1024 characters with trigger terms; body under 500 lines; references generated from the catalog |
| Wheel | `ulg/agent/AGENTS.snippet.md`, `ulg/py.typed`, Markdown docs | short consumer-side instructions ("never invent colours or patterns; run `ulg show <id> --json`") |
| CLI | `ulg catalog --json`, `ulg show <id> --json`, `ulg find "<text>" --json`, `ulg export <platform>`, `ulg check --json`, `ulg agent guide`, `ulg agent install [--claude] [--agents]`, `ulg mcp` | one-command access for any agent; `agent install` copies the skill to `.claude/skills/` and/or `.agents/skills/` and appends the snippet to `AGENTS.md`, only when the user runs it |
| Repository | `AGENTS.md`, `CLAUDE.md` containing `@AGENTS.md`, docs site with `llms.txt` and `.md` page mirrors | contributors and web-reading agents; verify in CI that the agent files are inside the built wheel and sdist |
| Optional | MCP server (`ulg[mcp]`, SDK v2 `MCPServer`) | tools `list_elements`, `get_element`, `find_element`, `export_style`, `check_palette`; resources `ulg://catalog`, `ulg://element/{id}`, `ulg://tokens/{theme}`; stateless, deterministic tool order, output schemas from the catalog schema |
| Optional | Claude Code plugin with `skills/urban-landscape-graphics/SKILL.md` | one-step install for Claude Code users |

