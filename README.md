Sammud Seleniumtest_rik.py testkeskkonna üles seadmiseks.

1. Kui Chrome veebilehitsejat pole installeeritud siis tuleks esmalt see installerida: https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAiAg9rxBRADEiwAxKDTurYAbsSfeI9L0rwPEkZ9Kq8rtKbmNtgQpdRyioxhCE65qgCdM7ngbhoCmw8QAvD_BwE&gclsrc=aw.ds

2. Installeeri Python 3.8.0 oma seadmesse. Windowsi masina jaoks leiad
õpetuse siit: https://docs.python.org/3/using/windows.html

3. Installeeri pip: https://pip.pypa.io/en/stable/installing/

4. Installeeri BeautifulSoup4:https://www.youtube.com/watch?v=yhgyICa98zk
5. Installeeri Seleniumi pakett: https://selenium-python.readthedocs.io/installation.html

6. Lae alla chromedriver seleniumi jaoks: https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.16/

7. Tee chromedriveri jaoks kaust mis asub C:\browserdriver\ ja lisa sinna chromedriver.exe, mille laadisid alla sammu 5 juures.



Programmi kirjeldus:

Programm testib https://www.rik.ee/ leheküljel olevaid linke ja annab tagasisidet, kas lingis kirjeldatud lehekülg päriselt sinna klikides ka avaneb.

Testitavad lingid:

1. E-äriregister
2. Euroopa äriregister
3. Ettevõtjaportaal
4. Kinnistuportaal

Programmi käivitamisele järgnevad protsessid:

1. Programm avab Chrome veebilehitseja.(lisaks veebilehitsejale avaneb ka Command Prompt)
2. Veebilehitseja navigeerib lehele https://ww.rik.ee/
3. Leiab lingi vastavalt lingi kirjeldusele.
4. klikib lingil
5. Ootab, et uus lehekülg jõuaks avaneda.
6. Otsib class elemendi seest "node-title" lehekülje pealkirja
7. Võrdleb lehekülje pealkirja vastavust lingikirjeldusega
8. Sulgeb veebibrauseri.
9. Kordab samme 1-8, kuni kõik testid on läbitud.
10. Kuvab testide tulemused Command Promptis.
11. Sulgeb Command Prompti.

Iga test on iseseisev. Iga testi alguses käivitatakse veebibrauser ja iga testi lõpus suletakse veebibrauser.
