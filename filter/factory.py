from filter.base import FilterStrategy
from filter.strategy import EqualFilter, GreaterThanFilter, LessThanFilter


class FilterFactory:
    @staticmethod
    def create(operator: str) -> FilterStrategy:
        match operator:
            case ">":
                return GreaterThanFilter()
            case "<":
                return LessThanFilter()
            case "=":
                return EqualFilter()
            case _:
                raise ValueError(f"Unsupported operator: {operator}")
