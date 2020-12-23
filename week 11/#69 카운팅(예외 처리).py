def count_items(sequence):
    count = {}
    for item in sequence:
        try:
            count[item] += 1
        except KeyError:
            count[item] = 1
    return count


t = ['python', 'c++', 'python', 'go', 'java', 'java']
print(count_items(t))