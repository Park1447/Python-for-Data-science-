import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

myFile = open('city_vehicle_survey.txt')
data1 = myFile.readlines()
data1 = [float(x) for x in data1]
myFile.close()


# code for question 2
print('Problem 2 Answers:')
# code below this line
population_mean = 5
sample_size = len(data1)
sample_mean = np.mean(data1)
std_dev = np.std(data1, ddof=1)
std_error = std_dev / ((sample_size) ** 0.5)
z_score = ((sample_mean - population_mean)) / std_error
p_value = 2 * stats.norm.cdf(-abs(z_score))  
print("sample size is", sample_size)
print("sample_mean is ", sample_mean)
print("std_error is ", std_error)
print("z_score is ", z_score)
print("p_value is ", p_value)

# code for question 3
print('Problem 3 Answers:')
# code below this line

alpha = 0.05
critical_z = stats.norm.ppf(1 - alpha / 2)
largest_std_error = (sample_mean - population_mean) / critical_z
print("largest_std_error is", largest_std_error)
min_sam_size = (std_dev / largest_std_error) ** 2
print("minimum sample size is", min_sam_size)
# code for question 5
print('Problem 5 Answers:')
# code below this line

myFile1 = open('vehicle_data_1.txt')
data1 = myFile1.readlines()

myFile2 = open('vehicle_data_2.txt')
data2 = myFile2.readlines()

data1 = [float(x) for x in data1]
data2 = [float(y) for y in data2]
myFile1.close()
myFile2.close()

size_with = len(data1)
size_without = len(data2)
mean_with = np.mean(data1)
mean_without = np.mean(data2)
std_dev_with = np.std(data1, ddof=1)
std_dev_without = np.std(data2, ddof=1)
std_error_withor = np.sqrt((std_dev_with ** 2 / size_with) + (std_dev_without ** 2 / size_without))
z_score_withor = (mean_with - mean_without) / std_error_withor
p_value_withor = 2 * stats.norm.cdf(-abs(z_score_withor))

print("Data1 sample size is: ", size_with)
print("Data2 sample size is: ", size_without)
print("Data1 sample mean is: ", mean_with)
print("Data2 sample mean is: ", mean_without)
print("Standard error is: ", std_error_withor)
print("z-score is: ", z_score_withor)
print("p-value is:", p_value_withor)











