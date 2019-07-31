print('''Benvenuto in Dictionatorator!!! 
Questo script creerà degli utili dizionari a partire da alcune parole.

10 parole differenti portano a circa 1 milione di possibili risultati, cerca di non esagerare ;)

Premi 1 per scegliere alcune parole per cominciare. 
Inserisci le tue parole e, quando hai finito, scrivi %%% (3 volte '%') per uscire!''')
lista = []
scelta = input()
if scelta == '1':
    while True:
        parola = input('Parola -> ')
        if parola == '%%%':
            print('Hai inserito {} parole! Calcolo le possibili password...'.format(len(lista)))
            break
        else:
            lista.append(parola)

composte = []
maius = []
def maiuscole(lista):
    print('Le maiuscolizzo....')
    for parola in lista:
        maiusc = parola.upper()
        maius.append(maiusc)
minus = []

def minuscole(lista):
    print('Le minuscolizzo...')
    for parola in lista:
        minusc = parola.lower()
        minus.append(minusc)

titles = []

def titler(lista):
    print('Le titolizzo...')
    for parola in lista:
        titled = parola.title()
        titles.append(titled)


def compositore(maius, minus, titles):
    print('Faccio le moltiplicazioni...')
    import itertools
    compostemaius = maius + maius + list(''.join(e) for e in itertools.product(maius, maius))
    composteminus = minus + minus + list(''.join(e) for e in itertools.product(minus, minus))
    compostetitles = titles + titles + list(''.join(e) for e in itertools.product(titles, titles))
    compostemaiusminus = maius + minus + list(''.join(e) for e in itertools.product(maius, minus))
    composteminusmaius = minus + maius + list(''.join(e) for e in itertools.product(minus, maius))
    compostemaiustitles = maius + titles + list(''.join(e) for e in itertools.product(maius, titles))
    compostetitlesmaius = titles + maius + list(''.join(e) for e in itertools.product(titles, maius))
    composteminustitles = minus + titles + list(''.join(e) for e in itertools.product(minus, titles))
    compostetitlesminus = titles + minus + list(''.join(e) for e in itertools.product(titles, minus))
    finale = set(compostemaius + composteminus + compostetitles + compostemaiusminus + composteminusmaius
                 + compostemaiustitles + compostetitlesmaius + composteminustitles + compostetitlesminus)
    return finale



parolenumerate = []
def numeratore(lista):
    print('Aggiungo dei numeri...')
    for parola in lista:
        for i in ["{0:03}".format(i) for i in range(0, 101)]:
            newparola = parola + str(i)
            if len(newparola) > 6:
                parolenumerate.append(newparola)
        for i in ["{0:02}".format(i) for i in range(0, 101)]:
            newparola = parola + str(i)
            if len(newparola) > 6:
                parolenumerate.append(newparola)
        for i in ["{0:02}".format(i) for i in range(0, 101)]:
            newparola = str(i) + parola
            if len(newparola) > 6:
                parolenumerate.append(newparola)
        for i in ["{0:04}".format(i) for i in range(0, 1001)]:
            newparola = parola + str(i)
            if len(newparola) > 6:
                parolenumerate.append(newparola)
        for i in ["{0:03}".format(i) for i in range(0, 101)]:
            newparola =  str(i) + parola
            if len(newparola) > 6:
                parolenumerate.append(newparola)
        for i in range(1,100):
            newparola =  str(i) + parola
            if len(newparola) > 6:
                parolenumerate.append(newparola)
        for i in range(1,100):
            newparola = parola + str(i)
            if len(newparola) > 6:
                parolenumerate.append(newparola)



maiuscole(lista)
minuscole(lista)
titler(lista)

composte = compositore(maius, minus, titles)
numeratore(composte)
finalissimo = set(parolenumerate+maius+minus+titles+list(composte))
with open('output.txt', 'a+') as output:
    for elem in finalissimo:
        output.write('{}\n'.format(elem))

print('Il tuo file è stato creato con successo! Pronto a fare {} tentativi?'.format(len(finalissimo)))
