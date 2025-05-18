#Practicing binary search

def bin_search(sequence, item): #<---- Takes 2 arguments
    begin_index = 0 #<---- "start with the first element"
    end_index = len(sequence) - 1 #<---- "end with the last element" is it -1 because of python indexing

    while begin_index <= end_index: #<---- "as long as begin index is lower that end index"
        mid_point = begin_index + (end_index - begin_index) // 2 #<---- midpoint = the first item + rest of the items left to search - division withouit remainder (//)
        mid_point_value = sequence[mid_point] #<--- this returns the value not the index position on the midpoint
        if mid_point_value == item:
            return mid_point

        elif item < mid_point_value:
            end_index = mid_point - 1

        else:
            begin_index = mid_point + 1
            
    return "Item not found"


sequence_a = [2,4,5,6,7,9,10,11,12,13,14] #<---- has to be an already sorted list of numbers
item_a = 12

print(bin_search(sequence_a, item_a))
