import math 
 
def read_data(filename): 
    file = open(filename, "r") 
    lines = file.read().strip().split("\n") 
    file.close() 
    headers = lines[0].split(",") 
    data = [] 
    for i in range(1, len(lines)): 
        data.append(lines[i].split(",")) 
    return headers, data 
 
def entropy(values): 
    total = len(values) 
    ent = 0 
    unique = [] 
    for v in values: 
        if v not in unique: 
            unique.append(v) 
    for u in unique: 
        count = 0 
        for v in values: 
            if v == u: 
                count += 1 
        p = count / total 
        ent = ent - p * math.log2(p) 
    return ent 
 
def information_gain(data, attr_index, target_index, total_entropy, 
attr_name): 
    print("\nAttribute:", attr_name) 
    print("-" * 50) 
    values = [] 
    for row in data: 
        if row[attr_index] not in values: 
            values.append(row[attr_index]) 
    total_records = len(data) 
    weighted_entropy = 0 
    print("Frequency Table") 
    print("Value\tPass\tFail\tEntropy") 
    for val in values: 
        subset = [] 
        for row in data: 
            if row[attr_index] == val: 
                subset.append(row[target_index]) 
        pass_count = 0 
        fail_count = 0 
        for s in subset: 
            if s == "Pass": 
                pass_count += 1 
            else: 
                fail_count += 1 
        ent = entropy(subset) 
        weight = len(subset) / total_records 
        weighted_entropy = weighted_entropy + (weight * ent) 
        print(val, "\t", pass_count, "\t", fail_count, "\t", round(ent, 4)) 
    print("\nWeighted Entropy =", round(weighted_entropy, 4)) 
    gain = total_entropy - weighted_entropy 
    print("Information Gain =", round(gain, 4)) 
    return gain 
 
def find_root_node(filename): 
    headers, data = read_data(filename) 
    target_index = len(headers) - 1 
    target_name = headers[target_index] 
    target_values = [] 
    for row in data: 
        target_values.append(row[target_index]) 
    total_entropy = entropy(target_values) 
    print("Target Attribute:", target_name) 
    print("Total Entropy =", round(total_entropy, 4)) 
    gains = {} 
    for i in range(target_index): 
        gain = information_gain(data, i, target_index, total_entropy, 
headers[i]) 
        gains[headers[i]] = gain 
    print("\nSummary of Information Gain") 
    print("-" * 40) 
    max_gain = -1 
    root = "" 
    for attr in gains: 
        print(attr, ":", round(gains[attr], 4)) 
        if gains[attr] > max_gain: 
            max_gain = gains[attr] 
            root = attr 
    print("\nRoot Node:", root) 
    print("Maximum Information Gain:", round(max_gain, 4)) 
 
find_root_node("data.txt") 