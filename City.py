# БД
# Ном перв города, ном кон город, сумма
one = [
    [2,3,1],
    [1,2,1],
    [3,1,3],
    [3,2,1],
    [3,4,1],
    [1,3,3],
    [2,1,1],
    [2,4,4],
    [4,2,4],
    [4,3,1],
    [5,3,1],
    [3,5,1],
    [5,4,1],
    [4,5,1]
]



def dsfsdf (d,z):
    summa = 0
    f=[]
    # Поиск с первого раза
    for i in one:
        if i[0] == d:
            if i[1] == z:
                print("Два города:","Сумма", i[2], "Город:", i[0], "Город:",i[1])
                print("---"*10)
                continue
            else:
                # Поиск со второго раза
                for vtor in one:
                    if vtor[0] == i[1]:
                        summa = i[2]
                        if vtor[1] == z:
                                summa += vtor[2]
                                # f.append("new")
                                # f.append(summa)
                                # f.append(i[0])
                                # f.append(i[1])
                                # f.append(vtor[1])
                                print("Три города:","Сумма", summa, "Город:", i[0], "Город:",i[1], "Город:",vtor[1])
                                # print(f)
                                print("---"*10)

def fdgdfg (d,z):
    summa = 0
    f=[]
    summa = 0
    # Поиск с первого раза
    for i in one:
            if i[0] == d:
                summa = i[2]
                f.append("new")
                f.append(i[0])
                f.append(i[1])
                summa = i[2]
                if i[1] == z: continue
                # print("Два города:","Сумма", i[2], "Город:", i[0], "Город:",i[1])
                for dsf in one:
                    if dsf[0] == i[1] and dsf[1] != d and dsf[1] != z:
                        # print("Три города:","Сумма", summa, "Город:", i[0], "Город:",i[1], "Город:",vtor[1])
                        f.append(dsf[1])
                        summa += dsf[2]
                        for dfgdf in one:
                            if dfgdf[0] == dsf[1] and dfgdf[1] == z and dfgdf[1] !=d:
                                f.append(dfgdf[1])
                                summa += dfgdf[2]
                                print(f)
                                print(summa)
                                # print("Четыре города:","Сумма", summa, "Город:", f[0], "Город:",f[1], "Город:",f[2], "Город:",f[3])
                                print("---" * 10)






dsfsdf(1,5)
fdgdfg(1,5)




