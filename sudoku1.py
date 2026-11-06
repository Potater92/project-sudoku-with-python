
import sys
from clingo.application import Application, clingo_main


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
        atoms = model.symbols(shown=True)
        sorted_atoms = sorted(str(atom) for atom in atoms)
        print(" ".join(sorted_atoms))

if __name__ == "__main__":
    clingo_main(ClingoApp(), sys.argv[1:])