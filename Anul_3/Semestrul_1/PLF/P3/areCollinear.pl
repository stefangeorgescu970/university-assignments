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
