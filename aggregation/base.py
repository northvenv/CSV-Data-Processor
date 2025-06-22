from abc import ABC, abstractmethod
from typing import List, Dict


class AggregationStrategy(ABC):
    @abstractmethod
    def aggregate(self, data: List[Dict[str, str]], column: str) -> float: ...

    @staticmethod
    def _get_numeric_values(data: List[Dict[str, str]], column: str) -> List[float]:
        try:
            return [float(row[column]) for row in data]
        except ValueError:
            raise ValueError(f"Cannot aggregate non-numeric column: {column}")