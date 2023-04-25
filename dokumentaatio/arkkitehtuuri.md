# Arkkitehtuurikuvaus

## Ohjelman rakenne

Tässä on esitelty sovelluksen tuleva pakkausrakenne ja keskeisimmät luokat:

![Pakkaus- ja luokkarakenne](./kuvat/arkkitehtuuri-pakkaus-luokat.png)

## Keskeisiä toiminnallisuuksia

### Sekvenssikaavio Aloita peli -napin painamisesta

Tämä sekvenssikaavio kuvaa sitä, kun käyttäjä painaa Aloita peli -painiketta. Ensin ohjelma selvittää, minkä visailun käyttäjä on valinnut listalta. Sitten se hakee tietokannasta visailun tiedot, jotka tietokanta palauttaa Quiz-oliona. Tämän jälkeen ohjelma luo GameService-palvelun, joka tarvitsee Quiz-olion parametrikseen. Lopulta voidaan siirtyä GameView-näkymään ja peli alkaa.

```mermaid
sequenceDiagram

actor User
User->>+OpeningView: click "Aloita peli" button
OpeningView->>+ManagementService: find_quiz(selection)
ManagementService->>+QuizRepository: find_quiz(selection)
QuizRepository-->>-ManagementService: Quiz
ManagementService-->>-OpeningView: Quiz
OpeningView->>-UI: _show_game_view(Quiz)
activate UI
UI->>game_service: GameService(Quiz)
UI->>-game_view: GameView(game_service)

```