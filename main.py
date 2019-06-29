# 1 - Import library
# try :
#    import pygame_sdl2
#    pygame_sdl2.import_as_pygame()
#    from pygame.locals import *
#except ImportError:
#    pass
import pygame
import math
import random
import pickle

# objective :
# a : (tutorial) 
# b : kata n huruf 
# c : score 
# d : selesaikan dalam waktu x detik
# e : mode survival (timer nambah tiap kata benar)
# f : story mode (sesuaikan kata dengan cerita)
# g : memory mode (ada huruf yang dihidden, ditampilkan waktu di awal)
# h : fever mode (kalo sudah nemu sekian kata, bisa ngakses bebas)
# i : multiplayer mode
# j : rotasi mode
# k : collapse / replace waktu ada kata yang ketemu
# l : kasih skor negatif kalo salah nebak. kasih achievement dan skor lebih kalo selesai sebelum waktu tertentu

def randomize(area):
    #mengacak alfabet dalam area permainan
    for x in range(w):
        for y in range(h):
            # uniform randomness
            # area[x][y] = alfabet[random.randrange(len(alfabet))]

            # proporsional randomness
            angka = random.randrange(100000)
            if angka<14203:
                area[x][y]='a'
            elif angka < 15105:
                area[x][y]='c'
            elif angka < 17496:
                area[x][y]='b'
            elif angka < 25754:
                area[x][y]='e'
            elif angka < 28203:
                area[x][y]='d'
            elif angka < 32358:
                area[x][y]='g'
            elif angka < 33291:
                area[x][y]='f'
            elif angka < 42460:
                area[x][y]='i'
            elif angka < 44060:
                area[x][y]='h'
            elif angka < 49701:
                area[x][y]='k'
            elif angka < 50550:
                area[x][y]='j'
            elif angka < 54697:
                area[x][y]='m'
            elif angka < 59536:
                area[x][y]='l'
            elif angka < 64719:
                area[x][y]='o'
            elif angka < 71976:
                area[x][y]='n'
            elif angka < 71986:
                area[x][y]='q'
            elif angka < 75105:
                area[x][y]='p'
            elif angka < 81340:
                area[x][y]='s'
            elif angka < 87780:
                area[x][y]='r'
            elif angka < 92640:
                area[x][y]='u'
            elif angka < 98386:
                area[x][y]='t'
            elif angka < 98960:
                area[x][y]='w'
            elif angka < 99292:
                area[x][y]='v'
            elif angka < 99825:
                area[x][y]='y'
            elif angka < 99839:
                area[x][y]='x'
            else:
                area[x][y]='z'
    return area

def penyesuaian(area,katavalid,a,b):
    #mencari area permainan yang isiannya antara a dan b buah kata valid
    num = len(katavalid)
    i=2
    while(len(katavalid)<a or len(katavalid)>b):
        change = random.randrange(w*h)
        print "random number =",change
        x = change/w
        y = (change-x*w)
        area[x][y]=alfabet[random.randrange(len(alfabet))]
        print "diubah posisi",x,",",y,"menjadi",area[x][y]
        katavalid=[]
        listall(area,katavalid)
        print area
        print "percobaan ke-",i,"katavalid ada",len(katavalid)
        i+=1

