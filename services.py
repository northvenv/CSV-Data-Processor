import argparse
import re
from abc import ABC, abstractmethod
from typing import Dict, List

from tabulate import tabulate

from aggregation.factory import AggregationFactory
from filter.factory import FilterFactory


class ParserFactory:
    @staticmethod
    def create_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            description="Process CSV file with filtering and aggregation."
        )
        parser.add_argument("--file", required=True, help="Path to CSV file")
        parser.add_argument(
            "--where", help='Filter condition (e.g. "brand=apple" or "price>1000")'
        )
        parser.add_argument(
            "--aggregate", help='Aggregate condition (e.g. "price=avg")'
        )

        return parser


class Printer(ABC):
    @abstractmethod
    def print_table(self, data: List[Dict[str, str]]): ...

    @abstractmethod
    def print_aggregation(self, column: str, operation: str, result: float): ...


class ConsolePrinter(Printer):
    def print_table(self, data: List[Dict[str, str]]):
        print(tabulate(data, headers="keys", tablefmt="grid"))

    def print_aggregation(self, column: str, operation: str, result: float):
        print(f"{operation}({column}) = {result}")


class Processor(ABC):
    @abstractmethod
    def apply_filter(
        self, data: List[Dict[str, str]], column: str, operator: str, value: str
    ) -> List[Dict[str, str]]: ...

    @abstractmethod
    def apply_aggregation(
        self, data: List[Dict[str, str]], column: str, operation: str
    ) -> float: ...

    @abstractmethod
    def parse_where_condition(self, where_str: str) -> tuple[str, str, str]: ...

    @abstractmethod
    def parse_aggregate_condition(self, agg_str: str) -> tuple[str, str, str]: ...


class DataProcessor(Processor):
    def apply_filter(
        self, data: List[Dict[str, str]], column: str, operator: str, value: str
    ) -> List[Dict[str, str]]:
        filter_strategy = FilterFactory.create(operator)
        filtered_data = filter_strategy.filter(data, column, value)
        return filtered_data

    def apply_aggregation(
        self, data: List[Dict[str, str]], column: str, operation: str
    ) -> float:
        aggregation_strategy = AggregationFactory.create(operation)
        return aggregation_strategy.aggregate(data, column)

    def parse_where_condition(self, where_str: str) -> tuple[str, str, str]:
        match = re.fullmatch(r"^([a-zA-Z_]\w*)([><=])([a-zA-Z0-9_.]+)$", where_str)
        if not match:
            raise ValueError(
                f"Invalid WHERE condition: '{where_str}'. "
                "Strict format required: 'column[>|<|=]value' with no spaces or compound operators"
            )

        column, operator, value = match.groups()
        return column, operator, value

    def parse_aggregate_condition(self, agg_str: str) -> tuple[str, str, str]:
        if not isinstance(agg_str, str):
            raise ValueError("Aggregate condition must be a string")

        if not re.fullmatch(r"^[a-z][a-z0-9_]*=(avg|min|max)$", agg_str):
            raise ValueError(
                f"Invalid aggregate condition: '{agg_str}'. "
                "Expected format: 'column=operation' where operation is avg, min or max"
            )

        column, operation = agg_str.split("=")
        return column, operation
