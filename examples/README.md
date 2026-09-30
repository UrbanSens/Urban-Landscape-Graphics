# Examples

Run from the repository root after `pip install -e ".[all]"` (or with `PYTHONPATH=src`). Output goes
to `examples/output/`, which is not tracked.

| Script | Shows |
|---|---|
| [`quickstart.py`](quickstart.py) | look-ups, a 1:1500 plan as SVG and PNG, a German legend, the PlanZV and black-and-white themes, a Matplotlib figure |
| [`osm_workflow.py`](osm_workflow.py) | OpenStreetMap tags → elements, stacked areas and street centre lines, `flatten`, site figures |
| [`indicators.py`](indicators.py) | sealing shares, biotope area factor, runoff, albedo, green space, canopy; DIN 18920 root zones |
| [`qgis_project.py`](qgis_project.py) | QGIS styles and a GeoPackage ready to open, also in PlanZV colours |
| [`themes.py`](themes.py) | the demo quarter in all seven themes |
| [`web/`](web/) | a MapLibre page with the demo quarter and the OSM block: `python examples/web/build.py`, then `python -m http.server 8765 --directory examples/web` |

`data/osm_sample.geojson` is an invented block tagged like OpenStreetMap (no OSM data, no licence
obligations); `data/make_osm_sample.py` regenerates it.
