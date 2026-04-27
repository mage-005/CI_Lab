import csv
import math
import random


def load_data(filename,sample_size=150):
    data=[]
    with open(filename,'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if len(row)==0:
                continue
            features=list(map(float,row[:-1]))
            label=row[-1]
            data.append((features,label))
    return random.sample(data,sample_size)


def normalize_dataset(data):
    dim=len(data[0][0])
    mins=[min(row[0][i] for row in data) for i in range(dim)]
    maxs=[max(row[0][i] for row in data) for i in range(dim)]
    norm_data=[]
    for features,label in data:
        norm_feat=[]
        for i in range(dim):
            if maxs[i]==mins[i]:
                norm_feat.append(0)
            else:
                norm_feat.append((features[i]-mins[i])/(maxs[i]-mins[i]))
        norm_data.append((features,norm_feat,label))
    return norm_data,mins,maxs


def normalize_query(query,mins,maxs):
    norm_q=[]
    for i in range(len(query)):
        if maxs[i]==mins[i]:
            norm_q.append(0)
        else:
            norm_q.append((query[i]-mins[i])/(maxs[i]-mins[i]))
    return norm_q


def distance_metrics(train,query,method):
    distances=[]
    for orig,norm_feat,label in train:
        if method=="euclidean":
            d=math.sqrt(sum((a-b)**2 for a,b in zip(norm_feat,query)))
        else:
            d=sum(abs(a-b) for a,b in zip(norm_feat,query))
        distances.append((orig,norm_feat,d,label))
    return distances


def assign_ranks(distances):
    sorted_copy=sorted(distances,key=lambda x:x[2])
    ranked_list=[]
    for rank,item in enumerate(sorted_copy,start=1):
        ranked_list.append((*item,rank))
    return ranked_list,sorted_copy


def voting(neighbors,vote_type):
    count={}
    weight={}
    for orig,norm,dist,label in neighbors:
        count[label]=count.get(label,0)+1
        weight[label]=weight.get(label,0)+1/(dist+1e-9)
    print("\nMajority Count:",count)
    print("Weighted Scores:",{k:round(v,4) for k,v in weight.items()})
    if vote_type=="weighted":
        return max(weight,key=weight.get)
    else:
        return max(count,key=count.get)


print("NEAREST NEIGHBOR MODEL – TRANSFUSION DATASET")

data=load_data("transfusion.data")
norm_data,mins,maxs=normalize_dataset(data)
dim=len(data[0][0])

print("\nEnter Test Features:")
test=[]
for i in range(dim):
    test.append(float(input(f"f{i+1}: ")))
norm_test=normalize_query(test,mins,maxs)

method=input("\nMethod (euclidean/manhattan): ").lower()
if method not in ["euclidean","manhattan"]:
    method="euclidean"

distances=distance_metrics(norm_data,norm_test,method)
ranked,sorted_dist=assign_ranks(distances)

print("\nFeatures | Class | Distance | Rank")
for orig,norm,dist,label,rank in ranked:
    print(orig,label,round(dist,4),rank)

k=int(input("\nEnter K value: "))
print("\nTop K (Sorted by Distance):")
for item in sorted_dist[:k]:
    print(item[0],item[3],round(item[2],4))

vote_type=input("\nVoting (majority/weighted): ").lower()
prediction=voting(sorted_dist[:k],vote_type)

print("\nFinal Prediction:",prediction)
