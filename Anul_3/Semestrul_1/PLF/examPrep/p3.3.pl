genList(B, E, R):-
    B =< E,
    NB is B + 1,
    genList(NB, E, RT),
    R = [B | RT].

genList(B, E, R) :-
    B > E,
    R = [].


decomp(N, CB, C, CS, R) :-
    CS < N,
    CN is C + 1,
    CSN is CS + CN,
    decomp(N, CB, CN, CSN, R).

decomp(N, CB, _, _, R) :-
    CB < N / 2,
    CBN is CB + 1,
    decomp(N, CBN, CBN, 0, R).

decomp(N, CB, C, CS, R) :-
    CS =:= N,
    genList(CB, C, R).

findOne(N, R) :- decomp(N, 1, 1, 0, R).

findAll(N, R) :-
    findall(RC, findOne(N, RC), RT),
    sort(RT, R).

