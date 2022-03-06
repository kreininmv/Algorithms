mas = [0] * 8

for i in range(2, 10):
    flag = 0
    
    for j in range(1, 7):
        mas[j] = (i ** j) % 7
    
    #print(mas)
    if ((mas[1] + mas[2] + mas[3] + mas[4] + mas[5] + mas[6]) % 7 == 0):
        flag = 1

    for j in range(1, 7):
        for k in range(1, 7):
            if (mas[k] == mas[j] and k != j):
                flag = 0
    
    if (flag == 1):
        print(mas, i)
        break