def eksis(kata,area,ke,pos,ada):
    #kata dikirim penuh ke rekursi selanjutnya. area dihilangkan abjad yang sudah dipakai
    #"ke" menunjukkan urutan abjad yang diperiksa, "pos" adalah posisi terakhir kursor
    #melihat apakah kata ada di dalam area permainan secara rekursif
    #ke = 0 dan pos = 0 artinya awal kalimat, bisa dimulai dari posisi manapun
    #variabel start menyimpan semua nomor kotak yang berhuruf sama dengan huruf awal kata
    #kotak dinomori 1,2, dst dari kiri atas ke kanan, dan baris selanjutnya
    if ke == 0 :
        #awal, cari semua kandidat lokasi awal
        start = []
        ada = False
        for x in range(w):
            for y in range(h):
                if area[x][y] == kata[0]:
                    start.append((x,y))
        for posisi in start:
            x,y = posisi[0], posisi[1]
            area[x][y]=""
            ada = eksis(kata,area,ke+1,posisi,ada)
            area[x][y]=kata[ke]
            if ada:
                return ada
        return ada
    elif (ke == len(kata)-1):
        #cek huruf terakhirnya ada gak di sekitar posisi terakhir
        huruf = kata[-1]
        x,y = pos[0], pos[1] 
        try :
            if area[x+1][y+1]==huruf:
                ada = True
        except Exception:
            pass
        try :
            if area[x+1][y]==huruf:
                ada = True
        except Exception:
            pass
        try :
            if area[x+1][y-1]==huruf:
                ada = True
        except Exception:
            pass 
        try :
            if area[x][y-1]==huruf :
                ada = True
        except Exception:
            pass
        try :
            if area[x-1][y-1]==huruf :
                ada = True
        except Exception:
            pass
        try :
            if area[x-1][y]==huruf :
                ada = True
        except Exception:
            pass
        try :
            if area[x-1][y+1]==huruf :
                ada = True
        except Exception:
            pass
        try :
            if area[x][y+1]==huruf :
                ada = True
        except Exception:
            pass
        return ada
        #kata ketemu dalam papan
    elif (not ada):
        #iterasi ke huruf selanjutnya
        next = []
        huruf = kata[ke]
        x,y = pos[0], pos[1]
        try: 
            if area[x+1][y+1]==huruf: #Tenggara
                next.append((x+1,y+1))
        except Exception:
            pass
        try: 
            if area[x][y+1]==huruf: #Selatan
                next.append((x,y+1))
        except Exception:
            pass
        try: 
            if area[x-1][y+1]==huruf: #Barat Daya
                next.append((x-1,y+1))
        except Exception:
            pass
        try: 
            if area[x-1][y]==huruf: #Barat
                next.append((x-1,y))
        except Exception:
            pass
        try: 
            if area[x-1][y-1]==huruf: #Barat Laut
                next.append((x-1,y-1))
        except Exception:
            pass
        try: 
            if area[x][y-1]==huruf: #Utara
                next.append((x,y-1))
        except Exception:
            pass
        try: 
            if area[x+1][y-1]==huruf: #Timur Laut
                next.append((x+1,y-1))
        except Exception:
            pass
        try: 
            if area[x+1][y]==huruf: #Timur
                next.append((x+1,y))
        except Exception:
            pass
        for posisi in next:
            x,y = posisi[0], posisi[1]
            area[x][y]=""
            ada = eksis(kata,area,ke+1,posisi,ada)
            area[x][y]=kata[ke]
            if ada:
                return ada
        return ada
 
def listall(area,katavalid):
    #mendaftar semua kata dalam bahasa indonesia yang ada di dalam area
    #panjang maksimal = ?
    for kata in daftar:
        if(eksis(kata,area,0,0,0)):
            katavalid.append(kata)

def cekkoordinat(posisi):
    x,y = posisi[0],posisi[1]
    kx = (x-40)/(box.get_width()+5)
    ky = (y-40)/(box.get_height()+5)
    cx,cy = (40+kx*(box.get_width()+5),40+ky*(box.get_height()+5))
    #print x,y,cx,cy,kx,ky
    #return (kx,ky)
    if (cx+15<x<cx+60) and (cy+15<y<cy+60):
        return (kx,ky)
    else :
        return (-1,-1)

# 2 - Initialize the game
# 2.a - Terkait dengan pygame
pygame.init()
width, height = 640, 480
areawidth, areaheight = 400, 400
w,h = 5, 5
area = [['' for x in range(w)] for y in range(h)] 
screen=pygame.display.set_mode((width, height))
keys = [False, False, False, False]
tilepos=[0,0]
pygame.mixer.init()
fontObj = pygame.font.Font('freesansbold.ttf', 18)

