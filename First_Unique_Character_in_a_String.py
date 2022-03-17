s = "aabb"

def check(s):
    sam_list = list(s)

    frequency = {}
    result = -1

    for item in sam_list:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1

    for i in frequency:
        if frequency.get(i) == 1:
            result = sam_list.index(i)
            break
        
    return result
            
print(check(s))