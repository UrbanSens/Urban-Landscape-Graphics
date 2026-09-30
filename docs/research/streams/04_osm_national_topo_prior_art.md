# Stream 04: OpenStreetMap tagging, large-scale national topographic models, prior-art habitat symbology

Research date: 2026-09-30 · Scope: OSM tags and OSM Carto colours; NL BGT/IMGeo; CH amtliche Vermessung; AT DKM; UK habitat/metric systems; other European large-scale conventions · Purpose: crosswalks and colour lessons for the "Urban Landscape Graphics" element catalog (house style "UrbanSens – Ecological Vector Style").

## How to read this file

**Evidence marks (every table carries one per row or one for the whole table):**

| Mark | Meaning |
|---|---|
| **V** | Verified by me this session in a primary source; URL given. Text pages were read through a fetch tool that converts the page and answers through a small extraction model, so wording is sometimes shortened; codes/hex values that matter were cross-checked where stated. |
| **V-img** | Verified by reading the PDF page images of the primary source myself (no intermediate extraction model). Highest confidence. |
| **S** | Secondary source (community repository, search-engine snippet, documentation assistant answer). |
| **R** | Recalled from memory, not verified this session. Treat as a lead, not a fact. |
| **D** | Derived by me from a verified value (e.g. CMYK→RGB conversion, LESS `lighten()`), i.e. not printed in the source. |

**Method limits.** The session-wide web-search budget ran out during the prior-art part, so GeoDanmark, Finland, Berlin and the official UKHab palette could only be approached by direct URL guesses. Everything that could not be verified is listed in section 9 "Open points". No tag, code or colour in this file is invented; where a source contains an obvious misprint it is quoted as printed and flagged.

## Key findings in brief

1. **OSM is sufficient for automatic styling if three keys are combined:** cover from `landuse`/`natural`/`leisure`, material from `surface` (45 documented values, all mapped in 8.2), and object attributes (`leaf_type`, `diameter_crown`, `wetland`, `water`, `meadow`, `basin`, `green_roof`). Direct hooks for existing classes exist (`meadow=wildflower`, `wetland=reedbed`, `surface=wood`). `landcover=*` is marginal (largest value 292k uses vs 34 million `natural=tree`).
2. **OSM Carto v6.1.0** colours are verified from the style files (section 2), including the Lch design comments; planted shrub beds (`natural=shrubbery`), `landuse=greenery` and surface materials are not rendered at all by the default map.
3. **BGT/IMGeo** offers the finest official material vocabulary (16 vegetated and 6 unvegetated classes, about 40 IMGeo "plus" sub-types) and three verified official colour sets: saturated *standaard*, grouped *achtergrond*, near-grey *pastel* (section 3.5).
4. **Swiss AV** has 26 land-cover values and published RGB values (2024 instruction); the convention is black/white first, colour for five things only, symbol rasters for the rest (section 4.2).
5. **Austria's DKM** has 26 use classes with stable numeric codes but no fills at all: line plus glyph at the polygon reference point (section 5).
6. **England's statutory biodiversity metric** supplies a complete scored urban element list (21 urban habitat types, tree size classes, hedgerow types); the official tool workbook was parsed (section 6.3). The official UKHab colour palette is licence-gated and could not be verified.
7. **Published RGB prior art at 1:1,000–1:5,000:** LBP-Musterlegendenkatalog (DE, section 6.5) and the OS MasterMap "Outdoor style" (GB, section 7.1); both are pastel and both use state/pattern modifiers.
8. **The 16-class sheet lacks** lines and points (hedge, tree row, wall, fence, furniture), planted-bed types, the private-garden mosaic, semi-sealed and water-bound surfaces, natural-stone sett and clinker, sports/play synthetics, SuDS elements, green roofs/walls, and an "unknown / in transition" element (section 8.3).

## 0. Versions checked (state 2026-09-30)

