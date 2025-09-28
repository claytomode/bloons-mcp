
import asyncio
import json
from typing import Any

import httpx
from pydantic import BaseModel, ConfigDict, Field, ValidationError

# --- Pydantic Response Models ---
class Btd6race(BaseModel):
    """Pydantic model for _btd6race"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """Race Event ID"""

    name: str | None = Field(default=None, alias='name')
    """Race Name"""

    start: int | float | None = Field(default=None, alias='start')
    """Race start time in unix epoch milliseconds"""

    end: int | float | None = Field(default=None, alias='end')
    """Race end time in unix epoch milliseconds"""

    total_scores: int | float | None = Field(default=None, alias='totalScores')
    """The total number of scores submitted"""

    leaderboard: str | None = Field(default=None, alias='leaderboard')
    """URL to leaderboard data"""

    metadata: str | None = Field(default=None, alias='metadata')
    """URL to full Race metadata"""


class Btd6raceleaderboard(BaseModel):
    """Pydantic model for _btd6raceleaderboard"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    display_name: str | None = Field(default=None, alias='displayName')
    """The display name for this user"""

    score: int | float | None = Field(default=None, alias='score')
    """The Race score in milliseconds"""

    score_parts: list | None = Field(default=None, alias='scoreParts')
    """When the leaderboard includes multiple scores they will be included here"""

    submission_time: int | float | None = Field(default=None, alias='submissionTime')
    """The epoch time in milliseconds when the score was submitted (-1 when not available)"""

    profile: str | None = Field(default=None, alias='profile')
    """URL to the players public profile"""


class Btd6challengedocument(BaseModel):
    """Pydantic model for _btd6challengedocument"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    name: str | None = Field(default=None, alias='name')
    """Challenge Name"""

    created_at: int | float | None = Field(default=None, alias='createdAt')
    """Challenge creation time in unix epoch milliseconds"""

    id: str | None = Field(default=None, alias='id')
    """Unique Challenge ID"""

    creator: str | None = Field(default=None, alias='creator')
    """URL to the creators profile"""

    game_version: str | None = Field(default=None, alias='gameVersion')
    """Version of the game this challenge was created in"""

    map: str | None = Field(default=None, alias='map')
    """Map Name"""

    map_url: str | None = Field(default=None, alias='mapURL')
    """URL to the map icon"""

    mode: str | None = Field(default=None, alias='mode')
    """Game Mode"""

    difficulty: str | None = Field(default=None, alias='difficulty')
    """Challenge Difficulty"""

    disable_double_cash: str | None = Field(default=None, alias='disableDoubleCash')
    """true when Double Cash Mode is disabled"""

    disable_instas: str | None = Field(default=None, alias='disableInstas')
    """true when Instas are disabled"""

    disable_mk: str | None = Field(default=None, alias='disableMK')
    """true when Monkey Knowledge is disabled"""

    disable_powers: str | None = Field(default=None, alias='disablePowers')
    """true when Powers are disabled"""

    disable_selling: str | None = Field(default=None, alias='disableSelling')
    """true when Selling is disabled"""

    starting_cash: int | float | None = Field(default=None, alias='startingCash')
    """Starting cash value"""

    lives: int | float | None = Field(default=None, alias='lives')
    """Starting lives"""

    max_lives: int | float | None = Field(default=None, alias='maxLives')
    """Maximum allowed lives"""

    max_towers: int | float | None = Field(default=None, alias='maxTowers')
    """Maximum towers allowed"""

    max_paragons: int | float | None = Field(default=None, alias='maxParagons')
    """Maximum paragons allowed"""

    start_round: int | float | None = Field(default=None, alias='startRound')
    """Starting round"""

    end_round: int | float | None = Field(default=None, alias='endRound')
    """End Round"""

    plays: int | float | None = Field(default=None, alias='plays')
    """Total number of attempts"""

    wins: int | float | None = Field(default=None, alias='wins')
    """Total number of wins"""

    losses: int | float | None = Field(default=None, alias='losses')
    """Total number of losses"""

    upvotes: int | float | None = Field(default=None, alias='upvotes')
    """Total number of upvotes"""

    plays_unique: int | float | None = Field(default=None, alias='playsUnique')
    """Total number of unique attempts"""

    restarts: int | float | None = Field(default=None, alias='restarts')
    """Total number of restarts"""

    wins_unique: int | float | None = Field(default=None, alias='winsUnique')
    """Total number of unique player wins"""

    losses_unique: int | float | None = Field(default=None, alias='lossesUnique')
    """Total number of unique player losses"""

    ability_cooldown_reduction_multiplier: int | float | None = Field(default=None, alias='abilityCooldownReductionMultiplier')
    """Ability Cooldown Multiplier"""

    least_cash_used: int | float | None = Field(default=None, alias='leastCashUsed')
    """Least Cash Used Setting"""

    least_tiers_used: int | float | None = Field(default=None, alias='leastTiersUsed')
    """Least Tier Used"""

    no_continues: int | float | None = Field(default=None, alias='noContinues')
    """Are continues enabled"""

    seed: int | float | None = Field(default=None, alias='seed')
    """The RNG seed"""

    removeable_cost_multiplier: int | float | None = Field(default=None, alias='removeableCostMultiplier')
    """Blocker removal cost multiplier"""

    round_sets: list[str] | None = Field(default=None, alias='roundSets')
    """Bloon Round Information"""

    powers_data: dict[str, Any] | None = Field(default=None, alias='_powers')
    """[!] Power restrictions"""

    bloon_modifiers_data: dict[str, Any] | None = Field(default=None, alias='_bloonModifiers')
    """[!] Bloon Modifiers"""

    towers_data: dict[str, Any] | None = Field(default=None, alias='_towers')
    """[!] Tower restrictions"""


class Btd6boss(BaseModel):
    """Pydantic model for _btd6boss"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """Boss Event ID"""

    name: str | None = Field(default=None, alias='name')
    """Boss Name"""

    start: int | float | None = Field(default=None, alias='start')
    """Boss start time in unix epoch milliseconds"""

    end: int | float | None = Field(default=None, alias='end')
    """Boss end time in unix epoch milliseconds"""

    boss_type: str | None = Field(default=None, alias='bossType')
    """The name of the Boss"""

    boss_type_url: str | None = Field(default=None, alias='bossTypeURL')
    """Boss Icon"""

    total_scores_standard: int | float | None = Field(default=None, alias='totalScores_standard')
    """Total scores in the Standard leaderboard"""

    total_scores_elite: int | float | None = Field(default=None, alias='totalScores_elite')
    """Total scores in the Elite leaderboard"""

    leaderboard_standard_players_1: str | None = Field(default=None, alias='leaderboard_standard_players_1')
    """URL to Elite Difficulty Single Player leaderboard data"""

    leaderboard_elite_players_1: str | None = Field(default=None, alias='leaderboard_elite_players_1')
    """URL to Elite Difficulty Single Player leaderboard data"""

    metadata_standard: str | None = Field(default=None, alias='metadataStandard')
    """URL to full metadata for Standard Mode"""

    metadata_elite: str | None = Field(default=None, alias='metadataElite')
    """URL to full metadata for Elite Mode"""

    scoring_type: str | None = Field(default=None, alias='scoringType')
    """[Deprecated] - Use normalScoringType and eliteScoringType."""

    normal_scoring_type: str | None = Field(default=None, alias='normalScoringType')
    """The score type for this leaderboard when playing standard mode."""

    elite_scoring_type: str | None = Field(default=None, alias='eliteScoringType')
    """No description available."""


class Btd6bossleaderboard(BaseModel):
    """Pydantic model for _btd6bossleaderboard"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    display_name: str | None = Field(default=None, alias='displayName')
    """The display name for this user"""

    score: int | float | None = Field(default=None, alias='score')
    """The Boss score in milliseconds (lower is better)"""

    score_parts: list | None = Field(default=None, alias='scoreParts')
    """When the leaderboard includes multiple scores they will be included here"""

    submission_time: int | float | None = Field(default=None, alias='submissionTime')
    """The epoch time in milliseconds"""

    profile: str | None = Field(default=None, alias='profile')
    """URL to the players public profile"""


