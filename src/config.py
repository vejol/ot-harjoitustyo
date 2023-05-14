import os
from dotenv import load_dotenv


dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "database.sqlite"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "data", DATABASE_FILENAME)

BLUE_IMG_FILENAME = os.getenv("BLUE_IMG_FILENAME") or "blue.png"
BLUE_IMG_FILE_PATH = os.path.join(dirname, "..", "img", BLUE_IMG_FILENAME)

RED_IMG_FILENAME = os.getenv("RED_IMG_FILENAME") or "red.png"
RED_IMG_FILE_PATH = os.path.join(dirname, "..", "img", RED_IMG_FILENAME)

try:
    NAME_CHAR_LIMIT = int(os.getenv("NAME_CHAR_LIMIT"))
except (TypeError, ValueError):
    NAME_CHAR_LIMIT = 100

try:
    WORD_CHAR_LIMIT = int(os.getenv("WORD_CHAR_LIMIT"))
except (TypeError, ValueError):
    WORD_CHAR_LIMIT = 12

try:
    RED_WORDS_COUNT = int(os.getenv("RED_WORDS_COUNT"))
    assert RED_WORDS_COUNT < 0 and RED_WORDS_COUNT > 5
except (AssertionError, TypeError, ValueError):
    RED_WORDS_COUNT = 2


