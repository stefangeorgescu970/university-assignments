% consecSeq(L: list, R: list)
% consecSeq(L: input, R: output)

consecSeq([], []).
consecSeq([H | T], Rez) :- H mod 2 =\= 0,
    consecSeq(T, Rez).
consecSeq([H | T], Rez) :- H mod 2 =:= 0,
    conseqSeqHelp(T, [], 0, [H], 1, Rez).

