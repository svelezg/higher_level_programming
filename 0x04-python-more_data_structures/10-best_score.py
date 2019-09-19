#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return

    my_list = list(a_dictionary.keys())
    key = my_list[0]
#    print("key = {}".format(key))

    max = int(a_dictionary[key])
    for i in my_list:
        if int(a_dictionary[i]) > max:
            max = int(a_dictionary[i])
            key = i
#            print("Este = {}".format(key))
    return key
