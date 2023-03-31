```mermaid
---
title: Monopoli
---
classDiagram
    
    Pelilauta "1" -- "40" Ruutu
    Pelaaja "1" -- "1" Pelinappula
    Pelaaja "2-8" -- "1" Pelilauta
    Pelinappula "*" -- "1" Ruutu
    Pelilauta "1" -- "2" Noppa
    class Ruutu{
        -seuraava_ruutu
    }
```