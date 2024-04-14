# The class should be able to filter, aggreate and trasnform dataa
from typing import Generator


class DataProcessor:

    @staticmethod
    def read_csv(file_name: str) -> Generator[str, None, None]:
        """Takes a csv file and yeild each
        line one at a time

        Args:
            file_name (str): csv file to read

        Returns:
            Generator[str, None, None]: a line representing an entry in the csv file
        """
        with open(file_name, 'r') as taxi_data:
            for lines in taxi_data.readlines():
                yield lines.strip('\n').split(sep=',')

    @staticmethod
    def data_filter(fn, data):
        pass

    @staticmethod
    def data_map(fn, data):
        pass


if __name__ == '__main__':
    taxi_file = DataProcessor.read_csv('train.csv')
