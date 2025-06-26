#creates a list with elements 1 to 10
o_list = [i for i in range(1,11)]
print(f'Original list: {o_list}')

#Takes out the first 5 digits from the o_list
sliced_list = o_list[:5]
print(f'Extracted first five elements: {sliced_list}')

#Modifies the sliced_list and prints it
sliced_list.reverse()
print(f'Reversed extracted elements: {sliced_list}')