ins([], E, [E]).
ins(L, E, R) :- R = [E | L].
ins([H|T], E, R) :- ins(T, E, RT), R = [H | RT].
