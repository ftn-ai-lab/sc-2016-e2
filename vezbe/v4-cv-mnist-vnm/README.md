# Takmičenje u sabiranju brojeva na slikama uz korišćenje veštačkih neuronskih mreža


----------


### Opis zadatka


----------


Na osnovu slika iz obučavajućeg skupa potrebno je napisati program koji sabira sve cifre koje se na njima pojavljuju. Cifre su preuzete iz MNIST dataset-a.
Kao rešenje, potrebno je svom asistent dostaviti popunjen `out.txt` fajl koji sadrži programski dobijene rezultate i programski kod vašeg rešenja.
Za implementaciju koristiti veštačke neuronske mreže i programski jezik po izboru. Klasifikacija cifara korišćenjem veštačkih neuronskih mreža je već obrađena na predavanju, korišćenjem Python programskog jezika i Keras razvojnog okvira za rad sa VNM. Pošto sada cifre nemaju uokvirenu pozadinu i pošto nisu iste veličine, koristiti pokretni prozor dimenzija 28x28 unutar koga će se vršiti klasifikacija korišćenjem obučene veštačke neuronske mreže, po uzoru na primer sa predavanja.

Rešenje, `out.txt` mora da sadrži sledeće:
  * **Broj indeksa**, **ime** i **prezime**
  * Popunjene podatke koliki je zbir cifara na svakoj slici (parovi ime slike i zbir cifara)


**Rok za dostavljanje rešenja je: 20.11.2016. 23:59:59**
Prijave nakon isteka predviđenog vremena neće biti uzete u razmatranje.

### Skup podataka


----------


Podaci su podeljeni u 2 kategorije: **train** i **test**. Obe arhive sa podacima se mogu preuzeti sa sledećeg linka: [https://drive.google.com/drive/folders/0B1ZJXQY32LBUVVJwMWVjc19QQnM?usp=sharing](https://drive.google.com/drive/folders/0B1ZJXQY32LBUVVJwMWVjc19QQnM?usp=sharing)

#### Train skup


Zip arhiva sa podacima za treniranje sadrži sledeće:
* folder `Images` sadrži slike na kojima treba da detektujete i klasifikujete cifre, a nakon toga da ih sve saberete
* `test.py` program koji validira uspešnost vašeg rešenja nad train skupom podataka (na osnovu `res.txt` i `out.txt`)
* `res.txt` tačno rešenje za svaku sliku (kombinacija ime fajla i zbir svih cifara)
* `out.txt` fajl u koji je potrebno upisati zbir cifara koje je vaš program izračunao (trenutno su sve nule)


#### Test skup


Zip arhiva sa podacima za testiranje sadrži sledeće:
* folder `Images` sadrži slike na kojima treba da detektujete i klasifikujete cifre, a nakon toga da ih sve saberete
* `out.txt` fajl u koji je potrebno upisati zbir cifara koje je vaš program izračunao (trenutno su sve nule). **Ovaj fajl treba da popunite programski i da ga pošaljete svom asistentu.**



----------
#### Rezime
Skup podataka za treniranje koristite u fazi razvoja, sve dok ne postignete željenu tačnost.

Kada postignete željenu tačnost na slikama za treniranje, izvršite vaš program nad slikama za testiranje. Rezultat bi trebao da bude `out.txt` fajl sa vašim rezultatima. Taj fajl šaljete svom asistentu, zajedno sa programskim kodom.