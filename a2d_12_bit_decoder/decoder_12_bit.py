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
    }
}

def decode_12bit(raw_digital_values):
    raw_values_in_range = ignore_out_of_bound(sensor_details_12bit, raw_digital_values)
    return convert_to_amps(sensor_details_12bit, raw_values_in_range)
    