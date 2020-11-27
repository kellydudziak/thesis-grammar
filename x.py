import dicts

def print_dicts():
    for k1,v1 in dicts.tales.items():
        temp = ""
        temp += k1 + "  \n"
        for k2,v2 in v1.items():
            temp = temp + " " + k2 + " (" + str(len(v2['acc'])) + ") " + str(v2['acc']) + "\n"
        print(temp)
