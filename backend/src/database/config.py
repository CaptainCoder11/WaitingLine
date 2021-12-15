import os


class Config:
    user = os.getenv('DB_USER')

    password = os.getenv('DB_PASSWORD')

    server = os.getenv('DB_SERVER','localhost')

    port = os.getenv('DB_PORT',5432)

    db = os.getenv('DB_NAME')


    url =  str("postgresql+psycopg2://root:root@postgres-service/postgres")

config = Config()