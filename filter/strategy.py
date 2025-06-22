from filter.base import BaseFilterStrategy


class GreaterThanFilter(BaseFilterStrategy):
    def _should_include(self, row_value: str, filter_value: str) -> bool:
        a, b = self._convert_values(row_value, filter_value)
        return a > b


class LessThanFilter(BaseFilterStrategy):
    def _should_include(self, row_value: str, filter_value: str) -> bool:
        a, b = self._convert_values(row_value, filter_value)
        return a < b


class EqualFilter(BaseFilterStrategy):
    def _should_include(self, row_value: str, filter_value: str) -> bool:
        a, b = self._convert_values(row_value, filter_value)
        return a == b
