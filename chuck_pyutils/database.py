import pymysql
import os


def db_connect(db_config, path=None):
    return (
        pymysql.connect(
            host=db_config['HOST'],
            user=db_config['USER'],
            password=db_config['PASS'],
            db=db_config['DBNAME'],
            cursorclass=pymysql.cursors.DictCursor,
            ssl={'ca': os.path.join(path, db_config['CA_FILE'])},
        )
        if 'CA_FILE' in db_config
        else pymysql.connect(
            host=db_config['HOST'],
            user=db_config['USER'],
            password=db_config['PASS'],
            db=db_config['DBNAME'],
            cursorclass=pymysql.cursors.DictCursor,
        )
    )
