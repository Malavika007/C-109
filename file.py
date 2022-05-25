import pandas as pd
import csv
import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
dice_results =[]
for i in range(1,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_results.append(dice1+dice2)
    

mean = sum(dice_results)/len(dice_results)
std_deviation = statistics.stdev(dice_results)

median = statistics.median(dice_results)
mode = statistics.mode(dice_results)

#Finding 1 standard deviation stard and end values, and 2 standard deviations stard and end values

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation)

#Plotting the chart, and lines for mean, 1 standard deviation and 2 standard deviations
fig= ff.create_distplot([dice_results],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17],mode = "lines",name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y= [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y= [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y= [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1"))

fig.show()
#Printing the findings
list_of_data_within_1_std_deviation = [result for result in dice_results if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in dice_results if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in dice_results if result > third_std_deviation_start and result < third_std_deviation_end]


print("mean of this data is {}".format(mean))

print("median of this data is {}".format(median))

print("mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))

print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_results)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_results)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_results)))

fig = ff.create_distplot([dice_results],["Result"], show_hist = False)
fig.show()