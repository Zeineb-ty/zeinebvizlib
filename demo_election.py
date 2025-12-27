import zeinebviz

csv_url = "https://raw.githubusercontent.com/binorassocies/rimdata/refs/heads/main/data/results_elections_rim_2019-2024.csv"
shp_path = r"data\mrshape\mrt_admbnda_adm2_ansade_20240327.shp"

zeinebviz.styled_election_map_bokeh(
    csv_url=csv_url,
    shp_path=shp_path,
    region_col_shp="ADM2_EN",
    region_col_csv="moughataa",
    candidate_col="candidate",
    votes_col="nb_votes",
    title="Election map (ADM2 Moughataa) – winner votes"
)
