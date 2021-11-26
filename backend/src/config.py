import os


class Config:
    user = os.getenv('DB_USER')

    password = os.getenv('DB_PASSWORD')

    server = os.getenv('DB_SERVER','localhost')

    port = os.getenv('DB_PORT',5432)

    db = os.getenv('DB_NAME')


    url =  f"postgresql+psycopg2://{user}:{password}@db/{db}"

config = Config()