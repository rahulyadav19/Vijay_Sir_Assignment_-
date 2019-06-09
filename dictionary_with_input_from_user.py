dict1 = {"a":4, "b":7, "c":9}
print (dict1)


dict2 = {}
i = 0
counter = input("Enter the number of items to input")
list1=[]
list2=[]
while int(i) < int(counter):
    list1=input("Enter keys")
    list2=input("Enter values")
    i=i+1
    for items in list1:
        for values in list2:
            if items in dict2:
                dict2[items[0]].append(values[0])
            else:
                dict2[items[0]] = [items[1]]

for test, final in dict.items():
        print(test, ", ".join(final))
