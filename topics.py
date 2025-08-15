import pandas as pd

class TopicReader:
    """
    A class to read topic data from a CSV file.

    Its main responsibility is to handle the data source logic,
    extracting the topics and providing them in a simple format.
    """
    def __init__(self, filepath):
        """
        Initializes the TopicReader with the path to the data file.

        Args:
            filepath (str): The path to the CSV file containing the topics.
        """
        self.filepath = filepath
        
    def get_topics(self):
        """
        Reads the CSV file and returns the topic data.

        Handles the case where the file is not found, returning an
        empty list to prevent errors.

        Returns:
            list[dict]: A list of dictionaries, where each dictionary
                        represents a topic (e.g., {'Topic': 'Python', 'Pages': 5}).
                        Returns an empty list if the file is not found.
        """
        try:
            df = pd.read_csv(self.filepath)
            return df.to_dict('records')
        except FileNotFoundError:
            print(f"Error: The topic file was not found at {self.filepath}")
            return []