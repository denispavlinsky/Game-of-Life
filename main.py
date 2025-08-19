import pygame
import random

# inicializácia Pygame
pygame.init()

# definovanie farieb: (red, green, blue)
col_background = (33, 33, 33)
col_lines = (211, 211, 211)
col_squares = (0, 194, 199)

# rozmery vykresľovanej mriežky (v pixeloch)
width = 1350
height = 680

# rozmery vykresľovanej mriežky (v počte jednotlivých buniek / štvorčekov)
square_size = 5
grid_width = width // square_size
grid_height = height // square_size

# limitné veľkosti buniek
max_square_size = 100
min_square_size = 5
fps = 60

# inicializácia obrazovky a počítadla času
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

# posuny pre zoomovanie mriežky
offset_x, offset_y = 0, 0

# generuje množinu náhodných buniek v mriežke
def rand(number):
    list_rand = []
    for _ in range(number):
        rand_1 = random.randrange(0, grid_width)  # horizontálna súradnica bunky
        rand_2 = random.randrange(0, grid_height)  # vertikálna súradnica bunky
        list_rand.append((rand_1, rand_2))
    return set(list_rand)

# vykresľuje mriežku a žijúce bunky
def make_grid(positions, square_size, offset_x, offset_y):
    for col, row in positions:
        x = col * square_size + offset_x
        y = row * square_size + offset_y
        if 0 <= x + square_size and x < width and 0 <= y + square_size and y < height:
            pygame.draw.rect(screen, col_squares, (x, y, square_size, square_size))

    # vykresľuje horizontálne čiary mriežky
    for row in range(grid_height + 1):
        y = row * square_size + offset_y
        if 0 <= y < height:
            pygame.draw.line(screen, col_lines, (0, y), (width, y), 1)

    #  vykresľuje vertikálne čiary mriežky
    for col in range(grid_width + 1):
        x = col * square_size + offset_x
        if 0 <= x < width:
            pygame.draw.line(screen, col_lines, (x, 0), (x, height), 1)

# obmedzuje scrollovanie mriežky tak, aby nebolo možné zobraziť prázdnu oblasť mimo mriežky
def clamp_offset(offset_x, offset_y, square_size):

    # rozmery mriežky v pixeloch (po zoomovaní)
    grid_pixel_width = grid_width * square_size
    grid_pixel_height = grid_height * square_size

    # minimálne posunutie (o koľko sa ešte dá posunúť hore/doľava)
    min_offset_x = min(0, width - grid_pixel_width)
    min_offset_y = min(0, height - grid_pixel_height)

    # zúženie možného posunu na vyhovujúci rozsah
    offset_x = min(max(offset_x, min_offset_x), 0)
    offset_y = min(max(offset_y, min_offset_y), 0)

    return offset_x, offset_y

# určuje novú generáciu buniek podľa pravidiel života hry
def edit_grid(coords):
    all_neighs = set()
    new_coords = set()
    for pos in coords:
        neighbors = give_neighbors(pos)
        all_neighs.update(neighbors)
        neighbors = [x for x in neighbors if x in coords]  # filtruje živých susedov bunky

        if len(neighbors) == 2 or len(neighbors) == 3:
            new_coords.add(pos)  # bunka prežíva

    for pos in all_neighs:
        neighbors = give_neighbors(pos)
        neighbors = [x for x in neighbors if x in coords]

        if len(neighbors) == 3:
            new_coords.add(pos)  # narodenie novej bunky

    return new_coords

# vracia susedov danej bunky (horizontálne, vertikálne aj diagonálne)
def give_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # ak je to tá istá bunka
            if 0 <= x + dx < grid_width and 0 <= y + dy < grid_height:
                    neighbors.append((x + dx, y + dy))  # ak je v rozsahu mriežky

    return neighbors

# hlavná časť
def main():
    global square_size, offset_x, offset_y
    coords = set()  # žijúce bunky
    running = True  # označuje, či je okno hry otvorené
    playing = False  # označuje, či simulácia beží (nie je zapauzovaná)
    count = 0
    update_freq = 15  # frekvencia obnovy generácie

    # kým sa nezavrie okno hry
    while running:
        clock.tick(fps)

        if playing:
            count += 1
        
        if count >= update_freq:
            count = 0
            coords = edit_grid(coords) # obnovenie generácie

        # titulok okna hry
        pygame.display.set_caption("Prebieha" if playing else "Pauza")

        # reakcie na kliknutia
        for event in pygame.event.get():
            
            # zavretie okna hry
            if event.type == pygame.QUIT:
                running = False
            
            # kliknutie myšou na živú bunku ju zruší
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                grid_x = (mouse_x - offset_x) // square_size
                grid_y = (mouse_y - offset_y) // square_size
                pos = (grid_x, grid_y)

                if pos in coords:
                    coords.remove(pos)
                else:
                    coords.add(pos)

            # zoomovanie v mriežke pomocou kolieska myši
            if event.type == pygame.MOUSEWHEEL:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # pozícia pred zoomovaním/odzoomovaním
                grid_x_before = (mouse_x - offset_x) / square_size
                grid_y_before = (mouse_y - offset_y) / square_size

                new_size = square_size + event.y * 5
                new_size = max(min_square_size, min(max_square_size, new_size))

                if new_size != square_size:
                    if new_size != min_square_size:
                        square_size = new_size

                        # opravenie posunu - zachovanie pozície kurzora
                        offset_x = mouse_x - round(grid_x_before * square_size)
                        offset_y = mouse_y - round(grid_y_before * square_size)

                        offset_x, offset_y = clamp_offset(offset_x, offset_y, square_size)
                    else:
                        square_size = new_size
                        offset_x, offset_y = clamp_offset(offset_x, offset_y, square_size)

            # ovládanie tlačidlami klávesnice
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing  # spustenie/zapauzovanie simulácie (medzerou) 

                if event.key == pygame.K_d or event.key == pygame.K_BACKSPACE:
                    coords = set()  # vymaže všetky živé bunky (backspaceom)

                if event.key == pygame.K_r:
                    coords = rand(random.randint(20, 40) * grid_width)  # oživí náhodné bunky v mriežke (r)

                if event.key == pygame.K_ESCAPE:
                    running = False  # uzavrie okno hry (escapeom)

                if event.key == pygame.K_UP:
                    update_freq -= 5
                    if update_freq <= 0:
                        update_freq = 5  # zníži frekvenciu obnovovania generácie - zrýchli simuláciu (šípkou hore)


                if event.key == pygame.K_DOWN:
                    update_freq += 5  # zväčší frekvenciu obnovovania generácie - spomalí simuláciu (šípkou dole)

        # vykreslenie mriežky a obsahu
        screen.fill(col_background)
        make_grid(coords, square_size, offset_x, offset_y)
        pygame.display.update()

    pygame.quit()

# spustenie hlavnej funkcie
if __name__ == "__main__":
    main()