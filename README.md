# Game of Life

Jednoduchá simulace buněčného automatu **Conway's Game of Life** vytvořená v Pythonu jako součást semestrálního projektu z programování.

---

## 📝 Dokumentace (v češtině)

### 🟢 Spuštění
Před spuštěním je třeba mít nainstalovaný **Python**.  
V adresáři projektu spusťte:

```bash
pip install -r requirements.txt
Program spustíte příkazem:

bash
Kopírovať
Upraviť
python main.py
🖥️ Rozhraní
🧭 Ovládání
Akce	Popis
Levé tlačítko myši	Aktivuje nebo deaktivuje buňku v mřížce.
Kolečko myši (zoom)	Přibližuje nebo oddaluje mřížku pod kurzorem.
Mezerník	Spustí nebo pozastaví simulaci.
R	Náhodně vygeneruje buňky.
D nebo Backspace	Vymaže všechny buňky.
Šipky nahoru/dolů	Zrychlují nebo zpomalují simulaci.
Esc	Zavře aplikaci.

📐 Mřížka
Mřížka se skládá z čtvercových buněk, které mohou být:

živé (aktivní)

mrtvé (neaktivní)

Během spuštěné simulace se buňky mění podle pravidel Game of Life.
Pomocí zoomování a posunu se lze pohybovat po větší mřížce.

⚙️ Pravidla simulace
Simulace běží podle klasických pravidel Game of Life:

Živá buňka přežije, pokud má 2 nebo 3 živé sousedy.

Mrtvá buňka ožije, pokud má přesně 3 živé sousedy.

Ve všech ostatních případech buňka zanikne nebo zůstane mrtvá.