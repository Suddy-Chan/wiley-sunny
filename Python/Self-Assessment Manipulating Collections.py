# Name: Chan Ho Yeung (Sunny)    Date: 10 Aug 2022

# Define a tuple that contains 12 individual numbers.
num = (4,8,7,10,1,14,24,43,2,56,48,11)
print("Original tuple:", num)
# Split the items in the tuple into three new lists, so each list includes four items from the original tuple.
list1 = []
list2 = []
list3 = []
for i in num:
    if len(list1) < 4:
        list1.append(i)
        continue
    if len(list2) < 4:
        list2.append(i)
        continue
    if len(list3) < 4:
        list3.append(i)
print("New lists:",list1,list2,list3)
# Reverse the values in each list and display the results.
list1.reverse()
list2.reverse()
list3.reverse()
print("Updated lists:",list1,list2,list3)