#2.b - Terkait game
daftar = pickle.load(open("helper/kata.p","rb"))
katavalid = []
kataterpilih = []
alfabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
picalfabet = {}
pushalfabet = {}
score = 0
randomize(area)
listall(area,katavalid)
print "list pertama, katavalid ada",len(katavalid)
#if(len(katavalid)>50):
#    penyesuaian(area,katavalid,20,40)

# 3 - Load image
background = pygame.image.load("resource/bg1.jpeg")
box = pygame.image.load("resource/box75.png")
menubar = pygame.image.load("resource/menubar.png")
gameover = pygame.image.load("resource/gameover.png")
youwin = pygame.image.load("resource/youwin.png")
for letter in alfabet:
    picalfabet[letter] = pygame.image.load("alfabet/"+letter+".png")
    pushalfabet[letter] = pygame.image.load("alfabet/"+letter+"2.png")
# 3.1 - Load audio
klik = pygame.mixer.Sound("resource/klik.wav")
klik.set_volume(0.05)
pygame.mixer.music.load('resource/moonlight.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# 4 - keep looping through
running = 1
exitcode = 0
push = False
selection = []
while running:
    # 5 - clear the screen before drawing it again
    screen.fill(0)
    # 6 - draw background and menu
    screen.blit(background,(0,0))
    screen.blit(menubar,(480,0))
    for x in range(w):
        for y in range(h):
            screen.blit(box,(40+x*(box.get_width()+5),40+y*(box.get_height()+5)))
    # 6 - draw alphabet
    for x in range(w):
        for y in range(h):
            screen.blit(picalfabet[area[x][y]],(40+x*(box.get_width()+5),40+y*(box.get_height()+5)))
    # 6 - draw selected alphabet
    for x,y in selection:
        screen.blit(pushalfabet[area[x][y]],(40+x*(box.get_width()+5),40+y*(box.get_height()+5)))
    # draw list
    x = 500
    y = 60
    i = 0
    textSurfaceObj = fontObj.render("Score = "+str(score), True, (0,0,128), (128,128,128))
    screen.blit(textSurfaceObj, (x,30)) 
    for kata in kataterpilih:
        textSurfaceObj = fontObj.render(kata, True, (0,0,128), (128,128,128))
        lokasi = (x,y+i*20)
        i+=1
        screen.blit(textSurfaceObj, lokasi) 
    
    # 7 - update the screen
    pygame.display.flip()
    for event in pygame.event.get():
        # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos = cekkoordinat(event.pos)
            if (pos not in selection and pos[0] in range(w) and pos[1] in range(h)):
                selection.append(pos)
                print "start di posisi", pos
            push = True
        elif event.type==pygame.MOUSEMOTION:
            if(push):
                pos = cekkoordinat(event.pos)
                if (pos not in selection and pos[0] in range(w) and pos[1] in range(h)):
                    try :
                        if (abs(pos[0]-selection[-1][0]) <2 and abs(pos[1]-selection[-1][1])<2):
                            selection.append(pos)
                            print pos
                    except Exception:
                        if(len(selection)==0):
                            selection.append(pos)
                            print pos
            
        elif event.type==pygame.MOUSEBUTTONUP:
            push = False
            #cek kata yang dipilih ada di list katavalid atau tidak 
            print "up di posisi", cekkoordinat(event.pos)
            kata = ""
            for pos in selection :
                kata= kata + area[pos[0]][pos[1]]
            selection = []               
            if kata in katavalid:
                # tambah skor
                print "kata",kata,"ada di list"
                if kata in kataterpilih :
                    print "kata itu sudah didaftarkan"
                else :
                    kataterpilih.append(kata)
                    score+=len(kata)
            else:
                print "kata",kata,"tidak ada"

            
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()

