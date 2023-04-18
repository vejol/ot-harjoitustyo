# Bumtsibum-sovellus

Sovellus on Bumtsibum-visailuohjelmaan perustuva peli, joka on suunnattu peruskoulun ja lukion musiikinopettajien käyttöön. Sovelluksessa opettaja voi luoda visailuja, joita voidaan sitten pelata oppilasryhmän kanssa. Oppilasryhmä jaetaan kahteen joukkueeseen ja opettaja toimii pelinjohtajana, joka tietää oikeat vastaukset ja jakaa pisteitä oman harkintansa mukaan.

Pelinäkymässä on viisi numeroitua luukkua, joiden jokaisen taakse on piilotettu jokin sana. Vuorossa oleva joukkue valitsee ensin avattavan luukun. Sitten joukkueen tehtävänä on keksiä mikä tahansa laulu, jossa luukusta paljastunut sana esiintyy. Arvaus tehdään laulamalla kyseistä laulua. Tässä onnistuessaan joukkue saa itselleen uuden arvausvuoron ja voi avata uuden luukun. Toisaalta jos joukkueen arvaama laulu on opettajan tarkoittama tehtävään piilotettu laulu, kierros päättyy ja joukkue saa pisteen.

Jos joukkue ei keksi mitään laulua, jossa luukusta paljastunut sana esiintyisi, vuoro siirtyy toiselle joukkueelle. Jokaiseen tehtävään on piilotettu myös kaksi punaisella pohjalla olevaa sanaa, ja tällaisen luukun avaaminen siirtää myös vuoron toiselle joukkueelle.

## Python-versio

Sovellus on suunniteltu Python-versiolla `3.8`. Vanhempien python-versioiden kanssa toimintaa ei voida taata.

## Dokumentaatio
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](./dokumentaatio/tyoaikakirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Tarvittavat riippuvuudet ennen suorittamista tulee asentaa komennolla:

```bash
poetry install
```

2. Sovellus käynnistetään komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelma suoritetaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Automaattiset testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Html-muotoinen testikattavuusraportti luodaan komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Tiedostossa .pylintrc määritellyt koodin laatutarkistukset suoritetaan komennolla:

```bash
poetry run invoke lint
```