generateAll(CP, R) :-
    CP =< 4,
    NCP is CP + 1,
    generateAll(NCP, RT),
    R = [ 1 | RT].

generateAll(CP, R) :-
    CP =< 4,
    NCP is CP + 1,
    generateAll(NCP, RT),
    R = [ 2 | RT].

generateAll(CP, R) :-
    CP =< 4,
    NCP is CP + 1,
    generateAll(NCP, RT),
    R = [ 3 | RT].

generateAll(CP, R) :-
    CP > 4,
    R = [].


lastElem([H], H).
lastElem([_ | T], R) :- lastElem(T, R).


numOfElem([], _, 0).
numOfElem([H | T], E, R) :-
    H =:= E,
    numOfElem(T, E, RT),
    R is RT + 1.
numOfElem([H | T], E, R) :-
    H =\= E,
    numOfElem(T, E, R).


findOne(R) :-
    generateAll(1, RT),
    numOfElem(RT, 3, TS),
    TS =< 2,
    lastElem(RT, E),
    E =\= 2,
    R = RT.
