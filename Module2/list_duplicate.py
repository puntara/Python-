number_list=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

bucket=[]
bucket1=[]
for var in number_list:
    if var not in bucket:
        bucket.append(var)
    else:
        if var not in bucket1: # check for duplicate and append 
            bucket1.append(var)
print(bucket1)
