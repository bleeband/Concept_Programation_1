class Board:
    def __init__(self):
        self.valeur_nulle = " . "
        self.grid = [
            [self.valeur_nulle for _ in range(3)]
            for _ in range(3)
        ]

    def display(self):
        for row in self.grid:
            for cell in row:
                print(cell, end="")
            print()

    def position_to_index(self, position):
        row = (position - 1) // 3
        col = (position - 1) % 3
        return row, col

    def is_empty(self, row, col):
        return self.grid[row][col] == self.valeur_nulle

    def place_symbol(self, position, symbol):
        row, col = self.position_to_index(position)
        if self.is_empty(row, col):
            self.grid[row][col] = symbol
            return True
        return False

    def check_win(self):
        # lignes
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != self.valeur_nulle:
                return True

        # colonnes
        for j in range(3):
            if self.grid[0][j] == self.grid[1][j] == self.grid[2][j] != self.valeur_nulle:
                return True

        # diagonales
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != self.valeur_nulle:
            return True

        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != self.valeur_nulle:
            return True

        return False

    def check_draw(self):
        for row in self.grid:
            for cell in row:
                if cell == self.valeur_nulle:
                    return False
        return True

    def reset(self):
        self.grid = [
            [self.valeur_nulle for _ in range(3)]
            for _ in range(3)
        ]
