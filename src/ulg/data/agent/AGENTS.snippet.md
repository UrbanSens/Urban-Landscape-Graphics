<!-- ulg:start -->
## Maps and landscape graphics

This project draws maps with the UrbanSens style library `ulg` (Urban Landscape Graphics).

- Never invent colours, hatches or symbols for landscape elements; look them up with `ulg find "<text>" --json` or `ulg show <element> --json`, or in Python with `ulg.element(id)`.
- Map source data to elements with crosswalks (`ulg.classify(gdf, "osm" | "alkis" | "clc" | ...)`), not with hand-written dictionaries.
- Render with `ulg.render_svg(gdf, scale=...)` or `ulg.plot(gdf)`; use `theme=` for official conventions (planzv, alkis, basemap, bfn, osm, mono).
- Run `ulg agent` for the full guide.
<!-- ulg:end -->
