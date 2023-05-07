# Changelog

## Viikko 3

- Sovelluksen toteutuksen hahmoitteleminen aloitettu
- Käynnistettäessä pelinäkymän hahmotelma avautuu, mutta mitään aktiviteettia ei ole vielä toteutettu
- Sovelluksen rakennetta hahmoteltu
- Lisätty sovelluslogiikasta vastaava luokka GameService
- Testattu, että vuorossa olevaa joukkuetta vaihtava metodi toimii

## Viikko 4

- Toteutettu OpeningView-luokka, joka avautuu sovelluksen käynnistyessä
- Toteutettu CreateNewQuizView-luokan runko, jonka kautta voi luoda uuden visailun
- Perehdytty Tkinteriin ja toteutettu siirtymät näkymien välille painikkeiden avulla
- Hoidettu kuntoon projektin muita asioita kuten testaaminen, testiraportit ja pylint

## Viikko 5

- Aloitusnäkymään lisätty Listbox, joka listaa kaikki tietokannassa olevat visailut
- Pelinäkymän toiminnallisuutta on kehitetty niin, että laatikoita voi nyt avata, jolloin piilossa oleva sana paljastuu
- SQLite tietokanta otettu käyttöön
- Lisätty ManagementService-luokka, joka hoitaa pelinäkymän ulkopuolisia palveluita
- Päädytty luomaan erilliset luokat Quiz ja Puzzle, eli Puzzle on "arvoitus" ja Quiz on "visailu", visailuun voi liittyä monta arvoitusta

## Viikko 6
- Siirretty pelinäkymä kokonäytön tilaan
- Lisätty pelinäkymään punaisten sanojen toiminnallisuus: game_service arpoo jokaiseen visailuun kaksi punaista sanaa
- Luotu visailujenluomisnäkymään käyttöliittymä oman visailun tekemiseen (Logiikka puuttuu)
- Lisätty pelinäkymään joukkueen 1 pistelaskuri

## Viikko 7 
- Lisätty pelinäkymään joukkueen 2 pistelaskuri
- Lisätty pelinäkymään oikean vastauksen paljastamistoiminto
- Muutettu visailunluomisnäkymää niin, että uuden arvoituksen tiedot annetaan erillisessä ikkunassa
