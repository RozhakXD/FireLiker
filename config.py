from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
DRIVER_PATH = BASE_DIR / "drivers" / "chromedriver.exe"

BASE_URL = "https://fireliker.com"
LOGIN_URL = BASE_URL
WELCOME_URL = BASE_URL + "/welcome.php"
AUTO_VIEWS_URL = BASE_URL + "/autoviews.php"

COOLDOWN_SLEEP = 120
MEDIUM_TIMEOUT = 10

USERNAME = "rozhak_official"