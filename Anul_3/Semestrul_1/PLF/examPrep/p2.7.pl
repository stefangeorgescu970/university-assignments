myMax([], -9999).
myMax([H|T], R) :-
    myMax(T, RT),
    H > RT,
    R is H.
myMax([H|T], R) :-
    myMax(T, RT),
    H =< RT,
    R is RT.

posOfNum([], _, _, []).
posOfNum([H|T], N, CP, R) :-
    H =:= N,
    CPN is CP + 1,
    posOfNum(T, N, CPN, RT),
    R = [CP | RT].
posOfNum([H|T], N, CP, R) :-
    H =\= N,
    CPN is CP + 1,
    posOfNum(T, N, CPN, R).

main([], []).
main(L, R) :-
    myMax(L, M),
    posOfNum(L, M, 1, R).
