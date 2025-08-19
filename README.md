# Game of Life
---
Jednoduchá simulácia dvojrozmerného bunkového automatu **Conway's Game of Life** (John H. Conway, 1970), ktorý v štvorčekovej mriežke prostedníctvom daných pravidiel simuluje vývoj spoločenstva buniek.

## Dokumentácia
---
### Pravidlá simulácie
**1.** Každá živá bunka s menej ako dvoma živými susedmi zomrie (underpopulation).

**2.** Každá živá bunka s dvoma alebo troma živými susedmi zostáva v ďalšom kroku živá (survival/prežitie).

**3.** Každá živá bunka s viac ako troma živými susedmi zomrie (overpopulation).

**4.** Každá mŕtva bunka s práve troma susedmi v ďalšom kroku ožije (reproduction/rozmnoženie).

### Spustenie
Pred spustením  simulácie je potrebné mať nainštalovaný **Python**. V adresári projektu treba spustiť: ``` pip install -r requirements.txt``` 

Program spustíte príkazom: ``` python game_of_life/main.py```

### Rozhranie

#### Mriežka
Mriežka, na ktorej prebieha simulácia Game of Life sa skladá zo štvorcových buniek, ktoré môžu nadobúdať dva stavy:
- živé/aktívne
- mŕtve/neaktívne

Počas spustenej simulácie sa stav buniek mení podľa pravidiel uvedených vyššie. Pomocou kolieska myši sa dá prizoomovať na ľubovoľnú časť mriežky a takisto odzoomovať.

#### Ovládanie
| Akcia              | Popis                                        |
| ------------------ | ------------------------------               |
| ľavé tlačidlo myši | oživí/zahubí bunku v mriežke                 |
| koliesko myši      | prizoomovanie/odzoomovanie                   |
| medzera            | zapauzovanie simulácie                       |
| D alebo Backspace  | vymazanie všetkých aktuálne živých buniek    |
| R                  | náhodne v mriežke vygeneruje žijúce bunky    |
| šípky hore/dole    | zrýchľujú/spomaľujú simuláciu                |
| Esc                | zavrie okno so simuláciou                    |
