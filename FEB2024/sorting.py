# Chapter 12 - List Manipulation

# Selection Sorting

name = ['Vijaya', 'Sanvi', 'Ruby', 'Zafar', 'Maya', 'Anya']
length_of_name = len(name)

for i in range(length_of_name):
    mid_index = i
    for j in range(i,length_of_name-1):
        if name[mid_index] > name[j+1]:
            mid_index = j+1
    name[i], name[mid_index] = name[mid_index], name[i]

print(name)
