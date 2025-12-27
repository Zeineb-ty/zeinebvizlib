import pandas as pd
import geopandas as gpd

from bokeh.plotting import figure, show
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool
from bokeh.palettes import Viridis256


def styled_election_map_bokeh(
    csv_url: str,
    shp_path: str,
    region_col_shp: str = "ADM2_EN",
    region_col_csv: str = "moughataa",
    candidate_col: str = "candidate",
    votes_col: str = "nb_votes",
    title: str = "Election map (ADM2 Moughataa) – winner votes",
):
    """
    Interactive election map (Bokeh) – ADM2 (moughataa)
    Good practices:
    - One map
    - One color scale
    - One geometry per moughataa (dissolved)
    - Candidates only (no parties)
    """

    # ------------------------------------------------------------------
    # 1) Load CSV
    df = pd.read_csv(csv_url)

    # ------------------------------------------------------------------
    # 2) Keep only real candidates (exclude parties/lists)
    cand = df[candidate_col].fillna("").astype(str)

    mask_org = cand.str.lower().str.contains(
        r"(parti|union|rassemblement|alliance|mouvement|front|coalition|liste)",
        regex=True
    )

    mask_person_like = (
        cand.str.contains(r"\b(Ould|ولد)\b", regex=True) |
        (cand.str.split().str.len() >= 2)
    )

    df = df[~mask_org & mask_person_like].copy()

    # ------------------------------------------------------------------
    # 3) Winner per moughataa
    df_winner = (
        df.sort_values(votes_col, ascending=False)
          .groupby(region_col_csv, as_index=False)
          .first()
          .rename(columns={
              region_col_csv: "region",
              candidate_col: "winner",
              votes_col: "winner_votes"
          })
    )

    # ------------------------------------------------------------------
    # 4) Load shapefile ADM2
    gdf = gpd.read_file(shp_path)
    gdf = gdf[[region_col_shp, "geometry"]].rename(
        columns={region_col_shp: "region"}
    )

    # ------------------------------------------------------------------
    # 5) DISSOLVE geometries 
    gdf = gdf.dissolve(by="region", as_index=False)

    # ------------------------------------------------------------------
    # 6) Merge geometry + election results
    gdf = gdf.merge(df_winner, on="region", how="left")
    gdf["winner"] = gdf["winner"].fillna("N/A")
    gdf["winner_votes"] = gdf["winner_votes"].fillna(0)

    # ------------------------------------------------------------------
    # 7) GeoJSON for Bokeh
    source = GeoJSONDataSource(geojson=gdf.to_json())

    # ------------------------------------------------------------------
    # 8) Single global color scale
    low = float(gdf["winner_votes"].min())
    high = float(gdf["winner_votes"].max())
    if high <= low:
        high = low + 1

    mapper = LinearColorMapper(palette=Viridis256, low=low, high=high)

    # ------------------------------------------------------------------
    # 9) Plot
    p = figure(
        title=title,
        tools="pan,wheel_zoom,reset,save",
        active_scroll="wheel_zoom",
        width=950,
        height=650,
    )
    p.grid.grid_line_alpha = 0.3

    p.patches(
        "xs", "ys",
        source=source,
        fill_color={"field": "winner_votes", "transform": mapper},
        fill_alpha=0.85,
        line_color="white",
        line_width=0.7,
    )

    # ------------------------------------------------------------------
    # 10) Hover (FINAL, CLEAN)
    hover = HoverTool(tooltips=[
        ("Moughataa", "@region"),
        ("Winner candidate", "@winner"),
        ("Votes", "@winner_votes{0,0}")
    ])
    p.add_tools(hover)

    # ------------------------------------------------------------------
    # 11) Color bar
    color_bar = ColorBar(color_mapper=mapper, label_standoff=8)
    p.add_layout(color_bar, "right")

    show(p)
