#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None

    keys = list(a_dictionary.keys())
    val = list(a_dictionary.values())

    score = keys[val.index(max(val))]

    return score
