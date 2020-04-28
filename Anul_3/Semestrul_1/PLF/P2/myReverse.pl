% myReverse(L: list, R: list)
% myReverse(L: i, R: o)

myReverse([], []).

myReverse([H | T], Rez) :- myReverse(T, RezT),
    myAppend(RezT, [H], Rez).