class Btd6userprofile(BaseModel):
    """Pydantic model for _btd6userprofile"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    display_name: str | None = Field(default=None, alias='displayName')
    """Current User Display Name"""

    rank: int | float | None = Field(default=None, alias='rank')
    """Player Rank"""

    veteran_rank: int | float | None = Field(default=None, alias='veteranRank')
    """Player Veteran Rank"""

    achievements: str | None = Field(default=None, alias='achievements')
    """Number of achievements unlocked"""

    most_experienced_monkey: str | None = Field(default=None, alias='mostExperiencedMonkey')
    """Most Experienced Monkey"""

    highest_round: int | float | None = Field(default=None, alias='highestRound')
    """[Deprecated] Use gameplay.highestRound"""

    avatar: str | None = Field(default=None, alias='avatar')
    """User avatar icon"""

    banner: str | None = Field(default=None, alias='banner')
    """User banner icon"""

    avatar_url: str | None = Field(default=None, alias='avatarURL')
    """URL to avatar icon"""

    banner_url: str | None = Field(default=None, alias='bannerURL')
    """URL to banner icon"""

    followers: int | float | None = Field(default=None, alias='followers')
    """Number of followers"""

    bloons_popped: dict[str, Any] | None = Field(default=None, alias='bloonsPopped')
    """Bloon Pop Stats"""

    gameplay: dict[str, Any] | None = Field(default=None, alias='gameplay')
    """Gameplay Stats"""

    heroes_placed: dict[str, Any] | None = Field(default=None, alias='heroesPlaced')
    """Hero Stats"""

    towers_placed: dict[str, Any] | None = Field(default=None, alias='towersPlaced')
    """Tower Stats"""

    stats: dict[str, Any] | None = Field(default=None, alias='stats')
    """A number of miscellaneous stats"""

    boss_badges_normal: dict[str, Any] | None = Field(default=None, alias='bossBadgesNormal')
    """Normal Boss Badges"""

    boss_badges_elite: dict[str, Any] | None = Field(default=None, alias='bossBadgesElite')
    """Normal Boss Badges"""

    medals_single_player_data: dict[str, Any] | None = Field(default=None, alias='_medalsSinglePlayer')
    """[!] Single Player Medals"""

    medals_multiplayer_data: dict[str, Any] | None = Field(default=None, alias='_medalsMultiplayer')
    """[!] Multiplayer Medals"""

    medals_boss_data: dict[str, Any] | None = Field(default=None, alias='_medalsBoss')
    """[!] Boss Medals"""

    medals_boss_elite_data: dict[str, Any] | None = Field(default=None, alias='_medalsBossElite')
    """[!] Elite Boss Medals"""

    medals_ct_local_data: dict[str, Any] | None = Field(default=None, alias='_medalsCTLocal')
    """[!] CT Local Medals"""

    medals_ct_global_data: dict[str, Any] | None = Field(default=None, alias='_medalsCTGlobal')
    """[!] CT Global Medals"""

    medals_race_data: dict[str, Any] | None = Field(default=None, alias='_medalsRace')
    """[!] Race Medals"""


class Btd6challengetype(BaseModel):
    """Pydantic model for _btd6challengetype"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    type: str | None = Field(default=None, alias='type')
    """Challenge Filter Name"""

    challenges: str | None = Field(default=None, alias='challenges')
    """URL to view challenges with this filter"""


