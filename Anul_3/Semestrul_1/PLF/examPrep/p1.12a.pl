replace([], _, _, []).
replace([H|T], E, RL, R) :-
    H =:= E,
    replace(T, E, RL, RT),
    myAppend(RL, RT, R).

replace([H|T], E, RL, R) :-
    H =\= E,
    replace(T, E, RL, RT),
    R = [H | RT].

