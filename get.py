import pickle

class PickleRepository:

    def __init__(self, data_path):
        self._data_path = data_path
        self._analysis_path = self._data_path + "/extracted"

    def all(self):
        analysis = PickleRepository.load_obj(self._analysis_path)
        return analysis

    @staticmethod
    def load_obj(path):
        data = []
        with open(path + '.pkl', 'rb') as f:
            while True:
                try:
                    for obj in pickle.load(f):
                       data.append(obj)
                except EOFError:
                    break
        return data