class Btd6challenge(BaseModel):
    """Pydantic model for _btd6challenge"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    name: str | None = Field(default=None, alias='name')
    """Challenge Filter Name"""

    created_at: int | float | None = Field(default=None, alias='createdAt')
    """Challenge creation time in unix epoch milliseconds"""

    id: str | None = Field(default=None, alias='id')
    """Unique Challenge ID"""

    creator: str | None = Field(default=None, alias='creator')
    """URL to the creators profile"""

    metadata: str | None = Field(default=None, alias='metadata')
    """URL to the full challenge information"""


class Btd6ct(BaseModel):
    """Pydantic model for _btd6ct"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """CT Event ID"""

    start: int | float | None = Field(default=None, alias='start')
    """Event start time in unix epoch milliseconds"""

    end: int | float | None = Field(default=None, alias='end')
    """Event end time in unix epoch milliseconds"""

    total_scores_player: int | float | None = Field(default=None, alias='totalScores_player')
    """Total scores in the Player leaderboard"""

    total_scores_team: int | float | None = Field(default=None, alias='totalScores_team')
    """Total scores in the Team leaderboard"""

    tiles: str | None = Field(default=None, alias='tiles')
    """URL to Information about each CT tile"""

    leaderboard_player: str | None = Field(default=None, alias='leaderboard_player')
    """URL to Top Player leaderboard"""

    leaderboard_team: str | None = Field(default=None, alias='leaderboard_team')
    """URL to Top Team leaderboard"""


class Btd6cttile(BaseModel):
    """Pydantic model for _btd6cttile"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """The CT ID"""

    tiles: list | None = Field(default=None, alias='tiles')
    """A list of CT tiles"""


class Btd6ctleaderboardplayer(BaseModel):
    """Pydantic model for _btd6ctleaderboardplayer"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    display_name: str | None = Field(default=None, alias='displayName')
    """The display name for this user"""

    score: int | float | None = Field(default=None, alias='score')
    """The CT score"""

    profile: str | None = Field(default=None, alias='profile')
    """URL to the players public profile"""


class Btd6ctleaderboardteam(BaseModel):
    """Pydantic model for _btd6ctleaderboardteam"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    display_name: str | None = Field(default=None, alias='displayName')
    """The display name for this Team"""

    score: int | float | None = Field(default=None, alias='score')
    """The CT score"""

    profile: str | None = Field(default=None, alias='profile')
    """URL to the team public profile"""

    group: str | None = Field(default=None, alias='group')
    """URL to the team's group leaderboard'"""


class Btd6guildprofile(BaseModel):
    """Pydantic model for _btd6guildprofile"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    name: str | None = Field(default=None, alias='name')
    """Guild Name"""

    owner: str | None = Field(default=None, alias='owner')
    """URL to the Owners public profile"""

    num_members: int | float | None = Field(default=None, alias='numMembers')
    """Number of players in Team"""

    status: str | None = Field(default=None, alias='status')
    """Status of the Team (OPEN, FILTERED, DISBANDED, CLOSED)"""

    banner: str | None = Field(default=None, alias='banner')
    """Banner Icon Name"""

    frame: str | None = Field(default=None, alias='frame')
    """Frame Icon Name"""

    icon: str | None = Field(default=None, alias='icon')
    """Team Icon Name"""

    banner_url: str | None = Field(default=None, alias='bannerURL')
    """URL to banner icon"""

    frame_url: str | None = Field(default=None, alias='frameURL')
    """URL to frame icon"""

    icon_url: str | None = Field(default=None, alias='iconURL')
    """URL to icon"""


