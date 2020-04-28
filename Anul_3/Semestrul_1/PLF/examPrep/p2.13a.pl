remCons([], _, []).

remCons([H1, H2|T], _, R) :-
    H1C is H2 - 1,
    H1 =:= H1C,
    remCons([H2|T], 1, R).

remCons([H1, H2|T], RN, R) :-
    H1C is H2 - 1,
    H1 =\= H1C,
    RN =:= 1,
    remCons([H2|T], 0, R).

remCons([H1, H2 | T], RN, R) :-
    H1C is H2 - 1,
    H1 =\= H1C,
    RN =:= 0,
    remCons([H2|T], 0, RT),
    R = [H1 | RT].

remCons([_], RN, R) :-
    RN =:= 1,
    R = [].

remCons([H|_], RN, R) :-
    RN =:= 0,
    R = [H].

