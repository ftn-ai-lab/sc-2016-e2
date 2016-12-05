# Takmičenje u brojanju cifara koje prelaze preko plave linije


----------


### Opis zadatka


----------


Na osnovu video snimaka iz obučavajućeg skupa potrebno je napisati program koji broji sve cifre koje u toku video snimka pređu plavu liniju. Cifre su preuzete iz MNIST dataset-a.
Kao rešenje, potrebno je svom asistent dostaviti popunjen `out.txt` fajl koji sadrži programski dobijene rezultate i programski kod vašeg rešenja.
Za implementaciju koristiti tehnike i programski jezik po izboru.

Rešenje, `out.txt` mora da sadrži sledeće:
  * **Broj indeksa**, **ime** i **prezime**
  * Popunjene podatke koliko je cifara prešlo plavu liniju na svakom video snimku (parovi ime video snimka i broj cifara)


**Rok za dostavljanje rešenja je: 04.12.2016. 23:59:59**
Prijave nakon isteka predviđenog vremena neće biti uzete u razmatranje.

### Skup podataka


----------


Podaci su podeljeni u 2 kategorije: **train** i **test**. Obe arhive sa podacima se mogu preuzeti sa sledećeg linka: [https://drive.google.com/drive/folders/0B1ZJXQY32LBUZkxLandQWkdlUGs?usp=sharing](https://drive.google.com/drive/folders/0B1ZJXQY32LBUZkxLandQWkdlUGs?usp=sharing)

#### Train skup


Zip arhiva sa podacima za treniranje sadrži sledeće:
* folder `videdos` sadrži video snimke na kojima treba da detektujete cifre, a nakon toga da prebrojite one koje pređu plavu liniju
* `test.py` program koji validira uspešnost vašeg rešenja nad train skupom podataka (na osnovu `res.txt` i `out.txt`)
* `res.txt` tačno rešenje za svaku sliku (kombinacija ime fajla i broj prebrojanih cifara)
* `out.txt` fajl u koji je potrebno upisati rezultat koje je vaš program izračunao (trenutno su sve nule)


#### Test skup


Zip arhiva sa podacima za testiranje sadrži sledeće:
* folder `videos` sadrži video snimka na kojima treba da detektujete cifre, a nakon toga da prebrojite one koje pređu plavu liniju
* `out.txt` fajl u koji je potrebno upisati rezultat koje je vaš program izračunao (trenutno su sve nule). **Ovaj fajl treba da popunite programski i da ga pošaljete svom asistentu.**



----------
#### Rezime
Skup podataka za treniranje koristite u fazi razvoja, sve dok ne postignete željenu tačnost.

Kada postignete željenu tačnost na video snimcima za treniranje, izvršite vaš program nad video snimcima za testiranje. Rezultat bi trebao da bude `out.txt` fajl sa vašim rezultatima. Taj fajl šaljete svom asistentu, zajedno sa programskim kodom.

OpenCV funkcije koje bi mogle biti od koristi, a nisu obrađene na predavanju:
* [cv2.inRange(src, lowerb, upperb[, dst]) → dst](http://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#inrange), [[pročitaj više]](http://stackoverflow.com/a/20053409)
