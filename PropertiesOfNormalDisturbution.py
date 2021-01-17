import pandas as pd
import csv
import statistics as st

df = pd.read_csv("StudentsPerformance.csv")

ms_list = df["math score"].to_list()
ms_mean = st.mean(ms_list)
ms_median = st.median(ms_list)
ms_mode = st.mode(ms_list)
ms_std = st.stdev(ms_list)

print(f"{ms_mean} is mean")
print(f"{ms_mode} is mode")
print(f"{ms_median} is median")
print(f"{ms_std} is standard deviation")

ms_1std_start, ms_1std_end = ms_mean - ms_std, ms_mean + ms_std
ms_2std_start, ms_2std_end = ms_mean - (2*ms_std), ms_mean + (2*ms_std)
ms_3std_start, ms_3std_end = ms_mean - (3*ms_std), ms_mean + (3*ms_std)

ms_list_of_data_within_1std = [result for result in ms_list if result > ms_1std_start and result <  ms_1std_end]
ms_list_of_data_within_2std = [result for result in ms_list if result > ms_2std_start and result <  ms_2std_end]
ms_list_of_data_within_3std = [result for result in ms_list if result > ms_3std_start and result <  ms_3std_end]

print("{}% of data for math score lies with 1 std".format(len(ms_list_of_data_within_1std)*100.0/len(ms_list)))
print("{}% of data for math score with 2 std".format(len(ms_list_of_data_within_2std)*100.0/len(ms_list)))
print("{}% of data for math score with 3 std".format(len(ms_list_of_data_within_3std)*100.0/len(ms_list)))