def count_log_endpoints(file):
    counter_table = {}

    for log in file:
        log_array = log.split(' ')
        if log_array[6] in counter_table:
            counter_table[log_array[6]] += 1
        else:
            counter_table[log_array[6]] = 1


    for key, value in counter_table.items():
        print(key, value)


file = open('log.txt')
count_log_endpoints(file)
