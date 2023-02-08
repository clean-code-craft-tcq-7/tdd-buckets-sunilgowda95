from decoder.decode import ignore_out_of_bound,\
    convert_to_amps

sensor_details_12bit = {
    "min" : {
        "raw" : 0,
        "amps" : 0
    },
    "max" : {
        "raw" : 4094,
        "amps" : 10
    },
    "reduce_by" : 0
}

def decode_12_bit(raw_digital_values):
    raw_values_in_range = ignore_out_of_bound(sensor_details_12bit, raw_digital_values)
    return convert_to_amps(sensor_details_12bit, raw_values_in_range)

def decode_12_bit_continous_range(raw_digital_values):
    current_values = decode_12_bit(raw_digital_values)
    from continuous_range.current_range import get_range
    return get_range(current_values)
    