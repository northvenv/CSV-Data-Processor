import pytest
import csv
from unittest.mock import Mock
from services import (
    Printer,
    Processor
)
from file_reader import (
    FileReader
)
from argparse import ArgumentParser
from main import CSVProcessorApp
from services import (
    DataProcessor,
    ConsolePrinter,
    ParserFactory
)
from file_reader import CSVReader



@pytest.fixture
def sample_data() -> list[dict]:
    return [
        {"name": "iPhone", "price": "999"},
        {"name": "Galaxy", "price": "899"}
    ]

@pytest.fixture
def processor():
    return DataProcessor()

@pytest.fixture
def reader():
    return CSVReader()

@pytest.fixture
def printer():
    return ConsolePrinter()

@pytest.fixture
def parser():
    return ParserFactory.create_parser()

@pytest.fixture
def app_mocks():
    reader = Mock(spec=FileReader)
    processor = Mock(spec=Processor)
    printer = Mock(spec=Printer)
    parser = Mock(spec=ArgumentParser)
    
    return CSVProcessorApp(reader, processor, printer, parser)

@pytest.fixture
def sample_csv_file(tmp_path):
    data = [
        {"name": "iPhone", "price": "999", "rating": "4.5"},
        {"name": "Galaxy", "price": "899", "rating": "4.3"},
        {"name": "Pixel", "price": "799", "rating": "4.1"}
    ]
    file_path = tmp_path / "test.csv"
    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price", "rating"])
        writer.writeheader()
        writer.writerows(data)
    return file_path