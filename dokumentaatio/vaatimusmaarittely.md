# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on [Bumtsibum](https://fi.wikipedia.org/wiki/Bumtsibum)-visailuohjelmaan perustuva peli, joka on suunnattu peruskoulun ja lukion musiikinopettajien käyttöön. Sovelluksessa opettaja voi luoda visailuja, joita voidaan sitten pelata oppilasryhmän kanssa. Oppilasryhmä jaetaan kahteen joukkueeseen ja opettaja toimii pelinjohtajana, joka tietää oikeat vastaukset ja jakaa pisteitä oman harkintansa mukaan.

Pelinäkymässä on viisi numeroitua luukkua, joiden jokaisen taakse on piilotettu jokin sana. Vuorossa oleva joukkue valitsee ensin avattavan luukun. Sitten joukkueen tehtävänä on keksiä mikä tahansa laulu, jossa luukusta paljastunut sana esiintyy. Arvaus tehdään laulamalla kyseistä laulua. Tässä onnistuessaan joukkue saa itselleen uuden arvausvuoron ja voi avata uuden luukun. Toisaalta jos joukkueen arvaama laulu on opettajan tarkoittama tehtävään piilotettu laulu, kierros päättyy ja joukkue saa pisteen.
  
Jos joukkue ei keksi mitään laulua, jossa luukusta paljastunut sana esiintyisi, vuoro siirtyy toiselle joukkueelle. Jokaiseen tehtävään on piilotettu myös kaksi punaisella pohjalla olevaa sanaa, ja tällaisen luukun avaaminen siirtää myös vuoron toiselle joukkueelle.

## Käyttäjät
Sovelluksessa on ainoastaan yksi käyttäjä, _normaali käyttäjä_. Jatkokehityksessä sovellukseen saatetaan lisätä tuki useammalle käyttäjälle, jotta eri käyttäjien luomat visailut voidaan pitää toisistaan erillään.

## Perusversion tarjoama toiminnallisuus

### Käyttöliittymä

Käyttöliittymässä on kolme päänäkymää:

- Aloitusnäkymä (**tehty**)
- Pelinäkymä (**tehty**)
- Luo uusi peli -näkymä (**tehty**)

Lisäksi käyttöliittymän toiminnallisuuteen kuuluu erilaisia pop up -ikkunoita sekä syötettä kysyviä ikkunoita.

### Sovelluksen käynnistäminen
Käynnistäessä avautuu aloitusnäkymä, jossa on:

- Listaus tallennetuista visailuista (**tehty**)
- Mahdollisuus valita haluamansa visailu ja aloittaa peli (**tehty**)
- Painikkeet visailujen luomiseen, muokkaamiseen ja poistamiseen (**tehty**)

### Uuden visailun luominen
Käyttäjä voi luoda uuden visailun, jossa on käyttäjän valitsema määrä arvoituksia. Käyttäjä valitsee jokaiseen arvoitukseen 5 luukkuihin piilotettavaa sanaa. Sanat tulee olla peräkkäisiä sanoja jonkun laulun sanoituksesta. Lisäksi arvoitukselle annetaan nimi, joka kuvaa arvoitukseen piilotettua kappaletta.

Teknisiä vaatimuksia visailun luomiselle:

- Käyttäjä antaa visailulle nimen (**tehty**)
- Käyttäjä voi liittää visailuun haluamansa määrän arvoituksia (**tehty**)
- Käyttäjä voi päättää arvaustehtävään piilotettavat sanat (**tehty**)
- Sovellus tarkistaa lopuksi, että mikään vaadituista kentistä ei ole tyhjänä (**tehty**)
- Visailu tallennetaan tietokantaan (**tehty**)

### Tallennettujen visailujen selaileminen
Käyttäjä voi katsoa järjestelmään tallennettujen visailujen tietoja. (**tehty**)

### Pelaaminen
- Käyttäjä voi käynnistää tallennetun visailun. (**tehty**)
- Sovellus näyttää tallennettuja tehtäviä yksi kerrallaan. (**tehty**)
- Käyttäjä voi klikata pelinäkymän luukkuja auki haluamassaan järjestyksessä. (**tehty**)
- Käyttäjä voi lisätä pisteitä joukkueille (**tehty**)
- Käyttäjä voi paljastaa oikean vastauksen. (**tehty**)
- Käyttäjä voi siirtyä seuraavaan arvoitukseen (**tehty**)

## Jatkokehitysideoita 
Perusversion toteutuksen jälkeen sovellukseen on mahdollista lisätä ajan salliessa esimerkiksi seuraavia ominaisuuksia:
- Visailuun voi liittää bonuskysymyksen, johon tehtävän ratkaissut joukkue saa yrittää vastata. Bonuskysymyksestä voi saada ylimääräisen pisteen
- Tuki useammalle käyttäjälle: Mahdollisuus tunnistautua käyttäjätunnuksella ja mahdollisesti salasanalla, jolloin eri käyttäjien luomat visailut voidaan pitää erillään toisistaan
- Pelin hallintapaneeli
  - Ideaalitilanteessa pelinäkymän painikkeet olisivat eriytettynä omaan ikkunaansa, "hallintapaneeliin". Hallintapaneelin ja pelinäkymän kokonaisuus olisi luenteeltaan samanlainen kuin Powerpoint-esityksen presentation view: opettaja voisi heijastaa pelinäkymän hdmi-portin kautta oppilaiden nähtäville ja hallintapaneeli olisi nähdävillä vain opettajan tietokoneelta. Näin pelinäkymästä tulisi siistimpi, koska mitään painikkeita ei tarvitsisi olla näkyvillä, ja lisäksi hallintapaneelissa voisi näyttää vain pelinjohtajalle kuuluvaa tietoa, kuten oikean vastauksen ja muita lisätietoja.
  - Hallintapaneeliin voisi toteuttaa painikkeet esimerkiksi:
    - luukkujen avaamiseen
    - pisteiden lisäämiseen ja vähentämiseen
    - sen ilmaisemiseen, oliko joukkeen antama vastaus oikein vai väärin
    - pelivuoron vaihtamiseen
    - pelin päättämiseen
