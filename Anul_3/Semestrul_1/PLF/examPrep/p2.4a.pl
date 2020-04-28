reverse([],[]).
reverse([H|T], R) :-
    reverse(T, RT),
    myAppend(RT, [H], R).
