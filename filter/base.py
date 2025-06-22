from abc import ABC, abstractmethod
from typing import List, Dict, Union, Tuple


class FilterStrategy(ABC):
    @abstractmethod
    def filter(self, data: List[Dict[str, str]], column: str, value: str) -> List[Dict[str, str]]: ...

    @staticmethod
    @abstractmethod
    def _convert_values(a: str, b: str) -> Union[Tuple[float, float], Tuple[str, str]]: ...


class BaseFilterStrategy(FilterStrategy, ABC):    
    def filter(self, data: List[Dict[str, str]], column: str, value: str) -> List[Dict[str, str]]:
        filtered_data = []
        for row in data:
            if self._should_include(row[column], value):
                filtered_data.append(row)
        return filtered_data
    
    @abstractmethod
    def _should_include(self, row_value: str, filter_value: str) -> bool: ...
    
    @staticmethod
    def _convert_values(a: str, b: str) -> Union[Tuple[float, float], Tuple[str, str]]:
        try:
            return float(a), float(b)
        except ValueError:
            return a.lower(), b.lower()