class Btd6odyssey(BaseModel):
    """Pydantic model for _btd6odyssey"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """Odyssey Event ID"""

    name: str | None = Field(default=None, alias='name')
    """Odyssey Name"""

    description: str | None = Field(default=None, alias='description')
    """Odyssey Description"""

    start: int | float | None = Field(default=None, alias='start')
    """Odyssey start time in unix epoch milliseconds"""

    end: int | float | None = Field(default=None, alias='end')
    """Odyssey end time in unix epoch milliseconds"""

    metadata_easy: Any | None = Field(default=None, alias='metadata_easy')
    """URL to Easy Mode Settings"""

    metadata_medium: Any | None = Field(default=None, alias='metadata_medium')
    """URL to Medium Mode Settings"""

    metadata_hard: Any | None = Field(default=None, alias='metadata_hard')
    """URL to Hard Mode Settings"""


class Btd6odysseymetadata(BaseModel):
    """Pydantic model for _btd6odysseymetadata"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """Odyssey Event ID"""

    is_extreme: str | None = Field(default=None, alias='isExtreme')
    """True when the Odyssey is extreme"""

    max_monkey_seats: int | float | None = Field(default=None, alias='maxMonkeySeats')
    """Maximum seats on the boat"""

    max_monkeys_on_boat: int | float | None = Field(default=None, alias='maxMonkeysOnBoat')
    """Maximum towers"""

    max_power_slots: int | float | None = Field(default=None, alias='maxPowerSlots')
    """Maximum number of powers"""

    starting_health: int | float | None = Field(default=None, alias='startingHealth')
    """Voyage starting health"""

    rewards_data: dict[str, Any] | None = Field(default=None, alias='_rewards')
    """[!] Rewards list"""

    available_powers_data: dict[str, Any] | None = Field(default=None, alias='_availablePowers')
    """[!] Powers that can be chosen"""

    available_towers_data: dict[str, Any] | None = Field(default=None, alias='_availableTowers')
    """[!] Towers that can be chosen"""

    default_powers_data: dict[str, Any] | None = Field(default=None, alias='_defaultPowers')
    """[!] Default event powers"""

    default_towers_data: dict[str, Any] | None = Field(default=None, alias='_defaultTowers')
    """[!] Defauly Towers"""

    maps: Any | None = Field(default=None, alias='maps')
    """URL to map information"""


class Btd6usersave(BaseModel):
    """Pydantic model for _btd6usersave"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    latest_game_version: str | None = Field(default=None, alias='latestGameVersion')
    """The latest version of the game that this player has played"""

    tower_xp: dict[str, Any] | None = Field(default=None, alias='towerXP')
    """Tower XP"""

    acquired_upgrades: dict[str, Any] | None = Field(default=None, alias='acquiredUpgrades')
    """Upgrades Unlocked"""

    acquired_knowledge: dict[str, Any] | None = Field(default=None, alias='acquiredKnowledge')
    """Upgrades Monkey Knowledge"""

    unlocked_towers: dict[str, Any] | None = Field(default=None, alias='unlockedTowers')
    """Towers Unlocked"""

    unlocked_heroes: dict[str, Any] | None = Field(default=None, alias='unlockedHeroes')
    """Towers Heros Unlocked"""

    unlocked_heros: dict[str, Any] | None = Field(default=None, alias='unlockedHeros')
    """[Deprecated] - Use unlockedHeroes"""

    unlocked_skins: dict[str, Any] | None = Field(default=None, alias='unlockedSkins')
    """Towers Hero Skins Unlocked"""

    games_played: int | float | None = Field(default=None, alias='gamesPlayed')
    """Total Games Played"""

    powers: dict[str, Any] | None = Field(default=None, alias='powers')
    """Powers Unlocked"""

    powers_pro: dict[str, Any] | None = Field(default=None, alias='powersPro')
    """Powers Unlocked"""

    insta_towers: dict[str, Any] | None = Field(default=None, alias='instaTowers')
    """Insta Towers (tier & count)"""

    monkey_money: int | float | None = Field(default=None, alias='monkeyMoney')
    """Current Monkey Money"""

    xp: int | float | None = Field(default=None, alias='xp')
    """Current XP"""

    rank: int | float | None = Field(default=None, alias='rank')
    """Current Rank"""

    veteran_xp: int | float | None = Field(default=None, alias='veteranXp')
    """Current Veteran XP"""

    veteran_rank: int | float | None = Field(default=None, alias='veteranRank')
    """Current Veteran Rank"""

    trophies: int | float | None = Field(default=None, alias='trophies')
    """Current Trophies"""

    lifetime_trophies: int | float | None = Field(default=None, alias='lifetimeTrophies')
    """Total trophies earned"""

    lifetime_team_trophies: int | float | None = Field(default=None, alias='lifetimeTeamTrophies')
    """Total Team Trophies Earned"""

    knowledge_points: int | float | None = Field(default=None, alias='knowledgePoints')
    """Current MK Points"""

    primary_hero: str | None = Field(default=None, alias='primaryHero')
    """Current Selected Hero"""

    achievements_claimed: list | None = Field(default=None, alias='achievementsClaimed')
    """Achievements Claimed"""

    highest_seen_round: int | float | None = Field(default=None, alias='highestSeenRound')
    """Highest Ever Round"""

    daily_reward_count: int | float | None = Field(default=None, alias='dailyRewardCount')
    """Daily Rewards Claimed"""

    total_daily_challenges_completed: int | float | None = Field(default=None, alias='totalDailyChallengesCompleted')
    """Total DC's completed"""

    consecutive_daily_challenges_completed: int | float | None = Field(default=None, alias='consecutiveDailyChallengesCompleted')
    """Current number of consecutive days a DC has been completed"""

    total_races_entered: int | float | None = Field(default=None, alias='totalRacesEntered')
    """Total Races Entered"""

    challenges_played: int | float | None = Field(default=None, alias='challengesPlayed')
    """Total Challenges Played"""

    challenges_shared: int | float | None = Field(default=None, alias='challengesShared')
    """Total Challenges Shared"""

    total_completed_odysseys: int | float | None = Field(default=None, alias='totalCompletedOdysseys')
    """Total Odysseys Complete"""

    unlocked_big_bloons: bool | None = Field(default=None, alias='unlockedBigBloons')
    """true when Big Bloons has been unlocked"""

    big_bloons_active: bool | None = Field(default=None, alias='bigBloonsActive')
    """true when Big Bloons is active"""

    unlocked_small_bloons: bool | None = Field(default=None, alias='unlockedSmallBloons')
    """true when Small Bloons has been unlocked"""

    small_bloons_active: bool | None = Field(default=None, alias='smallBloonsActive')
    """true when Small Bloons is active"""

    seen_big_towers: bool | None = Field(default=None, alias='seenBigTowers')
    """true when Big Bloons has been unlocked"""

    big_towers_active: bool | None = Field(default=None, alias='bigTowersActive')
    """true when Big Bloons is active"""

    unlocked_small_towers: bool | None = Field(default=None, alias='unlockedSmallTowers')
    """true when Small Bloons has been unlocked"""

    small_towers_active: bool | None = Field(default=None, alias='smallTowersActive')
    """true when Small Bloons is active"""

    unlocked_small_bosses: bool | None = Field(default=None, alias='unlockedSmallBosses')
    """true when Small Bosses has been unlocked"""

    small_bosses_active: bool | None = Field(default=None, alias='smallBossesActive')
    """true when Small Bosses is active"""

    named_monkeys: dict[str, Any] | None = Field(default=None, alias='namedMonkeys')
    """Named Monkey Names (note: Ninja Kiwi is not responsible for these names but they can be reported at https://support.ninjakiwi.com)"""

    collection_event_crates_opened: int | float | None = Field(default=None, alias='collectionEventCratesOpened')
    """Collect event crates opened"""

    continues_used: int | float | None = Field(default=None, alias='continuesUsed')
    """Continues Used"""

    trophy_store_items: dict[str, Any] | None = Field(default=None, alias='trophyStoreItems')
    """Trophy Store Items Purchased"""

    map_progress: dict[str, Any] | None = Field(default=None, alias='mapProgress')
    """A list of maps completed split by single/coop mode and difficulty."""

    rogue_legends: dict[str, Any] | None = Field(default=None, alias='rogueLegends')
    """Rogue Legends Stats"""

    quests: list | None = Field(default=None, alias='quests')
    """Quest Information"""


