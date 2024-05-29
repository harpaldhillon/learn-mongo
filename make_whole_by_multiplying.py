def make_whole_by_multiplying(number):
    text = number

    ind = number.rfind('.')
    if ind != -1:
        print(f"The period is at index {ind}.")
    else:
        return int(number)

    index = text.split('.')
    final_str = str(index[0]) + str(index[1])

    return int(final_str)

# Example usage
print(make_whole_by_multiplying("8.1110"))
