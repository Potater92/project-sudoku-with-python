from typing import Tuple
import clingo


class Sudoku:
    def __init__(self, sudoku: dict[Tuple[int, int], int]):
        self.sudoku = sudoku

    
    def __str__(self) -> str:
        s = ""
        for row in range(1, 10):
            for col in range(1, 10):
                value = self.sudoku.get((row, col), "-")
                s += str(value)

                if col < 9:
                    if col == 3 or col == 6:
                        s += "  "
                    else:
                        s += " "

            if row < 9:
                s += "\n"

                if row == 3 or row == 6:
                    s += "\n"

        return s


    @classmethod
    def from_str(cls, s: str) -> "Sudoku":
        sudoku = {}
        # YOUR CODE HERE
        return cls(sudoku)

    
    @classmethod
    def from_model(cls, model: clingo.solving.Model) -> "Sudoku":
        sudoku = {}

        for atom in model.symbols(shown=True):
            if atom.name == "sudoku" and len(atom.arguments) == 3:
                row = atom.arguments[0].number
                col = atom.arguments[1].number
                value = atom.arguments[2].number

                sudoku[(row, col)] = value

        return cls(sudoku)

