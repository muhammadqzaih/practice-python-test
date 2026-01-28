

print("hello")


def find_max_value(nmbers):
    max_value = nmbers[0]
    for number in nmbers:
        if number > max_value:
            max_value = number
    return max_value    


def find_min_value(nmbers):
    min_value = nmbers[0]
    for number in nmbers:
        if number < min_value:
            min_value = number
    return min_value

def calculate_average(nmbers):
    total = sum(nmbers)
    count = len(nmbers)
    average = total / count
    return average



if __name__ == '__main__':
    print("hi")