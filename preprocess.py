import os
import pandas as pd

def get_data_path(filename):
    path = os.path.join(
        os.path.dirname(__file__), os.pardir, "data", filename)
    if not os.path.exists(path):
        path = os.path.join(
            os.path.dirname(__file__), "data", filename)
    if not os.path.exists(path):
        path = os.path.join(
            os.path.dirname(__file__), filename)
    if not os.path.exists(path):
        raise Exception("Could not find data file: {}".format(filename))
    return path

class Dataset(object):

    def __init__(self, filename):
        self.datapath = get_data_path(filename)
        self.df = None

    def get_dataset():
        self.df = pd.read_csv(self.datapath)
        return self.df

    def get_x():
        self.df