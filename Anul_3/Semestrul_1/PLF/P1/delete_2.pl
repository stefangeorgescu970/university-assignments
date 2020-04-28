% delete2(E: element, L: List, R: List)
% delete2(i,i,o).
% Delete element from list

delete2(_, [], []).
delete2(E, [H|T], R):-
    H =:= E,
    R=T.
delete2(E, [H|T],R):-
    H=\=E,
    delete2(E, T, RT),
    R = [H | RT].

