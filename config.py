import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config(object):
    APP_ID = 4508955
    API_HASH = "171c024d0dc4bbf47b7c16fd08def2bc"
    BOT_TOKEN = "5448826427:AAEYmtlh6-qxZZsJzKMhGAWby_X_LvP2cU4"
    BOT_USERNAME = "mlaqobuzbot"
    OWNER_ID = 1256695927
    AUTH_IDS = [0]
    QOBUZ_MAIL = "myokoaung2023@gmail.com"
    HEROKU_APP_NAME = "xxxx" # dont touch
    HEROKU_API_KEY = "xxxx" # dont touch
    QOBUZ_PASS = "Myokoaung93"
    QOBUZ_QUAL = 27
    UPDATE_ALL = True
    LOG_CHANNEL = [-1001733180884]
    botStartTime = time.time() # dont touch
