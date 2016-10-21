## Uputsvo za instalaciju alata potrebnih za predmet Soft Computing (2016)


Alati koji će biti korišćeni na ovom kursu:

* **Anaconda (ver 4.2.0) - Python (ver 2.7)** distribucija sa preko 300 paketa za naučno istraživanje. Sadrži Python, PIP package manager i pomenute pakete/biblioteke.

* **OpenCV (ver 3.0.0)** - alati za računarsku viziju (eng. computer vision)

* **Theano (ver 0.7)** - Python biblioteka za optimizovanje simboličkih matematičkih izraza i numeričkih izračunavanja. 
Može da se izvršava na grafičkoj kartici (GPU) - CUDA, OpenCL...

* **Keras (ver 0.2)** - Python biblioteka za neuronske mreže, bazirana na Theano

**Napomena**: Biće prikazano uputstvo za instalaciju za Windows OS (ali i za Linux distribucije i Mac OSX je prilično slična instalacija).

----

### Instalacija - Anaconda


1. Preuzeti instalaciju za Anacondu sa [https://www.continuum.io/downloads](https://www.continuum.io/downloads). 
**OBAVEZNO: preuzeti verziju Anaconde sa Python-om 2.7 (a ne 3.5).**

2. Dupli-klik na preuzetu .exe datoteku i pratiti instrukcije za instalaciju.

3. Zapamtiti putanju gde je instalirana Anaconda (dalje u uputstvu ova putanja će se zvati ANACONDA_INSTALL_PATH)

----

### Instalacija - OpenCV


1. Preuzeti datoteku **opencv-3.0.0.exe** sa [http://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.0.0/](http://sourceforge.net/projects/opencvlibrary/files/opencv-win/3.0.0/).

2. Dupli-klik na preuzetu .exe datoteku - ovo će zapravo samo otpakovati OpenCV na zadatu putanju.

3. Otići u direktorijum gde je otpakovan OpenCV i pronaći direktorijum **opencv/build/python/2.7**.

4. Kopirati datoteku **cv2.pyd** u direktorijum **ANACONDA_INSTALL_PATH/lib/site-packages**


### Instalacija - Theano

Prvo je neophodno instalirati određene "dependencies" za Theano.

* 1. Otvoriti **Command prompt** i uneti:
```code
conda install mingw libpython
```

* 2. i zatim:

```code
conda update conda
conda update anaconda
```

* 3. Sad još samo instalirati Theano sa PIP:

```code
pip install Theano
```

----

### Instalacija - Keras

1. Potrebno je samo instalirati Keras sa PIP, dakle otvoriti **Command prompt** i uneti:

```code
pip install Keras
```

----

## Uputstvo za kreiranje virtualne mašine (VM)


### Instalacija virtualne mašine

1. Instalirati **Oracle VM VirtualBox (ver 5.x)**.

2. Preuzeti **ftn-ai-lab-2016-vm.7z** sa https://www.dropbox.com/s/ee9on8sivqu5mnq/ftn-ai-lab-2016-vm.7z?dl=1

3. Raspakovati datoteku **ftn-ai-lab-2016-vm.7z**

4. Otvoriti VirtualBox i napraviti novu VM: New -> Name: ftn-ai-lab-2016-vm, Type: Linux, Version: Ubuntu (64-bit) -> Next.

5. Dodeliti **bar 2GB (2048 MB) RAM** za VM -> Next.

6. Izabrati **Use an existing virtual hard disk file** i sa diska odabrati datoteku **ftn-ai-lab-2016-vm.vdi** -> Create.

7. Pokrenuti **ftn-ai-lab-2016-vm** virtualnu mašinu.

#### Kredencijali korisnika

*username*: student

*password*: student

### Šta se nalazi u VM?

* Linux Mint 17.3
* Python 2.7 + Anaconda 4.2.0
* Tensorflow 0.11
* Keras (bleeding-edge verzija sa git-a)

### Python IDE

Anaconda okruženje u sebi sadrži i Spyder IDE koje se može koristit za razvoj aplikacija.

Spyder je skroman IDE, tako da se preporučuje upotreba naprednijih:

* [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows) Community verzija
* [Visual Studio Code](https://code.visualstudio.com) i Python extenzija

### Napomena

Navedena okruženja i programski jezici su samo predlog za upotrebu prilikom izrade projekta. 
Projekat se može raditi u programskom jeziku  i bibliotekama po izboru.



