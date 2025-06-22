def test_full_workflow(
    reader, 
    processor,
    printer,
    sample_csv_file, 
    capsys
):
    data = reader.read(sample_csv_file)
    filtered = processor.apply_filter(data, "price", ">", "800")
    result = processor.apply_aggregation(filtered, "rating", "avg")
    printer.print_aggregation("rating", "avg", result)
    
    captured = capsys.readouterr()
    assert "avg(rating) =" in captured.out
    assert "4.4" in captured.out  

def test_workflow_with_table_output(
    reader, 
    processor,
    printer,
    sample_csv_file, 
    capsys
):
    data = reader.read(sample_csv_file)
    filtered = processor.apply_filter(data, "rating", ">", "4.2")
    printer.print_table(filtered)
    
    captured = capsys.readouterr()
    assert "iPhone" in captured.out
    assert "Galaxy" in captured.out
    assert "Pixel" not in captured.out  

