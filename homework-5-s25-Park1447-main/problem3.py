import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = np.array([135, 140, 130, 145, 150, 138, 142, 137, 136, 148, 141, 139, 143, 147, 149, 134, 133, 146, 144, 132])


# code for Question 1
print('Problem 1 Answers:')
# code below this line
sample_mean = np.mean(data)
sample_std = np.std(data, ddof=1)
sample_size = len(data)
std_error = sample_std / (sample_size ** 0.5)
alpha_90 = 0.90
df = sample_size - 1
t_c_90 = stats.t.ppf((1 - (1 - alpha_90) / 2), df)
max_value_90 = sample_mean + (t_c_90 * std_error)
min_value_90 = sample_mean - (t_c_90 * std_error)

print("Sample mean is: ", sample_mean)
print("Standard error is: ", std_error)
print("Standard score is: ", t_c_90)
print("90% confidence interval is: ", min_value_90, max_value_90)

# code for Question 2
print('Problem 2 Answers:')
# code below this line
alpha_95 = 0.95
t_c_95 = stats.t.ppf((1 - (1 - alpha_95) / 2), df)
max_value_95 = sample_mean + (t_c_95 * std_error)
min_value_95 = sample_mean - (t_c_95 * std_error)

print("Standard score is: ", t_c_95)
print("95% confidence interval is: ", min_value_95, max_value_95)
# code for Question 3
print('Problem 3 Answers:')
# code below this line

pop_std_dev = 5
std_error_pop = pop_std_dev / (sample_size ** 0.5)
z_score_pop = stats.norm.ppf(1 - (1 - alpha_95) / 2)
max_value_pop = sample_mean + (z_score_pop * std_error_pop)
min_value_pop = sample_mean - (z_score_pop * std_error_pop)

print("Standard error is: ", std_error_pop)
print("Standard score is: ", z_score_pop)
print("95% confidence interval is: ", min_value_pop, max_value_pop)
