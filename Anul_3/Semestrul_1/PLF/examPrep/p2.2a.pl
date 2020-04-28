insert([], E, [E]).
insert([H|T], E, R) :-
    H < E,
    insert(T, E, RT),
    R = [H | RT].
insert(L, E, R) :-
    R=[E | L].

mySort([], []).
mySort([H | T], R) :-
    mySort(T, RT),
    insert(RT, H, R).
