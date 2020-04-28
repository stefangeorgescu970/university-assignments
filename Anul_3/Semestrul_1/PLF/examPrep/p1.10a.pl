isValley([H1, H2 | T], H) :-
    H1 > H2,
    H =:= 0,
    isValley([H2 | T], H).

isValley([H1, H2 | T], H) :-
    H1 < H2,
    H =:= 1,
    isValley([H2 | T], H).

isValley([H1, H2 | T], H):-
    H1 < H2,
    H =:= 0,
    isValley([H2 | T], 1).

isValley([_], H) :- H =:= 1.

