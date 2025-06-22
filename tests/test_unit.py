import pytest
from services import DataProcessor


@pytest.mark.parametrize("input_str, expected", [
    ("price>100", ("price", ">", "100")),
    ("name=iPhone", ("name", "=", "iPhone")),
    ("rating<4.5", ("rating", "<", "4.5")),
    ("brand=apple", ("brand", "=", "apple")),
])
def test_parse_valid_where_conditions(processor, input_str, expected):
    assert processor.parse_where_condition(input_str) == expected


@pytest.mark.parametrize("invalid_input", [
    "invalid_condition",
    "price>>100",
    "name iPhone",
    "",
    "price=100=200",
])
def test_parse_invalid_where_conditions(processor, invalid_input):
    with pytest.raises(ValueError, match="Invalid WHERE condition"):
        processor.parse_where_condition(invalid_input)


@pytest.mark.parametrize("input_str,expected", [
    ("price=avg", ("price", "avg")),
    ("rating=max", ("rating", "max")),
    ("quantity=min", ("quantity", "min")),
])
def test_valid_aggregation_conditions(processor, input_str, expected):
    assert processor.parse_aggregate_condition(input_str) == expected


@pytest.mark.parametrize("invalid_input", [
    "price",                
    "=avg",                 
    "price=",               
    "=",                    
    "price avg",           
    "price>avg",            
    "price=avg=extra",      
    "price=average",       
    "price=maximum",        
    "price=123",            
    "price=avg!",           
    "@column=avg",          
    "price=av g",           
    "",                     
    "   ",                  
    "price = avg = extra", 
])
def test_invalid_aggregation_conditions(processor, invalid_input):
    with pytest.raises(ValueError):
        processor.parse_aggregate_condition(invalid_input)