from pathlib import Path

PATH_BASE = Path(__file__).parent
PATH_CONFIG = PATH_BASE / 'data' / 'config.json'
PATH_COGS = PATH_BASE / 'cogs'

PATH_DATA = PATH_BASE / 'data'

DATA_MAJORS = PATH_DATA / 'majors.json'
DATA_COURSES = PATH_DATA / 'classes.json'
DATA_CLUBS = PATH_DATA / 'clubs.json'
DATA_PARTNERS = PATH_DATA / 'partners.json'
DATA_PUNISHMENTS = PATH_DATA / 'punishments.json'
DATA_ROULETTE = PATH_DATA / 'roulette.json'
DATA_IMAGES = PATH_DATA / 'images.json'

DEFAULT_SUSAVE = PATH_DATA / 'default.susave'

DIFFICULTY_TIERS = ["beginner", "intermediate", "advanced", "master"]

# EMOJI_YES = '\U00002705'  # white check mark on green
# EMOJI_NO = '\U0000274C'  # red x
# COLOR_DEF = discord.Colour.from_rgb(0, 191, 0)  # red
# COLOR_CULT = discord.Colour.from_rgb(255, 0, 191)  # hot pink

# PATH_BASE = Path(__file__).parent
# PATH_DATA = PATH_BASE.parent
# PATH_USERS = PATH_DATA / 'data/users.json'
# PATH_AUTHORS = PATH_DATA / 'data/authors.json'
# PATH_Tasks = PATH_DATA / 'data/tasks.json'
# PATH_REWARDS = PATH_DATA / 'data/rewards.json'
# PATH_PUNISHMENTS = PATH_DATA / 'data/punishments.json'

# CHAN_ID_PROOF = 651594746891862044  # HoC_Bot_Dev | #images