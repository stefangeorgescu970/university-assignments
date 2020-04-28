findOne(L, R) :-
    subset(L, RS),
    minimumLen(RS),
    isListColinear(RS),
    R = RS.
