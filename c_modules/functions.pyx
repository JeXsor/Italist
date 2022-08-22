import itertools

#Keyword list to uppercase
cpdef maiuscole(list lista):
    print('\nTo uppercase...')

    cdef list maius = []

    for parola in lista:
        maiusc = parola.upper()
        maius.append(maiusc)
    return list(set(maius))


#keyword list to lowercase
cpdef minuscole(list lista):
    print('\nTo Lowercase...')

    cdef list minus = []

    for parola in lista:
        minusc = parola.lower()
        minus.append(minusc)
    return list(set(minus))

cpdef compositore(list lista, maxCombinationTreshold):
    print('\nThinking about combinations...')

    cdef list finale = []
    cdef list combinazioni = []

    for n in range(maxCombinationTreshold+1):
        print(n)
        combinazioni += itertools.combinations(lista, n)
        
    for combinazione in combinazioni:
        temp = ''.join(combinazione)
        finale.append(temp)

    return finale

#adds numbers to the keywords
cpdef numeratore(list parole):

    cdef list parolenumerate = []

    for parola in parole:
        for i in ["{0:03}".format(i) for i in range(0, 999)]:
            newparola = parola + str(i)
            parolenumerate.append(newparola)

        for i in ["{0:03}".format(i) for i in range(0, 999)]:
            newparola =  str(i) + parola
            parolenumerate.append(newparola)

        for i in ["{0:02}".format(i) for i in range(0, 999)]:
            newparola = parola + str(i)
            parolenumerate.append(newparola)

        for i in ["{0:02}".format(i) for i in range(0, 999)]:
            newparola = str(i) + parola
            parolenumerate.append(newparola)

        for i in ["{0:04}".format(i) for i in range(0, 9999)]:
            newparola = parola + str(i)
            parolenumerate.append(newparola)
        
        for i in ["{0:04}".format(i) for i in range(0, 9999)]:
            newparola = str(i) + parola
            parolenumerate.append(newparola)

        for i in range(1,999):
            newparola =  str(i) + parola
            parolenumerate.append(newparola)

        for i in range(1,9999):
            newparola = parola + str(i)
            parolenumerate.append(newparola)
    
    list(set(parolenumerate))
    return parolenumerate

cpdef addNumbers(list lista):
    cdef list newlista = []

    for i in range(999999):
        newlista.append(str(i))
    
    return newlista