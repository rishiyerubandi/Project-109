import pandas as pd
import csv
import plotly.figure_factory as pf
import statistics

df = pd.read_csv("StudentsPerformance.csv")
mathScore_list = df["math score"].to_list()
readingScore_list = df["reading score"].to_list()

math_mean = statistics.mean(mathScore_list)
math_median = statistics.median(mathScore_list)
math_mode = statistics.mode(mathScore_list)
math_sd = statistics.stdev(mathScore_list)

reading_mean = statistics.mean(readingScore_list)
reading_median = statistics.median(readingScore_list)
reading_mode = statistics.mode(readingScore_list)
reading_sd = statistics.stdev(readingScore_list)

print("Mean, Median, Mode, Standard Deviation of math = ", math_mean, math_median, math_mode, math_sd)
print("Mean, Median, Mode, Standard Deviation of reading = ", reading_mean, reading_median, reading_mode, reading_sd)

math_1sd_start, math_1sd_end = math_mean - math_sd, math_mean + math_sd
mathScore_list_1sd = [result for result in mathScore_list if result > math_1sd_start and result < math_1sd_end]
print("Percentage of data lies within 1sd = {} ", format(len(mathScore_list_1sd)*100/len(mathScore_list)))

math_2sd_start, math_2sd_end = math_mean - (2*math_sd), math_mean + (2*math_sd)
mathScore_list_2sd = [result for result in mathScore_list if result > math_2sd_start and result < math_2sd_end]
print("Percentage of data lies within 2sd = {} ", format(len(mathScore_list_2sd)*100/len(mathScore_list)))

math_3sd_start, math_3sd_end = math_mean - (3*math_sd), math_mean + (3*math_sd)
mathScore_list_3sd = [result for result in mathScore_list if result > math_3sd_start and result < math_3sd_end]
print("Percentage of data lies within 3sd = {} ", format(len(mathScore_list_3sd)*100/len(mathScore_list)))


reading_1sd_start, reading_1sd_end = reading_mean - reading_sd, reading_mean + reading_sd
readingScore_list_1sd = [result for result in readingScore_list if result > reading_1sd_start and result < reading_1sd_end]
print("Percentage of data lies within 1sd = {} ", format(len(readingScore_list_1sd)*100/len(readingScore_list)))

reading_2sd_start, reading_2sd_end = reading_mean - (2*reading_sd), reading_mean + (2*reading_sd)
readingScore_list_2sd = [result for result in readingScore_list if result > reading_2sd_start and result < reading_2sd_end]
print("Percentage of data lies within 2sd = {} ", format(len(readingScore_list_2sd)*100/len(readingScore_list)))

reading_3sd_start, reading_3sd_end = reading_mean - (3*reading_sd), reading_mean + (3*reading_sd)
readingScore_list_3sd = [result for result in readingScore_list if result > reading_3sd_start and result < reading_3sd_end]
print("Percentage of data lies within 3sd = {} ", format(len(readingScore_list_3sd)*100/len(readingScore_list)))