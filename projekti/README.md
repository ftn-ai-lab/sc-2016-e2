#Predmetni projekat - Soft Computing 2016 E2

## Osnovne informacije o projektu
Predmetni projekat se sastoji iz:

* **Praktični deo = 50 bodova**
* **Teorijski deo - usmeni (odbrana projekta + poster) = 50 bodova**

Projekat se radi u timu od **1-3 studenta**. Projekat je obavezan za sve studente.

Studenti mogu da biraju jednu od dve vrste projekta:

* Projekat na temu po izboru
* Predefinisani projekat


Studenti koji se odluče za **temu po svom izboru**, preporučljivo je da se pre početka izrade projekta dogovore sa asistentom u terminu vežbi ili profesorom u terminu predavanja oko teme i opsega/ozbiljnosti projekta. Ovakav tip projekta će zahtevati samostalno istraživanje na temeljima teorijskih osnova koje ste naučili na predavanjima i zamišljen je za studente kojima je gradivo interesantno i koji žele naučiti više.
**Predefinisani projekat** je namenjen studentima koji nemaju dovoljno jasnu ideju šta bi samostalno radili. Specifikacija predefinisanog projekta će biti data u nastavku ovog dokumenta.

>Predmetni projekat se ocenjuje isključivo u odnosu na kompletnost, kompleksnost i tačnost vašeg rešenja. I na predefinisani i na sopstveni projekat možete dobiti ocene u opsegu od 6 do 10. 

**Donošenje tuđih projekata će biti najstožije kažnjavano zabranom odbrane projekta na period od godinu dana. Sva vaša rešenja će biti analizirana, a preklapanja od bar 50% će se smatrati plagijatima.**

## Prijava projekta
Rok za prijavu projekta je **05.01.2016. do 12h.**

Rok za završetak izrade projekta je kraj januara meseca. Termin odbrane projekata će biti naknadno objavljen, a isti će biti početkom februara meseca.

Projekti se prijavljuju otvaranjem novog "issue" na stranici https://github.com/ftn-ai-lab/sc-2016-e2/issues. Prilikom prijave projekta, naslov "issue"-a neka bude tema projekta, u Assignee dodati vašeg asistenta, a u samom opisu neophodno je navesti:

* Ko su članovi tima, grupa sa vežbi? Ime, prezime, broj indeksa...
* Problem koji se rešava (detaljniji opis)
* Algoritam/algoritmi koji će se koristiti
* Metrika za poređenje performansi algoritama i/ili parametara algoritma
* Podaci koji se koriste - da li su već dostupni online, da li će se skupljati automatski ili manuelno, da li se moraju prvobitno obraditi?
* Na koji način planirate validaciju rešenja?

Nakon konačnog oformljivanja timova i odabira tema, asistenti će vam odgovoriti na "issue" da li vam je tema odobrena. Nakon što tema bude odobrena, morate napraviti javan Github repozitorijum na kom ćete držati sav izvorni kod, dokumentaciju (kako se koristi vaš kod, i šta je sve potrebno od softvera) i poster. Naravno, u vaš "issue" upišite link ka repozitorijumu.

**Studentima koji ne ispoštuju navedenu formu u opisima svojih projekata će biti dodeljen predefinisan projekat i neće im biti omogućena izrada projekta po izboru. Nekome ko prvi put vidi vaš opis treba biti jasno šta radite, kako to planirate, kako planirate validaciju rešenja i slično.**

## Specifikacija predefinisanog projekta

Predefinisani projekat je podeljen u tri kategorije, od kojih svaka naredna nosi mogućnost dobijanja veće ocene. Predefinisani projekat predstavlja proširenje domaćih zadataka koje ste rešavali u toku semestra. Ocena se formira na osnovu težine (levela) zadatka koji ste rešavali, na osnovu postignute tačnosti i na osnovu znanja koje pokažete na samoj usmenoj odbrani projekta.

* Level 1 - Predefinisani projekat za ocenu 6. Skup podatata nad kojim treba da odradite zadatak se nalazi na sledećem [linku](https://drive.google.com/drive/folders/0B1ZJXQY32LBUT3pwdll3eXU4eUU?usp=sharing). 
 > * Video zapis poseduje jednu liniju koja se uvek nalazi na istoj poziciji, uvek je iste boje i možete je detektovati tehnikom po vašoj želji.
 > * Video zapis sadrži pokretne cifre koje prelaze preko linije
 > * Izvršiti sabiranje svih cifara koje pređu preko linije
 > * Potrebno je postići tačnost prepoznavanja od bar 85%.
 
*  Level 2 - Predefinisani projekat za ocene 7 i 8. Skup podatata nad kojim treba da odradite zadatak se nalazi na sledećem [linku](https://drive.google.com/drive/folders/0B1ZJXQY32LBUMWdxWkEzcmVYblU?usp=sharing). 
  > * Video zapis poseduje jednu pokretnu liniju koja je uvek iste boje. Liniju detektovati korišćenjem Hough transformacije.
  > * Cifre se kreću za slučajan broj koraka i prolaze iza pokretne linije
  > * Potrebno je izvršiti sabiranje svih cifara koje prođu ispod linije
  > * Potrebno je postići tačnost prepoznavanja od bar 90%.
  
* Level 3 - Predefinisani projekat za ocene 9 i 10. Skup podatata nad kojim treba da odradite zadatak se nalazi na sledećem [linku](https://drive.google.com/drive/folders/0B1ZJXQY32LBUU3FiTS14a3NZd1U?usp=sharing). 
  > * Video zapis poseduje dve pokretne linije koje je potrebno detektovati Hough transformacijom.
  > * Cifre prolaze iza pokretnih linija.
  > * Cifre koje prođu ispod prve linije treba sabrati, a cifre koje pređu ispod druge linije treba oduzeti od konačnog rezultata.
  > * Pokušati rešiti slučaj preklapajućih cifara koje istovremeno prelaze preko linije, a nalaze se jedna preko druge u određenoj meri.
  > * Za najvišu ocenu je potrebno postići tačnost prepoznavanja od bar 95%.
