from continuous_range_count import get_continuous_range_and_count
from csv_format import create_csv_string

def sort_samples(input_samples):
    input_samples.sort()
    return input_samples[:]

def get_range(current_samples):
    sorted_current_samples = sort_samples(current_samples) # sorted unique samples
    
    continuous_range_and_count = get_continuous_range_and_count(sorted_current_samples)
    
    return create_csv_string(continuous_range_and_count)
