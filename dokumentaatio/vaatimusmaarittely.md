# Vaatimusmäärittely

## Sovelluksen tarkoitus
Sovellus on [Bumtibum](https://fi.wikipedia.org/wiki/Bumtsibum)-visailuohjelmaan perustuva peli, joka on suunnattu peruskoulun ja lukion musiikinopettajien käyttöön. Sovelluksessa opettaja voi luoda visailuja, joita voidaan sitten pelata oppilasryhmän kanssa. 

Oppilasryhmä jaetaan kahteen joukkueeseen. Pelinäkymässä on viisi numeroitua luukkua, joiden jokaisen taakse on piilotettu jokin sana. Vuorossa oleva joukkue valitsee ensin avattavan luukun. Sitten joukkueen tehtävänä on keksiä mikä tahansa laulu, jossa juuri luukusta paljastunut sana esiintyy. Arvaus tehdään laulamalla kyseistä laulua. Tässä onnistuessaan joukkue saa itselleen uuden vuoron ja voi avata uuden luukun. Jos joukkueen arvaama laulu on opettajan tarkoittama tehtävään piilotettu laulu, kierros päättyy ja joukkue saa pisteen.
  
Jos joukkue ei keksi mitään laulua, jossa luukusta paljastunut sana esiintyisi, vuoro siirtyy toiselle joukkueelle. Jokaiseen tehtävään on piilotettu myös kaksi punaisella pohjalla olevaa sanaa, ja tällaisen luukun avaaminen siirtää myös vuoron toiselle joukkueelle.

## Käyttäjät
Aluksi sovelluksessa on ainoastaan yksi käyttäjä, _pääkäyttäjä_. Myöhemmin sovellukseen saatetaan lisätä tuki useammalle käyttäjälle, jotta eri käyttäjien luomat visailut voidaan pitää toisistaan erillään.

## Perusversion tarjoama toiminnallisuus

### Uuden visailun luominen
Käyttäjä voi luoda uuden visailun, jossa on mielivaltainen määrä arvaustehtäviä. Käyttäjä valitsee 5 luukkuihin piilotettavaa sanaa. Lisäksi tehtävän yhteyteen voi liittää muita lisätietoja, kuten kappaleen nimen, esittäjän tai julkaisuvuoden. Näitä tietoja ei kuitenkaan näytetä visailun aikana, vaan ne ovat ainoastaan käyttäjän omaan käyttöön.

### Tallennettujen visailujen selaileminen
Käyttäjä voi katsoa järjestelmään tallennettujen visailujen tietoja.

### Pelaaminen
- Käyttäjä voi käynnistää sovellukseen tallennetun visailun.
- Sovellus näyttää tallennettuja tehtäviä yksi kerrallaan.
- Käyttäjä voi klikata pelinäkymän luukkuja auki haluamassaan järjestyksessä.
- Sovellus pitää kirjaa, kumman joukkueen vuoro on milloinkin

## Jatkokehitysideoita 
Perusversion toteutuksen jälkeen sovellukseen on mahdollista lisätä ajan salliessa esimerkiksi seuraavia ominaisuuksia:
- Käyttäjä voi muokata aiemmin tallennettuja visailuja
