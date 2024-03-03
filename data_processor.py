import matplotlib.pyplot as plt
import numpy as np


class DataProcessor:
    def __init__(self, data):
        self.data = data

    def calculate_total_items(self):
        """
        Calculate the total number of items in the data.

        Returns:
        - int: Total number of items.
        """
        return len(self.data)

    def create_chart(self):
        """
        Create Matplotlib charts using the data.

        1. Bar Chart: Number of completed and incomplete tasks.
        2. Pie Chart: Distribution of tasks based on their completion status.
        3. Histogram: Distribution of tasks based on user IDs.
        """
        # Processing a Bar Chart
        completed_tasks = sum(item['completed'] for item in self.data)
        incomplete_tasks = len(self.data) - completed_tasks

        plt.figure(figsize=(12, 4))

        plt.subplot(1, 3, 1)
        plt.bar(['Completed', 'Incomplete'], [completed_tasks, incomplete_tasks], color=['green', 'red'])
        plt.title('Task Completion Status')

        # Processing a Pie Chart
        completion_status_counts = [completed_tasks, incomplete_tasks]
        labels = ['Completed', 'Incomplete']

        plt.subplot(1, 3, 2)
        plt.pie(completion_status_counts, labels=labels, autopct='%1.1f%%', colors=['green', 'red'])
        plt.title('Task Completion Distribution')

        # Processing a Histogram
        user_ids = [item['userId'] for item in self.data]

        plt.subplot(1, 3, 3)
        plt.hist(user_ids, bins=np.arange(1, max(user_ids) + 1) - 0.5, edgecolor='black')
        plt.xlabel('User ID')
        plt.ylabel('Task Count')
        plt.title('Task Distribution Across User IDs')

        plt.tight_layout()
        plt.show()


class Aggregation:
    @staticmethod
    def count_completed_tasks(data):
        """
        Count the number of completed tasks.

        Parameters:
        - data (list): List of tasks.

        Returns:
        - int: Number of completed tasks.
        """
        return sum(item['completed'] for item in data)

    @staticmethod
    def count_incomplete_tasks(data):
        """
        Count the number of incomplete tasks.

        Parameters:
        - data (list): List of tasks.

        Returns:
        - int: Number of incomplete tasks.
        """
        return len(data) - Aggregation.count_completed_tasks(data)

    @staticmethod
    def task_distribution_by_user(data):
        """
        Calculate task distribution based on user IDs.

        Parameters:
        - data (list): List of tasks.

        Returns:
        - dict: Dictionary with user IDs as keys and task counts as values.
        """
        user_counts = {}
        for item in data:
            user_id = item['userId']
            user_counts[user_id] = user_counts.get(user_id, 0) + 1
        return user_counts

class Search:
    @staticmethod
    def search_by_title(data, search_term):
        """
        Search for tasks containing a specific title.

        Parameters:
        - data (list): List of tasks.
        - search_term (str): The search term to look for in task titles.

        Returns:
        - list: List of tasks matching the search term.
        """
        return [item for item in data if search_term.lower() in item['title'].lower()]

