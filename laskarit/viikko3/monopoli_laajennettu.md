```mermaid
---
title: Monopoli
---
classDiagram
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Pelaaja "2..8" -- "1" Monopolipeli
    Pelinappula "0..8" -- "1" Ruutu
    Pelaaja "1" -- "1" Pelinappula
    Monopolipeli "1" -- "2" Noppa
    
    Aloitusruutu --|> Ruutu
    Vankila --|> Ruutu
    Korttiruutu --|> Ruutu
    Sattuma --|> Korttiruutu
    Yhteismaa --|> Korttiruutu
    Asema --|> Ruutu
    Laitos --|> Ruutu
    Katu --|> Ruutu

    Sattumakortti "*" -- "2" Sattuma

    Sattumakortti: +toiminto

    Yhteismaakortti "*" -- "2" Yhteismaa

    Yhteismaakortti: +toiminto

    Monopolipeli: +Aloitusruutu
    Monopolipeli: +Vankila

    Katu: +omistaja
    Katu: +talot
    Katu: +hotellit

    Ruutu: +seuraava_ruutu

    Pelaaja: +rahat
```