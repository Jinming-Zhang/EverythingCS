import matplotlib.pyplot as plt
import numpy as np
from lrTraining import data_wrapper

file_path = "./finalSpotify/data.csv"


def plot_single_feature_label(data: data_wrapper, rows, feature, size=5):
    data.features = feature
    x = []
    y = []
    for i in range(rows):
        song_data = data.get_row(i)
        feature_v = data.get_feature_values(song_data)[0]
        x.append(feature_v)
        label = songs.get_label(song_data)
        y.append(label)

    plt.xlabel(feature)
    plt.ylabel('is Top 20')
    plt.scatter(x, y, s=size)


def plot_two_features_label(data: data_wrapper, rows, f1, f2):
    data.features = [f1, f2]
    x = []
    y = []
    clrs = []
    for i in range(rows):
        song_data = data.get_row(i)
        f1_value = data.get_feature_values(song_data)[0]
        f2_value = data.get_feature_values(song_data)[1]
        x.append(f1_value)
        y.append(f2_value)
        l = songs.get_label(song_data)
        if (l == 1):
            clrs.append('green')
        else:
            clrs.append('red')
    plt.xlabel(f1)
    plt.ylabel(f2)
    plt.scatter(x, y, c=clrs, s=5)


songs = data_wrapper(file_path, 1, 19)
plot_row = songs.get_no_rows()

plt.figure('Danceability')
plot_single_feature_label(songs, plot_row, ['danceability'])

plt.figure('energy')
plot_single_feature_label(songs, plot_row, ['energy'])

plt.figure('speechiness')
plot_single_feature_label(songs, plot_row, ['speechiness'])

plt.figure('instrumentalness')
plot_single_feature_label(songs, plot_row, ['instrumentalness'])

plt.figure('tempo')
plot_single_feature_label(songs, plot_row, ['tempo'])

plt.figure("Peak Distribution")
peak_songs = {}
for i in range(plot_row):
    song_data = songs.get_row(i)
    peak = songs.get_peak_rank(song_data)
    if (peak in peak_songs):
        peak_songs[peak] += 1
    else:
        peak_songs[peak] = 1
plt.xlabel("peak rank")
plt.ylabel("number of songs")
plt.scatter(peak_songs.keys(), peak_songs.values())

plt.figure("Danceability and Energy")
plot_two_features_label(songs, plot_row, 'danceability', 'energy')

plt.show()
