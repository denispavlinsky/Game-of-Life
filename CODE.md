# Technický popis
---
Kód je štruktúrovaný ako jeden hlavný súbor main.py, ktorý obsahuje celú logiku simulácie Game of Life.
Funkcie a premenné som sa snažil pomenovávať čo najprehľadnjšie, aby z ich názvov bolo jasné, čo robia a pomenúvajú.
Nepoužívajú sa žiadne triedy.

## Prehľad častí kódu
---

```
main.py
```

Je to hlavný a jediný spustiteľný súbor aplikácie. Obsahuje:

- inicializáciu Pygame a potrebných premenných
- definíciu logiky simulácie Game of Life
- obsluhu vstupov z myši a klávesnice (podrobnejšie popísané v **README.md**)
- nakreslenie mriežky a buniek
- samotnú simuláciu vývoja generácií buniek (podrobnejšie v **README.md**)

## Kľúčové funkcie
---
### make_grid
Zaisťuje vykreslenie všetkých aktívnych/žijúcich buniek a celej mriežky na obrazovku.

### edit_grid
Zmení stav mriežky podľa pravidiel Game of Life.

### give_neighbors
Vracia zoznam susedných buniek pre danú bunku (posudzuje všetkých 8 smerov).

### clamp_offset
Zamedzuje posunu zobrazenia okna mimo hranice mriežky (udržiava zobrazenie v rámci vykreslenej mriežky) pri scrollovaní a zoomovaní.

### rand
Vygeneruje náhodné aktívne bunky v mriežke.

### main()
Hlavná slučka programu – vykonáva simuláciu, spracúva vstupy, aktualizuje obrazovku.

## Interaktívne prvky
---
Uživateľská interakcia je riadená pomocou prostriedkov Pygame.

Funguje ovládanie simulácie myšou a klávesnicou (pauza, rýchlosť, náhodné bunky, atď.). Ovládanie je podrobnejšie vysvetlené v dokumente **README.md**

## Externé knižnice
---
Jediná použitá externá knižnica je **Pygame**, ktorá je špecifikovaná v **requirements.txt**. Slúži na vykresľovanie obsahu a obsluhu vstupov.
