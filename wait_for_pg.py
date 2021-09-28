import os
from time import time, sleep
import psycopg2

check_timeout = os.getenv("POSTGRES_CHECK_TIMEOUT", 30)
check_interval = os.getenv("POSTGRES_CHECK_INTERVAL", 1)
interval_unit = "second" if check_interval == 1 else "seconds"
config = {
    "dbname": os.getenv("POSTGRES_DB", "postgres"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
    "host": os.getenv("DATABASE_URL", "db")
}

start_time = time()


def pg_isready(host, user, password, dbname):
    while time() - start_time < check_timeout:
        try:
            conn = psycopg2.connect(**vars())
            conn.close()
            return True
        except psycopg2.OperationalError:
            print "Postgres isn't ready. Waiting..."
            sleep(check_interval)

    print "Could not connect to Postgres."
    return False


pg_isready(**config)