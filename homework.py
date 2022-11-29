print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x and y) <= (not z)) and (x <= y) or w) == False:
                    print(x, y, z, w)

s = ">" + 15 * "2" + 20 * "3" + 25 * "5"
while ">2" in s or ">3" in s or ">5" in s:
    if ">2" in s:
        s = s.replace(">2", "333>")
    if ">3" in s:
        s = s.replace(">3", "23>")
    if ">5" in s:
        s = s.replace(">5", "35>")
print(list[s])
result = 0
for i in range(len(s) -1):
    result += int(s[i])
print(result)