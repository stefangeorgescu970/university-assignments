% 2. Are given n points in a plan (represented using its coordinates). Write a predicate to determine all subsets of collinear points.

% subset(L: list, R: list)
% subset(i,o)

subset([], []).
subset( [H | T], R) :-
subset(T, RT),
R = [H | RT].
subset( [_ | T], R) :-
subset( T, R).


% minimumLen(L: List)
% minimumLen(i)

minimumLen([H1, H2, H3 | T]).


areColinear( P1, P2, P3 ) :- slope( P1, P2, S ), slope( P1, P3, S ).
areColinear( P1, P2, P3 ) :- slope( P1, P2, S ), slope( P2, P3, S ).
areColinear( P1, P2, P3 ) :- slope( P1, P3, S ), slope( P2, P3, S ).

slope( P1, P2, S ) :-
P1 = [X1, Y1 | _],
P2 = [X2, Y2 | _],
X2 =\= X1,
S is ((Y2-Y1)/(X2-X1)).

slope( P1, P2, S ) :-
P1 = [X1, Y1 | _],
P2 = [X2, Y2 | _],
X2 =:= X1,
S is 0.


isListColinear( [H1, H2, H3 | T]) :-
areColinear(H1, H2, H3),
isListColinear([H2, H3 | T]).

isListColinear([A,B]).


findOne(L, R) :-
subset(L, RS),
minimumLen(RS),
isListColinear(RS),
R = RS.


findAll(L, R) :-
findall(RO, findOne(L, RO), RI),
sort(RI, R).
