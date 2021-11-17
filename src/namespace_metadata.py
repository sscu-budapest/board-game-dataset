import datetime as dt

from sscutils import (
    BaseEntity,
    CompositeTypeBase,
    IndexBase,
    ScruTable,
    TableFeaturesBase,
)

class BoardGame(BaseEntity):
    """Board Game from BGG"""
    pass

class Person(BaseEntity):
    pass

class User(Person):
    """BGG User"""
    pass

class BoardGameIndex(IndexBase):
    bg_id = int

class UserIndex(IndexBase):
    user_id = str

class SubgroupIndex(IndexBase):
    subgroup_id = str

class MicrobadgeIndex(IndexBase):
    micro_id = int

class RatingIndex(IndexBase):
    bg_id = BoardGameIndex
    user_name = UserIndex

class PlayerNumberType(CompositeTypeBase):
    minplayers = int
    maxplayers = int

class RatingInfoType(CompositeTypeBase):
    num_ratings = int
    avg_rating = float
    bgg_rating = float
    stddev_rating = float

class WeightType(CompositeTypeBase):
    num_weights = int
    average_weight = float

class OwnershipType(CompositeTypeBase):
    owned = int
    trading = int
    wanting = int
    wishing = int

class BoardGameFeatures(TableFeaturesBase):
    bgg_rank = int
    name = str
    url = str
    release_year = int
    description = str
    player_num = PlayerNumberType
    rating_info = RatingInfoType
    weight = WeightType
    ownership = OwnershipType

class UserFeatures(TableFeaturesBase):
    user_url = str
    country = str

class RatingFeatures(TableFeaturesBase):
    rating = float
    date = dt.datetime
    comment_text = str
    summary_item_meta = str

class SubgroupFeatures(TableFeaturesBase):
    subgroup_type = str
    subgroup_name = str
    description = str

class MicrobadgeFeatures(TableFeaturesBase):
    micro_name = str
    micro_url = str
    description = str

class UserMicroFeatures(TableFeaturesBase):
    user_id = UserIndex
    microbadge = MicrobadgeIndex

class BGSubgroupFeatures(TableFeaturesBase):
    bg_id = BoardGameIndex
    subgroup_id = SubgroupIndex
    value = str

boardgame_table = ScruTable(BoardGameFeatures, BoardGameIndex, subject_of_records= BoardGame)
user_table = ScruTable(UserFeatures, UserIndex, subject_of_records= User)
rating_table = ScruTable(RatingFeatures, RatingIndex)
subgroup_table = ScruTable(SubgroupFeatures, SubgroupIndex)
microbadge_table = ScruTable(MicrobadgeFeatures, MicrobadgeIndex)
user_micro_table = ScruTable(UserMicroFeatures)
bg_subgroup_table = ScruTable(BGSubgroupFeatures)

