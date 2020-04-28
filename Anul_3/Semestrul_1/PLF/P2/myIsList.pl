myIsList(X) :-
        var(X), !,
        fail.
myIsList([]).
myIsList([_|T]) :-
        myIsList(T).
