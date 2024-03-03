import redis
import json

class RedisHandler:
    def __init__(self, host, port, db):
        self.r = redis.Redis(host=host, port=port, db=db)

    def insert_data(self, key, data):
        try:
            self.r.execute_command("JSON.SET", key, ".", json.dumps(data))
            print(f"Data inserted into RedisJSON with key: {key}")
        except redis.RedisError as e:
            print(f"Error inserting data into RedisJSON: {e}")
