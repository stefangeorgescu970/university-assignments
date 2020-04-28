% consecSeqHelp(L: list, Winner: list, WinnerL: int, Current: list,
% CurrentL: int, Rez: list)
% consecSeqHelp(L: i, Winner: i, WinnerL: i, Current: i, CurrentL: i,
% Rez: o)

conseqSeqHelp([], _, WinnerL, Current, CurrentL, Rez) :- CurrentL > WinnerL,
    myReverse(Current, Rez).

conseqSeqHelp([], Winner, _, _, _, Rez) :- myReverse(Winner, Rez).

conseqSeqHelp([H|T], Winner, WinnerL, _, CurrentL, Rez) :-
    CurrentL =:= 0,
    H mod 2 =:= 0,
    conseqSeqHelp(T, Winner, WinnerL, [H], 1, Rez).

conseqSeqHelp([H|T], Winner, WinnerL, _, CurrentL, Rez) :-
    CurrentL =:= 0,
    H mod 2 =\= 0,
    conseqSeqHelp(T, Winner, WinnerL, [], 0, Rez).


conseqSeqHelp([H|T], Winner, WinnerL, Current, CurrentL, Rez) :-
    Current = [X | _],
    Len is CurrentL + 1,
    ExpH is X + 2,
    H =:= ExpH,
    conseqSeqHelp(T, Winner, WinnerL, [H | Current], Len, Rez).

conseqSeqHelp([H|T], _, WinnerL, Current, CurrentL, Rez) :-
    Current = [X | _],
    ExpH is X + 2,
    H =\= ExpH,
    H mod 2 =:= 0,
    CurrentL > WinnerL,
    conseqSeqHelp(T, Current, CurrentL, [H], 1, Rez).

conseqSeqHelp([H|T], Winner, WinnerL, Current, _, Rez) :-
    Current = [X | _],
    ExpH is X + 2,
    H =\= ExpH,
    H mod 2 =:= 0,
    conseqSeqHelp(T, Winner, WinnerL, [H], 1, Rez).

conseqSeqHelp([H|T], _, WinnerL, Current, CurrentL, Rez) :-
    Current = [X | _],
    ExpH is X + 2,
    H =\= ExpH,
    H mod 2 =\= 0,
    CurrentL > WinnerL,
    conseqSeqHelp(T, Current, CurrentL, [], 0, Rez).

conseqSeqHelp([H|T], Winner, WinnerL, Current, _, Rez) :-
    Current = [X | _],
    ExpH is X + 2,
    H =\= ExpH,
    H mod 2 =\= 0,
    conseqSeqHelp(T, Winner, WinnerL, [], 0, Rez).