| Item | Version / date found | St. | Source |
|---|---|---|---|
| OpenStreetMap Carto (default osm.org style) | **v6.1.0, 2026-09-10** (v6.0.0 2026-03-11 moved to the osm2pgsql flex backend; v5.9.0 2024-10-17). Repository now lives at `openstreetmap-carto/openstreetmap-carto` (old `gravitystorm/…` URLs still resolve). | V | https://github.com/gravitystorm/openstreetmap-carto/tags · https://raw.githubusercontent.com/gravitystorm/openstreetmap-carto/master/CHANGELOG.md |
| taginfo (tag usage counts) | data until 2026-09-29T00:59:51Z | V | https://taginfo.openstreetmap.org/ (API calls cited in 1.6/1.7) |
| BGT/IMGeo visualisation rules | **BGT\|IMGeo Visualisatieregels 2.3**, 15 Oct 2018, "definitieve versie" | V | https://docs.geostandaarden.nl/bgt/visualisatie/ |
| BGT / IMGeo catalogues | Gegevenscatalogus BGT 1.2, IMGeo 2.2 current; IMGeo 2.3 draft on GitHub pages; successor "Samenhangende Objectenregistratie (SOR)" still in preparation | S | search snippets for https://docs.geostandaarden.nl/imgeo/catalogus/bgt/ and https://docs.geostandaarden.nl/imgeo/catalogus/imgeo/ |
| CH data model | DM.01-AV-CH (model file `DM.01-AV-CH_LV95_24d_ili1.ili`); successor **DMAV Version 1.0** being introduced | V | https://models.geo.admin.ch/V_D/DM.01-AV-CH_LV95_24d_ili1.ili |
| CH drafting instructions | Plan für das Grundbuch: Weisung 9 Mar 2007 (Stand 1 Feb 2014) · BP-AV: Weisung 22 Apr 2009 · Basisplan for DMAV 1.0: Weisung 1 Aug 2024 | V-img | URLs in section 4 |
| AT cadastre | BANU-V, BGBl. II Nr. 116/2010 (consolidated version in force since 07.05.2012) · DKM SHP interface v2.9 (04.12.2024) · DXF v2.6 (16.12.2024) · parcel CSV v1.2 (29.01.2025) | V / V-img | URLs in section 5 |
| UK statutory biodiversity metric | calculation tool **v1.0.4** (released 3 July 2025 according to the workbook's "Version History" sheet); user guide "June 2026" (gov.uk page last updated 2 June 2026); small sites metric tool 1.2.3, SSM user guide July 2025; condition sheets July 2025 | V | https://www.gov.uk/government/publications/statutory-biodiversity-metric-tools-and-guides |
| UKHab | v2.01 (July 2023) is the stable release in the community tooling; ukhab.org documentation page states v2.1 was released 7 July 2026, while its home page still speaks of a consultation, **conflicting, see Open points** | V (both pages) | https://www.ukhab.org/ukhab-documentation/ · https://www.ukhab.org/ |
| OS MasterMap Topography stylesheets | "Schema version 9" folder, colour workbook `OSMM-Topography-Layer-Colour-Values.xlsx` | V | https://github.com/OrdnanceSurvey/OSMM-Topography-Layer-stylesheets |
| GeoDanmark | Specifikation 6.0.2 (11.07.2024); 7.0 preliminary / in consultation | V | https://www.geodanmark.dk/anvend-geodata/specifikation/ |
| Hamburg biotope key | 7th revised edition, March 2025 | V-img | section 6.6 |
| LBP-Musterlegendenkatalog (Bundesnetzagentur) | 2nd version, December 2021 | V-img | section 6.5 |

---

## 1. OpenStreetMap tags for parcel-scale landscape features

All rows in 1.1–1.15 are **V** (OSM wiki page named in each heading, fetched this session) unless a row says otherwise. Meanings are the wiki descriptions, shortened faithfully. "Carto" = rendered by OSM Carto v6.1 according to `style/landcover.mss` (section 2).

### 1.1 `landuse=*`: https://wiki.openstreetmap.org/wiki/Key:landuse

| Tag | Wiki meaning | Note for the library |
|---|---|---|
| `landuse=grass` | "An area of mown and managed grass not otherwise covered by specific tag". Detail page: a smaller area of grass, usually mown and managed, e.g. roundabout middles, road verges, central reservations | → lawn / amenity grass. Most important urban grass tag. |
| `landuse=meadow` | Land primarily vegetated by grass and other non-woody plants, mainly used for hay or grazing | → meadow. Sub-key `meadow=*` see 1.2b |
| `landuse=village_green` | A distinctive area of grassy public land in a village centre | → lawn |
| `landuse=recreation_ground` | An open green space for general recreation | → lawn/park container |
| `landuse=flowerbed` | An area designated for flowers | → flower/perennial bed (missing in 16-class sheet) |
| `landuse=greenery` | "An area covered in unspecified or various types of decorative vegetation. Consider using a more specific tag instead" (status: in use) | → ornamental planting (mixed) |
| `landuse=forest` | Managed forest or woodland plantation | → woodland (treated like `natural=wood` by Carto) |
| `landuse=logging` | Area where some or all trees have been cut down | → bare/ruderal |
| `landuse=orchard` | Intentional planting of trees or shrubs maintained for food production | → orchard (missing) |
| `landuse=vineyard` | Land where grapes are grown | → vineyard (missing) |
| `landuse=allotments` | Land given over to local residents for growing vegetables and flowers | → allotment/kitchen garden (missing) |
| `landuse=plant_nursery` | Intentional planting of plants for the production of new plants | → nursery |
| `landuse=greenhouse_horticulture` | Area used for growing plants in greenhouses | → glasshouse |
| `landuse=farmland` | Farmland used for tillage (cereals, vegetables, oil plants, flowers) | → arable (missing) |
| `landuse=farmyard` | Land with farm buildings and associated open space | built context |
| `landuse=animal_keeping` | Land used to keep animals, particularly horses and livestock | paddock |
| `landuse=aquaculture` | Farming of freshwater and saltwater organisms | water |
| `landuse=cemetery` | Place for burials | → cemetery (function overlay) |
| `landuse=brownfield` | Land scheduled for new development where old buildings have been demolished | → ruderal / bare ground |
| `landuse=greenfield` | Land scheduled for new development where there have been no buildings before | → rough grass |
| `landuse=construction` | Site under active development and construction | → bare soil / construction |
| `landuse=landfill` | Place where waste is dumped | bare/ruderal |
| `landuse=quarry` | Surface mineral extraction | rock/gravel |
| `landuse=basin` | "An area of land artificially graded to hold water. Note that this definition includes also structures typically without water." Sub-key `basin=infiltration` (storm water seeps into the aquifer), `detention` (drains slowly into waterways), `retention` ("retains it, forming an artificial pond"), `settling`, `evaporation`; `intermittent=yes` if water is not permanent; alternative tagging `natural=water` + `water=basin` (https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dbasin) | → SuDS elements: `infiltration`/`detention` = dry grassed basin or rain garden; `retention` = pond |
| `landuse=reservoir` | deprecated variant; use `natural=water` + `water=reservoir` | water |
| `landuse=salt_pond` | Place where salt water is evaporated to extract salt | water |
| `landuse=railway` | Area for railway use | built context / ballast |
| `landuse=highway` | Area of land used for a highway, including footways and verges | built context |
| `landuse=depot`, `garages`, `port` | depot for vehicles · one-level garage boxes · coastal industrial area | built context |
| `landuse=residential`, `commercial`, `retail`, `industrial`, `education`, `institutional` (ambiguous), `fairground`, `religious`, `military`, `winter_sports`, `conservation` (deprecated) | zone-type land uses | not surface elements; use as context/background only |

### 1.2 `natural=*`: https://wiki.openstreetmap.org/wiki/Key:natural

| Tag | Wiki meaning | Note |
|---|---|---|
| `natural=wood` | Tree-covered area (forest or wood) | → woodland; refine with `leaf_type`, `leaf_cycle` |
| `natural=tree` | A single tree | → tree point symbol (attributes in 1.15) |
| `natural=tree_row` | A line of trees (approved tag; way drawn through the trunks) | → tree row line symbol |
| `natural=tree_stump` | Remains of a cut down or broken tree | habitat feature point |
| `natural=scrub` | Uncultivated land covered with shrubs, bushes or stunted trees | → shrub (wild) |
| `natural=shrubbery` | "An area of woody shrubbery that is actively maintained or pruned by humans. A slightly wilder look is also possible." Status *de facto* (proposed twice, rejected, growing use). Sub-keys `shrubbery:density=sparse/medium/dense`, `shrubbery:shape` (topiary), `height`, `leaf_type`, `leaf_cycle`, `genus`, `species`, `taxon`. Source: https://wiki.openstreetmap.org/wiki/Tag:natural%3Dshrubbery | → shrub (planted/ornamental); area hedges = shrubbery + density=dense |
| `natural=shrub` | individual bush, on a node (mentioned on the shrubbery page) | → shrub point symbol |
| `natural=heath` | Dwarf-shrub habitat, open, low growing woody vegetation | → heath (missing) |
| `natural=grassland` | Areas dominated by grasses and herbaceous plants (non-cultivated) | → meadow / rough grass |
| `natural=fell`, `tundra`, `moor` | habitats above tree line / upland low vegetation on acidic soils | rarely urban |
| `natural=wetland` | Natural area subject to inundation or with waterlogged ground; subtype in `wetland=*` (1.3) | → reed/wetland |
| `natural=water` | Any body of water; subtype in `water=*` (1.4) | → water |
| `natural=spring`, `hot_spring`, `geyser` | place where ground water flows naturally from the ground … | point symbol |
| `natural=mud` | Water saturated fine grained soil without vegetation | → mud / bare wet soil |
| `natural=sand` | Area covered by sand with no or very little vegetation | → sand |
| `natural=beach` | Landform along water of sand, shingle or loose material (+ `surface=*`) | → sand/shingle |
| `natural=shingle` | Accumulation of rounded rock fragments on beach or riverbed | → gravel (rounded) |
| `natural=scree` | Unconsolidated angular rocks formed by rockfall and weathering | → rock/scree |
| `natural=bare_rock` | Area with sparse soil or vegetation exposing bedrock | → rock |
| `natural=rock`, `stone` | notable rock attached to bedrock · single freestanding rock | point symbol (boulder) |
| `natural=cliff`, `earth_bank`, `gully`, `ridge`, `arete`, `dune`, `sinkhole`, `cave_entrance` | landform lines/points | line symbols |
| `natural=glacier`, `bay`, `cape`, `coastline`, `reef`, `shoal`, `strait`, `peninsula`, `isthmus`, `blowhole`, `crevasse`, `blockfield`, `arch`, `fumarole`, `gorge`, `hill`, `peak`, `saddle`, `valley`, `volcano` | remaining documented values | out of urban scope |

### 1.2b `meadow=*` (sub-key of landuse=meadow): https://wiki.openstreetmap.org/wiki/Tag:landuse%3Dmeadow

| Value | Wiki meaning | Note |
|---|---|---|
| `meadow=agricultural` | hay meadow or pasture, maintained by cutting, mowing or grazing | meadow |
| `meadow=pasture` | pasture for grazing livestock (not a hay meadow) | meadow (grazed) |
| `meadow=paddock` | area of grass where horses or other animals are kept | meadow (grazed) |
| `meadow=transitional` | grass transitioning to heath, scrub or woodland | rough grass / succession |
| `meadow=perpetual` | "meadow" retained by natural factors (natural=grassland more common) | rough grass |
| `meadow=meadow_orchard` | both an orchard and a meadow (Streuobstwiese) | meadow orchard |
| `meadow=wildflower` | "A wildflower meadow. It serves primarily as a habitat for insects and for nature conservation rather than for the production of grass and hay" | **→ wildflower meadow (direct hit for the existing class)** |

### 1.3 `wetland=*`: https://wiki.openstreetmap.org/wiki/Key:wetland

| Value | Wiki meaning | Carto pattern |
|---|---|---|
| `reedbed` | Inundated area dominated by tall non-woody plants (reeds, bulrushes) | `wetland_reed.png` on `@grass` |
| `marsh` | Periodically saturated/flooded, herbaceous vegetation | `wetland_marsh.png` on `@grass` |
| `wet_meadow` | Semi-wetland meadow saturated much of the year | `wetland_marsh.png` on `@grass` |
| `fen` | Groundwater-fed peat-forming wetland with grasses, sedges, reeds, wildflowers | `wetland_bog.png` on `@grass` |
| `bog` | Peat-filled depressions fed by rainfall | `wetland_bog.png` on `@heath` |
| `string_bog` | Bog of ridges and islands alternating with wet sedge mats | `wetland_bog.png` on `@heath` |
| `swamp` | Waterlogged forest with dense vegetation | `wetland_swamp.png` on `@forest` |
| `mangrove` | Coastal wetland with salt-tolerant trees and shrubs | `wetland_mangrove.png` on `@scrub` |
| `saltmarsh` | Coastal marsh exposed to tidal inundation | `wetland_marsh.png` + `salt-dots-2.png` on `@grass` |
| `tidalflat` | Intertidal sediment deposits | `@mud` fill |
| `dambo` | Shallow wetland of African plateaus | generic `wetland.png` |

### 1.4 `water=*` (with `natural=water`): https://wiki.openstreetmap.org/wiki/Key:water

| Group | Values (wiki meaning) |
|---|---|
| Natural | `lake` (body of relatively still water) · `river` (water area of a river) · `stream` (water area of a stream) · `oxbow` · `lagoon` · `stream_pool` · `rapids` · `cenote` |
| Artificial | `pond` (standing water, man-made in most cases, smaller than a lake) · `reservoir` · `basin` (land artificially graded to hold water) · `canal` · `ditch` · `drain` · `lock` · `moat` · `harbour` · `fish_pass` · `reflecting_pool` (shallow ornamental pool in gardens/parks) · `wastewater` (clarifier/settling basin) |

### 1.5 `leisure=*`: https://wiki.openstreetmap.org/wiki/Key:leisure

| Tag | Wiki meaning | Note |
|---|---|---|
| `leisure=park` | Open, green area for recreation, usually municipal | container; its inside still needs surface elements |
| `leisure=garden` | "A place where flowers and other plants are grown in a decorative and structured manner or for scientific purposes." | → garden (mixed). `garden:type`, `garden:style` below |
| `leisure=pitch` | "An area designed for practising sport, normally designated with appropriate markings." + `sport=*`, `surface=*`, `lit`, `hoops`, `covered`, `indoor` | → sports surface by `surface` |
| `leisure=track` | Track for running, cycling and other non-motorised racing | → sports surface |
| `leisure=playground` | Playground for little children | → play surface (by `surface`) |
| `leisure=swimming_pool` | A swimming pool (water area only) | → pool water |
| `leisure=dog_park` | Designated area where dogs may exercise unrestrained | function overlay |
| `leisure=nature_reserve` | Protected area of importance for wildlife, flora, fauna or geology | boundary overlay |
| `leisure=golf_course`, `miniature_golf`, `disc_golf_course` | golf facilities | function overlay |
| `leisure=sports_centre`, `stadium`, `sports_hall`, `fitness_centre`, `fitness_station`, `horse_riding`, `ice_rink`, `water_park`, `high_ropes_course`, `trampoline_park` | sport facilities | function overlay / built |
| `leisure=common` | common land (**deprecated**) | lawn |
| `leisure=picnic_table`, `firepit`, `bandstand`, `bird_hide`, `wildlife_hide`, `bleachers`, `outdoor_seating` | furniture-like features | point symbols |
| `leisure=marina`, `slipway`, `swimming_area`, `bathing_place`, `beach_resort`, `fishing`, `sunbathing`, `resort`, `summer_camp`, `sauna` | water-side and other leisure | overlay |
| `leisure=adult_gaming_centre`, `amusement_arcade`, `bowling_alley`, `dance`, `escape_game`, `hackerspace`, `tanning_salon` | indoor leisure | ignore |

`garden:type=*` (https://wiki.openstreetmap.org/wiki/Key:garden:type): `residential`, `private`, `community`, `botanical`, `landscaping`, `roof_garden` ("a garden on the roof of a building"), `school`, `green_wall` ("a vertical garden"), `rock_garden`, `show_garden`, `street_side` ("road verge with garden plants"), `arboretum`; `castle`, `monastery` (unclear). `garden:style=*` examples named on the leisure=garden page: `kitchen`, `rosarium`, `french`, `english` (full list only in taginfo, not verified).

`leisure=pitch` page (https://wiki.openstreetmap.org/wiki/Tag:leisure%3Dpitch): `sport=` soccer, basketball, tennis, baseball, cricket, rugby_union, american_football, field_hockey, handball, volleyball, badminton, ice_hockey, table_tennis, equestrian, skateboard, chess, multi; `surface=` artificial_turf, paved, acrylic, sand, concrete, carpet, paving_stones, clay, grass.

### 1.6 `landcover=*`: https://wiki.openstreetmap.org/wiki/Key:landcover

Status on the wiki: **"in use"** (not approved; many values flagged "not yet rendered"; the page advises double-tagging trees with `landuse=forest`/`natural=wood` and grass with `natural=grassland`). OSM Carto does not render the key. Usage (taginfo API `key/values?key=landcover`, data 2026-09-29, 248 distinct values): `trees` 292,418 · `mostly_rock` 78,708 · `grass` 69,156 · `scrub` 11,940 · `dry_swamp` 4,353 · `mostly_scree` 4,149 · `fell` 4,079 · `bare_ground` 3,688 · `greenery` 1,345 · `shrubbery` 1,209 · `water` 983 · `grassland` 896 · `gravel` 791 · `sand` 754 · `barren` 657 · `meadow` 584 · `reindeer_lichen` 463 · `bushes` 398 · `flowerbed` 339 · `concrete` 338 · `artificial_turf` 322 · `ground` 282 · `asphalt` 277 · `dirt` 274 · `forest` 200 · `heath` 170 · `hedge` 152 · `flowers` 110 · `woodchips` 108. Values documented on the wiki page: trees, grass, water, gravel, sand ("very rarely used"), hedge, greenery, mostly_rock, scrub, dry_swamp, fell, bare_ground, shrubbery, flowerbed. **Conclusion:** support `landcover=trees|grass|scrub|shrubbery|greenery|flowerbed|gravel|sand|bare_ground|water` as low-priority aliases; do not rely on the key.

### 1.7 `surface=*`: https://wiki.openstreetmap.org/wiki/Key:surface (all documented values) + taginfo counts

Counts: taginfo API `key/values?key=surface`, data 2026-09-29 (8,539 distinct values in the database; only the documented ones and the most used undocumented ones matter).

| Value | Wiki meaning | Uses | Group on wiki |
|---|---|---|---|
| `paved` | Predominantly paved: covered with paving stones, concrete or bitumen (generic) | 4,527,232 | paved |
| `asphalt` | Mineral aggregate bound by asphalt (asphalt concrete) | 37,747,007 | paved |
| `chipseal` | Thin bitumen base with aggregate pushed into it | 10,331 | paved |
| `concrete` | Portland cement concrete, typically cast in place with joints | 5,625,434 | paved |
| `concrete:lanes` | Long narrow concrete elements for two-tracked vehicles, other material between lanes | 37,867 | paved |
| `concrete:plates` | Large prefabricated concrete plates placed closely together | 233,745 | paved |
| `paving_stones` | Artificial blocks (block pavers, bricks) or natural stones (flagstones) with flat top forming an even, closed surface | 5,240,908 | paved |
| `paving_stones:lanes` | Lanes of paving stones for two-tracked vehicles | 1,120 | paved |
| `grass_paver` | Permeable paving with regular cell structure (grass grows through) | 64,875 | paved |
| `sett` | Natural stones cut with roughly flat top; do not cover the surface completely | 658,950 | paved |
| `unhewn_cobblestone` | Raw cobblestone of natural, uncut, rounded stones | 59,055 | paved |
| `cobblestone` | Unclear value; use `sett` or `unhewn_cobblestone` instead | 136,009 | paved |
| `bricks` | Surface paved with clay bricks | 9,745 (+ `brick` 8,276 undocumented spelling) | paved |
| `metal` | Metal-surfaced bridges or temporary tracks | 60,860 | paved |
| `metal_grid` | Metal grids (industrial-style bridges), slippery when wet | 5,746 | paved |
| `wood` | Wood surfaced bridges, plank walkways, garden decking | 298,021 | paved |
| `stepping_stones` | Stones or plates individually arranged in rows, surrounded by an unpaved medium | 4,017 | paved |
| `tiles` | Ceramic tiles (mostly indoor corridors) | 5,647 | paved |
| `fibre_reinforced_polymer_grate` | FRP grate on outdoor walkways | not in top 70 | paved |
| `resin_bound` | Pebbles/gravel coated in UV-resistant resin; water permeable, pedestrian use | not in top 70 | paved |
| `unpaved` | Predominantly unsealed: loose covering from compacted stone chippings to soil (generic) | 13,297,507 | unpaved |
| `compacted` | Mixture of larger and smaller parts compacted to a stable surface; water-bound macadam | 1,531,134 | unpaved |
| `fine_gravel` | Used inconsistently: fine loose gravel or alias of compacted | 584,436 | unpaved |
| `gravel` | Very broad: from track ballast to small gravel pieces | 2,461,877 | unpaved |
| `shells` | Crushed or whole seashells (footways in the Netherlands) | 1,283 | unpaved |
| `rock` | Big pieces of rock or exposed bare rock | 36,243 | unpaved |
| `pebblestone` | Loosely arranged rounded stones, typically 2–8 cm | 160,036 | unpaved |
| `ground` | "No special surface; the ground itself has marks of human or animal usage." | 3,852,714 | unpaved |
| `dirt` | Exposed soil (not sand, gravel or rock) | 2,035,293 | unpaved |
| `earth` | Same as dirt; use `dirt` instead | 155,678 | unpaved |
| `mud` | Like ground but wet most of the year | 34,843 | unpaved |
| `laterite` | Red-orange tropical soil | 2,667 | unpaved |
| `grass` | Grass covered ground | 1,640,757 | unpaved |
| `sand` | Small fractions (< 2 mm) of rock | 693,800 | unpaved |
| `woodchips` | Woodchips on playgrounds or walking trails | 19,108 | unpaved |
| `snow`, `ice`, `salt` | winter roads of compacted snow · ice roads · dry salt lakes | `ice` 2,933; others not in top 70 | unpaved |
| `clay` | Tennis courts mostly; also soccer, athletics, boules | 44,248 | sports |
| `tartan` | Synthetic all-weather surface for running/sport tracks | 49,339 | sports |
| `artificial_turf` | Synthetic fibres resembling natural grass | 57,770 | sports |
| `acrylic` | Acrylic resin-bound coating (tennis/basketball courts) | 11,025 | sports |
| `carpet` | Carpet (indoor tennis, some corridors) | not in top 70 | sports |
| `plastic` | Plastic surface for pitches and playgrounds | 6,813 | sports |
| `rubber` | Recycled rubber tyre products, playground safety surfacing | 11,406 | sports |

Frequent **undocumented** values worth aliasing (taginfo, same call): `stone` 16,940 · `dirt/sand` 8,944 · `soil` 7,194 · `trail` 5,505 · `cobblestone:flattened` 4,406 · `cement` 2,684 · `hard` 2,276 · `rocky` 1,528 · `bitmac` 1,353 · `bare_rock` 1,238 · `scrub` 1,166 · `interlock` 1,135 · `rocks` 1,109 · `brick_weave` 873 · `steel` 871 · `mulch` 862 · `concrete:tiles` 844 · `rubbercrumb` 735 · `moss` 729 · `bare_ground` 669 · `boardwalk` 660 · `turf` 646 · `natural` 646 · `decoturf` 612 · `mixed` 599 · `flagstone` 585; semicolon lists such as `ground;grass` 907 exist and must be split.

Detail keys for paving (https://wiki.openstreetmap.org/wiki/Tag:surface%3Dpaving_stones, V): `paving_stones:shape` = `square`, `rectangle`, `hexagon`, `zigzag`, `double_t`, `squarish_octagon`, `s-shape`, `irregular` · `paving_stones:pattern` = `stack_bond`, `half_bond`, `quarter_bond`, `herringbone`, `basket_weave`, `tudor`, `linen`, `interleaved`, `random_course` · `paving_stones:direction` (angle), `paving_stones:orientation` (angle, `along`, `across`) · `paving_stones:length`, `paving_stones:width` · `paving_stones:material` (stone, concrete, brick …) · `surface:colour`. Related keys on Key:surface: `smoothness`, `tracktype`, `sidewalk:surface`, `cycleway:surface`, `crossing:surface`.

### 1.8 `barrier=*`: https://wiki.openstreetmap.org/wiki/Key:barrier

| Tag | Wiki meaning | Note |
|---|---|---|
| `barrier=hedge` | "A line of closely spaced shrubs and tree species, which form a barrier or mark the boundary of an area." Map as a line; avoid `area=yes` (ambiguous); for wide/areal hedges use `natural=shrubbery`. Sub-tags `width`, `height`, `genus`, `species`, `leaf_type`, `leaf_cycle`, `taxon`. (https://wiki.openstreetmap.org/wiki/Tag:barrier%3Dhedge) | → hedge line symbol (missing in 16-class sheet) |
| `barrier=fence` | Structure supported by posts | line symbol |
| `barrier=wall` | Free-standing solid structure | line symbol |
| `barrier=retaining_wall` | Retains the lateral pressure of soil | line symbol (one-sided) |
| `barrier=city_wall` | Fortification | line symbol |
| `barrier=kerb` | Short solid barrier at road/path edges; describe with `kerb=flush` (~0 cm), `lowered` (≲3 cm), `raised` (>3 cm), `rolled`, `no`, `yes`; `kerb:height` (https://wiki.openstreetmap.org/wiki/Key:kerb) | edge line |
| `barrier=guard_rail`, `handrail`, `cable_barrier`, `jersey_barrier`, `chain`, `rope`, `bar`, `barrier_board`, `log`, `tyres`, `tank_trap`, `delineator_kerb`, `armadillo` | other linear barriers | line symbols |
| `barrier=ditch` | Trench, ditch or ravine not easily crossed | line symbol |
| `barrier=planter` | Plant box preventing large vehicles from passing | point symbol (planter) |
| `barrier=bollard`, `block`, `gate`, `lift_gate`, `swing_gate`, `sliding_gate`, `wicket_gate`, `kissing_gate`, `hampshire_gate`, `stile`, `horse_stile`, `turnstile`, `full-height_turnstile`, `cycle_barrier`, `motorcycle_barrier`, `cattle_grid`, `entrance`, `height_restrictor`, `kent_carriage_gap`, `toll_booth`, `border_control`, `bump_gate`, `bus_trap`, `coupure`, `debris`, `floating_boom`, `sally_port`, `sliding_beam`, `spikes`, `sump_buster`, `wedge` | access-control node barriers | point symbols (only bollard/gate/planter relevant) |

### 1.9 `waterway=*`: https://wiki.openstreetmap.org/wiki/Key:waterway

`river` (wide natural watercourse) · `stream` (too narrow to be a river) · `tidal_channel` · `flowline` · `canal` (artificial open waterway for transport, power, irrigation) · `drain` (artificial, carries superfluous water e.g. storm water) · `ditch` (small artificial waterway for drainage/irrigation) · `pressurised` · `link` · `fairway` · `fish_pass` · `canoe_pass` · `dock` · `boatyard` · `dam` · `weir` · `waterfall` · `rapids` · `lock_gate` · `sluice_gate` · `floodgate` · `debris_screen` · `security_lock` · `check_dam` · `turning_point` · `water_point` · `fuel`.

### 1.10 `man_made=*` (selection): https://wiki.openstreetmap.org/wiki/Key:man_made

`embankment` ("an artificial steep slope") · `dyke` (embankment restricting water) · `pier` ("raised walkway over water, supported by widely spread piles or pillars") · `quay` · `bridge` ("the outline of a bridge") · `breakwater` · `groyne` · `courtyard` ("area usually enclosed by walls or buildings") · `planter` ("a structure for planting flowers or other ornamental plants") · `cutline` · `clearcut` · `heap` · `spoil_heap` · `flagpole` · `street_cabinet` · `manhole` · `utility_pole` · `mast` · `tower` · `chimney` · `surveillance` · `water_tap` · `water_well` · `trough` · `insect_hotel` ("a structure intended to provide shelter for insects") · `nesting_site` · `beehive` · `wildlife_crossing` · `reservoir_covered` · `storage_tank` · `silo` · `pipeline` · `wastewater_plant` · `water_works` · `works`.

### 1.11 `amenity=*` (street furniture / open space): https://wiki.openstreetmap.org/wiki/Key:amenity

`bench` · `lounger` · `drinking_water` · `water_point` · `watering_place` · `fountain` ("for cultural/decorational/recreational purposes") · `toilets` · `shower` · `waste_basket` · `waste_disposal` · `recycling` · `grit_bin` · `parking` · `parking_space` · `parking_entrance` · `bicycle_parking` · `bicycle_rental` · `motorcycle_parking` · `charging_station` · `compressed_air` · `marketplace` · `public_bookcase` · `bbq` · `dog_toilet` · `kneipp_water_cure` · `give_box` · `shelter` · `clock` · `telephone` · `post_box` · `hunting_stand` · `grave_yard` ("smaller place of burial, often near a church"). Not amenity: street lamps are `highway=street_lamp`; picnic tables are `leisure=picnic_table`. `amenity=vending_machine`: **R** (not returned by the extraction).

### 1.12 `highway=*`: https://wiki.openstreetmap.org/wiki/Key:highway

| Group | Values |
|---|---|
| Roads | `motorway`, `trunk`, `primary`, `secondary`, `tertiary`, `unclassified`, `residential` (+ `*_link`) |
| Special | `living_street` (pedestrians have legal priority), `service` (access roads, car parks, alleys), `pedestrian` (mainly/exclusively pedestrians), `track` (agricultural/forestry), `bus_guideway`, `busway`, `escape`, `raceway`, `road` (unknown) |
| Paths | `footway` (designated footpaths; `footway=sidewalk`, `footway=crossing`), `path` (non-specific), `cycleway`, `bridleway`, `steps`, `corridor`, `via_ferrata` |
| Lifecycle | `proposed`, `construction` |
| Points/areas | `bus_stop`, `crossing`, `elevator`, `street_lamp`, `platform`, `rest_area`, `services`, `traffic_signals`, `turning_circle` |

Line features carry the material in `surface=*` (1.7); polygons of pedestrian areas are `highway=pedestrian` + `area=yes`. (`area:highway=*` for carriageway polygons: **R**.)

### 1.13 `building=*`: https://wiki.openstreetmap.org/wiki/Key:building

Accommodation: `apartments`, `barracks`, `bungalow`, `cabin`, `detached`, `annexe`, `dormitory`, `farm`, `ger`, `hotel`, `house`, `houseboat`, `residential`, `semidetached_house`, `static_caravan`, `stilt_house`, `terrace`, `tree_house`, `trullo` · Commercial: `commercial`, `industrial`, `kiosk`, `office`, `retail`, `supermarket`, `warehouse` · Religious: `religious`, `cathedral`, `chapel`, `church`, `kingdom_hall`, `monastery`, `mosque`, `presbytery`, `shrine`, `synagogue`, `temple` · Civic: `bakehouse`, `bridge`, `civic`, `clock_tower`, `college`, `fire_station`, `government`, `gatehouse`, `hospital`, `kindergarten`, `museum`, `public`, `school`, `toilets`, `train_station`, `transportation`, `university` · Agricultural: `barn`, `conservatory`, `cowshed`, `farm_auxiliary`, `greenhouse`, `slurry_tank`, `stable`, `sty`, `livestock` · Sports: `grandstand`, `pavilion`, `riding_hall`, `sports_hall`, `sports_centre`, `stadium` · Storage: `allotment_house`, `boathouse`, `hangar`, `hut`, `shed` · Cars: `carport`, `garage`, `garages`, `parking` · Technical: `digester`, `service`, `tech_cab`, `transformer_tower`, `water_tower`, `storage_tank`, `silo` · Other: `beach_hut`, `bunker`, `castle`, `construction`, `container`, `guardhouse`, `military`, `outbuilding`, `pagoda`, `quonset_hut`, `roof` (roof with open sides), `ruins`, `ship`, `tent`, `tower`, `triumphal_arch`, `windmill`, `yes`. For the catalog three renderings suffice: building (generic), glasshouse (`greenhouse`, `conservatory`), open roof/shelter (`roof`, `carport`).

### 1.14 Roofs and green roofs

| Tag | Wiki statement | St. | Source |
|---|---|---|---|
| `roof:material=*` | `roof_tiles`, `metal`, `concrete`, `tar_paper`, `asbestos`, `eternit`, `glass`, `acrylic_glass`, `metal_sheet`, `slate`, `tin`, `grass`, `copper`, `thatch`, `gravel`, `stone`, `wood`, `plastic`, `asphalt`, `asphalt_shingle`, `zinc`, `sandstone`, `bamboo`, `palm_leaves`, `banana_leaves`, `solar_panels` | V | https://wiki.openstreetmap.org/wiki/Key:roof:material |
| `roof:material=grass` | "Roof covered with living grass (or similar plants), sealed below" | V | same |
| `green_roof=yes/no` | Key status "in use". "Various types of green roofs may be seen as `roof:material=grass`, `roof:material=plants`, `roof:material=gravel` (sedum roofs) or `roof:material=roof_greening`, but with the exception of the latter tag these may also refer to other kinds of roofs." "`green_roof=*` is a simple way to provide basic information without having to make some arbitrary choices of roof material." No extensive/intensive values documented. | V | https://wiki.openstreetmap.org/wiki/Key:green_roof |
| `garden:type=roof_garden`, `garden:type=green_wall` | roof garden / vertical garden as `leisure=garden` sub-types | V | 1.5 |

Rule for the library: green roof if `green_roof=yes` OR `roof:material ∈ {grass, plants, roof_greening}` OR `leisure=garden`+`garden:type=roof_garden`; `roof:material=gravel` alone is *not* sufficient.

### 1.15 Tree attributes: https://wiki.openstreetmap.org/wiki/Tag:natural%3Dtree (+ key pages)

| Key | Wiki definition / values | St. |
|---|---|---|
| `leaf_type` | `broadleaved`, `needleleaved`, `mixed`, `leafless`; `palm` widely used but called botanically incorrect (use `taxon:family=Arecaceae`); `leaf_type=deciduous` is a tagging mistake (https://wiki.openstreetmap.org/wiki/Key:leaf_type) | V |
| `leaf_cycle` | `evergreen`, `deciduous`, `semi_evergreen`, `semi_deciduous`, `mixed` (https://wiki.openstreetmap.org/wiki/Key:leaf_cycle) | V |
| `species`, `genus`, `taxon`, `species:wikidata` | scientific names (Latin binomial / genus / any taxonomic level incl. cultivar / Wikidata QID); localized `species:de` etc. | V |
| `height` | tree height, metres if no unit | V |
| `circumference` | "For the circumference of the trunk (measured in a height of 1.3 metre above ground). If no unit is given metres are assumed." | V |
| `diameter` | trunk diameter at breast height (1.3 m); **millimetres** assumed if no unit; less popular than circumference | V |
| `diameter_crown` | "For the diameter of the crown of foliage of the tree … If no unit is given metres are assumed." | V |
| `denotation` | `landmark`, `natural_monument`, `agricultural`, `park`, `garden`, `avenue`, `urban`, `windbreak`; `cluster` deprecated/removed 2015 (https://wiki.openstreetmap.org/wiki/Key:denotation) | V |
| `protected`, `planted_date` / `start_date`, `name`, `ref`, `wikidata` | preservation order yes/no, planting date, identifiers | V |

Library use: crown symbol radius = `diameter_crown`/2; fallback from `circumference` (DBH = circumference/π) via an allometric default; symbol variant from `leaf_type`; seasonal variant from `leaf_cycle`.

### 1.16 Usage counts for prioritising the crosswalk (V, taginfo API `key/values`, data until 2026-09-30T00:59Z)

- `landuse=*`: farmland 11,746,878 · residential 10,726,843 · **grass 7,655,761** · forest 5,944,202 · meadow 5,578,523 · orchard 1,878,542 · farmyard 1,636,446 · industrial 1,446,572 · vineyard 875,545 · cemetery 602,364 · commercial 599,906 · allotments 491,110 · retail 419,892 · basin 276,173 · construction 274,610 · quarry 254,030 · recreation_ground 196,808 · reservoir 187,482 · religious 161,987 · brownfield 160,466 · **flowerbed 159,370** · greenhouse_horticulture 122,301 · aquaculture 102,489 · railway 99,992 · garages 98,303 · military 96,518 · greenfield 93,858 · village_green 91,553 · plant_nursery 78,722 · logging 76,621 · landfill 58,604 · education 44,512 · highway 30,456 · salt_pond 21,400 · **greenery 13,697** · animal_keeping 11,222 · undocumented but present: plantation 6,342, traffic_island 4,039.
- `natural=*`: **tree 34,278,415** · water 23,441,655 · wood 12,782,812 · scrub 5,740,277 · wetland 4,665,794 · grassland 2,410,258 · **tree_row 2,116,647** · bare_rock 1,330,917 · cliff 1,044,079 · heath 679,115 · sand 599,320 · scree 399,233 · **shrub 306,892** · spring 284,119 · beach 249,893 · rock 249,549 · glacier 117,838 · **shrubbery 102,705** · stone 93,485 · shingle 88,111 · fell 28,585 · mud 28,526 · earth_bank 23,178 · tree_group 18,028 (undocumented on the key page) · tree_stump 13,401.
- Reading: single trees are by far the most mapped landscape object; `landuse=grass` outnumbers `landuse=meadow`; planted-shrub and flower-bed tags are already six-figure; `landuse=greenery` and `landcover=*` are marginal.

---

## 2. OSM Carto default colours (v6.1.0 master, fetched 2026-09-30)

Files: `style/landcover.mss`, `style/style.mss`, `style/water.mss`, `style/water-features.mss`, `style/buildings.mss`, `style/roads.mss`, `style/road-colors-generated.mss`, `style/amenity-points.mss`, `style/golf.mss` under https://github.com/openstreetmap-carto/openstreetmap-carto/tree/master/style (raw: `https://raw.githubusercontent.com/gravitystorm/openstreetmap-carto/master/style/<file>`). All rows **V**; the Lch comments are in the source file and document the design intent.

### 2.1 Land-cover and land-use fills (`landcover.mss`, `style.mss`)

| Variable | Hex | Source comment | Applied to (feature selectors in the file) |
|---|---|---|---|
| `@land-color` | `#f2efe9` | map background | everything unmapped |
| `@water-color` | `#aad3df` | | water areas, `leisure=swimming_pool` (z17 outline `saturate(darken(@water-color,20%),20%)`), `landuse=salt_pond` |
| `@grass` | `#cdebb0` | Lch(90,32,128) "also grassland, meadow, village_green, garden, allotments" | `landuse=grass`, `landuse=meadow`, `natural=grassland`, `landuse=village_green`, base of `leisure=garden` and `landuse=flowerbed`, base of wetland reedbed/marsh/wet_meadow/fen/saltmarsh, golf tee/fairway/rough/driving_range, `#landcover-line` |
| `@scrub` | `#c8d7ab` | Lch(84,24,122) | `natural=scrub` (+ `symbols/scrub.png`), base of `wetland=mangrove` |
| `@forest` | `#add19e` | Lch(80,30,135) | `landuse=forest`, `natural=wood` (+ leaf-type symbols), base of `wetland=swamp`; `@hedge: @forest` |
| `@forest-text` | `#46673b` | Lch(40,30,135) | labels |
| `@park` | `#c8facc` | Lch(94,30,145) | `leisure=park` |
| `@leisure` | `lighten(@park, 5%)` ≈ `#dffce2` (D) | | `landuse=recreation_ground`, `leisure=playground`, `leisure=fitness_station`, `leisure=dog_park`; `@stadium: @leisure` (sports_centre, stadium, water_park) |
| `@allotments` | `#c9e1bf` | Lch(87,20,135) | `landuse=allotments` (+ `patterns/allotments.svg`) |
| `@orchard` | `#aedfa3` | "also vineyard, plant_nursery" | `landuse=orchard`, `landuse=vineyard`, `landuse=plant_nursery` (each with pattern) |
| `@farmland` / `-line` | `#eef0d5` / `#c7c9ae` | Lch(94,14,112) / Lch(80,14,112) | `landuse=farmland`, `landuse=greenhouse_horticulture` |
| `@farmyard` / `-line` | `#f5dcba` / `#d1b48c` | Lch(89,20,80) / Lch(75,25,80) | `landuse=farmyard` |
| `@heath` | `#d6d99f` | | `natural=heath`, base of `wetland=bog`/`string_bog` |
| `@sand` | `#f5e9c6` | | `natural=sand`, golf bunker |
| `@beach` | `#fff1ba` | | `natural=beach`, `natural=shoal` (+ `beach.png` / `beach_coarse.png`) |
| `@bare_ground` | `#eee5dc` | | `natural=bare_rock` (+ `rock_overlay.png`), `natural=scree`, `natural=shingle` (+ `scree_overlay.png`) |
| `@mud` | `rgba(203,177,154,0.3)` | "produces #e6dcd1 over @land" | `natural=mud`, `wetland=tidalflat` |
| `@pitch` | `#88e0be` | Lch(83,35,166) "also track" | `leisure=pitch`, `leisure=track` (z15 outline `desaturate(darken(@pitch,20%),10%)`), golf green |
| `@campsite` | `#def6c0` | "also caravan_site, picnic_site" | camp/caravan/picnic sites; `@golf_course: @campsite` |
| `@cemetery` | `#aacbaf` | "also grave_yard" | `landuse=cemetery`, `amenity=grave_yard` (+ religion patterns) |
| `@construction` | `#c7c7b4` | "also brownfield" | `landuse=construction`, `landuse=brownfield` |
| (literal) | `#b6b592` | | `landuse=landfill` |
| `@quarry` | `#c5c3c3` | | `landuse=quarry` (+ `symbols/quarry.svg`) |
| `@residential` / `-line` | `#e0dfdf` / `#b9b9b9` | Lch(89,0,0) / Lch(75,0,0) | `landuse=residential` (z13+); lower zooms `@built-up-lowzoom #d0d0d0`, `@built-up-z12 #dddddd` |
| `@retail` / `-line` | `#ffd6d1` / `#d99c95` | Lch(89,16,30) | retail, mall, marketplace |
| `@commercial` / `-line` | `#f2dad9` / `#d1b2b0` | Lch(89,8.5,25) | commercial |
| `@industrial` / `-line` | `#ebdbe8` / `#c6b3c3` | Lch(89,9,330) "also railway, wastewater_plant" | industrial, `landuse=railway`, works |
| `@societal_amenities` | `#ffffe5` | Lch(99,13,109) | hospital, clinic, university, college, school, kindergarten, community_centre, social_facility, arts_centre |
| `@place_of_worship` | `#d0d0d0` | "also landuse_religious" | |
| `@parking` | `#eeeeee` | outline `saturate(darken(@parking,40%),20%)` | `amenity=parking`, bicycle/motorcycle parking, taxi |
| `@garages` | `#dfddce` | | `landuse=garages` |
| `@transportation-area` | `#e9e7e2` | | aerodrome, ferry terminal, bus station |
| `@apron` | `#dadae0` | | `aeroway=apron` |
| `@rest_area` | `#efc8c8` | "also services" | |
| (literal) | `#F3E3DD` | | fire station, police |
| `@military` | `#f55` | | hatch |
| `@tourism` | `#660033` | | outline/labels |
| `@glacier` / `-line` | `#ddecec` / `#9cf` | (`water.mss`) | glacier, `leisure=ice_rink` |
| `@water-text` | `#4d80b3` | (`water.mss`) | water labels |

**Complete list of area/line features styled in `landcover.mss`** (V, second targeted read of the file): leisure_swimming_pool, landuse_recreation_ground, leisure_playground, leisure_fitness_station, tourism_camp_site, tourism_caravan_site, tourism_picnic_site, landuse_quarry, landuse_vineyard, landuse_orchard, leisure_garden, landuse_flowerbed, landuse_plant_nursery, landuse_cemetery, amenity_grave_yard, amenity_place_of_worship, landuse_religious, amenity_prison, landuse_residential, landuse_garages, leisure_park, leisure_ice_rink, leisure_dog_park, leisure_golf_course, leisure_miniature_golf, landuse_allotments, landuse_forest, natural_wood, landuse_farmyard, landuse_farmland, landuse_greenhouse_horticulture, natural_grassland, landuse_meadow, landuse_grass, landuse_village_green, landuse_retail, shop_mall, amenity_marketplace, landuse_industrial, man_made_works, man_made_wastewater_plant, man_made_water_works, landuse_railway, power_plant, power_generator, power_substation, landuse_commercial, landuse_brownfield, landuse_construction, landuse_landfill, landuse_salt_pond, natural_bare_rock, natural_scree, natural_shingle, natural_sand, natural_heath, natural_scrub, wetland_swamp, wetland_mangrove, wetland_reedbed, wetland_bog, wetland_string_bog, wetland_wet_meadow, wetland_fen, wetland_saltmarsh, wetland_marsh, amenity_hospital, amenity_clinic, amenity_university, amenity_college, amenity_school, amenity_kindergarten, amenity_community_centre, amenity_social_facility, amenity_arts_centre, amenity_fire_station, amenity_police, amenity_parking, amenity_bicycle_parking, amenity_motorcycle_parking, amenity_taxi, amenity_parking_space, aeroway_apron, aeroway_aerodrome, amenity_ferry_terminal, amenity_bus_station, natural_beach, natural_shoal, highway_services, highway_rest_area, railway_station, leisure_sports_centre, leisure_water_park, leisure_stadium, leisure_track, leisure_pitch, historic_citywalls, barrier_city_wall, barrier_hedge, natural_arete, natural_cliff, natural_ridge, man_made_embankment (plus `natural=mud` and the `wetland=*` patterns in the area-symbol layer).

**Not styled in `landcover.mss`** (V: the strings do not occur in the file): `natural=shrubbery`, `landuse=greenery`, any `landcover=*`; also absent from the list above: `landuse=greenfield`, `logging`, `education`, `animal_keeping`, `aquaculture`, `natural=fell/moor/tundra/dune`, `leisure=common`, and `surface=*` on areas. The default OSM map therefore shows nothing for planted shrub beds and generic greenery, a gap the library can fill.

### 2.2 Pattern and symbol images used for land cover

| Pattern file | Used for |
|---|---|
| `symbols/wetland.png` (generic), `wetland_marsh.png`, `wetland_reed.png`, `wetland_swamp.png`, `wetland_bog.png`, `wetland_mangrove.png`, `salt-dots-2.png` | wetlands by `wetland=*`, composited over the base fill with `polygon-pattern-alignment: global` from z10 |
| `symbols/scrub.png` | `natural=scrub` |
| `symbols/leaftype_broadleaved.svg`, `leaftype_needleleaved.svg`, `leaftype_mixed.svg`, `leaftype_leafless.svg`, `leaftype_unknown.svg` | `natural=wood` / `landuse=forest` by `leaf_type` |
| `patterns/orchard.svg`, `patterns/vineyard.svg`, `patterns/plant_nursery.svg` | orchard · vineyard · plant_nursery **and** `leisure=garden` (z13+, opacity 0.6 over `@grass`) |
| `symbols/flowerbed_mid_zoom.svg` (z15+), `flowerbed_high_zoom.svg` (z17+) | `landuse=flowerbed` over `@grass` |
| `patterns/allotments.svg` | `landuse=allotments` |
| `patterns/grave_yard_christian.svg`, `_jewish`, `_muslim`, `_generic` | cemeteries by `religion` |
| `patterns/dog_park.svg` | `leisure=dog_park` |
| `symbols/beach.png`, `beach_coarse.png` | beach/shoal by `surface` |
| `symbols/rock_overlay.png`, `scree_overlay.png` | bare_rock · scree/shingle |
| `symbols/reef.png`, `salt_pond.png`, `patterns/intermittent_water.svg` | reef · salt pond · intermittent water |
| `symbols/quarry.svg`, `symbols/golf_rough.svg`, `patterns/grey_vertical_hatch.svg`, `military_red_hatch.svg`, `danger_red_hatch.svg` | quarry · golf rough · prison · military |
| `symbols/cliff.svg`, `cliff2.svg`, `ridge-mid.svg`, `ridge2.svg`, `arete-mid.svg`, `arete2.svg`, `embankment.svg` | line patterns for cliff, ridge, arete, `man_made=embankment` |

Complete listing of `patterns/` (13 files, V): allotments, danger_red_hatch, dog_park, grave_yard_christian/generic/jewish/muslim, grey_vertical_hatch, intermittent_water, military_red_hatch, orchard, plant_nursery, vineyard.

### 2.3 Trees, hedges, buildings, paths

| Feature | Rendering | File |
|---|---|---|
| `natural=tree` | from z16: canopy marker `darken(@forest,10%)` (≈ `#90c17b`, D), opacity 0.6, diameter 2.5 px (z16) / 5 (z17) / 10 (z18) / 15 (z19) / 30 (z20); trunk marker `#6b8d5e`, opacity 0.4, 2 px (z18) / 3 (z19) / 6 (z20). Crown size is **not** data-driven. | `amenity-points.mss` |
| `natural=tree_row` | line `darken(@forest,10%)`, round caps, opacity 0.6, width 2.5 / 5 / 10 / 15 / 30 px (z16–z20) | same |
| `barrier=hedge` | line `@hedge` (= `@forest` `#add19e`), width 1.5 (z16) / 2 / 3 / 4 / 5 px (z20) | `landcover.mss` |
| Buildings | `@building-fill #d9d0c9`; `@building-line: darken(@building-fill,15%)` (≈ `#b9a99c`, D); major buildings `darken(@building-fill,10%)` (≈ `#c4b6ab`, D); bridges `#B8B8B8` | `buildings.mss` |
| Pedestrian areas / minor roads | `@pedestrian-fill #dddde8` (casing `#999`), `@living-street-fill #ededed`, `@residential-fill #ffffff` (= service; casing `#bbb`), `@tertiary-fill #ffffff` (casing `#8f8f8f`), `@road-fill #ddd`, `@platform-fill #bbbbbb`, `@raceway-fill #ffc0cb`, `@aeroway-fill #bbc` | `roads.mss` |
| Paths (lines) | `@footway-fill salmon`, `@steps-fill` = footway, `@cycleway-fill blue`, `@bridleway-fill green`, `@track-fill #996600`; no-access variants `#bbbbbb`, `#9999ff`, `#aaddaa`, `#e2c5bb`; casings white | `roads.mss` |
| Major roads | motorway `#e892a2` (casing `#dc2a67`), trunk `#f9b29c` (`#c84e2f`), primary `#fcd6a4` (`#a06b00`), secondary `#f7fabf` (`#707d05`) | `road-colors-generated.mss` |
| Water structures | dam `#adadad` (line `#5e5e5e`), weir/lock gate/breakwater/groyne `#aaa`, pier = `@land-color` | `water-features.mss` |
| Point-symbol tints | `@amenity-brown #734a08`, `@man-made-icon #666666`, `@barrier-icon #3f3f3f`, `@transportation-icon #0092da`, `@leisure-green: darken(@park,60%)`, `@protected-area #008000`, `@landform-color #d08f55`, `@wetland-text: darken(#4aa5fa,25%)` | `amenity-points.mss` |

---

## 3. Netherlands: BGT / IMGeo (Basisregistratie Grootschalige Topografie)

Structure: the **BGT** part is mandatory and nationwide (scale ≈ 1:500–1:5,000); **IMGeo** adds optional "plus" attributes (`plus-fysiekVoorkomen`, `plus-type`, `plus-functie`) and optional object types (trees, hedges, street furniture). Terrain is partitioned without gaps into *wegdeel*, *ondersteunend wegdeel*, *begroeid terreindeel*, *onbegroeid terreindeel*, *waterdeel*, *ondersteunend waterdeel*, *pand* and others. Class lists below: IMGeo objectenhandboek (Geonovum), V.

### 3.1 Begroeid terreindeel: `fysiekVoorkomen`: https://geonovum.github.io/IMGeo-objectenhandboek/begroeidterreindeel

| BGT value | Definition (shortened) | IMGeo plus values |
|---|---|---|
| `loofbos` | trees forming a more or less closed stand, deciduous | `griend en hakhout` (coppice) |
| `gemengd bos` | closed stand of conifers and deciduous trees | – |
| `naaldbos` | closed stand of conifers | – |
| `heide` | predominantly heather vegetation | – |
| `struiken` | non-cultivated low woody plants branching near the root | – |
| `houtwal` | boundary strip of limited width planted with trees or shrubs | – |
| `duin` | sand hill formed by wind or water | `open duinvegetatie`, `gesloten duinvegetatie` |
| `grasland overig` | grass vegetation not in agricultural use | – |
| `grasland agrarisch` | cultivated grassland for livestock (pasture/hay) | – |
| `moeras` | marsh vegetation in shallow standing water | – |
| `rietland` | predominantly reed vegetation | – |
| `kwelder` | salt marsh outside the dykes | – |
| `fruitteelt` | fruit trees, vines or soft fruit | `laagstam boomgaarden`, `hoogstam boomgaarden`, `wijngaarden`, `klein fruit` |
| `boomteelt` | tree/ornamental nursery | – |
| `bouwland` | arable land in crop rotation | `akkerbouw`, `braakliggend`, `vollegrondsteelt`, `bollenteelt` |
| `groenvoorziening` | "terreindeel met aangelegde beplanting, meestal gras, heesters of struiken" (laid-out planting) | `bosplantsoen` (woodland-type planting of native woody species, ornamental value not the aim), `gras- en kruidachtigen` (low continuous herbaceous vegetation), `planten` (managed unspecified planting bed), `struikrozen` (shrub roses), `heesters` (ornamental shrubs), `bodembedekkers` (ground cover) |

Further attributes: `begroeid terreindeel op talud` (on slope), `kruinlijn` (crest line, when slope ≥ 1:4 and height difference > 1 m), `relatieve hoogteligging`. A `haag` value under groenvoorziening has been *requested* (Geonovum/IMGeo-dev issue #173, S) but hedges are currently the separate IMGeo object *VegetatieObject*.

### 3.2 Onbegroeid terreindeel: `fysiekVoorkomen`: https://geonovum.github.io/IMGeo-objectenhandboek/onbegroeidterreindeel

| BGT value | Definition (shortened) | IMGeo plus values |
|---|---|---|
| `erf` | yard belonging to a building, not surveyed in detail, **a mix of vegetation, paving and/or water** | – |
| `gesloten verharding` | paving not removable without destruction (bitumen, cement, plastic) | `asfalt`, `cementbeton`, `kunststof` (synthetic, "zoals kunstgras") |
| `open verharding` | paving of bonded elements of limited size (clinkers, tiles) | `betonstraatstenen`, `gebakken klinkers`, `tegels`, `sierbestrating`, `beton element` |
| `half verhard` | material bound by compaction, or loose material | `grasklinkers` (grass pavers), `schelpen` (shells), `puin` (rubble), `grind` (pebble gravel), `gravel` (**crushed brick**, "veel gebruikt bij tennis") |
| `onverhard` | no paving and no continuous vegetation, not sand | `boomschors` (bark mulch), `zand` |
| `zand` | largely covered with sand | `strand en strandwal`, `zandverstuiving` |

Translation trap: Dutch `gravel` = red crushed-brick court surface (OSM `surface=clay`); Dutch `grind` = English gravel.

### 3.3 Wegdeel and ondersteunend wegdeel: https://geonovum.github.io/IMGeo-objectenhandboek/wegdeel · …/ondersteunendwegdeel

| Attribute | Values |
|---|---|
| Wegdeel `functie` (BGT) | `OV-baan`, `overweg`, `spoorbaan`, `baan voor vliegverkeer`, `rijbaan: autosnelweg`, `rijbaan: autoweg`, `rijbaan: regionale weg`, `rijbaan: lokale weg`, `fietspad`, `voetpad`, `voetpad op trap`, `ruiterpad`, `parkeervlak`, `voetgangersgebied`, `inrit`, `woonerf` (IMGeo plus-functie: `verbindingsweg`, `calamiteitendoorsteek`, `verkeersdrempel`) |
| Wegdeel `fysiekVoorkomen` (BGT → IMGeo plus) | `gesloten verharding` → `asfalt`, `cementbeton` · `open verharding` → `betonstraatstenen`, `gebakken klinkers`, `tegels`, `sierbestrating`, `beton element` · `half verhard` → `grasklinkers`, `schelpen`, `puin`, `grind`, `gravel` · `onverhard` → `boomschors`, `zand` |
| Ondersteunend wegdeel `functie` | `verkeerseiland` (traffic island), `berm` (verge) |
| Ondersteunend wegdeel `fysiekVoorkomen` | the four paving classes above **plus** `groenvoorziening` (→ `bosplantsoen`, `gras- en kruidachtigen`, `planten`, `struikrozen`, `heesters`, `bodembedekkers`) |

### 3.4 Water and vegetation objects: …/waterdeel · …/ondersteunendwaterdeel · …/vegetatieobject

| Object | Values |
|---|---|
| Waterdeel `type` (→ IMGeo plus-type) | `zee` · `waterloop` → `rivier`, `kanaal`, `beek`, `gracht`, `sloot`, `bron` · `watervlakte` → `haven`, `meer, plas, ven, vijver` · `greppel, droge sloot` |
| Ondersteunend waterdeel `type` | `oever, slootkant` (bank strip incl. zone between high and low water) · `slik` (unvegetated mud flooded at nearly every high water) |
| VegetatieObject (IMGeo, optional) | `boom` ("een markante boom …", point) · `haag` (row-shaped planted boundary of very limited width; line or polygon) |

### 3.5 Official visualisation rules (colours)

Source documents: BGT\|IMGeo Visualisatieregels 2.3 (https://docs.geostandaarden.nl/bgt/visualisatie/) define **seven visualisations**: *standaard* (BGT as main theme, aligned with the BRT), *achtergrond* (background map), *icoon*, *lijngericht*, *omtrekgericht*, *pastel* (background for civil-engineering use), *plan*. The document itself contains no colour values; they are in the implementation files at https://github.com/Geonovum/IMGeo/tree/master/visualisatie/2.3 (Excel rule sheets, SLD files, SVG/PNG patterns, SVG/TTF symbols). Rules of the text (V): terreindelen are styled by `bgt-fysiekvoorkomen`, wegdelen by `bgt-functie`, waterdelen by `bgt-type`; every polygon also gets an outline in the fill colour "om te voorkomen, dat er dunne, witte lijnen tussen de objecten blijven"; roads are drawn twice (casing, then fill) so carriageway parts are not separated by hard lines; vegetation objects (trees, hedges) only in the standaardvisualisatie; drawing order: unclassified → water → onbegroeid → begroeid → tunnel/bridge → ondersteunend wegdeel → wegdeel → spoor → pand → other structures → scheiding → vegetatieobject → labels.

**(a) Standaardvisualisatie**: V, Geonovum SLD 2.3 (`…/implementatiebestanden (SLD)/standaardvisualisatie/sld-0010-begroeidterreindeel.xml`, `sld-0011-…`, `sld-0021-wegdeel.xml`, `sld-0022-…`, `sld-0030-waterdeel.xml`, `sld-0044-pand.xml`), cross-checked against PDOK's Mapbox-GL implementation `bgt_standaardvisualisatie` (https://api.pdok.nl/lv/bgt/ogc/v1/styles/bgt_standaardvisualisatie__webmercatorquad?f=mapbox), identical values.

| Object / value | Fill | Outline | Pattern |
|---|---|---|---|
| begroeid: `grasland agrarisch`, `grasland overig`, `duin`, `kwelder` | `#c9eb70` | same | – |
| begroeid: `groenvoorziening`, `houtwal` | `#8ca800` | same | – |
| begroeid: `loofbos`, `naaldbos`, `gemengd bos`, `struiken` | pattern | `#8ca800` | `loofbos.png`, `naaldbos.png`, `gemengdbos.png`, `struiken.png` (32 px tiles) |
| begroeid: `moeras`, `rietland` | pattern | `#c9eb70` | `moeras.png` (64 px), `rietland.png` (32 px) |
| begroeid: `bouwland` | `#ffffcc` | same | – |
| begroeid: `boomteelt`, `fruitteelt` | pattern | `#ffffcc` | `boomteelt.png`, `fruitteelt.png` |
| begroeid: `heide` | `#fcb3fb` | same | – |
| onbegroeid: `erf`, `gesloten verharding`, `open verharding`, `half verhard` | `#ffffff` | `#535353`, width 3 (drawn first) | – |
| onbegroeid: `onverhard` | `#f3f5f6` | same | – |
| onbegroeid: `zand` | `#ffff99` | same | – |
| any: `transitie` | `#f2f2f2` | `#535353`, width 2, dash 6 3 | – |
| wegdeel: `rijbaan lokale weg`, `fietspad`, `inrit`, `parkeervlak`, `ruiterpad`, `woonerf`, `baan voor vliegverkeer` | `#ffffff` | casing `#535353` width 2 | – |
| wegdeel: `voetpad`, `voetpad op trap`, `voetgangersgebied` | `#ff9999` | casing `#535353` | – |
| wegdeel: `rijbaan regionale weg` / `rijbaan autoweg` / `rijbaan autosnelweg` | `#ffaa00` / `#e60000` / `#996089` | casing `#535353` | – |
| wegdeel: `OV-baan` / `overweg`, `spoorbaan` | `#CCCCCC` / `#c0c0c0` | casing `#535353` | – |
| ondersteunend wegdeel: `berm`, `verkeerseiland` | `#ff9999` | same, width 2 | – |
| waterdeel: `waterloop` / `watervlakte` / `zee` | `#73e9ff` / `#bee8ff` / `#99CCFF` | same, width 2 | – |
| waterdeel: `greppel, droge sloot` | slash hatch, stroke `#73e9ff` | dashed (40 19) | PDOK implementation uses base fill `#c9eb70` |
| ondersteunend waterdeel: `oever, slootkant` / `slik` | `#C9EB70` / `#73e9ff` (PDOK Mapbox) | | – |
| pand (building) | `#cc0000` | `#D73939`, width 1 (≤ 1:1,000) / 0.5 (≤ 1:2,500) / 0.25 (smaller) | – |
| overig bouwwerk: `open loods`, `overkapping`, `opslagtank`, `lage trafo` / `bassin`, `bezinkbak` / `windturbine` / `bunker` | `#CC0000` / `#BEE8FF` / `#990000` / `#000000` (PDOK Mapbox) | | – |
| scheiding (lines): `hek`, `damwand` / `muur` / `geluidsscherm` | – | `#000000` / `#cc0000` / `#6600cc`, width 2 (PDOK Mapbox) | – |
| kunstwerkdeel `perron` | `#ff9999` | `#535353` | – |

**(b) Pastelvisualisatie**: V, Geonovum SLD 2.3 (`…/pastelvisualisatie/pastel-*.sld`; all rules `MaxScaleDenominator 5000`, i.e. large scale only). Key XML rules were re-read verbatim.

| Object / value | Fill | Outline |
|---|---|---|
| begroeid: `loofbos`, `naaldbos`, `gemengd bos`, `boomteelt`, `heide`, `houtwal`, `kwelder`, `moeras`, `rietland` | `#d4dfd5` | fill-coloured 0.25; separate line rule `#787878` |
| begroeid: `grasland agrarisch`, `grasland overig`, `bouwland`, `fruitteelt`, `struiken` | `#e1e7e3` | same |
| begroeid: `duin`; onbegroeid: `zand` | `#f6f3db` | `#787878` 0.25 for zand |
| begroeid: `groenvoorziening` | `#FFFFFF` (sic, verified in the XML) | `#FFFFFF` 0.25 |
| ondersteunend wegdeel: `groenvoorziening` | `#e1e7e3` | `#787878` 0.25 |
| onbegroeid: `erf`, `gesloten verharding`, `open verharding`, `half verhard`, `onverhard`; ondersteunend wegdeel paving classes | `#ffffff` | `#787878` 0.25 |
| wegdeel: carriageways (`rijbaan autosnelweg`, `autoweg`, `regionale weg`, `lokale weg`) | `#f5f5f5` | casing `#787878` width 2 |
| wegdeel: all other functions | `#ffffff` | casing `#787878` width 2 |
| wegdeel / ondersteunend wegdeel with `bgt-fysiekVoorkomen` = `open verharding` or `half verhard` | additional GraphicFill of small circle marks (stroke `#787878`, size 1.5) | – |
| waterdeel (all types) | `#d2dfe6` | fill-coloured 0.25; line rule `#787878` |
| pand | `#e8e8e4` | `#787878`, width 0.4 |

**(c) Achtergrondvisualisatie**: V: Geonovum SLD 2.3 (`…/achtergrondvisualisatie/achtergrond_landuse_polygon.sld`, `achtergrond_urban_polygon.sld`, `achtergrond_water_polygon.sld`; all rules have `MaxScaleDenominator 5000`) and PDOK's Mapbox implementation (https://api.pdok.nl/lv/bgt/ogc/v1/styles/bgt_achtergrondvisualisatie__webmercatorquad?f=mapbox) carry identical values for land use, buildings and water. Road rows below come from the PDOK style only.

| Group (layer id) | Members | Fill | Outline |
|---|---|---|---|
| Landuse-natural-high-vegetation | `loofbos`, `gemengd bos`, `naaldbos`, `boomteelt`, `bosplantsoen` | `#c3dbb6` | same |
| Landuse-natural-low-vegetation | `groenvoorziening`, `struiken`, `houtwal`, `grasland overig` | `#e1eddb` | same |
| Landuse-natural-heather | `heide` | `#e3dce7` | same |
| landuse-natural-sand | `duin`, `moeras`, `rietland`, `kwelder`, `zand` | `#fdf6bb` | same |
| Landuse-human-made | `onverhard`, `gesloten verharding`, `open verharding`, `half verhard`, `fruitteelt`, `bouwland`, `grasland agrarisch`, `transitie` | `#fefefe` | `#d1c1be` |
| Landuse-man-made-private | `erf` | `#f9f9e7` | `#d1c1be` |
| water / Water_edge | all water types / `oever, slootkant` | `#9BCBE9` / `#e1eddb` | same |
| Roads: main | `rijbaan regionale weg`, `autosnelweg`, `autoweg` | `#fdf6bb` | casing `#d1c1be` |
| Roads: other motorised + cycle | `fietspad`, `inrit`, `parkeervlak`, `rijbaan lokale weg`, `overweg`, `OV-baan`, `spoorbaan` | `#ffffff` | casing `#d1c1be` |
| Roads: non-motorised | `voetpad`, `ruiterpad`, `voetgangersgebied`, `voetpad op trap`, `woonerf` | `#fdeff8` | casing `#d1c1be` |
| Ondersteunend wegdeel | `verkeerseiland` / `groenvoorziening` / other | `#fdeff8` / `#e1eddb` / `#ffffff` | `#d1c1be` |
| pand | all | `#d3d3d3` | `#b4b4b4`, width 0.5 up to 1:2,500; between 1:2,500 and 1:5,000 casing `#b4b4b4` 0.75 under a fill with outline `#cccccc` |

Notes: `bosplantsoen` and `zand` are matched on `plus_fysiekvoorkomen`; all fills carry a 0.25 outline in the fill colour except the human-made and `erf` groups (outline `#d1c1be`). The grouping itself is the lesson: sixteen vegetation classes collapse to **high vegetation / low vegetation / heather / sand-and-wet / human-made** for background use.

---

## 4. Switzerland: amtliche Vermessung (AV), Bodenbedeckung

### 4.1 Land-cover categories: DM.01-AV-CH, domain `BBArt` (V, INTERLIS model file https://models.geo.admin.ch/V_D/DM.01-AV-CH_LV95_24d_ili1.ili)

| Group | Value | Gloss |
|---|---|---|
| – | `Gebaeude` | building |
| `befestigt` (sealed) | `Strasse_Weg` · `Trottoir` · `Verkehrsinsel` · `Bahn` · `Flugplatz` · `Wasserbecken` · `uebrige_befestigte` | road/path · pavement · traffic island · railway · airfield · water basin · other sealed |
| `humusiert` (humus-covered) | `Acker_Wiese_Weide` · `Intensivkultur.Reben` · `Intensivkultur.uebrige_Intensivkultur` · `Gartenanlage` · `Hoch_Flachmoor` · `uebrige_humusierte` | arable/meadow/pasture · vineyard · other intensive crops · garden · raised bog/fen (one value, not two) · other |
| `Gewaesser` | `stehendes` · `fliessendes` · `Schilfguertel` | standing · flowing · reed belt |
| `bestockt` (wooded) | `geschlossener_Wald` · `Wytweide.Wytweide_dicht` · `Wytweide.Wytweide_offen` · `uebrige_bestockte` | closed forest · wooded pasture dense/open · other wooded |
| `vegetationslos` | `Fels` · `Gletscher_Firn` · `Geroell_Sand` · `Abbau_Deponie` · `uebrige_vegetationslose` | rock · glacier/firn · scree/sand · extraction/landfill · other |

Single objects, domain `EOArt` (V, same file): `Mauer`, `unterirdisches_Gebaeude`, `uebriger_Gebaeudeteil`, `eingedoltes_oeffentliches_Gewaesser`, `wichtige_Treppe`, `Tunnel_Unterfuehrung_Galerie`, `Bruecke_Passerelle`, `Bahnsteig`, `Brunnen`, `Reservoir`, `Pfeiler`, `Unterstand`, `Silo_Turm_Gasometer`, `Hochkamin`, `Denkmal`, `Mast_Antenne`, `Aussichtsturm`, `Uferverbauung`, `Schwelle`, `Lawinenverbauung`, `massiver_Sockel`, `Ruine_archaeologisches_Objekt`, `Landungssteg`, `einzelner_Fels`, `schmale_bestockte_Flaeche`, `Rinnsal`, `schmaler_Weg`, `Hochspannungsfreileitung`, `Druckleitung`, `Bahngeleise`, `Luftseilbahn`, `Gondelbahn_Sesselbahn`, `Materialseilbahn`, `Skilift`, `Faehre`, `Grotte_Hoehleneingang`, `Achse`, `wichtiger_Einzelbaum`, `Bildstock_Kruzifix`, `Quelle`, `Bezugspunkt`, `weitere`.

DMAV Version 1.0 (successor model): value names seen in the 2024 drafting instruction are the same except `fliessendes_Gewaesser`, `stehendes_Gewaesser` (instead of `fliessendes`, `stehendes`) and an additional single object `Jauchengrube_Mistlege` (V-img). The DMAV INTERLIS files themselves could not be fetched (guessed URLs returned 404), see Open points.

### 4.2 Official colours in the three federal drafting instructions (all V-img)

Sources: **GB** = Weisung "Amtliche Vermessung – Darstellung des Planes für das Grundbuch", 9 Mar 2007, Stand 1 Feb 2014 (https://www.cadastre-manual.admin.ch/dam/de/sd-web/pysw2JgMIIer/Weisung-GB-de.pdf) · **BP09** = Weisung "Darstellung des Basisplans der amtlichen Vermessung «BP-AV»", 22 Apr 2009 (https://www.cadastre-manual.admin.ch/dam/de/sd-web/Zi4MHUCeFgtz/Weisung-BP-AV-de.pdf; colours printed as CMYK only) · **BP24** = Weisung "Darstellungsmodell für den Basisplan der amtlichen Vermessung gemäss Geodatenmodell DMAV Version 1.0", 1 Aug 2024 (https://www.cadastre-manual.admin.ch/dam/de/sd-web/hjNRml-W3Qoz/240801_Basisplan_DE.pdf; colours printed as RGB).

| Category | GB black/white (mandatory look) | GB colour option (CMYK / RGB as printed) | BP09 colour version (CMYK as printed) | BP24 colour version (RGB as printed) |
|---|---|---|---|---|
| Gebäude | 30 % grey raster, RGB 178,178,178 | Rosa (0,25,25,0) / (255,191,191) | fill Rosa (0,25,25,0), outline (34,78,100,0); at 1:10,000 fill+outline (6,72,47,0); b/w black dot raster 0.5 mm | fill rosa (255,191,191) `#FFBFBF`; outline braun (161,51,0) `#A13300` 0.20 mm; b/w solid black |
| Unterirdisches Gebäude, Reservoir | 10 % grey raster, RGB 225,225,225 | dot raster (0,41,41,0) / (255,150,150), transparent background | Reservoir outline Blau (70,60,0,0), dotted | Reservoir outline blau (77,102,255) dotted; underground buildings not shown |
| stehendes / fliessendes Gewässer, Wasserbecken | outline only (solid) | Blau (30,10,0,0) / (179,230,255) | fill Blau (30,10,0,0), transparency 0 %; outline Blau (70,60,0,0); b/w: horizontal hatch 0.12 mm every 0.8 mm (standing water) | fill blau (179,230,255) `#B3E6FF`; outline blau (77,102,255) `#4D66FF` 0.20 mm |
| Strasse_Weg | outline only (solid) | Grau (0,0,0,25) / (191,191,191) | fill Weiss (0,0,0,0); outline black 0.25 mm | fill weiss (255,255,255); outline black 0.25 mm |
| Bahn | outline only (dashed) | – | fill Weiss (0,0,0,0) | fill weiss (255,255,255) |
| Trottoir, Flugplatz, übrige befestigte | outline only | Grau (0,0,0,12) / (224,224,224) | outlines black (Trottoir, Verkehrsinsel, übrige befestigte only at 1:2,500) | outlines black (same scale rule) |
| geschlossener Wald | dot raster: dots 0.3 mm, spacing 2 mm | Grün (39,0,39,0) / (156,255,152) | fill Grün (60,0,69,0), transparency 65 %; no outline; b/w dots 0.3 mm / 1.5 mm | fill grün (156,255,156) `#9CFF9C`, transparency 50 %; no outline; b/w dots 0.3 mm / 1.5 mm |
| übrige bestockte | dots 0.3 mm, spacing 4 mm | – | as Wald (priority table lists transparency 50) | as Wald |
| Wytweide dicht / offen | dots 0.3 mm, spacing 8 mm / 16 mm | – | fill Grün (25,0,45,0), transparency 65 %; b/w dots 0.3 mm / 4 mm | fill grün (191,255,140) `#BFFF8C`, transparency 65 % |
| schmale bestockte Fläche (single object) | line dashed (gestrichelt2) | – | line Grün (100,43,100,0); fill Grün (60,0,69,0) 65 % | line grün (0,145,0) `#009100`; fill (156,255,156) 50 % |
| Acker_Wiese_Weide | no fill, dashed outline | – | **no fill**; outline black dashed | not drawn (Table 3 "nein") |
| Gartenanlage | no fill, dashed outline | – | **no fill**; outline Grün (70,40,100,0) dashed (1:2,500, 1:5,000) | not drawn per Table 3 (Table 7 still lists outline grün (77,153,0)), inconsistency in source |
| Reben | symbol raster (CADASTRA glyph b), 3.0 mm, spacing 10 mm, 50 % grey | – | glyph v 2.0 mm in Grün (80,34,100,0), outline same | glyph v, grün (51,168,0) `#33A800`, spacing 1.5 mm / 1.75 mm |
| Hoch_Flachmoor | symbol raster (glyph D), 4 mm, spacing 10 mm, 50 % grey | – | glyph d 2.0 mm in Blau (70,60,0,0), spacing 9 / 4.5 mm; no outline | glyph d, blau (77,102,255), 10.0 / 5.0 mm |
| Schilfgürtel | symbol raster (glyph c), 3.0 mm, spacing 10 mm, 50 % grey | – | glyph c 1.8 mm in Blau (70,60,0,0), spacing 9 / 4.5 mm; no outline | glyph c, blau (77,102,255), 10.0 / 5.0 mm |
| Fels | symbol raster (glyph 1) | – | taken from the national map raster | glyph 1, grau (128,128,128) |
| Geröll_Sand | symbol raster (glyph 2) | – | glyph 2 in Grau (0,0,0,50) | glyph 2, grau (128,128,128) |
| Gletscher_Firn | dashed outline | – | fill Blau (47,31,25,0), transparency 65 %; outline Blau (98,72,31,0) | fill blau (135,176,191) `#87B0BF` 65 %; outline blau (5,71,176) `#0547B0` |
| Abbau_Deponie | dashed outline | – | random black dot raster 0.3 mm, ~1 mm | same |
| übrige humusierte / Intensivkultur / vegetationslose | dashed outline only | – | not drawn | not drawn |
| wichtiger Einzelbaum | glyph o (cloud-shaped crown outline with centre dot), H = 4 mm, black | – | glyph w 2.4 mm, Grün (100,43,100,0) | glyph o, grün (0,145,0) |
| Parcel boundaries | black, 0.40 mm | – | Granat (15,50,50,0), 0.20 mm | rosa (217,128,128) `#D98080`, 0.25 mm |
| Administrative boundaries | black line patterns | – | Granat (29,100,100,0), 0.40 mm | rot (181,0,0), 0.40 mm |
| Relief / contours | – | – | contours Braun (45,73,100,0); relief shading from light grey (0,0,0,15) to light yellow (0,0,8,0), "darf nicht zu kräftig wirken" | none: "keine Höhenlinien/-koten und kein Relief" |

Further verified rules:
- **Colour is optional.** GB 1.5.6: "Die Darstellungsbeschreibung des Planes für das Grundbuch benutzt die schwarze Farbe, die Verwendung von eingefärbten Elementen … ist optional." In the colour option only buildings, sealed areas, water, forest and underground buildings are coloured; everything else stays black/white.
- **Boundary line style encodes hardness** (GB 3.3): solid for `Gebaeude`, `Strasse_Weg`, `Trottoir`, `Verkehrsinsel`, `Flugplatz`, `Wasserbecken`, `stehendes`, `fliessendes`; dashed (`gestrichelt1`, 1.5 mm / 0.5 mm, 0.20 mm wide at 1:1,000) for all soft land covers (Acker, Garten, Wald, Moor, Reben, Schilf, Fels, Geröll, übrige …).
- **Scales.** GB: 1:200, 1:250, 1:500, 1:1,000, 1:2,000, 1:2,500, 1:5,000, 1:10,000; symbol sizes defined at 1:1,000 and scaled. BP: 1:2,500, 1:5,000 (reference), optionally 1:10,000; factor 1.4 (BP09) resp. 1.2 (BP24) for 1:2,500 and 0.7 for 1:10,000.
- **Font.** All symbols are glyphs of the font "Cadastra" (open source, based on Bitstream; may be modified if renamed).
- **Drawing priority** (both BP versions): labels and boundaries on top, point/line single objects, then roads/pavements, buildings, humus classes, water, and at the bottom forest, glacier, wooded pasture (transparent fills so relief remained visible in BP09).
- **D (my conversion):** the BP24 RGB values are the BP09 CMYK values under the naive conversion R = 255·(1−C)(1−K), e.g. (70,60,0,0)→(77,102,255), (80,34,100,0)→(51,168,0), (25,0,45,0)→(191,255,140), (47,31,25,0)→(135,176,191), (15,50,50,0)→(217,128,128). Only the forest fill changed: (60,0,69,0) = (102,255,79) at 65 % transparency in 2009 → (156,255,156) at 50 % in 2024. Effective colours on white paper: forest 2024 ≈ `#CEFFCE`, forest 2009 ≈ `#C9FFC1`, wooded pasture ≈ `#E9FFD7`, glacier ≈ `#D5E3E9`.

### 4.3 swisstopo general palette

- swisstopo **Light Base Map** vector-tile style (V, but read through the extraction model; filters simplified): style name `lightbasemap_v1.19.0`, https://vectortiles.geo.admin.ch/styles/ch.swisstopo.lightbasemap.vt/style.json, forest/wood rgb(186,210,172) · default land cover rgb(215,224,209) · glacier/ice rgb(205,232,244) · wetland rgb(204,229,245) · sand, landfill, quarry rgb(240,218,188) · pitch and grass runway rgb(224,234,221) · cemetery, zoo rgb(215,224,209) · parking rgb(255,255,255) · water rgb(209,228,240) → rgb(199,224,245) by zoom · buildings hsl(220,10%,82%) → hsl(220,10%,75%) · vineyard, orchard, swamp by pattern.
- RGB definitions of the printed national-map symbols (Zeichenerklärung): not found / not verified.

---

## 5. Austria: DKM (Digitale Katastralmappe), Benützungsarten and Nutzungen

### 5.1 Code list (V-img; BEV "CSV-Datei – Grundstücksdaten", interface description v1.2 of 29.01.2025, https://www.bev.gv.at/dam/jcr:a0e89772-7b55-4889-a029-69d93311811c/BEV_S_KA_Grundstuecksdaten-csv_V1.2.pdf; DKM symbol numbers from "Katastralmappe SHP", interface description v2.9 of 04.12.2024, https://www.bev.gv.at/dam/jcr:a6342749-e2c2-4525-9cee-3b7531474599/BEV_S_KA_Katastralmappe_SHP_V2.9.pdf; definitions from BANU-V § 2, https://www.ris.bka.gv.at/Dokumente/Bundesnormen/NOR40117347/NOR40117347.html, V, shortened)

| BA | NU | Benützungsart | Nutzung | DKM symbol no. `NS` (glyph) | Definition (BANU-V § 2) |
|---|---|---|---|---|---|
| 1 | 01 | Bauflächen | Gebäude | 41 (dot; drawn red) | permanently erected buildings |
| 1 | 02 | Bauflächen | Gebäudenebenflächen | 83 (small square) | "befestigte Flächen in Verbindung mit Gebäuden (Innenhöfe, Terrassen, kleine Vorplätze usw.)" |
| 2 | 01 | landwirtschaftlich genutzte Grundflächen | Äcker, Wiesen oder Weiden | 48 ("LN") | arable incl. green fallow, permanent grassland |
| 2 | 02 | landwirtschaftlich genutzte Grundflächen | Dauerkulturanlagen oder Erwerbsgärten | 40 | fruit/berry plantations, hop gardens, market gardens, tree and vine nurseries |
| 2 | 03 | landwirtschaftlich genutzte Grundflächen | Verbuschte Flächen | 57 (small arc) | bushes or emerging woodland, heath with canopy below 50 % |
| 3 | 01 | Gärten | Gärten | 52 (stylised tree) | "Haus-, Zier- und Vorgärten in Verbindung mit Gebäuden, Kleingärten oder Siedlungsflächen mit Bebauungsabsicht" |
| 4 | 01 | Weingärten | Weingärten | 53 (vine hook) | planted with vines |
| 5 | 01 | Alpen | Alpen | 54 | alpine pastures above the permanent settlement limit |
| 6 | 01 | Wald | Wälder | 56 (conifer) | forest |
| 6 | 02 | Wald | Krummholzflächen | 55 ("^") | dwarf-pine areas |
| 6 | 03 | Wald | Forststraßen | 58 ("FS") | non-public forest roads |
| 7 | 01 | Gewässer | Fließende Gewässer | 59 (flow arrow) | flowing water |
| 7 | 02 | Gewässer | Stehende Gewässer | 60 (stacked strokes) | lakes, ponds |
| 7 | 03 | Gewässer | Gewässerrandflächen | 64 ("GR") | "Böschungen, Dämme, Uferbegleitvegetation" |
| 7 | 04 | Gewässer | Feuchtgebiete | 61 (strokes + tufts) | "Schilfflächen, Sümpfe, Moore, regelmäßig überschwemmte Flächen" |
| 8 | 01 | Sonstige | Straßenverkehrsanlagen | 95 ("V") | motorways, roads, paths, squares incl. parking strips |
| 8 | 02 | Sonstige | Schienenverkehrsanlagen | 92 (diamond) | rail |
| 8 | 03 | Sonstige | Verkehrsrandflächen | 65 ("VR") | "Seitengräben, Böschungen, Begleitvegetationsstreifen, Dämme" |
| 8 | 04 | Sonstige | Parkplätze | 42 ("P") | sealed areas for stationary traffic |
| 8 | 05 | Sonstige | Betriebsflächen | 63 (wheel) | industrial/commercial, supply and disposal |
| 8 | 06 | Sonstige | Abbauflächen, Halden und Deponien | 84 ("A" in semicircle) | extraction, heaps, landfill |
| 8 | 07 | Sonstige | Freizeitflächen | 96 ("E") | "künstliche Grünflächen für Freizeit- oder Erholungszwecke" |
| 8 | 08 | Sonstige | Friedhöfe | 72 (gravestone) | cemeteries |
| 8 | 09 | Sonstige | Fels- und Geröllflächen | 87 | rock and scree without vegetation |
| 8 | 10 | Sonstige | Vegetationsarme Flächen | 62 (slashed ellipse) | sparse ground vegetation outside farming/forestry |
| 8 | 11 | Sonstige | Gletscher | 88 (six-armed star) | glacier |
| 9 | 01–04 | (legal overlay) | Rechtlich Weingarten / kein Weingarten / Wald / nicht Wald | `NS_RECHT` 77 / 78 / 74 / 73 | legal status, not land cover |

History: the 2012 reform replaced the older, finer list (e.g. 49 Acker, 50 Wiese, 51 Hutweide, 89 Streuobstwiese, 52 "Baufläche begrünt", 83 "Baufläche befestigt", 96 "Erholungsfläche", 62 "Ödland"), old data may still carry these codes (V-img).

### 5.2 Data layers people actually have (V-img, SHP interface v2.9)

`GST` parcels (polygon) · `NFL` Nutzungsflächen (polygon; attribute `NS` = symbol number above, `NS_RECHT`) · `NSL` use boundaries and other lines (`NSL` 1 Nutzungsgrenze, 2 Hausgrenze, 3 Hausgrenze aus Luftbild, 4 Sonstige Linie; `TYP` 1 = underground) · `NSY` use symbols (point; `MST_NS` 1 = half size, `ROT_NS`) · `VGG` administrative and parcel boundaries · `GNR` parcel numbers · `FPT`, `SGG` control/boundary points · `SSB` other symbols and labels. CRS EPSG:31254/31255/31256. Crosswalk key for the library: **`NFL.NS`**.

### 5.3 Official representation (V-img)

- The DKM is a **line-and-symbol map without area fills**: land use is shown by a glyph at the polygon reference point plus green use boundaries. DXF layer colours (interface v2.6 of 16.12.2024, https://www.bev.gv.at/dam/jcr:3a92eaa4-9e9e-4ce3-af96-c1fa6e722548/BEV_S_KA_Katastralmappe_DXF_V2.5.2.pdf), given as AutoCAD colour index screen / plot: parcel boundary `GG` white-7 / black-7 · building outline `HG` **red-1** · building outline from aerial imagery `HL` brown-9 / brown-8 · use boundary `NG` and use symbols `NS` **green-3** · other lines and symbols `SG`/`SS` **blue-5** · legal symbols orange-30 · municipal boundary yellow-51 / brown-8. "Das Nutzungssymbol FIG041 (Gebäude) wird rot dargestellt."
- BEV supplies a TrueType symbol font `BEV_DKM_Symbole.ttf` and ready projects `BEV0.qgz` / `BEV0.mxd` ("Katastralmappe-Symbole_SHP-INFO"), and states that the legal drawing key of the Vermessungsverordnung is "rechtlich nicht verbindlich" for DKM display (https://www.bev.gv.at/dam/jcr:be95ead9-0fff-4413-bc14-7eca52ffe6e6/BEV_B_KA_Katastralmappe_SHP_Symbolisierung_V1.0.pdf). **No official RGB fill colours for Nutzungen exist in these documents.**

---

## 6. Prior-art habitat / ecology symbology with published schemes

### 6.1 UKHab (UK Habitat Classification)

| Aspect | Finding | St. |
|---|---|---|
| Structure | Primary habitats in a hierarchy: level 2 (letters `g` grassland, `w` woodland and forest, `h` heathland and shrub, `f` wetland, `c` cropland, `u` urban, `s` sparsely vegetated land, `r` rivers and lakes, `t` marine inlets and transitional waters), level 3 (`g4` modified grassland), level 4 (`g3c` other neutral grassland), level 5 (`g3c5` …); plus numeric **secondary codes** for mosaics, management, origin and land use. Each code has allowed geometries (Area/Line/Point). | S, community extraction of the official tables, https://github.com/mrichar1/UKHAB-QGIS (`2.01/primary_codes.csv`, `secondary_codes.csv`) |
| Urban branch (identical in v2.01 and v2.1 extracts) | `u` Urban · `u1` Built-up areas and gardens · `u1b` Developed land – sealed surface · `u1b5` Buildings · `u1b6` Other developed land · `u1c` Artificial unvegetated – unsealed surface · `u1d` Suburban mosaic of developed and natural surface · `u1e` Built linear features · `u1f` Sparsely vegetated urban land | S |
| Urban-relevant secondary codes (v2.01 extract) | 10 scattered scrub · 32 scattered trees · 33 line of trees · 81 ruderal or ephemeral · 82 vacant or derelict land · 86 green roof · 87 biodiverse green roof · 88 intensive green roof · 89 other green roof · 90 cemeteries and churchyards · 106 mown · 108 frequently mown · 114 dry stone wall · 200 tree · 203 mature tree · 204 veteran tree · 209 avenue · 510 bare ground · 612 fence · 616 allotments · 800 road · 801 road verge or island · 802 railway · 804 car park · 806–812 park types (urban, pocket, neighbourhood, community, district, regional, country) · 820 natural sports pitches · 821 artificial sports pitches · 822 recreation ground · 823 children's play space · 827 garden · 828 vegetated garden · 829 unvegetated garden · 830 community garden · 841 green wall · 842 ground-based green wall · 843 facade-bound green wall · 844 balcony green · 845 ground level planters · 846 flower bed · 847 introduced shrub · 848 sustainable drainage system · 849 bioswale · 850 rain garden · 851 culvert · 852 water treatment filter bed · 853 mortared wall | S |
| v2.1 additions seen | `h2a` native hedgerow (`h2a5` species-rich, `h2a6` other), `h2b` non-native and ornamental hedgerow; more `g3c` sub-types (`g3c3`, `g3c4`, `g3c9` wet meadow) | S |
| Official colour palette / GIS styles | **Could not verify.** Downloads are gated: "All UKHab publications are published and only available under licence" (Free End User Licence v2, 31 March 2023; registration; bespoke commercial licences). Copyright "© UKHab Ltd 2018-2026. All rights reserved". Editions: Professional and abridged Basic. | V (https://www.ukhab.org/ukhab-documentation/, https://www.ukhab.org/) |
| Community colours (not official) | per level-2 letter, baseline / proposed RGB: g (0,252,4)/(128,255,130) · w (51,160,44)/(153,204,150) · h (130,104,214)/(179,159,230) · f (253,123,238)/(255,180,245) · c (255,127,0)/(255,180,100) · u (236,34,68)/(245,120,140) · s (168,168,164)/(200,200,198) · r (39,237,245)/(130,245,250) · t (0,0,255)/(100,100,255). Noteworthy idea: a **lighter tint of the same hue for "proposed" habitats**. | S (`config.py` of the repo above) |

### 6.2 JNCC Phase 1 habitat survey colours (the classic UK scheme that UKHab replaces): S (community SLD implementing the JNCC handbook: https://github.com/QGIS-UK/Styles/blob/master/Phase%201%20Habitat/phase_1_habitat.sld)

| Code | Habitat | Fill | Overlay |
|---|---|---|---|
| A1.1.1 / A1.1.2 | broadleaved woodland semi-natural / plantation | `#008000` / white | – / green diagonal hatch |
| A1.2.1 / A1.2.2 | coniferous woodland semi-natural / plantation | `#a0ffa0` / white | – / hatch |
| A2.1 | dense scrub | white | green cross-hatch `#008000` |
| B2.1, B2.2 | neutral grassland (unimproved, semi-improved) | `#ff8000` | – |
| B4, B6 | improved / poor semi-improved grassland | `#ffffd0` | – |
| C3.1 | tall ruderal | white | brown hatch `#a05000` |
| D1.1 | dry dwarf shrub heath | `#ffd040` | – |
| E1.6.1 | blanket bog | `#900090` | – |
| F1 | swamp | `#80d5ff` | – |
| G1, G2 | standing / running water | `#3030ff` | – |
| J1.1 | arable | `#e0e0e0` | – |
| J1.2 | amenity grassland | `#ffff00` | – |
| J1.3 | ephemeral/short perennial | white | black cross-hatch |
| J1.4 | introduced shrub | white | brown cross-hatch `#a05000` |
| J2.1 | hedge | `#00ff00` | – |
| J4 | bare ground | white | black dot fill |

Design principle visible in the scheme: **hue = habitat family, solid fill = semi-natural/unimproved, hatch in the same hue = planted/modified/mosaic.**

### 6.3 England's statutory biodiversity metric (Defra / Natural England): a habitat list tied to a score

Sources: user guide June 2026, 89 pp (V-img: https://assets.publishing.service.gov.uk/media/6a1d98e9c7335e2ca6daadd5/The_Statutory_Biodiversity_Metric_-_User_Guide_-_June_2026.pdf) and small sites metric (SSM) user guide July 2025, 63 pp (V-img: https://assets.publishing.service.gov.uk/media/686677acdd1a7e01559e6d45/The_Small_Sites_Metric__Statutory_Biodiversity_Metric__-_User_Guide_July_2025.pdf).

| Scoring component | Values | Source |
|---|---|---|
| Distinctiveness (by habitat type) | Very high 8 · High 6 · Medium 4 · Low 2 · Very low 1 (hedgerow module) · Very low 0 (area module) | guide Table 5, p. 27 |
| Condition | Good 3 · Fairly good 2.5 · Moderate 2 · Fairly poor 1.5 · Poor 1 · Condition assessment N/A 1 · N/A – other 0 | guide Table 6, p. 28 |
| Modules | area habitats (ha) · hedgerows and lines of trees (km) · watercourses (km) | guide |
| Individual trees ("tree helper") | Small: DBH > 7.5 cm and ≤ 30 cm = 0.0041 ha · Medium: > 30 and ≤ 60 cm = 0.0163 ha · Large: > 60 and ≤ 90 cm = 0.0366 ha · Very large: > 90 cm = 0.0765 ha ("a representation of canopy biomass … based on the root protection area formula, derived from BS 5837:2012") | guide Table 15, p. 62 |
| Urban rules | default 70:30 split "developed land; sealed surface" : "vegetated garden" for housing without detailed plans; new habitats in private gardens only as vegetated / unvegetated garden; green roofs on private dwellings only "other green roof"; green roof area is subtracted from the building footprint; green walls counted by vertical area and not part of site area; urban lines/groups of trees are recorded as individual trees, not as hedgerow-module "line of trees" | guide pp. 59–61 |
| Ponds vs lakes | water bodies < 2 ha are ponds, ≥ 2 ha lakes | guide p. 67 |
| SSM strategic significance | High 1.15 · Medium 1.10 · Low 1 | SSM guide |

**SSM "UKHab translation table" (Appendix 2, Table A2, pp. 58–63)**: written for landscape architects; this is the closest published prior art for the catalog's element names. Codes as printed.

| Landscape term (code) | Metric broad habitat – habitat type | Distinctiveness |
|---|---|---|
| Amenity grassland or grassland seed mix (g4) | Grassland – Modified grassland | Low |
| Amenity grassland or grassland seed mix (g4, as printed) | Grassland – Other neutral grassland | Medium |
| Meadow grassland or wildflower seeding (g3c / g1d / g1b) | Grassland – Other neutral grassland / Other lowland acid grassland / Upland acid grassland | Medium |
| Bracken (g1c) | Grassland – Bracken | Low |
| Native scrub (h3a, h3d, h3e, h3f, h3b, h3h) | Heathland and shrub – Blackthorn / Bramble / Gorse / Hawthorn / Hazel / Mixed scrub | Medium |
| Native scrub (h3cNE2) · Invasive scrub (h3g) | Sea buckthorn scrub (other) · Rhododendron scrub | Low |
| Native hedge (h2NE5, h2NE2, h2NE9) | Hedgerow – Native hedgerow / Species-rich native hedgerow / Native hedgerow associated with bank or ditch | Medium |
| Native hedge with standard trees (h2NE4) | Hedgerow – Native hedgerow with trees | Low (as printed) |
| Ornamental hedge (h2NE3) | Hedgerow – Non-native and ornamental hedgerow | Low |
| Standard trees (w1g6NE2, w1g6NE4 / w1g6NE3, w1g6NE1) | Hedgerow – Line of trees (± bank or ditch) / Ecologically valuable line of trees (± bank or ditch) | Low / Medium |
| Standard tree (1170) | Urban – Urban tree | Low (as printed) |
| Ornamental shrub planting (1160) | Urban – Introduced shrub | Low |
| Planters (1140) | Urban – Ground level planters | Low |
| Garden (231) / Garden (232) | Urban – Vegetated garden / Un-vegetated garden | Low / Very low |
| Allotments (910) | Urban – Allotments | Low |
| Cemetery (800) | Urban – Cemeteries and churchyards | Medium |
| Bare ground (510) | Urban – Vacant/derelict land/ bare ground | Low |
| Ruderals (17) | Sparsely vegetated land – Ruderal/ephemeral | Low |
| Biodiverse roof (1113) | Urban – Biodiverse green roof | Medium |
| Green roof (1111) | Urban – Other green roof | Medium (as printed) |
| Green roof – sedum (1112) | Urban – Intensive green roof (as printed) | Low |
| Green wall (1122 / 1121) | Urban – Facade-bound green wall / Ground based green wall | Low |
| SuDS (1192 / 1119) · Bioswale (1191) | Urban – Rain garden / Sustainable drainage system · Bioswale | Low |
| Impermeable hardscape (u1b) | Urban – Developed land; sealed surface | Very low |
| Permeable hardscape (u1c) | Urban – Artificial unvegetated, unsealed surface | Very low |
| Wall (u1e) | Urban – Built linear features | Very low |
| Quarry (1030) | Urban – Sand pit quarry or open cast mine | Low |
| Wildlife pond (r1b) · Ornamental pond (362) · Reservoirs (108) | Lakes – Ponds (non-priority habitat) · Ornamental lake or pond · Reservoirs | Medium · Low · Medium |
| Canal (r1eNE1) · Ditch (r1eNE2) · Culvert (rNE1) | Rivers & streams – Canals · Ditches · Culvert | Medium · Medium · Low |
| Native broadleaved / mixed woodland (w1g / w1h) · Conifer woodland (w2c / w2b) | Woodland and forest – Other woodland; broadleaved / mixed · Other coniferous woodland / Other Scot's pine woodland | Medium / Medium · Low / Medium |
| Orchard (c1e) · Horticulture (c1f) · Cropland (c1c, c1d, c1b) · Cropland margins (c1a…) | Cropland – Intensive orchards · Horticulture · Cereal / non-cereal crops, temporary grass and clover leys · Arable field margins | Low · Low · Low · Medium |
| Scree (s1d) · Saltmarsh (A2.5) | Sparsely vegetated land – Other inland rock and scree · Coastal saltmarsh | Medium · Medium |

Notes: (1) the numeric codes printed in this SSM guide table (1160, 1170, 1111 …) are *not* UKHab 2.x secondary codes; the statutory tool itself uses the UKHab codes (see next table). (2) The guide states that UKHab "is used under licence from UKHab Ltd. No onward licence implied or provided and, where applicable, the same shall be out of scope of the OGL v3.0", relevant for an open library. (3) Several SSM rows differ from the statutory tool (urban tree Low vs Medium; other green roof Medium vs Low; native hedgerow Medium vs Low), quoted as printed, cause not established.

**Statutory metric calculation tool v1.0.4, sheet "G-1 All Habitats" ("All Habitats Based on UKHab"), V** (parsed from the official workbook https://assets.publishing.service.gov.uk/media/6867e62810d550c668de3b4e/The_Statutory_Metric_Macro_Disabled_1.0.4.xlsx; columns: label, "Definitive UKHAB / EUNIS / NE Code", distinctiveness category and score).

| Broad habitat | Habitat type (code), distinctiveness score |
|---|---|
| **Urban** (21 types) | Developed land; sealed surface (u1b), V.Low 0 · Artificial unvegetated, unsealed surface (u1c), V.Low 0 · Built linear features (u1e), V.Low 0 · Unvegetated garden (829), V.Low 0 · Vegetated garden (828), Low 2 · Allotments (616), Low 2 · Introduced shrub (847), Low 2 · Ground level planters (845), Low 2 · Intensive green roof (88), Low 2 · Other green roof (89), Low 2 · Biodiverse green roof (87), Medium 4 · Facade-bound green wall (843), Low 2 · Ground based green wall (842), Low 2 · Bioswale (849), Low 2 · Rain garden (850), Low 2 · Sustainable drainage system (848), Low 2 · Bare ground (510), Low 2 · Vacant or derelict land (82), Low 2 · Actively worked sand pit quarry or open cast mine (85), Low 2 · Cemeteries and churchyards (90), Medium 4 · Open mosaic habitats on previously developed land (80), High 6 |
| **Individual trees** | Urban tree (NE0014), Medium 4 · Rural tree (NE0016), Medium 4 |
| **Grassland** | Modified grassland (g4), Low 2 · Bracken (g1c), Low 2 · Other neutral grassland (g3c), Medium 4 · Other lowland acid grassland (g1d), Medium 4 · Upland acid grassland (g1b), Medium 4 · Lowland calcareous grassland (g2a), High 6 · Upland calcareous grassland (g2b), High 6 · Traditional orchards (27), High 6 · Floodplain wetland mosaic and CFGM (19), High 6 · Tall herb communities (H6430) (s1a9), High 6 · Lowland meadows (g3a), V.High 8 · Lowland dry acid grassland (g1a), V.High 8 · Upland hay meadows (g3b), V.High 8 |
| **Heathland and shrub** | Rhododendron scrub (h3g), Low 2 · Other sea buckthorn scrub (h3c6), Low 2 · Blackthorn (h3a), Bramble (h3d), Gorse (h3e), Hawthorn (h3f), Hazel (h3b), Mixed (h3h), Willow (h3j) scrub, Medium 4 · Lowland heathland (h1a), Upland heathland (h1b), Dunes with sea buckthorn (h3c5), High 6 · Mountain heaths and willow scrub (h1c), V.High 8 |
| **Woodland and forest** | Other coniferous woodland (w2c), Low 2 · Other woodland; broadleaved (w1g), Medium 4 · Other woodland; mixed (w1h), Medium 4 · Other Scot's pine woodland (w2b), Medium 4 · Felled (206), Lowland mixed deciduous (w1f), Lowland beech and yew (w1c), Wet woodland (w1d), Upland oakwood (w1a), Upland mixed ashwoods (w1b), Upland birchwoods (w1e), Native pine woodlands (w2a), High 6 · Wood-pasture and parkland (26), V.High 8 |
| **Lakes** | Ornamental lake or pond (46), Low 2 · Ponds (non-priority habitat) (41), Medium 4 · Reservoirs (45), Medium 4 · Ponds (priority habitat) (40), High 6 · lake types by alkalinity, peat, marl, temporary (r1f5), High 6 · Aquifer fed naturally fluctuating water bodies (r1d), V.High 8 |
| **Sparsely vegetated land** | Ruderal/Ephemeral (81), Low 2 · Tall forbs (16), Low 2 · Other inland rock and scree (s1d), Medium 4 · Inland rock outcrop and scree habitats (s1a), Coastal sand dunes (s3a), Coastal vegetated shingle (s3b), Maritime cliff and slopes (s2a), High 6 · Limestone pavement (s1b), Calaminarian grasslands (s1c), V.High 8 |
| **Cropland** | Cereal crops (c1c), Winter stubble (c1c5), Non-cereal crops (c1d), Horticulture (c1f), Intensive orchards (c1e), Temporary grass and clover leys (c1b), Low 2 · Arable field margins: cultivated annually (c1a7), game bird mix (c1a8), pollen and nectar (c1a6), tussocky (c1a5), Medium 4 |
| **Wetland** | Reedbeds (f2e), High 6 · Blanket bog (f1a), Lowland raised bog (f1b), Fens (f2a/f2c/f2f), Purple moor grass and rush pastures (f2b), Transition mires and quaking bogs, Depressions on peat substrates (56), Oceanic valley mire, V.High 8 |
| Coastal and intertidal groups | Coastal lagoons, Rocky shore, Coastal saltmarsh, Intertidal sediment, Intertidal hard structures (artificial variants Low 2; "with integrated greening of grey infrastructure (IGGI)" Medium 4) · Watercourse footprint (NE0017), V.low 0 |
| **Hedgerow module** (sheet "G-6 Hedgerow Data") | Non-native and ornamental hedgerow, V.Low 1 · Native hedgerow, Low 2 · Line of trees (± bank or ditch), Low 2 · Native hedgerow with trees, Medium 4 · Native hedgerow associated with bank or ditch, Medium 4 · Species-rich native hedgerow, Medium 4 · Ecologically valuable line of trees (± bank or ditch), Medium 4 · Native hedgerow with trees associated with bank or ditch, High 6 · Species-rich native hedgerow with trees, High 6 · Species-rich native hedgerow associated with bank or ditch, High 6 · Species-rich native hedgerow with trees associated with bank or ditch, V.High 8 |

Reading for the catalog: the urban list is a complete, scored vocabulary of **built-environment elements** (sealed / unsealed artificial surface, walls, two garden types, planters, introduced shrub, three green-roof and two green-wall types, three SuDS types, bare/vacant land, allotments, cemetery, open mosaic habitat, urban tree). Every one of these should exist as a library element or modifier so a styled layer can be scored without re-classification.

### 6.4 Switzerland: TypoCH (Delarze, Gonseth, Eggenberg & Vust 2015), urban-relevant classes (V, https://www.infoflora.ch/en/habitats/typoch-(delarze-et-al.)/full-list-typoch.html)

Decimal hierarchy, 9 level-1 groups: 1 Gewässer · 2 Ufer und Feuchtgebiete · 3 Gletscher, Fels, Schutt und Geröll · 4 Grünland · 5 Krautsäume, Hochstaudenfluren und Gebüsche · 6 Wälder · 7 Pioniervegetation gestörter Plätze · 8 Pflanzungen, Äcker und Kulturen · 9 Bauten, Anlagen. The scheme deliberately reserves ".0" codes for artificial variants:

| Code | Name | Catalog relevance |
|---|---|---|
| 2.0 | Künstliche Ufer | hard banks |
| 4.0 | Kunstrasen: 4.0.1 Kunstwiese auf Fruchtfolgefläche · **4.0.2 Kunstrasen auf Sportplätzen, im Siedlungsraum, etc.** · 4.0.3 Begrünung in Tieflagen (Strassenböschungen, etc.) · 4.0.4 Begrünung in Hochlagen | lawn; verge greening |
| 4.2, 4.5, 4.6 | Trockenrasen · Fettwiesen und -weiden (4.5.1 Talfettwiese …) · Grasbrachen | meadow types |
| 5.1, 5.2 | Krautsäume · Hochstauden- und Schlagfluren | herb fringes |
| 5.3 | Gebüsche: **5.3.0 Naturferne Pflanzung** (5.3.0.1 sommergrüne, 5.3.0.2 immergrüne Arten) · 5.3.3 Mesophiles Gebüsch · 5.3.4 Brombeergestrüpp … | ornamental shrub planting vs native scrub |
| 6.0 | Forstpflanzungen | plantations |
| 7.1 | Trittrasen und Ruderalfluren: **7.1.0 Tritt- und Trümmerflächen ohne Vegetation** · 7.1.1 Feuchte Trittflur · 7.1.2 Trockene Trittflur · 7.1.4 Einjährige Ruderalflur · 7.1.5 Trockenwarme Ruderalflur · 7.1.6 Mesophile Ruderalflur | trampled and ruderal ground |
| 7.2 | Anthropogene Steinfluren: **7.2.0 Mauer oder Steinpflästerung ohne Vegetation** · 7.2.1 Trockenwarme Mauerflur · **7.2.2 Steinpflaster-Trittflur** | walls, vegetated paving joints |
| 8.1 | Baumschulen, Obstgärten, Rebberge: 8.1.1–8.1.2 Baumschule · 8.1.4 Hochstammobstgarten · 8.1.5 Niederstammobstgarten · 8.1.6 Rebberg · 8.1.7 Beerenkultur | orchard, vineyard, nursery |
| 8.2 | Feldkulturen (Äcker) incl. 8.2.3 Hackfruchtacker (Sommerkultur), **Garten** | arable, kitchen garden |
| 9.1 | Lagerplätze, Deponien | |
| 9.2 | Bauten (9.2.1 Bewohntes Gebäude … 9.2.2.4 Treibhaus … 9.2.5 Öffentliches Gebäude) | buildings |
| 9.3 | Verkehrswege: 9.3.2 Asphalt- und Betonstrasse (9.3.2.3 Weg ohne Vegetation (Beton, Kies)) · 9.3.3 Naturstrasse, Weg (Naturweg, Holzerweg, Pfad) · 9.3.4 Bahngleis | sealed vs unsealed ways |
| 9.4 | Versiegelter Sportplatz, Parkplatz etc. | sealed sports/parking |

No colour scheme is published with the typology on the InfoFlora pages (not found).

### 6.5 Germany: LBP-Musterlegendenkatalog (Bundesnetzagentur, 2nd version, Dec 2021): V-img, https://www.netzausbau.de/SharedDocs/Downloads/DE/Methodik/Eingriffsregelung/LBP-Musterlegendenkatalog.pdf?__blob=publicationFile

A federal model legend for landscape conservation plans at **1:1,000–1:5,000**, with RGB values per biotope "Obergruppe" (example codes use the Lower Saxony key of Drachenfels). Colours are mandatory ("Das Symbol selbst und die Farbe sind dabei beizubehalten"); over aerial imagery fills get "Transparenzwert … 35 %".

| Obergruppe | RGB as printed | Hex | Symbol |
|---|---|---|---|
| Laubwald | "0/168/132" as printed, **probable misprint**: swatch is light green and the planting hatch for Laubwald in chapter 5.3 is 137/205/102 | (`#89CD66`) | fill |
| Nadelwald | 114/137/68 | `#728944` | fill |
| Mischwald | area 137/205/102, lines 114/137/68 | `#89CD66` + `#728944` | vertical stripes |
| Waldrand / Waldlichtung | area 137/205/102, lines 163/255/115 | `#89CD66` + `#A3FF73` | diagonal stripes |
| Flächenhafter Gehölzbestand (scrub, hedges, tree rows as areas) | 163/255/115 | `#A3FF73` | fill |
| Solitärbaum, Einzelbaum, Neupflanzung/Jungbaum, Einzelstrauch | 163/255/115 | `#A3FF73` | point symbols (flower-shaped crown with dot; circle with dot; plain circle; small cloud) |
| Stillgewässer, Fließgewässer (line), Quellbereich (triangle) | 0/197/255 | `#00C5FF` | fill / line / point |
| Gehölzfreie Biotope der Sümpfe, Niedermoore und Ufer | 205/205/102 | `#CDCD66` | fill |
| Übergangsmoore | area 205/205/102, dots 168/112/0 | `#CDCD66` + `#A87000` | dot overlay |
| Hochmoore | 168/112/0 | `#A87000` | fill |
| Fels-, Gesteins- und Offenbodenbiotope | 245/162/122 | `#F5A27A` | fill |
| Heiden und Magerrasen | 245/122/182 | `#F57AB6` | fill |
| Grünland | 220/255/200 | `#DCFFC8` | fill |
| Trockene bis feuchte Stauden- und Ruderalfluren | 232/190/255 | `#E8BEFF` | fill |
| Acker- und Gartenbaubiotope | 255/255/220 | `#FFFFDC` | fill |
| Siedlungsbiotope: Grünanlagen (ornamental shrubs, house gardens, animal enclosures) | 158/215/194 | `#9ED7C2` | fill |
| Gebäude / Wohn- und Mischbebauung | 255/200/200 | `#FFC8C8` | fill |
| Verkehrs- und Industrieflächen / Infrastruktur im Außenbereich | 225/225/225 | `#E1E1E1` | fill |
| Biotope/land-use boundaries | existing-state plans grey 78/78/78; measures plans green 38/115/0 | `#4E4E4E` / `#267300` | line |

State modifiers (chapter 5): **new planting/development = diagonal hatch in the colour of the target biotope** (e.g. Grünland 220/255/200, Heiden 245/122/182, Gehölz 163/255/115); **extensification/forest conversion = dot overlay 0/168/132** on the base colour; trees to be protected = red ring 255/0/0 around the green symbol; tree loss = red X; unsealing = cross-hatch 78/78/78; timing labels yellow 255/255/0 (advance), orange 255/170/0 (during construction), blue 115/178/255 (after completion). A GIS style file "kann auf Anfrage von der Bundesnetzagentur … zur Verfügung gestellt werden".

### 6.6 Germany: Hamburg "Kartieranleitung und Biotoptypenschlüssel", 7th ed., March 2025: V-img, https://www.hamburg.de/resource/blob/1036252/de53ab36043c5d658b46aa8d4337c97b/kartieranleitung-biotoptypenschluessel-maerz-2025-data.pdf

City-wide, area-covering biotope **and** land-use key (451 types, modelled on the Lower Saxony key), digitised at ≥ 1:1,000; polygons for features wider than 5 m, lines up to 5 m, points for single trees and springs; legend is built from the first letter (`GRUPPE`). No RGB table in the pages read. Groups: A Gras-, Stauden- und Ruderalfluren · B Biotopkomplexe der Siedlungsflächen · E Biotopkomplexe der Freizeit-, Erholungs-, Grünanlagen · F Lineare und Fließgewässer · G Grünländer · H Gebüsche und Kleingehölze · K Küstenbiotope · L Biotope landwirtschaftlich genutzter Flächen · M Hoch- und Übergangsmoore · N Sümpfe und Niedermoore · O Offenbodenbiotope · S Stillgewässer · T Heiden, Borstgrasrasen, Magerrasen · V Verkehrsflächen · W Wälder · Y Biotope vegetationsarmer Flächen mit Spontanvegetation · Z Vegetationsbestimmte Habitatstrukturen besiedelter Bereiche.

The two urban element groups map almost one-to-one onto a parcel-scale element catalog:

| Code | Type | Code | Type |
|---|---|---|---|
| ZRT | Scher- und Trittrasen (mown/trampled lawn) | YFV | Asphalt- oder Betondecke |
| ZRW | Stadtwiese (urban meadow) | YFP | Gepflasterte Fläche, Ziegel, Betonplatten etc. |
| ZRE / ZRR | Raseneinsaat / Extensivrasen-Einsaat | YFR | Pflasterritzen (vegetated paving joints) |
| ZZ | Zierbeet, Rabatte (ornamental bed) | YFK | Kies- oder Schotterdecke |
| ZN | Nutzbeet (vegetable bed) | YFW | Unbefestigte, verdichtete Erd- oder Sandfläche |
| ZSS | Schnitthecke (clipped hedge) | YFB | Unbefestigter Rand, Baumscheibe (tree pit) |
| ZSH | Zierstrauchhecke | YFS | Stein- und Blockschüttung |
| ZSF / ZSN | Zier-Gebüsch, non-native / native species | YFZ | Sonstige befestigte Fläche |
| ZSR | Rankengewächse, Lianen (climbers) | YDG | Begrüntes Dach (green roof) |
| ZHF / ZHN | Gepflanzter Gehölzbestand, non-native / native | YDK / YDZ / YDR / YDX | Kiesdach / Ziegeldach / Reetdach / sonstiges Dach |
| HEE / HEA / HEG | Einzelbaum / Baumreihe, Allee / Baumgruppe | YMN / YMZ / YMH / YMF / YMW / YMX | Natursteinmauer / Ziegelwand / Holzwand / Fachwerk / Wand im Wasserwechselbereich / sonstige |
| HHS / HHM / HHB / HW… | Strauchhecke / Strauch-Baumhecke / Baumhecke / Knick (hedge bank) | OWL / OWS / OWX | Lehmweg / Sandweg / sonstiger unbefestigter Weg |
| APT / APM / APF | Ruderalflur trocken / mittel / feucht | OAG / OAS | Schotterfläche, Steinhaufen / Sandaufschüttung |
| AKT / AKM / AKF | Halbruderale Gras- und Staudenflur | NRS … | Schilf-Röhricht and other reed types |
| SXG / SXR / SER | Naturfernes Ziergewässer / Rückhaltebecken naturfern / naturnahes Regenrückhaltebecken | VSF / VSM / VSP | Fußgängerfläche und Radwege / Städtischer Platz / Parkplatz |

Function complexes (overlay level): EP Park/Grünanlage (EPI intensiv gepflegt, EPA/EPK kleinteilig naturnah/naturfern, EPL alter Landschaftspark …), EH Hausgarten (EHZ Ziergarten, EHG Gemüsegarten, EHO Obstgarten, EHN Naturgarten …), EK Kleingartenanlage, EF Friedhof, ES Sportplatz, ET Spielplatz; B… building structure types. Tree size classes by DBH: 7–<13 cm, 13–<50 cm, 50–<70 cm, ≥ 70 cm.

Berlin (Umweltatlas 06.02 "Grün- und Freiflächenbestand", Biotoptypenliste): categories only from search snippets (Park/Grünfläche, Stadtplatz/Promenade, Friedhof, Kleingarten, Brachfläche, Sportnutzung, Baumschule/Gartenbau, Wald, Gewässer …), **S**; colour values not verified (pages returned navigation only).

---

## 7. Other de-facto European conventions (short notes)

### 7.1 Ordnance Survey MasterMap Topography Layer (GB, 1:1,250–1:10,000)

Features carry `descriptiveGroup` (Building, Buildings Or Structure, Built Environment, General Feature, General Surface, Glasshouse, Height Control, Historic Interest, Inland Water, Landform, Natural Environment, Network Or Polygon Closing Geometry, Path, Political Or Administrative, Rail, Road Or Track, Roadside, Structure, Terrain And Height, Tidal Water, Unclassified), `descriptiveTerm` and `make` (Manmade, Multiple, Natural, Unclassified, Unknown), S (OS documentation assistant answer on https://docs.os.uk/os-downloads/products/maps-and-imagery-portfolio/os-mastermap-topography-layer/os-mastermap-topography-layer-technical-specification/enumerations.md). Feature codes seen (V, feature-code lookup table of the same specification): 10021 Building · 10053 General Surface / Multi Surface · 10054 General Surface / Step · 10056 General Surface · 10062 Glasshouse · 10089 Inland Water · 10111 Natural Environment · 10123 Path / Step · 10172 Road Or Track · 10183 Roadside · 10185 Structure · 10096 Landform / Slope · 10099 Landform / Cliff · 10203 Tidal Water / Foreshore · points 10048 Positioned Nonconiferous Tree, 10050 Positioned Coniferous Tree, 10051 Positioned Boulder.

**Official OS style, "Outdoor style" colour values**: V (parsed from the OS workbook https://github.com/OrdnanceSurvey/OSMM-Topography-Layer-stylesheets → `Schema version 9/Stylesheets/Colour Values/OSMM-Topography-Layer-Colour-Values.xlsx`, Open Government Licence 3.0; assignment rules from `Schema version 9/SQL/PostGIS/Array/topographicarea_createtable_array.sql`):

| style_code | style_description | Hex | Assigned when |
|---|---|---|---|
| 1 | Multi Surface Fill (private gardens) | `#eeefda` | descriptiveTerm = Multi Surface |
| 34 | Building Fill | `#dcd7c6` (outline `#bbb49c`) | descriptiveGroup contains Building |
| 45 | Glasshouse Fill | `#f3f9f4` | descriptiveGroup = Glasshouse |
| 44 | Structure Fill | `#e7c9c8` | descriptiveGroup contains Structure |
| 35 / 46 | Natural Fill / Landform Natural Fill | `#e4efda` | General Surface or Landform with make = Natural |
| 36 / 48 | Manmade Fill / Landform Manmade Fill | `#f2f2e9` | General Surface with make = Manmade or Unknown |
| 37 | Road Or Track Fill | `#fcfdff` | Road Or Track, make = Manmade |
| 9 / 10 / 41 | Track Fill / Step Fill / Path Fill | `#dcdcdb` | term Track, Step; group Path |
| 38 / 39 | Roadside Natural / Roadside Manmade Fill | `#dde6d5` / `#f2f2e9` | Roadside by make |
| 42 / 43 | Rail Manmade / Rail Natural Fill | `#cccbcb` / `#dce5d3` | Rail by make |
| 13 / 14 / 15 / 17 / 18 | Mixed Woodland / Nonconiferous Tree / Coniferous Tree / Orchard / Coppice Or Osiers Fill | `#cee6bd` | term contains (Non)coniferous Trees (also "(Scattered)"), Orchard, Coppice Or Osiers |
| 16 | Agricultural Land Fill | `#d6edcf` | term Agricultural Land |
| 19 / 23 / 24 | Scrub / Rough Grassland / Heath Fill | `#e2efce` | term Scrub, Rough Grassland, Heath |
| 25 / 29 | Saltmarsh / Marsh Fill | `#e4f3f4` | term Marsh Reeds Or Saltmarsh, Saltmarsh, Marsh |
| 30 | Reeds Fill | `#aadeef` | term Reeds |
| 11 / 40 / 47 | Canal / Inland Water / Tidal Water Fill | `#aadeef` (water lines `#7ed2e0`) | term Canal; groups Inland Water, Tidal Water |
| 26 | Sand Fill | `#f4f0d3` | term Sand |
| 27 | Mud Fill | `#e8e4dd` | term Mud |
| 20 / 21 / 22 / 28 | Boulders / Rock / Scree / Shingle Fill | `#eaeae4` | terms Boulders, Rock (also "(Scattered)"), Scree, Shingle |
| 31 | Foreshore Fill | `#eaead3` | term Foreshore |
| 32 / 33 | Slope / Cliff Fill | `#669966` / `#666666`, "refer to a dashed line pattern rather than a solid fill" | term Slope / Cliff |
| 3 / 5 / 12 | Road Bridge / Bridge / Footbridge Fill | `#e6dddd` / `#d6d2d2` / `#e8cfcc` | term Bridge by group; Footbridge |
| 2 / 8 | Archway / Pylon Fill | `#dcd7c6` / `#eee8d3` | |
| 99 | Unclassified | `#f8f6f0` | fallback |
| points | Positioned (non)coniferous tree, other point symbols | `#8c8c8c` | |
| text | colour codes 1–5 | `#655314`, `#318fae`, `#857660`, `#296314`, `#ff98ff` | |

### 7.2 OS MasterMap Greenspace Layer: V (https://docs.os.uk/os-downloads/products/land-and-terrain-portfolio/os-mastermap-greenspace-layer/os-mastermap-greenspace-layer-technical-specification/code-lists-and-enumerations/function.md and …/form.md)

A two-axis typology worth copying: **function** (use) × **form** (cover).
- `primaryFunction` / `secondaryFunction`: Allotments Or Community Growing Spaces · Amenity – Residential or Business · Amenity – Transport · Bowling Green · Camping Or Caravan Park · Cemetery · Golf Course · Institutional Grounds · Land Use Changing · Natural · Other Sports Facility · Play Space · Playing Field · Private Garden · Public Park or Garden · Religious Grounds · School Grounds · Tennis Court.
- `primaryForm` / `secondaryForm`: Woodland ("trees with an area larger than 0.1 hectares and width greater than 5m") · Open Semi-Natural (scrub, heath, rough grassland) · Inland Water · Beach Or Foreshore · Manmade Surface · Multi Surface ("multiple surface types, such as grass, decking and hard standing making up a private garden polygon").

### 7.3 OS NGD land cover code lists: V (https://docs.os.uk/osngd/code-lists/code-lists-overview/landcovertieravalue.md, …/landcovertierbvalue.md)

Tier A: Excavated Or Deposited · Made · Mineral · Multiple (residential gardens) · Open Vegetation · Open Vegetation And Mineral · Trees · Under Construction · Water. Tier B: Bare Earth Or Grass · Boulders · Coniferous Trees · Deposited · Excavated · Heath · Inter Tidal · **Made Sealed** ("solid material that is bonded") · **Made Unsealed** ("enhanced by the addition of a loose material") · Made Unknown · Marsh · Mud · Non-Coniferous Trees · Orchard · Peat · Reeds · Residential Garden · Rock · Rough Grassland · Saltmarsh · Sand · Scattered Boulders · Scattered Coniferous Trees · Scattered Non-Coniferous Trees · Scattered Rock · Scree · Scrub · Shingle · Solar Panels · Under Construction · Vineyard. Thresholds: trees "generally spaced not more than 30m apart" (else "scattered"); boulders > 0.2 m.

### 7.4 GeoDanmark (DK municipal/state base data): partly V

Specification 6.0.2 (11.07.2024), 7.0 in consultation (V, https://www.geodanmark.dk/anvend-geodata/specifikation/). Object types named on that page: Plads, Hede, Skov, Sø, Dige, Vandløbskant, Brønddæksel, Nedløbsrist, Telemast (V). The full object catalogue (help-system frameset at https://www.geodanmark.nu/Spec6/…) could not be read; further object names (BYGNING, VÅDOMRÅDE, KRAT/BEVOKSNING, TRÆ, TRÆGRUPPE, LEVENDE HEGN, SAND/KLIT, RÅSTOFOMRÅDE, GARTNERI, BEGRAVELSESOMRÅDE, REKREATIVT OMRÅDE, VEJKANT, PARKERING …) are **R**.

### 7.5 Finland: partly V

NLS Topographic Database (Maastotietokanta): nationwide, 1:10,000 (positional accuracy class 1:5,000–1:10,000), themes transport, buildings and structures, administrative borders, names, land use, waters, elevation; SHP/GML/GeoPackage, CC BY 4.0, object model as Excel (V, https://www.maanmittauslaitos.fi/kartat-ja-paikkatieto/asiantuntevalle-kayttajalle/tuotekuvaukset/maastotietokanta-0). Feature-class codes and the municipal conventions (city base map "kantakartta", Helsinki register of public areas, national green-area maintenance classification with classes R/A/M/S/E) are **R**: not verified.

### 7.6 Germany: ALKIS/ATKIS

Not researched in this stream (presumably covered elsewhere). **R:** ALKIS "tatsächliche Nutzung" (object types 41001–44007, e.g. 43001 Landwirtschaft, 43002 Wald, 43003 Gehölz, 41008 Sport-, Freizeit- und Erholungsfläche, 41009 Friedhof) with the GeoInfoDok signature catalogue is the German counterpart of BGT / AV / DKM and must be in the crosswalk set.

---

## 8. Implications for the element catalog

Element names below are **my proposals** (not taken from any source). "16" marks classes of the current style sheet.

### 8.1 (a) OSM tag → generic element

| Proposed element | In sheet | OSM area tags (first match wins, top to bottom) | Lines / points | Attribute refinements |
|---|---|---|---|---|
| `lawn` | 16 Lawn | `landuse=grass` · `landuse=village_green` · `landuse=recreation_ground` · `leisure=common` · `leisure=pitch`/`golf`/`playground` with `surface=grass` · `landcover=grass` | path with `surface=grass` | – |
| `meadow` | 16 Meadow | `landuse=meadow` (incl. `meadow=agricultural`, `pasture`, `paddock`) · `natural=grassland` · `landuse=greenfield` | – | grazed variant from `meadow=pasture/paddock` |
| `wildflower_meadow` | 16 Wildflower meadow | `landuse=meadow` + `meadow=wildflower` | – | – |
| `rough_grass_ruderal` | new | `landuse=brownfield` · `meadow=transitional` · `meadow=perpetual` · `natural=fell` | – | – |
| `flower_bed` (perennials, annuals) | new | `landuse=flowerbed` · `landcover=flowerbed` | `man_made=planter`, `barrier=planter` (point: planter) | – |
| `ornamental_planting_mixed` | new | `landuse=greenery` · `landcover=greenery` · `leisure=garden` (non-private, no finer data) | – | `garden:type`, `garden:style` |
| `garden_private_mosaic` | new | `leisure=garden` + `garden:type=residential/private` (or `access=private`) | – | – |
| `shrub` | 16 Shrub | `natural=scrub` (native/wild variant) · `natural=shrubbery` (planted variant) · `landcover=scrub/shrubbery/bushes` | `natural=shrub` (point) | `shrubbery:density`, `leaf_cycle` |
| `hedge` | new | `natural=shrubbery` + `shrubbery:density=dense` · `barrier=hedge` + `area=yes` (discouraged but exists) | `barrier=hedge` (line; width from `width`) | `height`, `leaf_cycle`, clipped vs free from `shrubbery:shape` |
| `woodland` | 16 Woodland | `natural=wood` · `landuse=forest` · `landcover=trees` · `wetland=swamp` (wet variant) | – | `leaf_type` → broadleaved / needleleaved / mixed; `leaf_cycle` |
| `tree` | 16 Urban trees | – | `natural=tree` (point), `natural=tree_row` (line), `natural=tree_stump` | `diameter_crown`, `circumference`, `height`, `leaf_type`, `leaf_cycle`, `denotation`, `genus`/`species` |
| `orchard` / `vineyard` / `nursery` | new | `landuse=orchard` (`meadow=meadow_orchard` → meadow orchard) · `landuse=vineyard` · `landuse=plant_nursery` | – | `trees=*`, `crop=*` (R) |
| `allotment_kitchen_garden` | new | `landuse=allotments` · `leisure=garden` + `garden:style=kitchen` · `garden:type=community` | – | – |
| `arable` | new | `landuse=farmland` | – | – |
| `heath` | new | `natural=heath` · `natural=moor` | – | – |
| `reed_wetland` | 16 Reed/wetland | `natural=wetland` + `wetland=reedbed` (reed) · `marsh`, `wet_meadow`, `fen` (marsh variant) · `bog`, `string_bog` (bog variant) · `saltmarsh` | – | variant by `wetland=*` |
| `water` | 16 Water body | `natural=water` (+ `water=pond/lake/reservoir/basin/river/canal/stream/moat/ditch/drain/reflecting_pool…`) · `leisure=swimming_pool` (pool variant) · `landuse=basin` with `basin=retention` (pond) · `landuse=reservoir` | `waterway=river/stream/canal/drain/ditch` (lines), `natural=spring`, `amenity=fountain` (points) | standing vs flowing from `water=*`; `intermittent=yes` |
| `suds_basin_swale` (rain garden, swale, dry basin) | new | `landuse=basin` with `basin=infiltration` or `detention` (or no `basin=*` and `intermittent=yes`) | `waterway=ditch/drain` with `intermittent=yes` (R) | – |
| `bare_soil` | 16 Soil/bare ground | `landuse=construction` · `landuse=logging` · `natural=mud` (wet variant) · `landcover=bare_ground` · areas with `surface=ground/dirt/earth/mud` | paths with those surfaces | – |
| `sand` | 16 Sand | `natural=sand` · `natural=beach` (+`surface=sand` or none) · `natural=dune` · playground/pitch with `surface=sand` · golf bunker | – | – |
| `gravel` | 16 Gravel | `natural=shingle` · `natural=beach` + `surface=gravel/pebbles` · `landcover=gravel` · areas/ways with `surface=gravel/pebblestone/shells` | – | – |
| `compacted_waterbound` | new | areas/ways with `surface=compacted/fine_gravel/unpaved` | – | – |
| `rock_scree` | new | `natural=bare_rock` · `natural=scree` · `landuse=quarry` · `surface=rock` | `natural=rock/stone` (point: boulder), `natural=cliff` (line) | – |
| `mulch` | new | areas/ways with `surface=woodchips` | – | – |
| paved elements | 16 (5 classes) | `highway=pedestrian`/`footway`/`service` + `area=yes`, `amenity=parking`, `man_made=courtyard`, `leisure=pitch/playground/track`, `highway=*` lines, element chosen **only by `surface=*`**, see 8.2 | kerbs `barrier=kerb` | `paving_stones:*`, `surface:colour` |
| `building` | new (context) | `building=*` (except below) | – | `roof:material`, `green_roof` |
| `glasshouse` | new | `building=greenhouse/conservatory` · `landuse=greenhouse_horticulture` | – | – |
| `green_roof` | new | `building=*` + (`green_roof=yes` or `roof:material=grass/plants/roof_greening`) · `leisure=garden` + `garden:type=roof_garden` | `garden:type=green_wall` (line: green wall) | – |
| `wall` / `fence` / `retaining_wall` | new (lines) | – | `barrier=wall/city_wall` · `barrier=fence` · `barrier=retaining_wall` · `man_made=embankment` (slope hachures) | `height`, `material` (R) |
| furniture points | new | – | `amenity=bench/waste_basket/drinking_water/fountain/bicycle_parking/bbq`, `highway=street_lamp`, `leisure=picnic_table`, `barrier=bollard`, `man_made=planter/manhole/flagpole/insect_hotel` | – |
| function overlays (no own surface) | – | `leisure=park`, `landuse=cemetery`, `leisure=playground/dog_park/nature_reserve`, `landuse=residential…` | – | draw as outline/tint/label only; never as the surface element |

### 8.2 (a) Complete `surface=*` → element table (all wiki-documented values; aliases from taginfo)

| `surface=` | Proposed element | In sheet | Remark |
|---|---|---|---|
| `asphalt`, `chipseal` (+ alias `bitmac`) | `asphalt` | 16 Asphalt | chipseal = coarser speckle variant |
| `concrete` (+ alias `cement`) | `concrete` | 16 Concrete | cast in place, joint lines |
| `concrete:plates` | `concrete` variant "plates" | 16 Concrete | large slab grid |
| `concrete:lanes` | `concrete` variant "two-track" | 16 Concrete | two strips with grass/gravel between |
| `paving_stones` (+ aliases `interlock`, `flagstone`, `concrete:tiles`) | `paving_light` by default; `paving_dark` if `surface:colour` is dark; `clinker_brick` if `paving_stones:material=brick` | 16 Paving (light/dark) | pattern from `paving_stones:pattern` (herringbone, basket_weave, stack_bond …) and `:shape` |
| `paving_stones:lanes` | paving variant "two-track" | 16 | |
| `bricks` (+ alias `brick`, `brick_weave`) | `clinker_brick` | new | BGT `gebakken klinkers` |
| `sett`, `cobblestone` (+ `cobblestone:flattened`) | `sett` (natural-stone sett) | new | regular small blocks, open joints |
| `unhewn_cobblestone` | `sett` variant "rounded cobble" | new | |
| `stepping_stones` | `paving_light` variant "stepping stones" | 16 | slabs on lawn/gravel background |
| `tiles` | `paving_light` variant "tiles" | 16 | mostly indoor |
| `grass_paver` | `grass_paver` | new | BGT `grasklinkers`; semi-sealed |
| `paved` | `paved_generic` → render as `paving_light`, neutral | 16 | lowest-information fallback |
| `wood` (+ alias `boardwalk`) | `wood_decking` | 16 Wood decking | |
| `metal`, `metal_grid`, `fibre_reinforced_polymer_grate` (+ alias `steel`) | `metal_grating` | new | bridges, ramps |
| `resin_bound` | `gravel` variant "bound" (or `compacted_waterbound`) | 16 Gravel | permeable |
| `unpaved` | `unpaved_generic` → render as `compacted_waterbound` | new | fallback |
| `compacted` | `compacted_waterbound` | new | the typical park path (wassergebundene Decke) |
| `fine_gravel` | `compacted_waterbound` (wiki: inconsistent, fine loose gravel or alias of compacted) | new | |
| `gravel` | `gravel` | 16 Gravel | |
| `pebblestone` | `gravel` variant "pebbles" | 16 | rounded 2–8 cm |
| `shells` | `gravel` variant "shells" (light) | 16 | BGT `schelpen` |
| `rock` (+ aliases `bare_rock`, `rocky`, `rocks`, `stone`) | `rock_scree` | new | `stone` is ambiguous (16,940 uses) |
| `ground`, `dirt`, `earth` (+ aliases `soil`, `bare_ground`, `natural`, `trail`) | `bare_soil` | 16 Soil/bare ground | |
| `mud` | `bare_soil` variant "wet" | 16 | |
| `laterite` | `bare_soil` variant "red" | 16 | non-European |
| `grass` (+ alias `turf`, `moss`) | `lawn` | 16 Lawn | |
| `sand` (+ alias `dirt/sand`) | `sand` | 16 Sand | |
| `woodchips` (+ alias `mulch`) | `mulch` | new | BGT `boomschors` |
| `clay` | `clay_court` | new | BGT half verhard `gravel` (crushed brick) |
| `tartan`, `acrylic`, `plastic`, `rubber`, `carpet` (+ aliases `rubbercrumb`, `decoturf`) | `synthetic_sport_play` | new | colour often red/green/blue → honour `surface:colour` |
| `artificial_turf` | `artificial_turf` | new | BGT `kunststof` |
| `snow`, `ice`, `salt` | none (neutral fallback) | – | out of scope |
| values with `;` or `/` | split, use first token | – | e.g. `ground;grass` |
| anything else (`hard`, `mixed`, …) | fallback by `highway` type / unknown style | – | |

### 8.3 (b) Elements present in BGT, Swiss AV and the UK metric list but missing from the 16-class sheet

| Missing element (proposal) | NL BGT / IMGeo | CH AV | UK metric / UKHab | Also in |
|---|---|---|---|---|
| Hedge (line + area; clipped/native/ornamental) | VegetatieObject `haag`; `houtwal` | `schmale_bestockte_Flaeche` | Native hedgerow, species-rich, with trees; non-native and ornamental hedgerow | Hamburg ZSS, ZSH, HH… |
| Tree row / line of trees; tree size classes | VegetatieObject `boom` | `wichtiger_Einzelbaum` | Line of trees; Urban tree with 4 DBH classes (0.0041–0.0765 ha) | OSM tree_row; Hamburg HEA |
| Ornamental shrub planting vs native scrub | `heesters`, `struikrozen` vs `struiken`, `bosplantsoen` | `uebrige_bestockte` | Introduced shrub vs mixed/bramble/hawthorn scrub | TypoCH 5.3.0; Phase 1 J1.4 vs A2 |
| Ground cover / perennial and flower beds / planters | `bodembedekkers`, `planten` | (`Gartenanlage`) | Ground level planters; flower bed (UKHab 846) | OSM flowerbed; Hamburg ZZ |
| Private garden mosaic ("unknown mix") | `erf` | `Gartenanlage` | Vegetated garden / Unvegetated garden | OS Multi Surface / Residential Garden; AT Gärten (NS 52) |
| Allotments, kitchen garden, vegetable bed | (bouwland `vollegrondsteelt`) | `uebrige_Intensivkultur` | Allotments | OSM allotments; Hamburg ZN, EK |
| Orchard (high-/low-stem), vineyard, nursery, arable | `fruitteelt` (+4 plus types), `boomteelt`, `bouwland` | `Reben`, `Intensivkultur`, `Acker_Wiese_Weide` | Traditional orchard, intensive orchard, cropland types | AT NS 40, 53, 48 |
| Rough grass / ruderal / tall herb; vacant land | `grasland overig` (partly) | `uebrige_humusierte` | Ruderal/ephemeral; vacant or derelict land; open mosaic habitat; bracken | Hamburg AP, AK; TypoCH 7.1 |
| Grass quality split (species-poor amenity vs species-rich) | `gras- en kruidachtigen` | – | Modified grassland (Low) vs other neutral grassland (Medium) + condition score | Hamburg ZRT vs ZRW |
| Heath | `heide` | – | heathland types | OSM heath |
| Marsh / bog / fen separate from reed | `moeras` vs `rietland`, `kwelder` | `Hoch_Flachmoor` vs `Schilfguertel` | fens, reedbeds, saltmarsh | AT Feuchtgebiete |
| Bank / shore strip, mud flat | `oever, slootkant`, `slik` | `Uferverbauung` | – | AT Gewässerrandflächen |
| Ditch, dry ditch, swale, rain garden, SuDS basin | `greppel, droge sloot` | `Rinnsal` | Ditches; bioswale; rain garden; sustainable drainage system | Hamburg SER/SXR |
| Pool / basin / ornamental pond | overig bouwwerk `bassin` | `Wasserbecken`, `Brunnen` | Ornamental lake or pond; ponds (non-priority) | OSM reflecting_pool, swimming_pool |
| Green roof (biodiverse / intensive / other), green wall | – | – | Biodiverse / intensive / other green roof; facade-bound / ground-based green wall | OSM green_roof; Hamburg YDG |
| Semi-sealed: grass pavers | `grasklinkers` | – | (artificial unvegetated, unsealed surface) | OSM grass_paver |
| Water-bound / compacted surface | `half verhard` | `uebrige_befestigte` | Artificial unvegetated, unsealed surface | OSM compacted; Hamburg YFW |
| Shells, rubble, bark mulch, crushed-brick court | `schelpen`, `puin`, `boomschors`, `gravel` | – | – | OSM shells, woodchips, clay |
| Synthetic surfaces, artificial turf | `kunststof` | – | artificial sports pitches (UKHab 821) | OSM tartan, artificial_turf |
| Paving material split: clinker, concrete block, slab, ornamental, natural-stone sett, vegetated joints | `gebakken klinkers`, `betonstraatstenen`, `tegels`, `sierbestrating`, `beton element` | – | – | Hamburg YFP, YFR; TypoCH 7.2.2 |
| Rock, scree, boulders | `zand` sub-types only | `Fels`, `Geroell_Sand` | Other inland rock and scree | OS Boulders/Rock/Scree |
| Dune, salt marsh, glacier, wooded pasture | `duin`, `kwelder` | `Gletscher_Firn`, `Wytweide` | coastal types | regional extension pack |
| Extraction / landfill / construction / "transition" state | `transitie` | `Abbau_Deponie` | Land use changing (OS), development site | OSM construction/brownfield |
| Built context: building, underground building, glasshouse, open roof, wall, retaining wall, steps, bridge, railway, traffic island, verge, pavement | `pand`, `overig bouwwerk`, `scheiding`, `kunstwerkdeel`, `berm`, `verkeerseiland`, wegdeel functions | `Gebaeude`, `Mauer`, `wichtige_Treppe`, `Trottoir`, `Verkehrsinsel`, `Bahn` | Developed land; sealed surface; built linear features | all models |

Structural consequences: (1) every national model separates **cover/material** from **function/use** (BGT fysiekVoorkomen vs functie; OS form vs function; Hamburg Z/Y elements vs E/B complexes; OSM surface vs landuse/leisure), the catalog needs both axes, with function drawn as overlay. (2) Every model has a **"mixed garden / yard" class** because gardens are not surveyed in detail; the library needs a deliberate mosaic element instead of pretending to know. (3) All need an **"unknown / in transition"** element. (4) The models at this scale carry **lines and points** (hedge, wall, fence, tree, steps, fountain) as first-class objects. (5) A score-linked catalog (UK metric) needs **condition and size attributes** (grass quality, tree DBH class, roof type), so elements should accept modifiers rather than multiply classes.

### 8.4 (c) Lessons from the colour systems

1. **Pastel is the established answer at parcel scale.** OS "Outdoor style" uses near-white tints (building `#dcd7c6`, natural surface `#e4efda`, made surface `#f2f2e9`, trees `#cee6bd`, water `#aadeef`); BGT ships a dedicated *pastel* and an *achtergrond* set next to the saturated standard; the Swiss base plan colours only five things and applies 50–65 % transparency. OSM Carto documents its fills in Lch with L 80–99 and chroma up to 35 (vegetation 20–35, built-up land uses 0–16). A house palette with L ≈ 80–95 and low chroma is squarely inside the convention.
2. **Few hues, many textures.** OSM Carto reuses `@grass` for six wetland and garden types and distinguishes them by pattern; BGT standard uses two greens plus PNG tree/reed patterns; Swiss AV distinguishes forest, other wooded and wooded pasture only by dot spacing (2 / 4 / 8 / 16 mm at 1:1,000 in the Grundbuchplan); Phase 1 uses solid vs hatch in the same hue for semi-natural vs planted. This supports the library's "pastel fill + light hand-drawn texture" concept: hue for the family, texture for the type.
3. **Conventional hue families are stable across countries:** water light blue (`#aad3df` OSM, `#B3E6FF` CH, `#bee8ff` BGT, `#aadeef` OS); woodland a darker/yellower green than grass; heath pink-violet (BGT `#fcb3fb`, `#e3dce7`; LBP `#F57AB6`) or olive (OSM `#d6d99f`); sand pale yellow (`#f5e9c6`, `#ffff99`, `#f4f0d3`, `#fdf6bb`); arable pale cream (`#eef0d5`, `#ffffcc`, `#FFFFDC`); ruderal/tall herb violet (LBP `#E8BEFF`); buildings pink-red in cadastral tradition (CH `#FFBFBF`, LBP `#FFC8C8`, BGT `#cc0000`, AT red outline) versus neutral beige-grey in topographic web maps (OSM `#d9d0c9`, OS `#dcd7c6`, PDOK `#d3d3d3`). Offer both building conventions as themes.
4. **Paved surfaces are almost never differentiated by colour** in the official systems: BGT draws all paving classes white (roads by function), Swiss AV white/grey, OS two greys. Material appears only as pattern (BGT pastel: dot marks for open/half paving). The catalog's asphalt / concrete / light / dark paving split is therefore an *addition* to the conventions and should rest on texture plus a narrow grey-warm range, so base maps still read as "paved".
5. **Outline rules matter as much as fills:** BGT strokes each polygon in its fill colour to hide slivers and draws roads casing-then-fill so adjacent carriageway parts merge; Swiss AV encodes hard edges (solid) vs soft vegetation edges (dashed) and draws soft covers without outline in colour mode. Recommended default: no dark outline between soft vegetation elements, thin solid outline on built edges.
6. **State modifiers instead of new classes:** LBP uses diagonal hatch in the target colour for "to be planted", dot overlay for "extensified", red ring/X for protected/lost trees; the UKHab community style uses a lighter tint for "proposed". A generic `state` modifier (existing / proposed / removed / protected) fits the library better than duplicating elements.
7. **Function as overlay:** BGT "functioneel gebied" is drawn as boundary plus centre icon; Austria places a glyph at the polygon reference point; OSM Carto tints parks/cemeteries underneath. Provide icon-in-polygon and outline-only renderings for function classes, and a monochrome "cadastral" theme (line + glyph, no fills) for AT/CH-style plans.
8. **Scale guards:** BGT pastel rules stop at 1:5,000; Swiss symbol sizes are defined at a reference scale with fixed factors (1.4/1.2, 1.0, 0.7); OSM Carto grows tree markers by zoom because crown data are rarely mapped. Textures in the library should be specified in map units at a reference scale (1:500 or 1:1,000) with scale factors, and tree crowns should use `diameter_crown` when present.
9. **Background use:** LBP prescribes 35 % transparency over aerial imagery; BP-AV is explicitly "Planhintergrund … der mit zusätzlicher Thematik überlagert werden kann". Ship a semi-transparent "over orthophoto" variant of every fill.

---

## 9. Open points (not verified: do not treat as facts)

| # | Item | What is missing |
|---|---|---|
| 1 | UKHab official colour palette / QGIS and ArcGIS style files | Licence-gated download (registration and acceptance of terms); only a community palette was seen. Also unclear whether v2.1 is released (documentation page) or still in consultation (home page). Redistribution rights for UKHab codes/names in an open library need a legal check. |
| 2 | Statutory biodiversity metric vs small sites metric | The full statutory list is now in 6.3 (resolved). Remaining: several SSM guide rows differ from the statutory tool (urban tree Low vs Medium, other green roof Medium vs Low, native hedgerow Medium vs Low, sedum roof printed as "Intensive green roof"), SSM simplification or misprints, not established; the SSM tool workbook 1.2.3 and the condition-assessment criteria per habitat (xlsx, July 2025) were not opened. |
| 3 | BGT/IMGeo remaining gaps | Land-use, building and water colours of the achtergrondvisualisatie are confirmed against the Geonovum SLDs; its road colours come from PDOK's style only (`achtergrond_infra*.sld` not read). The icoon-, lijngerichte, omtrekgerichte and plan visualisations and the tree/hedge symbols were not read. IMGeo "plus" lists come from the objectenhandboek, not from the normative catalogue tables; street-furniture object types (bak, bord, paal, put, straatmeubilair …) not collected. |
| 4 | DMAV 1.0 INTERLIS enumerations | Model files not found at guessed URLs; DMAV names taken from the 2024 drafting instruction only. |
| 5 | Austria: official fill colours | None exist in the BEV documents read; the legal "Zeichenschlüssel" of the Vermessungsverordnung was not read. Colours inside `BEV0.qgz` not inspected. |
| 6 | German city green-space typology with published colours (Berlin Umweltatlas, Berlin Biotoptypen, municipal GRIS) | Berlin pages returned navigation only; Hamburg key has no RGB table in the pages read. BfN "Planzeichen für die Landschaftsplanung" not checked. Berlin Biotopflächenfaktor factors not verified. |
| 7 | GeoDanmark object catalogue, Finnish feature classes and municipal conventions, ALKIS | See 7.4–7.6 (R). |
| 8 | OSM extraction risk | Wiki and style pages were read through an extraction model; long lists (leisure, man_made, building, barrier) may have lost rare values. `amenity=vending_machine`, `area:highway`, `trees=*`, `crop=*`, `material=*` are R. taginfo counts were fetched for `surface`, `landcover`, `landuse` and `natural` only. |
| 9 | LBP-Musterlegendenkatalog misprints | Laubwald RGB printed as 0/168/132 (contradicts swatch); Naturschutzgebiet printed as "02300/169". |
| 10 | swisstopo national-map RGB values | Only the Light Base Map vector style was read (via extraction model). |
