import json

data_names = ['SOP1.dat', 'SOP2.dat', 'SOP3.dat']
all_data = {}
for file in data_names:
    path_to_data = './data/' + file
    f = open(path_to_data).read()
    all_data[file] = f.split('\n')

with open('all_data.json', 'w') as f:
    json.dump(all_data, f)
