import pandas as pd
import numpy as np
import random
import json
# file_path = 'D:\\Projects\\ObsidianNotes\\NEU_Courses_Repo\\FundamentalsAI\\Assignments\\PythonUtils\\finalSpotify\\data.csv'
file_path = './finalSpotify/data.csv'


class data_wrapper:
    def __init__(self, file_path, min_label, max_label, features=None) -> None:
        self.df = pd.read_csv(file_path)
        if features != None:
            self.features = features
        else:
            self.features = ['danceability', 'tempo']
        self.seasons = ['summer', 'fall', 'spring', 'winter']
        self.initial_weights = [1 for x in self.features]
        self.initial_bias = 0
        self.min_label = min_label
        self.max_label = max_label

    def get_label(self, data_point):
        peak = data_point['peak']
        if (peak >= self.min_label and peak <= self.max_label):
            return 1
        return 0

    def get_label_2(self, data_point):
        return data_point['hit']

    def get_peak_rank(self, data_point):
        peak = data_point['peak']
        return peak

    def get_feature_values_2(self, data_point):
        res = []
        for f in self.features:
            res.append(data_point[f])
        return res

    def get_feature_values(self, data_point):
        # format into json by replacing ' with "
        data_features = data_point['features'].replace("'", "\"")
        data_features = json.loads(data_features)
        # convert to a list
        season_features = data_point['seasons']
        season_features = season_features[1:len(season_features)-1]
        season_features = season_features.replace('\'', '').split(',')
        song_artists = data_point['artist'].split('&')
        res = []
        for f in self.features:
            # if the feature is tempo, try normalized it to lower it's value
            if f == 'tempo':
                res.append(data_features[f]/200.0)
            # if the feature is a season, the value is 1 if the song is popular in that season
            # 0 otherwise
            elif f in self.seasons:
                if f in season_features:
                    res.append(1)
                else:
                    res.append(0)
            else:
                res.append(data_features[f])
        return res

    def get_no_rows(self):
        return len(self.df.index)

    def get_row(self, index):
        return self.df.loc[index]


class lr_model:
    def __init__(self, data_wrapper: data_wrapper, weights, bias, learning_rate, epoch, training_data_pct=1) -> None:
        '''
        data: data_wrapper object that contains list of datapoints, representing the whole training dataset
        weights: initial weights of the features
        bias: initial bias
        learning_rate, epoch: logistic regression settings
        get_label: a function that takes in a data point and gives out its label: get_label(data_point)-> 0 or 1
        get_features: a function that takes in a data point and gives out a list of feature values: get_features(data_point)-> [features]
        '''
        self.data_wrapper = data_wrapper
        self.weights = weights
        self.bias = bias
        self.learning_rate = learning_rate
        self.epoch = epoch
        self.training_row = int(
            self.data_wrapper.get_no_rows()*training_data_pct)

    def score(self, feature_values):
        if (len(feature_values) != len(self.weights)):
            print('unbalanced feature and weights')
            return
        return np.array(feature_values).dot(np.array(self.weights))+self.bias

    def single_error_fn(self, features, label):
        pred = self.lr_prediction(features)
        log_loss = -label*np.log(pred)-(1-label)*np.log(1-pred)
        return log_loss

    def total_error_fun(self):
        total_rows = self.training_row
        total_error = 0
        for i in range(total_rows):
            data_point = self.data_wrapper.get_row(i)
            label = self.data_wrapper.get_label(data_point)
            features_value = self.data_wrapper.get_feature_values(data_point)
            total_error += self.single_error_fn(features_value, label)
        return total_error

    def sigmoid(self, score):
        return 1.0/(1+np.exp(-score))

    def lr_prediction(self, features):
        return self.sigmoid(self.score(features))

    def lr_trick(self, features, label):
        diff = label - self.lr_prediction(features)
        new_weights = [w for w in self.weights]
        for i in range(len(new_weights)):
            new_weights[i] = new_weights[i] + new_weights[i] * \
                features[i]*self.learning_rate*diff
        self.bias = self.bias+self.learning_rate*diff
        self.weights = new_weights

    def lr_train(self):
        for i in range(self.epoch):
            j = random.randint(0, self.training_row-1)
            data_point = self.data_wrapper.get_row(j)
            label = self.data_wrapper.get_label(data_point)
            features_value = self.data_wrapper.get_feature_values(data_point)
            self.lr_trick(features_value, label)
            if (i % 1000 == 0):
                print('traning iteration:', i)
                print('total error:', self.total_error_fun())

    def lr_classify(self, data_point):
        features = self.data_wrapper.get_feature_values(data_point)
        score = self.score(features)
        return self.sigmoid(score)


def classify(data_wrapper: data_wrapper, start_index, end_index, *lrs):
    i = start_index
    correct_counter = 0
    failed_counter = 0

    while i < end_index:
        data_point = data_wrapper.get_row(i)
        rank = data_wrapper.get_peak_rank(data_point)
        rank_index = int((rank-1)/20)

        probabilities = []
        for lr in lrs:
            prediction = lr.lr_classify(data_point)
            probabilities.append(prediction)
        total = sum(probabilities)
        probabilities = [x/total for x in probabilities]
        max_index = 0
        maxProb = probabilities[0]
        for pro_index in range(len(probabilities)):
            p = probabilities[pro_index]
            if p > maxProb:
                max_index = pro_index
                maxProb = p

        if max_index == rank_index:
            correct_counter += 1
        else:
            failed_counter += 1
        i += 1
    return [correct_counter, failed_counter]


if __name__ == '__main__':
    top1_19 = data_wrapper(file_path, 1, 19)
    top20_39 = data_wrapper(file_path, 20, 39)
    top40_59 = data_wrapper(file_path, 40, 59)
    top60_79 = data_wrapper(file_path, 60, 79)
    top80_100 = data_wrapper(file_path, 80, 100)

    top1_19Lr = lr_model(top1_19, top1_19.initial_weights,
                         top1_19.initial_bias, 0.0001, 200000, 0.7)
    top20_39Lr = lr_model(top20_39, top20_39.initial_weights,
                          top20_39.initial_bias, 0.0001, 200000, 0.7)
    top40_59Lr = lr_model(top40_59, top40_59.initial_weights,
                          top40_59.initial_bias, 0.0001, 200000, 0.7)
    top60_79Lr = lr_model(top60_79, top60_79.initial_weights,
                          top60_79.initial_bias, 0.0001, 200000, 0.7)
    top80_100Lr = lr_model(top80_100, top80_100.initial_weights,
                           top80_100.initial_bias, 0.0001, 200000, 0.7)
    top1_19Lr.lr_train()
    top20_39Lr.lr_train()
    top40_59Lr.lr_train()
    top60_79Lr.lr_train()
    top80_100Lr.lr_train()

    test_start = top1_19Lr.training_row+1
    test_end = top1_19.get_no_rows()-1
    result = classify(top1_19, test_start, test_end, top1_19Lr,
                      top20_39Lr, top40_59Lr, top60_79Lr, top80_100Lr)
    print(result)

    # ---------------------- tests -------------------------
    # data_point = top20.get_row(5)
    # print(data_point)
    # features = top20.get_feature_values(data_point)
    # label = top20.get_label(data_point)
    # print(top20Lr.single_error_fn(features, label))
    # print(top20Lr.lr_classify(data_point))
    # ---------------------- end tests -------------------------