class Btd6maptype(BaseModel):
    """Pydantic model for _btd6maptype"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    type: str | None = Field(default=None, alias='type')
    """Map Filter Name"""

    maps: str | None = Field(default=None, alias='maps')
    """URL to view maps with this filter"""


class Btd6map(BaseModel):
    """Pydantic model for _btd6map"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    name: str | None = Field(default=None, alias='name')
    """Map Filter Name"""

    created_at: int | float | None = Field(default=None, alias='createdAt')
    """Map creation time in unix epoch milliseconds"""

    id: str | None = Field(default=None, alias='id')
    """Unique Map ID"""

    creator: str | None = Field(default=None, alias='creator')
    """URL to the creators profile"""

    metadata: str | None = Field(default=None, alias='metadata')
    """URL to the full map information"""


class Btd6mapdocument(BaseModel):
    """Pydantic model for _btd6mapdocument"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    name: str | None = Field(default=None, alias='name')
    """Map Name"""

    created_at: int | float | None = Field(default=None, alias='createdAt')
    """Map creation time in unix epoch milliseconds"""

    id: str | None = Field(default=None, alias='id')
    """Unique Map ID"""

    creator: str | None = Field(default=None, alias='creator')
    """URL to the creators profile"""

    game_version: str | None = Field(default=None, alias='gameVersion')
    """Version of the game this map was created in"""

    map: str | None = Field(default=None, alias='map')
    """Map Name"""

    map_url: str | None = Field(default=None, alias='mapURL')
    """URL to the map icon"""

    plays: int | float | None = Field(default=None, alias='plays')
    """Total number of attempts"""

    wins: int | float | None = Field(default=None, alias='wins')
    """Total number of wins"""

    losses: int | float | None = Field(default=None, alias='losses')
    """Total number of losses"""

    upvotes: int | float | None = Field(default=None, alias='upvotes')
    """Total number of upvotes"""

    plays_unique: int | float | None = Field(default=None, alias='playsUnique')
    """Total number of unique attempts"""

    restarts: int | float | None = Field(default=None, alias='restarts')
    """Total number of restarts"""

    wins_unique: int | float | None = Field(default=None, alias='winsUnique')
    """Total number of unique player wins"""

    losses_unique: int | float | None = Field(default=None, alias='lossesUnique')
    """Total number of unique player losses"""


class Battles2hom(BaseModel):
    """Pydantic model for _battles2hom"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """HoM Event ID"""

    name: str | None = Field(default=None, alias='name')
    """Season Name"""

    start: int | float | None = Field(default=None, alias='start')
    """Event start time in unix epoch milliseconds"""

    end: int | float | None = Field(default=None, alias='end')
    """Event end time in unix epoch milliseconds"""

    live: bool | None = Field(default=None, alias='live')
    """When 'true', this is the live in-game HoM event"""

    total_scores: int | float | None = Field(default=None, alias='totalScores')
    """The total number of scores submitted"""

    leaderboard: str | None = Field(default=None, alias='leaderboard')
    """URL to leaderboard data"""


class Battles2homleaderboard(BaseModel):
    """Pydantic model for _battles2homleaderboard"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    display_name: str | None = Field(default=None, alias='displayName')
    """The display name for this user"""

    score: int | float | None = Field(default=None, alias='score')
    """The HoM score"""

    profile: str | None = Field(default=None, alias='profile')
    """URL to the players public profile"""

    currently_in_ho_m: bool | None = Field(default=None, alias='currentlyInHoM')
    """When true, the player is currenty in the HoM. This might be false if the user has been demoted from HoM by finishing in the demotion zone of an arena league"""


