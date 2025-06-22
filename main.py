from argparse import ArgumentParser
from file_reader import CSVReader, FileReader
from services import (
    ConsolePrinter,
    DataProcessor,
    ParserFactory,
    Processor,
    Printer
)


class CSVProcessorApp:
    def __init__(
        self, 
        reader: FileReader,
        processor: Processor,
        printer: Printer,
        parser: ArgumentParser
    ):
        self.reader: FileReader = reader
        self.processor: Processor = processor
        self.printer: Printer = printer
        self.parser: ArgumentParser = parser
    
    def run(self):
        args = self.parser.parse_args()
        
        try:
            data = self.reader.read(args.file)
            
            if args.where:
                column, operator, value = self.processor.parse_where_condition(args.where)
                filtered_data = self.processor.apply_filter(data, column, operator, value)
            else:
                filtered_data = data
            
            if args.aggregate:
                column, operation = self.processor.parse_aggregate_condition(args.aggregate)
                result = self.processor.apply_aggregation(filtered_data, column, operation)
                self.printer.print_aggregation(column, operation, result)
            else:
                self.printer.print_table(filtered_data)
        
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == '__main__':
    app = CSVProcessorApp(
        reader=CSVReader(),
        processor=DataProcessor(),
        printer=ConsolePrinter(),
        parser=ParserFactory.create_parser()
    )
    app.run()