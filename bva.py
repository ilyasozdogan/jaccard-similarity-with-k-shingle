

from __future__ import division #islemlerin ondalik sonuc vermesini saglar or:8/7=1.14285 olarak verir
import binascii   #stringleri numerik degiskenlere cevirir "signed 32-bit CRC" kullanarak
from stop_words import get_stop_words  #ingilizcedeki stop wordleri alir


stop_words = get_stop_words('english') #ingilizcedeki stop wordleri stop_words dizinine aktariyoruz.
#The Supreme Court in Johnnesberg on Friday postponed until March 14
#uygulamada 3 tip shingle bulunmaktadir
# 1. si shingle lari kelime olarak alir (2-shingle The Supreme,Supreme Court,Court in gibi)
# 2. si shingle lari karakter olarak alir (2-shingle Th,he,e , S,Su  gibi)
# 3. su stop wordslerden sonraki kelimler dikkate alir (2-shingle The Supreme,in Johnnesberg gibi)


shingle_tipi=3 #shingle tipi secilir
shingle_sayisi=3 # shingle sayisi secilir
esikdegeri = 0.8 #Jaccard benzerligi bu degerden buyuk olan dokumanlar listelenir



dokuman_say = 0
shingle=""
dosya = "dokumanlar.txt" #ayni klasorde dokumanlarin yer aldigi text dosyasi
# bu dosyada her bir dokuman 1 satir yer kaplayacak sekilde siralanir
satir=0
with open (dosya,'rb') as f: # dosya acilarak satir sayisi sayilir
    for line in f:
        satir+=1

dokuman_sayisi=satir # dosyadaki satir sayisi dokuman sayisini bize verir
print str(shingle_tipi)+". yontem kullanilarak"
print str(shingle_sayisi)+" shingle sayisi ile"
print str(dokuman_sayisi)+" tane dokumanin jaccard benzerligi hesaplaniyor..."

print "Jaccard benzerligi "+str(esikdegeri)+ "'den yuksek olanlar ekrana yazdirilacak"

dokuman_shingle = {} #her bir dokumanin shingle kumeleri bu degiskende saklanacak


f = open(dosya, "rU") #dosya acilarak shingle lar olusturulmaya baslanir

dokuman_adi = []
satirlar=[]
satirlar2=""
if shingle_tipi == 2:
    dokuman_sayisi=20
for i in range(0, dokuman_sayisi):#her bir satira islem yapmak icin for dongusu kullanilir
    kelimeler = f.readline().split(" ") #dokumanlari bosluklari kullanarak kelimelere ayiriyoruz
    dokuman_ID = kelimeler[0] #satirin basindaki dokuman isimleri dokuman_ID degiskenine atilir
    dokuman_adi.append(dokuman_ID) #dokuman isimleri dokuman_adi dizisine atilir.
    del kelimeler[0] # dizinin ilk elemani dokuman adi oldugu icin, sadece kelimelerin bulunmasi adina ilk eleman silinir
    dokumandaki_shingle = set()
    # The Supreme Court in Johnnesberg on Friday postponed until March 14
    if shingle_tipi == 1:
        for index in range(0, len(kelimeler) - (shingle_sayisi)):
            #3 shingle icin yukaridaki cumleyi ele alirsak kumede 8 eleman yer alir
            #8 sayisina ulasabilmek icin kelime sayisi(11)-shingle sayisi(3)=8 islemi yapilir
            for t in range(0, (shingle_sayisi)):
                shingle += kelimeler[index+t] + " "
                #kac shingle ise o kadar kelime birlestirilir
                #3 shingle icin ilk shingle "The Supreme Court" olur
            shingle=shingle.strip() #olusturulan shingle in basindaki ve sonundaki bosluk silinir
            crc = binascii.crc32(shingle) & 0xffffffff # olusturulan shingle lar numeric ifadeye donusturulur
            dokumandaki_shingle.add(crc) #dokumanda bulunan shingle lar bu degiskende saklanir
            shingle="" # bir sonraki shingle icin degisken degeri silinir
    if shingle_tipi == 2:
        for kelime in range(0, len(kelimeler)):
            satirlar2+=kelimeler[kelime]+" " #kelimeleri birlestirerek tek bir cumle haline getirilir
        satirlar2=satirlar2.strip()
        for kelime2 in range(0, len(satirlar2)-(shingle_sayisi)):
            #3 karakter shingle icin yukaridaki cumleyi ele alirsak kumede 67 eleman yer alir
            #67 sayisina ulasabilmek icin karakter sayisi(70)-shingle sayisi(3)=67 islemi yapili
            for t in range(0, (shingle_sayisi)):
                shingle += satirlar2[kelime2+t]
                # kac shingle ise o kadar karakter birlestirilir
                # 3 shingle icin ilk shingle "The" olur
            crc = binascii.crc32(shingle) & 0xffffffff # olusturulan shingle lar numeric ifadeye donusturulur
            dokumandaki_shingle.add(crc) #dokumanda bulunan shingle lar bu degiskende saklanir
            shingle="" # bir sonraki shingle icin degisken degeri silinir
    if shingle_tipi == 3:
        for index in range(0, len(kelimeler) - (shingle_sayisi)):
            # Cumledeki tum kelimelerin stopword oldugu varsayilarak kume sayisi hesaplanir
            # Kume sayisindan shingle sayisi cikarilarak max dongu sayisi bulunur
            if kelimeler[index] in stop_words: #her bir kelimenin stop words olup olmadigi kontrol edilir
                for t in range(0, (shingle_sayisi)):
                    shingle += kelimeler[index+t] + " " #stop word ise kelimeden sonrakiler shingle sayisina gore birlestirilir
                shingle=shingle.strip() #olusturulan shingle in basindaki ve sonundaki bosluk silinir
                crc = binascii.crc32(shingle) & 0xffffffff # olusturulan shingle lar numeric ifadeye donusturulur
                dokumandaki_shingle.add(crc)  #dokumanda bulunan shingle lar bu degiskende saklanir
                shingle="" # bir sonraki shingle icin degisken degeri silinir
    dokuman_shingle[dokuman_ID] = dokumandaki_shingle #dokumandaki butun shingle lar id ye gore saklanir

f.close()

print "                              Jaccard Benzerligi"


for i in range(1, dokuman_sayisi-1):
        for j in range(i + 1, dokuman_sayisi):
        # her dokuman kendinden sonraki dokumanlar ile karsilastirilir
        #satir baslarindaki id lere gore dokumandaki tum shingle lar s1 e atanir
        #sonraki dokumandaki shingle lar s2 ye atanir
            s1 = dokuman_shingle[dokuman_adi[i]]
            s2 = dokuman_shingle[dokuman_adi[j]]
        #kumelerin kesisim degeri birlesim degerine bolunerek jaccard benzerligi bulunur
            J = (len(s1.intersection(s2)) / len(s1.union(s2)))


            if J > esikdegeri: #eger jaccard degeri esik degerden buyukse print edilir
                print "  %5s <--> %5s -----> %.2f" % (dokuman_adi[i], dokuman_adi[j], J)



print("bitti")
raw_input()