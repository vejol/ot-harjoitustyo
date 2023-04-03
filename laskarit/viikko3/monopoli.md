```mermaid
---
title: Monopoli
---
classDiagram
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Pelaaja "2-8" -- "1" Monopolipeli
    Pelinappula "*" -- "1" Ruutu
    Pelaaja "1" -- "1" Pelinappula
    Monopolipeli "1" -- "2" Noppa
    
    class Ruutu{
        -seuraava_ruutu
    }
```