def todasMonedas(list1, list2):
    monedas = []
    list1.sort()
    list2.sort()
    
    i = 0
    j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            monedas.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1

    return monedas

print("monedas: ", todasMonedas([1,42,12,55], [12,4,60,42]))