def get_unique_list(input):
    return list(set(input))

def get_range(current_samples):
    unique_current_sample = get_unique_list(current_samples)
    return "{}-{}, {}".format(unique_current_sample[0], unique_current_sample[-1], len(current_samples))