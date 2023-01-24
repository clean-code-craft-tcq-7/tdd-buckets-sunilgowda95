def value_is_continuous(first_value, second_value):
    if(second_value - first_value == 0) or\
        (second_value - first_value == 1):
        return True
    return False

def get_continuous_range(sorted_samples):
    # init values
    continuous_range = []
    start_value = sorted_samples[0]
    next_value = sorted_samples[0]
    
    for each_sample in sorted_samples:
        if value_is_continuous(next_value, each_sample):
            next_value = each_sample          
            continue
        else:
            continuous_range.append([start_value, next_value])
            start_value = each_sample
            next_value = each_sample 
    continuous_range.append([start_value, sorted_samples[-1]]) # append last range
    return continuous_range   

def get_key(range_value):
    return "{}-{}".format(range_value[0],range_value[1])

def in_limits(value, high, low):
    return (value>=low and value <= high)

def get_count_for_range(samples, high, low):
    count = 0
    for sample in samples:
        if in_limits(sample, high, low):
            count += 1
    return count
    # return len([x for x in samples if x>=low and x<=high])

def get_continuous_count(samples, range_list):
    range_count = {}
    for range_value in range_list:
        range_key = get_key(range_value)
        range_count[range_key] = get_count_for_range(samples, range_value[1], range_value[0])
    return range_count
 
def get_continuous_range_and_count(sorted_samples):
    continuous_range = get_continuous_range(sorted_samples)
    return get_continuous_count(sorted_samples, continuous_range)