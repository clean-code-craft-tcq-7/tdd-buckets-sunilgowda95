def check_boundaries(sensor_details, each):
    return (sensor_details['min']['raw'] <= each and each <= sensor_details['max']['raw'])

def ignore_out_of_bound(sensor_details, raw_values):
    values_in_range = []
    for each in raw_values:
        if check_boundaries(sensor_details, each):
            values_in_range.append(each)
    return values_in_range

def divide(sensor_details, value):
    return (value * sensor_details['max']['amps'])//sensor_details['max']['raw']

def round_off_offset(sensor_details, value):
    return ( (((value * sensor_details['max']['amps']) / sensor_details['max']['raw']) % 1) > 0.49 )

def convert_to_amps(sensor_details, raw_values_in_range):
    converted_values = []
    for each in raw_values_in_range:
        # convert to amps and round off to nearest integer
        converted_values.append( divide(sensor_details, each) + \
                         round_off_offset(sensor_details, each))
    return converted_values