import io

def main():
    list1 = []
    list2 = []
    with open("input") as f:
        file_text = f.read()
        lines = file_text.split("\n")
        for line in lines:
            values = get_val_from_line(line)
            list1.append(values[0])
            list2.append(values[1])
    list1.sort()
    list2.sort()
    list_similarity = 0
    for x in list1:
        appeared = numberOfTimesInList(list2, x)
        similarity_score = x * appeared
        list_similarity += similarity_score
    print(list_similarity)
        
    #total_d = 0
    #for i in range(0, len(list1)):
        #d = list1[i] - list2[i]
        #total_d += abs(d)
    #print(total_d)
        
            
def get_val_from_line(line):
    lineGroup = line.split(" ")
    isFirstDone = False
    result = []
    for element in lineGroup:
        if(element != ""):
            result.append(int(element))
    return result; 

def numberOfTimesInList(arr, x):
    appeared = 0
    for y in arr:
        if(y == x):
            appeared += 1
    return appeared

main()