class Battles2userprofile(BaseModel):
    """Pydantic model for _battles2userprofile"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    display_name: str | None = Field(default=None, alias='displayName')
    """User Display Name"""

    is_vip: bool | None = Field(default=None, alias='is_vip')
    """VIP Status (deprecated)"""

    is_club_member: bool | None = Field(default=None, alias='is_club_member')
    """Club Membership Status"""

    equipped_avatar: str | None = Field(default=None, alias='equippedAvatar')
    """Selected avatar"""

    equipped_avatar_url: str | None = Field(default=None, alias='equippedAvatarURL')
    """Avatar Icon"""

    equipped_banner: str | None = Field(default=None, alias='equippedBanner')
    """Selected Banner"""

    equipped_banner_url: str | None = Field(default=None, alias='equippedBannerURL')
    """Banner Icon"""

    equipped_border: str | None = Field(default=None, alias='equippedBorder')
    """Selected Border"""

    equipped_border_url: str | None = Field(default=None, alias='equippedBorderURL')
    """Border Icon"""

    equipped_title: str | None = Field(default=None, alias='equippedTitle')
    """Selected Title"""

    casual_stats: dict[str, Any] | None = Field(default=None, alias='casualStats')
    """User Display Name"""

    ranked_stats: dict[str, Any] | None = Field(default=None, alias='rankedStats')
    """User Display Name"""

    badges_equipped: Any | None = Field(default=None, alias='badges_equipped')
    """Currently Equpped badges"""

    badges_all: Any | None = Field(default=None, alias='badges_all')
    """All Badges"""

    chests: list[str] | None = Field(default=None, alias='chests')
    """Pending Chests"""

    chests_opened: int | float | None = Field(default=None, alias='chestsOpened')
    """Total Chests Opened"""

    current_season: str | None = Field(default=None, alias='currentSeason')
    """The most recent season the user has played in"""

    current_season_highest_arena_index: int | float | None = Field(default=None, alias='currentSeason_highestArenaIndex')
    """Numerical Representation of Highest Arena Reached"""

    current_season_highest_arena: str | None = Field(default=None, alias='currentSeason_highestArena')
    """Highest Arena Reached during the most recent event"""

    current_season_trophies: int | float | None = Field(default=None, alias='currentSeason_trophies')
    """Current Season Trophies"""

    lifetime_highest_arena_index: int | float | None = Field(default=None, alias='lifetime_highestArenaIndex')
    """Numerical Representation of Highest Arena reached across all seasons"""

    lifetime_highest_arena: str | None = Field(default=None, alias='lifetime_highestArena')
    """Highest Arena reached across all seasons"""

    lifetime_trophies: int | float | None = Field(default=None, alias='lifetime_trophies')
    """Highest Trophies across all seasons"""

    matches: str | None = Field(default=None, alias='matches')
    """Recent match information"""

    homs: str | None = Field(default=None, alias='homs')
    """Recent HoM leaderboard scores"""

    in_guild: bool | None = Field(default=None, alias='inGuild')
    """True when the player is part of a guild"""

    guild: str | None = Field(default=None, alias='guild')
    """URL to guild profile"""

    accolades: Any | None = Field(default=None, alias='accolades')
    """All Accolades"""

    arena_league_tier: int | float | None = Field(default=None, alias='arenaLeagueTier')
    """The players current arena league. Tiers start at RBC=0 through HOM=8"""

    bloon_stats_data: dict[str, Any] | None = Field(default=None, alias='_bloonStats')
    """User Display Name"""

    towers_data: dict[str, Any] | None = Field(default=None, alias='_towers')
    """Tower Usage Stats"""


class Battles2usermap(BaseModel):
    """Pydantic model for _battles2usermap"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """A unique ID for this match"""

    gametype: str | None = Field(default=None, alias='gametype')
    """Match type"""

    map: str | None = Field(default=None, alias='map')
    """Map Name"""

    duration: int | float | None = Field(default=None, alias='duration')
    """Duration of the match in seconds"""

    end_round: int | float | None = Field(default=None, alias='endRound')
    """Round the match ended"""

    player_left: dict[str, Any] | None = Field(default=None, alias='playerLeft')
    """Details about the Left Side Player"""

    player_right: dict[str, Any] | None = Field(default=None, alias='playerRight')
    """Details about the Right Side Player"""

    map_url: str | None = Field(default=None, alias='mapURL')
    """Map Icon URL"""


class Battles2userhomrank(BaseModel):
    """Pydantic model for _battles2userhomrank"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    id: str | None = Field(default=None, alias='id')
    """HoM Event ID"""

    name: str | None = Field(default=None, alias='name')
    """HoM Season Name"""

    season: str | None = Field(default=None, alias='season')
    """HoM Season Index"""

    rank: int | float | None = Field(default=None, alias='rank')
    """The players current rank (1 = top)"""

    score: int | float | None = Field(default=None, alias='score')
    """The users current HoM score"""

    total_scores: int | float | None = Field(default=None, alias='totalScores')
    """Total players in the HoM"""

    leaderboard: str | None = Field(default=None, alias='leaderboard')
    """URL to the full leaderboard data"""


class Battles2guild(BaseModel):
    """Pydantic model for _battles2guild"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    name: str | None = Field(default=None, alias='name')
    """Guild Name"""

    num_members: int | float | None = Field(default=None, alias='numMembers')
    """The number of members currently in the guild"""

    status: str | None = Field(default=None, alias='status')
    """The current status of the guild. Can be OPEN|FILTERED|CLOSED|DISBANDED"""

    owner: str | None = Field(default=None, alias='owner')
    """The guild owner's profile"""

    tagline: str | None = Field(default=None, alias='tagline')
    """Guilds' tagline. Ninja Kiwi is not responsible for any content from services linked to from taglines"""

    banner: str | None = Field(default=None, alias='banner')
    """The Guild Banner"""

    banner_url: str | None = Field(default=None, alias='bannerURL')
    """The Guild Banner"""

    wars: str | None = Field(default=None, alias='wars')
    """Recent wars this guild has taken part in"""


class Battles2guildwar(BaseModel):
    """Pydantic model for _battles2guildwar"""
    model_config = ConfigDict(use_attribute_docstrings=True)

    event_state: str | None = Field(default=None, alias='eventState')
    """The curent event state. Can be NOT_STARTED,WAR_WARMUP,WAR_RUNNING,WAR_GRACE_PERIOD,WAR_FINISHED"""

    reward_state: str | None = Field(default=None, alias='rewardState')
    """After a war, you can check if rewards have been given out. Can be TOO_EARLY,PROCESSING,FINISHED"""

    tier: int | float | None = Field(default=None, alias='tier')
    """The guild's tier in this event"""

    next_match_epoch: int | float | None = Field(default=None, alias='nextMatchEpoch')
    """Unix epoch timestamp. This is when the daily matches will reset"""

    group_guild_leaderboard: Any | None = Field(default=None, alias='groupGuildLeaderboard')
    """An array of guild scores for all the guilds in this group"""

    member_contributions_leaderboard: Any | None = Field(default=None, alias='memberContributionsLeaderboard')
    """An array of scores. This represents the medallions won be each player in the current guild. This can include members not currently in the guild if they won a match but left during the event"""


