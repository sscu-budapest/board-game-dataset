import pandas as pd
from colassigner import get_all_cols
from sscutils import dump_dfs_to_tables

import src.namespace_metadata as ns


def update_data(data_root = "C:/programozas/bgg/data/final_table"):

    boardgame_df = pd.read_json(f"{data_root}/boardgame.json")
    rating_df = pd.read_json(f"{data_root}/rating.json")
    user_df = pd.read_json(f"{data_root}/user.json")
    bg_subgroup_df = pd.read_json(f"{data_root}/bg_subgroup.json")
    microbadge_df = pd.read_json(f"{data_root}/microbadge.json")
    subgroup_df = pd.read_json(f"{data_root}/subgroup.json")
    user_micro_df = pd.read_json(f"{data_root}/user_micro.json")

    dump_dfs_to_tables(
        None,
        [
            (boardgame_df, ns.boardgame_table),
            (rating_df, ns.rating_table),
            (user_df, ns.user_table),
            (bg_subgroup_df, ns.bg_subgroup_table),
            (microbadge_df, ns.microbadge_table),
            (subgroup_df, ns.subgroup_table),
            (user_micro_df, ns.user_micro_table)
        ],
    )