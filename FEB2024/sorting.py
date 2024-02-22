# Chapter 12 - List Manipulation

# Selection Sorting

name = ['Vijaya', 'Sanvi', 'Ruby', 'Zafar', 'Maya', 'Anya']

for i in range(len(name)):
    midindex = i
    for j in range(i,len(name)-1):
        if name[midindex] > name[j+1]:
            midindex = j+1
    name[i], name[midindex] = name[midindex], name[i]

print(name)