# --- API Client Class ---
class NinjaKiwiAPI:
    """
    An asynchronous Python wrapper for the Bloons TD 6 and Battles 2 Data API.
    This wrapper was auto-generated from the API documentation.
    """
    def __init__(self, base_url="https://data.ninjakiwi.com"):
        self.client = httpx.AsyncClient(base_url=base_url, follow_redirects=True)

    async def _get_request(self, endpoint: str) -> Any | None:
        """Internal method to handle GET requests."""
        try:
            response = await self.client.get(endpoint)
            response.raise_for_status()
            data = response.json()
            if data and data.get('error'):
                print(f"API Error for {endpoint}: {data['error']}")
                return None
            return data.get('body')
        except httpx.HTTPStatusError as e:
            print(f"HTTP Error for endpoint '{endpoint}': {e}")
            return None
        except (httpx.RequestError, json.JSONDecodeError) as e:
            print(f"An error occurred with endpoint '{endpoint}': {e}")
            return None

    async def close(self):
        """Closes the httpx client."""
        await self.client.aclose()


    async def get_btd6_races(self) -> list[Btd6race] | None:
        """
        A list of all available Race events
        URL: https://data.ninjakiwi.com/btd6/races
        """
        endpoint = f"btd6/races"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6race.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_races_by_race_id_leaderboard(self, race_id: str) -> list[Btd6raceleaderboard] | None:
        """
        A race leaderboard
        URL: https://data.ninjakiwi.com/btd6/races/:raceID/leaderboard
        """
        endpoint = f"btd6/races/{race_id}/leaderboard"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6raceleaderboard.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_races_by_race_id_metadata(self, race_id: str) -> Btd6challengedocument | None:
        """
        Metadata for a race event
        URL: https://data.ninjakiwi.com/btd6/races/:raceID/metadata
        """
        endpoint = f"btd6/races/{race_id}/metadata"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6challengedocument.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_bosses(self) -> list[Btd6boss] | None:
        """
        List all available Boss events
        URL: https://data.ninjakiwi.com/btd6/bosses
        """
        endpoint = f"btd6/bosses"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6boss.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_bosses_by_boss_id_leaderboard_by_type_by_team_size(self, boss_id: str, type: str, team_size: str) -> list[Btd6bossleaderboard] | None:
        """
        Load a Boss event leaderboard
        URL: https://data.ninjakiwi.com/btd6/bosses/:bossID/leaderboard/:type/:teamSize
        """
        endpoint = f"btd6/bosses/{boss_id}/leaderboard/{type}/{team_size}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6bossleaderboard.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_bosses_by_boss_id_metadata_by_difficulty(self, boss_id: str, difficulty: str) -> Btd6challengedocument | None:
        """
        Load Boss event Metadata
        URL: https://data.ninjakiwi.com/btd6/bosses/:bossID/metadata/:difficulty
        """
        endpoint = f"btd6/bosses/{boss_id}/metadata/{difficulty}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6challengedocument.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_users_by_user_id(self, user_id: str) -> Btd6userprofile | None:
        """
        Load information about a BTD6 Player
        URL: https://data.ninjakiwi.com/btd6/users/:userID
        """
        endpoint = f"btd6/users/{user_id}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6userprofile.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_challenges(self) -> list[Btd6challengetype] | None:
        """
        List all available Challenge Filters
        URL: https://data.ninjakiwi.com/btd6/challenges
        """
        endpoint = f"btd6/challenges"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6challengetype.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_challenges_filter_by_challenge_filter(self, challenge_filter: str) -> list[Btd6challenge] | None:
        """
        List challenges based on a filter
        URL: https://data.ninjakiwi.com/btd6/challenges/filter/:challengeFilter
        """
        endpoint = f"btd6/challenges/filter/{challenge_filter}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6challenge.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_challenges_challenge_by_challenge_id(self, challenge_id: str) -> Btd6challengedocument | None:
        """
        Get specific information about a challenge
        URL: https://data.ninjakiwi.com/btd6/challenges/challenge/:challengeID
        """
        endpoint = f"btd6/challenges/challenge/{challenge_id}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6challengedocument.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_ct(self) -> list[Btd6ct] | None:
        """
        Load information about current and historical CT events
        URL: https://data.ninjakiwi.com/btd6/ct
        """
        endpoint = f"btd6/ct"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6ct.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_ct_by_ct_id_tiles(self, ct_id: str) -> Btd6cttile | None:
        """
        Load Information about the tiles from a CT event
        URL: https://data.ninjakiwi.com/btd6/ct/:ctID/tiles
        """
        endpoint = f"btd6/ct/{ct_id}/tiles"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6cttile.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_ct_by_ct_id_leaderboard_player(self, ct_id: str) -> list[Btd6ctleaderboardplayer] | None:
        """
        Load Top Player Leaderboard for a CT event
        URL: https://data.ninjakiwi.com/btd6/ct/:ctID/leaderboard/player
        """
        endpoint = f"btd6/ct/{ct_id}/leaderboard/player"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6ctleaderboardplayer.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_ct_by_ct_id_leaderboard_team(self, ct_id: str) -> list[Btd6ctleaderboardteam] | None:
        """
        Load Top Team Leaderboard for a CT event
        URL: https://data.ninjakiwi.com/btd6/ct/:ctID/leaderboard/team
        """
        endpoint = f"btd6/ct/{ct_id}/leaderboard/team"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6ctleaderboardteam.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_ct_by_ct_id_leaderboard_group_by_group_id(self, ct_id: str, group_id: str) -> list[Btd6ctleaderboardteam] | None:
        """
        Load information about a Team's group
        URL: https://data.ninjakiwi.com/btd6/ct/:ctID/leaderboard/group/:groupID
        """
        endpoint = f"btd6/ct/{ct_id}/leaderboard/group/{group_id}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6ctleaderboardteam.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_guild_by_guild_id(self, guild_id: str) -> Btd6guildprofile | None:
        """
        Load information about a BTD6 Team
        URL: https://data.ninjakiwi.com/btd6/guild/:guildID
        """
        endpoint = f"btd6/guild/{guild_id}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6guildprofile.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_odyssey(self) -> list[Btd6odyssey] | None:
        """
        A list of all available Odyssey events
        URL: https://data.ninjakiwi.com/btd6/odyssey
        """
        endpoint = f"btd6/odyssey"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6odyssey.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_odyssey_by_odyssey_id_by_difficulty(self, odyssey_id: str, difficulty: str) -> Btd6odysseymetadata | None:
        """
        A odyssey event metadata
        URL: https://data.ninjakiwi.com/btd6/odyssey/:odysseyID/:difficulty
        """
        endpoint = f"btd6/odyssey/{odyssey_id}/{difficulty}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6odysseymetadata.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_odyssey_by_odyssey_id_by_difficulty_maps(self, odyssey_id: str, difficulty: str) -> list[Btd6challengedocument] | None:
        """
        A odyssey event map information
        URL: https://data.ninjakiwi.com/btd6/odyssey/:odysseyID/:difficulty/maps
        """
        endpoint = f"btd6/odyssey/{odyssey_id}/{difficulty}/maps"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6challengedocument.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_save_by_oak_id(self, oak_id: str) -> Btd6usersave | None:
        """
        Load detailed information about a players' progress. Requires an OAK Token from the player
        URL: https://data.ninjakiwi.com/btd6/save/:oakID
        """
        endpoint = f"btd6/save/{oak_id}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6usersave.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_maps(self) -> list[Btd6maptype] | None:
        """
        List all map filters
        URL: https://data.ninjakiwi.com/btd6/maps
        """
        endpoint = f"btd6/maps"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6maptype.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_maps_filter_by_map_filter(self, map_filter: str) -> list[Btd6map] | None:
        """
        List maps based on a filter
        URL: https://data.ninjakiwi.com/btd6/maps/filter/:mapFilter
        """
        endpoint = f"btd6/maps/filter/{map_filter}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Btd6map.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_btd6_maps_map_by_map_id(self, map_id: str) -> Btd6mapdocument | None:
        """
        Get specific information about a map
        URL: https://data.ninjakiwi.com/btd6/maps/map/:mapID
        """
        endpoint = f"btd6/maps/map/{map_id}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Btd6mapdocument.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_battles2_homs(self) -> list[Battles2hom] | None:
        """
        A list of current Hall of Masters events
        URL: https://data.ninjakiwi.com/battles2/homs
        """
        endpoint = f"battles2/homs"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Battles2hom.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_battles2_homs_by_hom_id_leaderboard(self, hom_id: str) -> list[Battles2homleaderboard] | None:
        """
        A HoM leaderboard
        URL: https://data.ninjakiwi.com/battles2/homs/:homID/leaderboard
        """
        endpoint = f"battles2/homs/{hom_id}/leaderboard"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Battles2homleaderboard.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_battles2_users_by_user_id(self, user_id: str) -> Battles2userprofile | None:
        """
        Information about a Battles 2 Player
        URL: https://data.ninjakiwi.com/battles2/users/:userID
        """
        endpoint = f"battles2/users/{user_id}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Battles2userprofile.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_battles2_users_by_user_id_matches(self, user_id: str) -> list[Battles2usermap] | None:
        """
        Recent match information
        URL: https://data.ninjakiwi.com/battles2/users/:userID/matches
        """
        endpoint = f"battles2/users/{user_id}/matches"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Battles2usermap.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_battles2_users_by_user_id_homs(self, user_id: str) -> list[Battles2userhomrank] | None:
        """
        Recent hall of masters positions
        URL: https://data.ninjakiwi.com/battles2/users/:userID/homs
        """
        endpoint = f"battles2/users/{user_id}/homs"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, list):
            return None
        try:
            return [Battles2userhomrank.model_validate(item) for item in body]
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_battles2_guild_by_guild_id(self, guild_id: str) -> Battles2guild | None:
        """
        Information about a Battles 2 Guild/Clan
        URL: https://data.ninjakiwi.com/battles2/guild/:guildID
        """
        endpoint = f"battles2/guild/{guild_id}"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Battles2guild.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None



    async def get_battles2_guild_by_guild_id_war(self, guild_id: str) -> Battles2guildwar | None:
        """
        A list of recent wars the guild has taken part in
        URL: https://data.ninjakiwi.com/battles2/guild/:guildID/war
        """
        endpoint = f"battles2/guild/{guild_id}/war"
        body = await self._get_request(endpoint)
        if not body or not isinstance(body, dict):
            return None
        try:
            return Battles2guildwar.model_validate(body)
        except ValidationError as e:
            print(f"Pydantic validation error for endpoint '{endpoint}': {e}")
            return None

# --- Example Usage ---

async def main():
    """Example usage of the auto-generated NinjaKiwiAPI wrapper."""
    api = NinjaKiwiAPI()
    print("Welcome to the BTD6 API Wrapper Example!")
    print("-" * 40)

    try:
        print("\nFetching BTD6 races...")
        races = await api.get_btd6_races()

        if races and len(races) > 0:
            latest_race = races[0]
            print(f"Successfully fetched {len(races)} races. Latest race: '{latest_race.name}' (ID: {latest_race.id})")

            if latest_race.id:
                print(f"\nFetching leaderboard for race: {latest_race.name}...")
                leaderboard = await api.get_btd6_races_by_race_id_leaderboard(race_id=latest_race.id)
                if leaderboard and len(leaderboard) > 0:
                    top_player = leaderboard[0]
                    print(f"Top player: {top_player.display_name} with score {top_player.score}")
                else:
                    print("Could not retrieve leaderboard or it is empty.")
        else:
            print("Failed to fetch BTD6 races or no races are available.")

    finally:
        print("\nClosing API client.")
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())