from api_reader import ApiReader
from redis_handler import RedisHandler
from data_processor import DataProcessor, Aggregation, Search

def main():
    api_url = "https://jsonplaceholder.typicode.com/todos" # example url
    reader = ApiReader(api_url)
    data = reader.fetch_data()

    if data:
        redis_host = "localhost"
        redis_port = 6379 # default redis port number 
        redis_db = 0
        redis_key = "my_data"

        redis_handler = RedisHandler(redis_host, redis_port, redis_db)
        redis_handler.insert_data(redis_key, data)

        processor = DataProcessor(data)
        total_items = processor.calculate_total_items()
        print(f"Total items in data: {total_items}")

        # Calling another processing method; create_chart
        processor.create_chart()  # create charts using matplotlib



        # Aggregationing example
        completed_tasks = Aggregation.count_completed_tasks(data)
        incomplete_tasks = Aggregation.count_incomplete_tasks(data)
        user_distribution = Aggregation.task_distribution_by_user(data)
        print(f"Completed tasks: {completed_tasks}")
        print(f"Incomplete tasks: {incomplete_tasks}")
        print(f"Task distribution by user: {user_distribution}")

        # Searching example
        search_term = "task"
        matching_items = Search.search_by_title(data, search_term)
        print(f"Items matching the search term '{search_term}': {matching_items}")


if __name__ == "__main__":
    main()
