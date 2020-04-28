isListColinear( [H1, H2, H3 | T]) :-
    areColinear(H1, H2, H3),
    isListColinear([H2, H3 | T]).

isListColinear([A,B]).
