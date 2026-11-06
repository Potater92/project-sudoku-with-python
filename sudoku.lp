
% Sudoku Solver

% each cell gets exactly one number (1..9)
{ sudoku(X, Y, N) : N = 1..9 } = 1 :- X = 1..9, Y = 1..9.

% initial numbers are part of the answer
sudoku(X, Y, N) :- initial(X, Y, N).

% no repeated numbers in a row
:- sudoku(X, Y1, N), sudoku(X, Y2, N), Y1 != Y2.

% no repeated numbers in a column
:- sudoku(X1, Y, N), sudoku(X2, Y, N), X1 != X2.

% determine which 3x3 subgrid a cell belongs to
subgrid(X, Y, G) :-
    X = 1..9,
    Y = 1..9,
    G = 1 + (((X-1)/3)*3 + (Y-1)/3).

% no repeated numbers in a subgrid
:- sudoku(X1, Y1, N),
   sudoku(X2, Y2, N),
   subgrid(X1, Y1, G),
   subgrid(X2, Y2, G),
   X1 != X2,
   Y1 != Y2.

#show sudoku/3.
