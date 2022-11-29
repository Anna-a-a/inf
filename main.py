with open('data.txt', 'r') as file:
    data = file.readlines()
    data = list(map(int, data))

result = []
for i in range(len(data) - 1):
    if abs(data[i]) % 2 == 0 or abs(data[i + 1]) % 2 == 0:
        result.append(data[i] + data[i + 1])

print(f"Ответ 184 :{len(result), max(result)}")


with open('data7.txt', 'r') as file:
    data1 = file.readlines()
    data1 = list(map(int, data1))

result = []
for i in range(len(data1) - 1):
    if len(str(abs(data1[i]))) == 1:
        if abs(data1[i]) % 3 == 0:
            result.append(data1[i])
    if len(str(abs(data1[i]))) == 2:
        if (int(str(abs(data1[i]))[0]) + int(str(abs(data1[i]))[1])) % 3 == 0:
            result.append(data1[i])
    if len(str(abs(data1[i]))) == 3:
        if (int(str(abs(data1[i]))[0]) + int(str(abs(data1[i]))[1]) + int(str(abs(data1[i]))[2])) % 3 == 0:
            result.append(data1[i])

print(f"Ответ 192 :{len(result), max(result)}")


with open('data9.txt', 'r') as file:
    data2 = file.readlines()
    data2 = list(map(int, data))

result = []
for i in range(len(data2) - 2):
    a, b, c = data2[i], data2[i + 1], data2[i + 2]
    counter = 0
    if bin(a)[2:].count('1') >= 3 and bin(a)[2:].count('0') > 0:
        counter += 1
    if bin(b)[2:].count('1') >= 3 and bin(b)[2:].count('0') > 0:
        counter += 1
    if bin(c)[2:].count('1') >= 3 and bin(c)[2:].count('0') > 0:
        counter += 1
    if counter > 1:
        result.append(max([a, b, c]))

print(f"Ответ 195 :{len(result), max(result)}")