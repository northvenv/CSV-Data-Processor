from aggregation.base import AggregationStrategy
from aggregation.strategy import AvgAggregation, MaxAggregation, MinAggregation


class AggregationFactory:
    @staticmethod
    def create(operation: str) -> AggregationStrategy:
        match operation:
            case "avg":
                return AvgAggregation()
            case "min":
                return MinAggregation()
            case "max":
                return MaxAggregation()
            case _:
                raise ValueError(f"Unsupported operation: {operation}")
