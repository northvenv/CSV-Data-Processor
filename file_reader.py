import csv
from abc import ABC, abstractmethod
from typing import List, Dict


class FileReader(ABC):
    @abstractmethod
    def read(self, file_path: str) ->  List[Dict[str, str]]: ...


class CSVReader(FileReader):
    def read(self, file_path: str) ->  List[Dict[str, str]]:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            return list(reader)
