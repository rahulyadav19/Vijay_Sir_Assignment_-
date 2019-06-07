#multiple values assigned to keys
dict={}

with open("data.txt") as txt1:
    for line in txt1:
        line=line.strip().split("\t")
        if line[0] in dict:
            dict[line[0]].append(line[1])
        else:
            dict[line[0]] = [line[1]]

    for test, final in dict.items():
        print(test, ", ".join(final))
