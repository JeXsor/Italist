import multiprocessing
from tqdm import tqdm
import itertools
import time

numberOfKeywords = 0
maxCombinationTreshold = 2
maxLettersTreshold = 256
minLettersTreshold = 0
maius = True
minus = False
composite = True
numbers = True
simbolsfront = False
simbolrear = False

def getSettings():
    global maxCombinationTreshold
    global maxLettersTreshold
    global minLettersTreshold
    global maius
    global minus
    global composite
    global numbers 
    global simbolsfront
    global simbolsrear

    maxCombinationTreshold = int(input("\nSet maximum number of words per combinations: "))
    maxLettersTreshold = int(input("\nSet maximum number of letters: "))
    minLettersTreshold = int(input("\nSet minumum number of letters: "))

    maius = input("\nAdd every word in caps? [Y\\n]")
    if maius == "y" or maius == "Y":
        maius = True
    else:
        maius = False

    maius = input("\nAdd every word in lows? [Y\\n]")
    if minus == "y" or minus == "Y":
        minus = True
    else:
        minus = False
    
    composite = input("\nAdd composite words? [Y\\n]")
    if composite == "y" or composite == "Y":
        composite = True
    else:
        composite = False
    
    numbers = input("\nAdd some random numbers? [Y\\n]")
    if numbers == "y" or numbers == "Y":
        numbers = True
    else:
        numbers = False

    simbolsfront = input("\nAdd some random simbols at the end? (WARNING: can cause really heavy load and may crash the computer) [Y\\n]")
    if simbolsfront == "y" or simbolsfront == "Y":
        simbolsfront = True
    else:
        simbolsfront = False
    
    simbolsrear = input("\nAdd some random simbols at the beginning? (WARNING: can cause really heavy load and may crash the computer) [Y\\n]")
    if simbolsrear == "y" or simbolsrear == "Y":
        simbolsrear = True
    else:
        simbolsrear = False

#stampa il titolo
def title():
    print(r"""                            _""")
    print(r"""                           .' `'.__""")
    print(r"""                          /      \ `'"-,""")
    print(r"""         .-''''--...__..-/ .     |      \ """)
    print(r"""       .'               ; :'     '.  a   |                   DICTIONATOR""")
    print(r"""      /                 | :.       \     =\  """)
    print(r"""      ;                   \':.      /  ,-.__;.-;`""")
    print(r"""     /|     .              '--._   /-.7`._..-;`                PROUDLY""")
    print(r"""    ; |       '                |`-'      \  =|               MADE IN ITALY""")
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
    # result.send(parolenumerate) 
    return parolenumerate

def addNumbers(lista):
    newlista = []

    for i in tqdm(range(999999)):
        newlista.append(str(i))
    
    return newlista

def addSimbolsFront(lista):
    print("\n\nAdding some simbols")
    simboli = ["!", "#", "@", "*", "-", "+", "&"]
    for i in range(3):
        temp = itertools.combinations(simboli, i)
        for combinazione in temp:
            simboli.append(''.join(combinazione))
        print(simboli)
    for parola in tqdm(lista):
        for s in simboli:
            newparola = parola + s
            simboli.append(newparola)

    return simboli

def addSimbolsRear(lista):
    print("\n\nAdding some simbols")
    simboli = ["!", "#", "@", "*", "-", "+", "&"]
    for i in range(3):
        simboli += itertools.combinations(simboli, i)
    for parola in tqdm(lista):
        for s in simboli:
            newparola = s + parola
            simboli.append(newparola)

    return simboli

    

def setTreshold(lista):
    print("\n\nThinning the list based on letters tresholds...")
    newlista = []
    for item in tqdm(lista):
        if len(item) > minLettersTreshold and len(item) < maxLettersTreshold:
            newlista.append(item)
    return newlista


if __name__ == '__main__':
    title()
    getSettings()
    keylist = getList()
    if maius:
        keylist = keylist + maiuscole(keylist)
    if minus:
        keylist = keylist + minuscole(keylist)
    if composite:
        keylist = compositore(keylist)

    #optimized numberisation
    print("\nThrowing in some numbers...")
    # n = int(len(keylist)/4)

    # result, functRes = multiprocessing.Pipe()

    # lista1 = keylist[:n]
    # lista2 = keylist[n:n*2]
    # lista3 = keylist[n*2:n*3]
    # lista4 = keylist[n*3:]

    # p1 = multiprocessing.Process(target=numeratore, args=(lista1,functRes))
    # p2 = multiprocessing.Process(target=numeratore, args=(lista2,functRes))
    # p3 = multiprocessing.Process(target=numeratore, args=(lista3,functRes))
    # p4 = multiprocessing.Process(target=numeratore, args=(lista4,functRes))

    # p1.start()
    # p2.start()
    # p3.start()
    # p4.start()
    # p3.join()
    # p4.join()
    
    # p1.join()
    # p2.join()

    # keylist = keylist + result.recv()
    if numbers:
        keylist = keylist + numeratore(keylist, "")
        keylist = keylist + addNumbers(keylist)
    
    if simbolsfront:
        keylist = keylist + addSimbolsFront(keylist)
    
    if simbolsrear:
        keylist = keylist + addSimbolsRear(keylist)
   
    keylist = setTreshold(keylist)

    with open('output.txt', 'w') as output:
        print("\n\nFinally writing on a file...")
        for elem in tqdm(keylist):
            output.write('{}\n'.format(elem))

    print('\n\nFile with {} passwords ready, get a coffe and a HashCat!'.format(len(keylist)))
