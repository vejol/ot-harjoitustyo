# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on [Bumtsibum](https://fi.wikipedia.org/wiki/Bumtsibum)-visailuohjelmaan perustuva peli, joka on suunnattu peruskoulun ja lukion musiikinopettajien käyttöön. Sovelluksessa opettaja voi luoda visailuja, joita voidaan sitten pelata oppilasryhmän kanssa. Oppilasryhmä jaetaan kahteen joukkueeseen ja opettaja toimii pelinjohtajana, joka tietää oikeat vastaukset ja jakaa pisteitä oman harkintansa mukaan.

Pelinäkymässä on viisi numeroitua luukkua, joiden jokaisen taakse on piilotettu jokin sana. Vuorossa oleva joukkue valitsee ensin avattavan luukun. Sitten joukkueen tehtävänä on keksiä mikä tahansa laulu, jossa luukusta paljastunut sana esiintyy. Arvaus tehdään laulamalla kyseistä laulua. Tässä onnistuessaan joukkue saa itselleen uuden arvausvuoron ja voi avata uuden luukun. Toisaalta jos joukkueen arvaama laulu on opettajan tarkoittama tehtävään piilotettu laulu, kierros päättyy ja joukkue saa pisteen.
  
Jos joukkue ei keksi mitään laulua, jossa luukusta paljastunut sana esiintyisi, vuoro siirtyy toiselle joukkueelle. Jokaiseen tehtävään on piilotettu myös kaksi punaisella pohjalla olevaa sanaa, ja tällaisen luukun avaaminen siirtää myös vuoron toiselle joukkueelle.

## Käyttäjät
Aluksi sovelluksessa on ainoastaan yksi käyttäjä, _normaali käyttäjä_. Myöhemmin sovellukseen saatetaan lisätä tuki useammalle käyttäjälle, jotta eri käyttäjien luomat visailut voidaan pitää toisistaan erillään.

## Perusversion tarjoama toiminnallisuus

### Käyttöliittymä

Käyttöliittymässä on kolme näkymää:

- Aloitusnäkymä (**tehty osittain**)
- Pelinäkymä (**tehty osittain**)
- Luo uusi peli -näkymä (**tehty osittain**)

### Uuden visailun luominen
Käyttäjä voi luoda uuden visailun, jossa on käyttäjän valitsema määrä arvaustehtäviä. Käyttäjä valitsee jokaiseen tehtävään 5 luukkuihin piilotettavaa sanaa. Sanat tulee olla peräkkäisiä sanoja jonkun laulun sanoituksesta. Lisäksi tehtävän yhteyteen voi liittää muita lisätietoja, kuten kappaleen nimen, esittäjän tai julkaisuvuoden. Näitä tietoja ei kuitenkaan näytetä visailun aikana, vaan ne ovat ainoastaan käyttäjän omaan käyttöön.

Teknisiä vaatimuksia visailun luomiselle:

- Käyttäjä antaa visailulle nimen
- Käyttäjä voi liittää visailuun haluamansa määrän arvaustehtäviä
- Käyttäjä voi päättää arvaustehtävään piilotettavat sanat
- Sovellus tarkistaa lopuksi, että mikään vaadituista kentistä ei ole tyhjänä
- Visailu tallennetaan tietokantaan

### Tallennettujen visailujen selaileminen
Käyttäjä voi katsoa järjestelmään tallennettujen visailujen tietoja.

### Pelaaminen
- Käyttäjä voi käynnistää sovellukseen tallennetun visailun.
- Sovellus näyttää tallennettuja tehtäviä yksi kerrallaan.
- Käyttäjä voi klikata pelinäkymän luukkuja auki haluamassaan järjestyksessä.

## Jatkokehitysideoita 
Perusversion toteutuksen jälkeen sovellukseen on mahdollista lisätä ajan salliessa esimerkiksi seuraavia ominaisuuksia:
- Käyttäjä voi muokata aiemmin tallennettuja visailuja
- Visailuun voi liittää bonuskysymyksen, johon tehtävän ratkaissut joukkue saa yrittää vastata. Bonuskysymyksestä voi saada ylimääräisen pisteen

### Pelin hallintapaneeli
Sovellukseen voi toteuttaa pelinjohtajalle pelin ohjaamiseen tarvittavia painikkeita:
- pisteiden lisäämiseen ja vähentämiseen
- sen ilmaisemiseen, oliko joukkeen antama vastaus oikein vai väärin
- vuoron vaihtamiseen
- pelin päättämiseen
