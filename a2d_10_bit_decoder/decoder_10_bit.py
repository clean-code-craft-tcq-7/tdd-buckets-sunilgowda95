from decoder.decode import \
    ignore_out_of_bound,\
    convert_to_amps

sensor_details_10bit = {
    "min" : {
        "raw" : 0,
        "amps" : -15
    },
    "max" : {
        "raw" : 1022,
        "amps" : 15
    },
    "reduce_by" : 15
}

def decode_10_bit(raw_digital_values):
    raw_values_in_range = ignore_out_of_bound(sensor_details_10bit, raw_digital_values)
    return convert_to_amps(sensor_details_10bit, raw_values_in_range)

def convert_to_absolute(current_values):
    abs_values = []
    for each in current_values:
        abs_values.append(abs(each))
    return abs_values

def decode_10_bit_continous_range(raw_digital_values):
    current_values = decode_10_bit(raw_digital_values)
    absolute_current_values = convert_to_absolute(current_values)
    from continuous_range.current_range import get_range
    return get_range(absolute_current_values)
    