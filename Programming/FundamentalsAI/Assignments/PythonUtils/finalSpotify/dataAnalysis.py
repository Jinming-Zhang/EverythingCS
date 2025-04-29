from lrTraining import data_wrapper

file_path = './finalSpotify/data.csv'

data = data_wrapper(file_path, 1, 10)
worst_peak = 1
for i in range(0, data.get_no_rows()):
    dp = data.get_row(i)
    peak = data.get_peak_rank(dp)
    if peak > worst_peak:
        worst_peak = peak
        print(dp)
print(worst_peak)
