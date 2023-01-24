def create_csv_string(continuous_range_and_count):
    csv_string = "Range, Readings"
    for key, value in continuous_range_and_count.items():
        csv_string += "\n{}, {}".format(key, value)
    return csv_string