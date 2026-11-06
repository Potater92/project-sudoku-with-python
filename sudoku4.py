
import sys
from clingo.application import Application, clingo_main
from sudoku_board import Sudoku


class ClingoApp(Application):
    def main(self, control, files):
        control.load("sudoku.lp")

        for file in files:
            control.load(file)

        if not files:
            control.load("-")

        control.ground([("base", [])])
        control.solve()

    def print_model(self, model, printer):
        sudoku = Sudoku.from_model(model)
        print(sudoku)

if __name__ == "__main__":
    clingo_main(ClingoApp(), sys.argv[1:])