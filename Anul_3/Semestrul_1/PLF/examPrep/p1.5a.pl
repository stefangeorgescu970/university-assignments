genPairs(_, [], []).
genPairs(E, [H|T], R):-
    genPairs(E, T, RT),
    R = [[E, H] | RT].

allPairs([], _, []).
allPairs([H|T], [_|TS], R) :-
    genPairs(H, TS, RGEN),
    allPairs(T, TS, RT),
    myAppend(RGEN, RT, RINT),
    R = RINT.


