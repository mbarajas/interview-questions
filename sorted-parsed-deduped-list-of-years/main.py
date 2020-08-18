def parse_years(years):
    years_list = years.split(",")

    for year in years_list:
        if "-" in str(year):
            start, end = year.split("-")
            years_list.remove(year)
            years_list.extend(range(int(start),int(end) + 1))

    years_list = list(map(int, years_list))
    return years_list

def dedupe_list(years_list):
    return list(dict.fromkeys(years_list))

def quick_sort(years_list, starting_index, ending_index):
    if starting_index < ending_index:
        partition_index = partition(years_list, starting_index, ending_index)
        quick_sort(years_list, starting_index, partition_index - 1)
        quick_sort(years_list, partition_index + 1, ending_index)

def partition(years_list, starting_index, ending_index):
    low_index = (starting_index - 1)
    pivot = years_list[ending_index]

    for current_element in range(starting_index, ending_index):
        if years_list[current_element] < pivot:
            low_index = low_index + 1
            years_list[low_index], years_list[current_element] = years_list[current_element], years_list[low_index]

    years_list[low_index + 1], years_list[ending_index] = years_list[ending_index], years_list[low_index + 1]
    return low_index + 1

years = "1995,1990,1989,2000-2005,1492,2015,2020,1860-1865,1776,2020,1990"

years_list = parse_years(years)
print(years_list)

years_list = dedupe_list(years_list)
print(years_list)

#years_list.sort() #easy way if sorting algorithm doesnt have to be implemented
quick_sort(years_list,0,len(years_list) - 1)
print(years_list)
