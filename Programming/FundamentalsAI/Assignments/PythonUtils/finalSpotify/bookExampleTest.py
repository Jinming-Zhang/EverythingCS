from lrTraining import lr_model


class boop:
    def __init__(self) -> None:
        self.scores = {}
        self.scores['aack'] = 1
        self.scores['beep'] = 1
        self.bias = -4
        pass

    def get_label(self, data_point):
        if data_point == 'aack beep beep beep aack beep beep!':
            return 0

    def get_feature_values(self, data_point):
        aack_no = 0
        beep_no = 0
        for word in data_point.split(' '):
            if word == 'aack':
                aack_no += 1
            if word == 'beep':
                beep_no += 1
        return [aack_no, beep_no]

    def get_no_rows(self):
        return 1

    def get_row(self, index):
        return 'aack beep beep beep aack beep beep!'


alian = boop()
feature_values = alian.get_feature_values(alian.get_row(1))
# weight of aack, beep
akk = lr_model(alian, [1, 1], -4, 0.01, 1000)
score = akk.score(feature_values)
sigmoid = akk.sigmoid(score)
print('score:', score)
print('sigmoid:', sigmoid)
print('error:', akk.single_error_fn(
    feature_values, alian.get_label(alian.get_row(1))))
akk.lr_trick(feature_values, alian.get_label(alian.get_row(1)))
score = akk.score(feature_values)
sigmoid = akk.sigmoid(score)
print('score:', score)
print('sigmoid:', sigmoid)
print('error:', akk.single_error_fn(
    feature_values, alian.get_label(alian.get_row(1))))
