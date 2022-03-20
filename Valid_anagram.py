def isAnagram(s: str, t: str) -> bool:

    s = list(s)
    t = list(t)
    
    if len(s) >= 1 and len(t) <= 50000:
        
        frequency_s = {}

        for item in s:
            if item in frequency_s:
                frequency_s[item] += 1
            else:
                frequency_s[item] = 1

        frequency_t = {}

        for item in t:
            if item in frequency_t:
                frequency_t[item] += 1
            else:
                frequency_t[item] = 1

        if frequency_t == frequency_s:
            return True
        else:
            return False

s = "rat"
t = "car"

x = isAnagram(s, t)
print(x)
