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
