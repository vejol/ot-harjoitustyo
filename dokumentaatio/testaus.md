# Testausdokumentti

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikkaa on testattu kolmessa osassa TestEditService-, TestGameService- ja TestManagementService-testiluokilla. Testauksessa on käytetty oikean SQLite-repositorion sijaan yksinkertaista FakeRepository-luokkaa, joka pitää kirjaa tallennetuista tiedoista listarakenteen avulla muistissa.

- EditService-luokan testaus:
  - Testiluokka TestEditService testaa EditService-luokkaa sekä tilanteessa jossa käyttäjä haluaa luoda uuden visailun, että tilanteessa, jossa käyttäjä haluaa muokata olemassa olevaa visailua. 
  - Luokan atribuutti self.edit_service1 kuvaa luokan ilmentymää, jossa lähtötilanteena on tyhjä visailu eli uuden visailun luominen. Luokan atribuutti self.edit_service2 kuvaa tilannetta, jossa lähtökohtana on olemassa oleva visailu eli visailun muokkaaminen.

- GameService-luokan testaus:
  - Tämän luokan testiluokka TestGameService alustaa GameService-olion, jolle injektoidaan riippuvuudeksi kaksi arvoitusta sisältävä Quiz-olio testejä varten

- ManagementService-luokan testaus:
  - ManagementService-olio alustetaan injektoimalla sille riippuvuudeksi FakeRepository-olio
  - Lisäksi alustuksessa luodaan kaksi testivisailua, joita eri testit käyttävät hyväkseen

### Repositorio-luokka

Ohjelman QuizRepository-luokalle on käytössä omat, testejä varten luotavat tiedostot. Testit eivät siis käytä muun ohjelman käytössä olevaa SQLite-tietokantaa, vaan testien käyttämät tiedostojen nimet haetaan .env.test-tiedostosta. Jokaisen testin lähtötilanteessa testitietokanta on tyhjä. Lisäksi testien alustustoimenpiteenä luodaan kaksi Quiz-oliota testien käytettäväksi.

### Testauskattavuus

Sovelluksen testauskattavuus on 93%. Käyttöliittymän testaaminen on suoritettu manuaalisesti, eikä se sisälly tähän testauskattavuuteen.

Testikattavuuden ulkopuolelle jäi testattavista tiedostoista vain yksittäisiä rivejä, kuten _build.py-_ ja _initialize_database.py_-tiedostojen komentoriviltä suorittaminen.

## Järjestelmätestaus

### Asennus ja konfigurointi

Sovellusta on testattu manuaalisesti monipuolisesti eri järjestelmissä. Sovellusta on kokeiltu sekä Linux- että Windows-ympäristössä. Testaus on sisältänyt [käyttöohjeen](./dokumentaatio/kayttoohje.md) kuvaaman tavan ottaa sovellus käyttöön, tilanteet, jossa sovellukseen ei ole vielä tallennettuna visailuja sekä tilanteet, jossa olemassa olevia visailuja jo on. Lisäksi on testattu sovelluksen konfigurointia parametrein .env-tiedostosta käsin.

### Toiminnallisuudet

Testauksessa on yritetty antaa ei-toivottuja syötteitä ja navigoida käyttöliittymässä epätarkoituksenmukaisella tavalla. Manuaalinen testaus kattaa kaikki [määrittelydokumentissa](./dokumentaatio/vaatimusmaarittely.md) kuvatut ominaisuudet.

## Sovellukseen jääneet laatuongelmat
- Käyttöliittymän visuaalisessa ilmeessä on epäjohdonmukaisuutta Linux- ja Windows-ympäristöjen välillä
- Sovellus ei anna käyttäjäystävällistä virheilmoitusta, jos SQLite-tietokantaa ei ole alustettu käyttöohjeen mukaan