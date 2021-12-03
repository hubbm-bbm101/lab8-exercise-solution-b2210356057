import sys
arguments = sys.argv

with open(arguments[1]) as iFile:
    
    record_dict = {}
    
    for line in iFile:
        name, uni_depart = line.split(":")
        record_dict[name] = uni_depart[:-1]
for name in arguments[2].split(","):
        try:
            print("Name: {}".format(name))
            print("University, Department: {}".format(record_dict[name]))
        except:
            print("No record '{}' was found! ".format(name))