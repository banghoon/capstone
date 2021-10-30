import pandas as pd


def search(datum, values):
    result = []
    for data in datum:
        if values in str(data):
            result.append(True)
        else:
            result.append(False)
    return result
