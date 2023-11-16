from time import sleep
from random import randint

def vali_sõna(arv):
    with open('sõnad.txt', encoding='utf-8') as f:
        sisu = f.read()
        sisu = sisu.split('\n')
        if arv == 'r' or arv == 'R':
            sisu = sisu[0].split(',')
            return sisu[randint(0,6)]
        if arv == '8':
            sisu = sisu[1].split(',')
            return sisu[randint(0,22)]
        if arv == '9':
            sisu = sisu[2].split(',')
            return sisu[randint(0,6)]
        if arv == '10':
            sisu = sisu[3].split(',')
            return sisu[randint(0,9)]
        if arv == '11':
            sisu = sisu[4].split(',')
            return sisu[randint(0,7)]

        
while True:
    print('Mänguks on ülespoomine. Pead tähti pakkudes ära arvama sõna enne, kui elud otsa saavad (elusid on kokku 7). Kaotad elu iga valesti pakutud tähe eest.')
    sleep(1)
    mode = input('Vali mängurežiim!\n8 Tähte -> 8\n 9 Tähte -> 9\n 10 Tähte -> 10\n 11 Tähte -> 11\n Eriti rasked sõnad -> r\n QUIT -> Q\n: ')
    if mode == 'q' or mode == 'Q':
        print('Hüvasti!')
        break
    else:
        print('_'*50)
        print(vali_sõna(mode))