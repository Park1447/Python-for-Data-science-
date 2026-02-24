from typing import List, Tuple

def histogram(input_dictionary: dict) -> list:
    # data is a dictionary that contains the following keys: 'data', 'n', 'min_val', 'max_val'
    # n is an integer
    # min_val and max_val are floats
    # data is a list

    # Write your code here
    n = input_dictionary.get('n')
    data = input_dictionary.get('data')
    min_val = input_dictionary.get('min_val')
    max_val = input_dictionary.get('max_val')

    if min_val == max_val:
        print("Error: min_val and max_val are the same value")
        return []
    if min_val > max_val:
        temp = min_val
        min_val = max_val
        max_val = temp
    if n <= 0:
        return [] 
    hist = [0] * n
    bin_width = ((max_val - min_val) / n)
    index = 0
    incre = 0
    while index <= (n - 1):
        min_range = min_val + (incre * bin_width)
        max_range = min_val + (bin_width * (incre + 1))
        for i in data:
            if min_range <= i and max_range > i:
                hist[index] += 1

        incre += 1
        index += 1
    return hist 
    # return the variable storing the histogram
    # Output should be a list
    pass

# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day: List[Tuple[str, int]], 
                          person_to_month: List[Tuple[str, int]], 
                          person_to_year: List[Tuple[str, int]]) -> dict:
    #person_to_day, person_to_month, person_to_year are list of tuples

    # Write your code here
    curr_year = 2025
    month_to_people_data = {}
    for month_name, month in person_to_month:
        for day_name, day in person_to_day:
            if day_name == month_name:
                corr_day = day
        for year_name, year in person_to_year:
            if year_name == month_name:
                corr_year = year
        cal_age = curr_year - corr_year
        gen_tuple = (month_name, corr_day, corr_year, cal_age)
        if month not in month_to_people_data:
            month_to_people_data[month] = gen_tuple
        else:
            temp_data = month_to_people_data[month]
            month_to_people_data[month] = [temp_data]
            month_to_people_data[month].append(gen_tuple)
    return (month_to_people_data)
    # return the variable storing output
    # Output should be a dictionary

    pass

# We first define the current year as 2025, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_people_data that will store the final data in the format specified in the problem statement.
# We iterate over the both values in the tuple of the person_to_month list (note that person_to_month is a list of tuples, which means each item in the list is a tuple) 
# using a for loop. For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year lists using the current name as the "key".
# We then use the current month as the key and a tuple of (name, day, year, age) as the value to update the month_to_people_data dictionary.
# Only change the value to a list data type, when there are multiple entries with the same key. This will help append for other tuples to the same month.
# Finally, we return the month_to_people_data dictionary as the output of the function.
