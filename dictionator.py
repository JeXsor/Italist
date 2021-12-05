import multiprocessing
from tqdm import tqdm

numberOfKeywords = 0
maxCombinationTreshold = 3
maxLettersTreshold = 256
minLettersTreshold = 0

#stampa il titolo
def title():
    print(r"""                            _""")
    print(r"""                           .' `'.__""")
    print(r"""                          /      \ `'"-,""")
    print(r"""         .-''''--...__..-/ .     |      \ """)
    print(r"""       .'               ; :'     '.  a   |""")
    print(r"""      /                 | :.       \     =\                    PROUDLY""")
    print(r"""      ;                   \':.      /  ,-.__;.-;`           MADE IN ITALY""")
    print(r"""     /|     .              '--._   /-.7`._..-;`""")
    print(r"""    ; |       '                |`-'      \  =|""")
    print(r"""    |/\        .   -' /     /  ;         |  =/""")
    print(r"""    (( ;.       ,_  .:|     | /     /\   | =|""")
    print(r"""     ) / `\     | `""`;     / |    | /   / =/""")
    print(r"""       | ::|    |      \    \ \    \ `--' =/""")
    print(r"""      /  '/\    /       )    |/     `-...-`""")
    print(r"""     /    | |  `\    /-'    /;""")
    print(r"""     \  ,,/ |    \   D    .'  \ """)
    print(r"""       `""`  \  nnh  D_.-'L__nnh""")
    print(r"""              `"'"`                               """)
    print()
    
#get list of keywords (seeds)
def getList():
    lista = []
    choice = True
    title()
    print("Insert some keywords to process, each separated with a comma [,]. Any spaces will be removed.\n\n\tes: KEYWORDS -> Avocado, Banana, Coffee ...\n\n")
    while choice:
        keywords = input("KEYWORDS -> ")
        keywords = keywords.split(",")
        for word in keywords:
            word = word.strip(" ")
            lista.append(word.lower())
            for letter in range(len(word)):
                temp = word[:letter] + word[letter].capitalize() + word[letter+1:]
                lista.append(temp)
        print("You inserted %d keywords, is that it? [Y/n]" %len(keywords), end=" ")
        temp = input()
        if temp == "Y" or temp == "y" or temp == "yes" or temp == "Yes" or temp == "YES":
            choice = False

    list(set(lista))
    global numberOfKeywords 
    numberOfKeywords = len(lista)
    return lista

#Keyword list to uppercase
def maiuscole(lista):
    print('\nTo uppercase...')

    maius = []

    for parola in tqdm(lista, ncols=50):
        maiusc = parola.upper()
        maius.append(maiusc)
    return list(set(maius))

#keyword list to lowercase
def minuscole(lista):
    print('\nTo Lowercase...')

    minus = []

    for parola in tqdm(lista, ncols=50):
        minusc = parola.lower()
        minus.append(minusc)
    return list(set(minus))

#combines all the keywords
def compositore(list):
    print('\nThinking about combinations...')
    import itertools

    finale = []
    combinazioni = []
    for n in tqdm(range(maxCombinationTreshold+1), ncols=50):
        combinazioni += itertools.combinations(list, n)
        
    for combinazione in combinazioni:
        temp = ''.join(combinazione)
        finale.append(temp)

    return finale

#adds numbers to the keywords
def numeratore(parole, result):

    parolenumerate = []

    for parola in tqdm(parole, ncols=50):
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
    result.send(parolenumerate) 

def addNumbers(lista):
    for i in range():
        lista.append(str(i))

def setTreshold(lista):
    print("\n\nThinning the list based on letters tresholds...")
    newlista = []
    for item in tqdm(lista):
        if len(item) > minLettersTreshold and len(item) < maxLettersTreshold:
            newlista.append(item)
    return newlista


if __name__ == '__main__':
    keylist = getList()
    keylist = keylist + maiuscole(keylist) + minuscole(keylist)
    keylist = compositore(keylist)

    #optimized numberisation
    print("\nThrowing in some numbers...")
    n = int(len(keylist)/4)

    result, functRes = multiprocessing.Pipe()

    lista1 = keylist[:n]
    lista2 = keylist[n:n*2]
    lista3 = keylist[n*2:n*3]
    lista4 = keylist[n*3:]

    p1 = multiprocessing.Process(target=numeratore, args=(lista1,functRes))
    p2 = multiprocessing.Process(target=numeratore, args=(lista2,functRes))
    p3 = multiprocessing.Process(target=numeratore, args=(lista3,functRes))
    p4 = multiprocessing.Process(target=numeratore, args=(lista4,functRes))

    p1.start()
    p2.start()
    keylist = keylist + result.recv()
    keylist = keylist + result.recv()
    p1.join()
    p2.join()
    
    p3.start()
    p4.start()
    keylist = keylist + result.recv()
    keylist = keylist + result.recv()
    p3.join()
    p4.join()

    keylist = addNumbers(keylist)
    keylist = setTreshold(keylist)

    with open('output.txt', 'w') as output:
        print("\n\nFinally writing on a file...")
        for elem in tqdm(keylist):
            output.write('{}\n'.format(elem))

    print('\n\nFile with {} passwords ready, get a coffe and a HashCat!'.format(len(keylist)))
