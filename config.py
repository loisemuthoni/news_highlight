NEWS_API_KEY = '<4775dbcae3f5456aaf9c252121f498f6>'

import os

class Config:

    NEWS_API_BASE_URL ='https://api.thenewsdb.org/3/news/{}?api_key={}'
    NEWS_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}