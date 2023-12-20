import sys, pygame, os, math, random
from button import Button

pygame.init()
ekraan = pygame.display.set_mode((1280, 720))
tähed = pygame.font.Font("assets/font.ttf", 30)
FPS=60
clock = pygame.time.Clock()
clock.tick(FPS)
pygame.display.set_caption("Menüü")

BG = pygame.image.load("assets/Background.png")

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

raadius = 25
vahe = 15
nupud = []
ax=925
ay=150
A = 65    
tähearv = 8
nupud_seaded = []
nupud_seaded = []
valikud = [8,9,10,11,12,13]
axn=550
ayn=250
A = 65
for i in range(6):
    for n in range(3):
        x = axn + ((raadius+20) * 2 + (vahe+5)) * (i%3)
        y = ayn + ((i//3) * ((vahe+5) + (raadius+20)*2))
    nupud_seaded.append([x,y,valikud[i],True])

pildid = []
for i in range(7):
    pildid.append(pygame.image.load("assets/h" + str(i) + ".png" ))
global äraarvatud_tähed
äraarvatud_tähed = []
global mehikese_olukord

mehikese_olukord = 0 #pildi muutuja
tähed = pygame.font.Font("assets/font.ttf", 30)
def vali_sõna(tähearv):
    while True:
        
        if tähearv < 13:
            
            sobivad_sõnad = [sõna for sõna in sõnad if len(sõna) == tähearv]
            return random.choice(sobivad_sõnad)
                
        elif tähearv == 13:
            return random.choice(erilised_sõnad)

with open('assets/sõnad.txt', encoding='UTF-8') as f: #Loen failist sõnad muutujatesse sõnad/erilised_sõnad
    erilised_sõnad = f.readline().split(',')
    sõnad = set()
    for rida in f:
        rida = rida.strip().strip("'").split("', '")
        sõnad.update(rida)

for i in range(26):
    for n in range(3):
        x = ax + (raadius * 2 + vahe) * (i%5)
        y = ay + ((i//5) * (vahe + raadius*2))
    nupud.append([x,y,chr(A+i),True])

x = ax + (raadius * 2 + vahe) * (26%5)
y = ay + ((26//5) * (vahe + raadius*2))
nupud.append([x,y,"Õ",True])
x = ax + (raadius * 2 + vahe) * (27%5)
y = ay + ((27//5) * (vahe + raadius*2))
nupud.append([x,y,"Ä",True])
x = ax + (raadius * 2 + vahe) * (28%5)
y = ay + ((28//5) * (vahe + raadius*2))
nupud.append([x,y,"Ö",True])
x = ax + (raadius * 2 + vahe) * (29%5)
y = ay + ((29//5) * (vahe + raadius*2))
nupud.append([x,y,"Ü",True])

def ekraanile(): #kuvab ekraanile sõna, sobiva pildi ja pakkumisvõimalused
    
    ekraan.fill((255,255,255))
    ekraan.blit(pildid[mehikese_olukord], (0,-2))
    
    arvatav_sõna = ""
    global äraarvatud_tähed
    global sõna
    for täht in sõna:
        if täht in äraarvatud_tähed:
            arvatav_sõna += täht + " "
        else: 
            arvatav_sõna += "_ "
    tekst = tähed.render(arvatav_sõna, 1, "Black")
    ekraan.blit(tekst, (250,640))

    for nupp in nupud:
        x,y,täht,vajutamata = nupp
        if vajutamata:
            pygame.draw.circle(ekraan, (0,0,0) , (x,y), raadius, width=5)
            tekst = tähed.render(täht, 1, (0,0,0))
            ekraan.blit(tekst, (x - tekst.get_width()/2,y - tekst.get_width()/2))




def mäng():  #käivitab mängu
    global mehikese_olukord
    mehikese_olukord = 0
    global äraarvatud_tähed
    äraarvatud_tähed = []
    global sõna
    sõna = vali_sõna(tähearv)

    ekraan = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Mäng")
    
    ekraan.fill((255,255,255))
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        
        PLAY_BACK = Button(image=None, pos=(1200, 700), 
                            text_input="Tagasi", font=get_font(20), base_color="Black", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(ekraan)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                hx, hy = pygame.mouse.get_pos()
                for nupp in nupud:
                    x,y,täht,vajutamata = nupp
                    if vajutamata:
                        kaugus = math.sqrt((x-hx)**2 + (y-hy)**2 )
                        if kaugus < raadius:
                            nupp[3] = False
                            äraarvatud_tähed.append(täht)
                            if täht not in sõna:
                                mehikese_olukord += 1     
        #ekraanile()  
        if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
            main_menu()
        ekraanile()
        võit = True
        for täht in sõna:
            if täht not in äraarvatud_tähed:
                võit = False
                break
        if võit:
            tekst = tähed.render("Võitsid!", 1, "Green")
            ekraan.blit(tekst, (600,400))
            pygame.display.update()
            pygame.time.delay(3000)
            for nupp in nupud:
                nupp [3] = True
            main_menu()
        if mehikese_olukord == 6:
            tekst = tähed.render("Kaotasid", 1, "Red")
            ekraan.blit(tekst, (600,400))
            pygame.display.update()
            pygame.time.delay(3000)
            for nupp in nupud:
                nupp [3] = True
            main_menu()
        pygame.display.update()




def seaded():
    global tähearv 
    ekraan = pygame.display.set_mode((1280, 720))
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        ekraan.fill("Black")

        OPTIONS_TEXT = get_font(45).render("vali raskusaste", True, "White")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 75))
        ekraan.blit(OPTIONS_TEXT, OPTIONS_RECT)
        for nupp_seaded in nupud_seaded:
            x,y,kiri,vajutamata = nupp_seaded
            if vajutamata:
                pygame.draw.circle(ekraan, (255,255,255) , (x,y), raadius+20, width=5)
                tekst = tähed.render(str(kiri), 1, (255,255,255))
                ekraan.blit(tekst, (x - tekst.get_width()/2,y - tekst.get_width()/4))

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="Tagasi", font=get_font(50), base_color="White", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(ekraan)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                hx, hy = pygame.mouse.get_pos()
                for nupp_seaded in nupud_seaded:    
                    x,y,kiri,vajutamata = nupp_seaded
                    if vajutamata:
                        kaugus = math.sqrt((x-hx)**2 + (y-hy)**2 )
                        if kaugus < (raadius+20):
                            tähearv = kiri  
                            nupp_seaded[3] = False
                    else: nupp_seaded[3] = True

                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def main_menu():
    ekraan = pygame.display.set_mode((1280, 720))
    while True:
        ekraan.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Menüü", True, "#b66f66")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 250), 
                            text_input="Mäng", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="Seaded", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 550), 
                            text_input="Välja", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        ekraan.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(ekraan)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mäng()


                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    seaded()


                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

while True:
    main_menu()