#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.num_mines = mines
        # On ne place plus les mines ici pour permettre la sécurité au 1er clic
        self.mines = set()
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flags = set()
        self.game_over = False
        self.first_move = True

    def generate_mines(self, start_x, start_y):
        # Génère les mines en évitant la case du premier clic
        possible_positions = [i for i in range(self.width * self.height) if i != (start_y * self.width + start_x)]
        self.mines = set(random.sample(possible_positions, self.num_mines))

    def print_board(self, reveal_all=False):
        clear_screen()
        # En-tête des colonnes
        print('    ' + ' '.join(f"{i:2}" for i in range(self.width)))
        print('    ' + '---' * self.width)
        
        for y in range(self.height):
            print(f"{y:2} |", end=' ')
            for x in range(self.width):
                pos = y * self.width + x
                if reveal_all and pos in self.mines:
                    print('* ', end=' ')
                elif (x, y) in self.flags:
                    print('F ', end=' ')
                elif self.revealed[y][x]:
                    count = self.count_mines_nearby(x, y)
                    print(f"{count if count > 0 else ' '} ", end=' ')
                else:
                    print('. ', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if self.first_move:
            self.generate_mines(x, y)
            self.first_move = False

        if (y * self.width + x) in self.mines:
            return False
        
        if self.revealed[y][x]:
            return True

        self.revealed[y][x] = True
        
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def check_win(self):
        revealed_count = sum(row.count(True) for row in self.revealed)
        return revealed_count == (self.width * self.height - self.num_mines)

    def play(self):
        while True:
            self.print_board()
            try:
                choice = input("Action (R x y pour Révéler, F x y pour Drapeau): ").split()
                if not choice: continue
                
                action = choice[0].upper()
                x, y = int(choice[1]), int(choice[2])

                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Hors limites !")
                    continue

                if action == 'F':
                    if (x, y) in self.flags: self.flags.remove((x, y))
                    else: self.flags.add((x, y))
                elif action == 'R':
                    if (x, y) in self.flags:
                        print("Il y a un drapeau ici !")
                        continue
                    if not self.reveal(x, y):
                        self.print_board(reveal_all=True)
                        print("BOOM ! Game Over.")
                        break
                    if self.check_win():
                        self.print_board(reveal_all=True)
                        print("Félicitations ! Tu as gagné !")
                        break
            except (ValueError, IndexError):
                print("Entrée invalide. Format: R x y ou F x y")

if __name__ == "__main__":
    game = Minesweeper(10, 10, 10)
    game.play()