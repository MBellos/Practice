#Bubble sort using python
def list_Sorting(List):
    pos = 0
    for num in range(0, len(List) - 1):# Its the length of the list -1 so that the code doesn't run forever.
        for pos in range(len(List) - 1):
            if(List[pos] > List[pos+1]):
                temp = List[pos]
                List[pos] = List[pos+1]
                List[pos+1] = temp
                
    return List   
            

List = [6, 2, 8, 4, 9, 5]
print("Unorganised list : ", List)
print("Organised list : ", list_Sorting(List))
