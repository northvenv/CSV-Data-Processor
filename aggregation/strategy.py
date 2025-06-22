from aggregation.base import AggregationStrategy
from typing import List, Dict


class AvgAggregation(AggregationStrategy):
    def aggregate(self, data: List[Dict[str, str]], column: str) -> float:
        values = self._get_numeric_values(data, column)
        return sum(values) / len(values) if values else 0


class MinAggregation(AggregationStrategy):
    def aggregate(self, data: List[Dict[str, str]], column: str) -> float:
        values = self._get_numeric_values(data, column)
        return min(values) if values else 0


class MaxAggregation(AggregationStrategy):
    def aggregate(self, data: List[Dict[str, str]], column: str) -> float:
        values = self._get_numeric_values(data, column)
        return max(values) if values else 0
