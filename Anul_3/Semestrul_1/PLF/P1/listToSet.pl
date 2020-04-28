% listToSet(L: list, REZ: list)
% listToSet(i, o).
% Turn a list into a set, items ordered by their last appearances

listToSet([],[]).
listToSet([H|T],REZ) :-
    myMember(H,T),
    listToSet(T,REZ).
listToSet([H|T],REZ) :-
    listToSet(T, REZ_T),
    myAppend([H], REZ_T, REZ).

