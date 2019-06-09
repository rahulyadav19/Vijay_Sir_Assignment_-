# Program 1
#dict1 = { "a":1, "a":2, "a":3, "a":4, "b":5, "b":6, "b":7, "c":8, "c":9 }
#print (dict1)

#my_dict = dict1
#print(my_dict)


num_of_values= input("Enter number of key-value pairs")
type(num_of_values)

tot= num_of_values*2
i=0
for i in tot:
    print (i)
    keys=input("Enter Key")
    values=input("Enter value")
    i=i+1


for line in list:
    id = line[0]
    values = line[1]



$ Program 2

test_dict = { "a":1, "a":2, "a":3, "a":4, "b":5, "b":6, "b":7, "c":8, "c":9}
dict1={}
for line in test_dict:
    if line[0] in test_dict:
        test_dict[line[0]].append(line[0])
    else:
        test_dict[line[0]] = [line[1]]


