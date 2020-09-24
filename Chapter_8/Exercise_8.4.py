names=[]
with open("romeo.txt", "r") as fh:
    for line in fh:
        if line not in names:
            names.append(line.strip())
for name in names.sort():
    print(name)
