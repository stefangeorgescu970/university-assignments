% subset(L: list, R: list)
% subset(i,o)

subset([], []).
subset( [H | T], R) :-
    subset(T, RT),
    R = [H | RT].
subset( [_ | T], R) :-
    subset( T, R).
