import random

def poomismäng(sõna):
    äraarvatud_tähed = set()
    elud = 6
    lüngad = ['_' if täht.isalpha() else ' ' for täht in sõna]
    kontroll = 'ABCDEFGHIJKLMNOPQRSTUVWYZÕÄÖÜ'

    while elud > 0:
        print(' '.join(lüngad))
        
        pakkumine = input('Sisesta täht: ').upper()

        if pakkumine in äraarvatud_tähed:
            print('Seda tähte on juba pakutud. Proovi uuesti.')
            continue
        äraarvatud_tähed.add(pakkumine)

        if pakkumine in sõna:
            for i, täht in enumerate(sõna):
                if täht == pakkumine:
                    lüngad[i] = pakkumine
        else:
            if pakkumine.upper() not in kontroll:
                print(f'{pakkumine} ei ole pakutav sümbol')
            if pakkumine.upper() in kontroll:
                elud -= 1
                print(f'Antud tähte selles sõnas pole, {elud} elu alles')

        if all(täht != '_' for täht in lüngad):
            print(f'{sõna}\n Arvasite sõna ära! Elusid jäi alles {elud}')
            break

    if elud == 0:
        print(f"Kahjuks kaotasid. Õige sõna oli {sõna}.")

def vali_sõna():
    while True:
        gamemode = input('Kas soovite ära arvata tavalist sõna (1) või extra-rasket sõna (2): ')
        if gamemode == '1':
            tähearv = int(input('Mitmetähelist sõna soovite see kord ära arvata (sõnapikkused on 8st tähest 12ni): '))
            sobivad_sõnad = [sõna for sõna in sõnad if len(sõna) == tähearv]
            if not sobivad_sõnad:
                print(f"Vabandust, pole {tähearv}-tähelisi sõnu saadaval.")
                return None
            else:
                return random.choice(sobivad_sõnad)
                
        elif gamemode == '2':
            return random.choice(erilised_sõnad)
        else:
            print('Vigane sisend. Palun sisestada 1 või 2')


with open('sõnad.txt', encoding='UTF-8') as f: #Loen failist sõnad muutujatesse sõnad/erilised_sõnad
    erilised_sõnad = f.readline().split(',')
    sõnad = set()
    for rida in f:
        rida = rida.strip().strip("'").split("', '")
        sõnad.update(rida)

print('POOMISMÄNG. Teile antakse 6 elu, teie eesmärk on ükshaaval tähti pakkudes sõna ära arvata.')

poomismäng(vali_sõna())