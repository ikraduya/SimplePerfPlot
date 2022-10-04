import json
import re
import string
import sys

import pandas as pd
from matplotlib import pyplot as plt

def mean_repeat_list(list, n):
    ser = pd.Series(list)
    return ser.groupby(ser.index//n).mean().to_list()

def str_to_type(str):
    if str == "int":
        return int
    elif str == "float":
        return float
    elif str == "string":
        return string
    else:
        return string

class TableColumn:
    def __init__(self, name, str_type, pattern, repeatable):
        self.name = name
        self.type = str_to_type(str_type)
        self.pattern = pattern
        self.repeatable = repeatable

class Config:
    def __init__(self):
        self.table = []
        self.plot = {}

def read_config_file(filepath):
    json_raw = json.load(open(filepath, 'r'))
    conf = Config()

    # read table configuration
    print(json_raw["table"])
    for name, tab in json_raw["table"].items():
        tab_col = TableColumn(name, tab["type"], tab["pattern"], tab["repeatable"])
        conf.table.append(tab_col)

    # read plot configuration
    print(json_raw["plot"])
    conf.plot = json_raw["plot"]

    return conf

def save_csv(df, outname):
    df.to_csv(outname + ".csv", index=False)

def plot_data(df, conf, outname):
    set_in_ax = {}
    if "x_label" in conf.plot:
        set_in_ax["x_label"] = conf.plot.pop("x_label")
    if "y_label" in conf.plot:
        set_in_ax["y_label"] = conf.plot.pop("y_label")

    ax = df.plot(**conf.plot)

    if "x_label" in set_in_ax:
        ax.set_xlabel(set_in_ax["x_label"])
    if "y_label" in set_in_ax:
        ax.set_ylabel(set_in_ax["y_label"])
    plt.savefig(outname + '.png')

def main(filename, config_file, repeat, outname):
    conf = read_config_file(config_file)
    
    fp = open(filename, 'r')
    all_str = fp.read()

    data = {}

    for col in conf.table:
        if col.type != string:
            col_data = [col.type(x) for x in re.findall(col.pattern, all_str)]
        else:
            col_data = re.findall(col.pattern, all_str)
        
        if col.repeatable:
            col_data = mean_repeat_list(col_data, repeat)
        print(col_data)
    
        data[col.name] = col_data

    df = pd.DataFrame(data)
    print(df)

    save_csv(df, outname)

    plot_data(df, conf, outname)


if __name__ == "__main__":
    if (len(sys.argv) < 5):
        print("Needs input file, config file, repeat count, and output name")
        exit(0)
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4])