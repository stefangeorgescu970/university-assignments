
% 14.
% a. Define a predicate to determine the longest sequences of consecutive even numbers (if exist more maximal sequences one of them).
% b. For a heterogeneous list, formed from integer numbers and list of numbers, define a predicate to replace every sublist with the longest sequences of even numbers from that sublist.
% Eg.: [1, [2, 1, 4, 6, 7], 5, [1, 2, 3, 4], 2, [1, 4, 6, 8, 3], 2, [1, 5], 3] =>
% [1, [4, 6], 5, [2], 2, [4, 6, 8], 2, [], 3]


% Point a

% myAppend(L1: list, L2: list, R: list)
% myAppend(i,i,o).
% Put the contents of L2 after the contents of L1 and store them in R

% Model matematic
% myAppend(l1…ln, p1…pm) =
% p1….pm, n = 0
% l1 U myAppend(l2…ln, p1…pm), n != 0

myAppend([],R,R).
myAppend([H|T],L2,[H|R]) :-myAppend(T,L2,R).


% myReverse(L: list, R: list)
% myReverse(L: i, R: o)

% Model matematic
% myReverse(l1….ln)
% [], n==0
% myReverse(l2…ln) U l1, n != 0

myReverse([], []).

myReverse([H | T], Rez) :- myReverse(T, RezT),
myAppend(RezT, [H], Rez).


% consecSeqHelp(L: list, Winner: list, WinnerL: int, Current: list,
% CurrentL: int, Rez: list)
% consecSeqHelp(L: i, Winner: i, WinnerL: i, Current: i, CurrentL: i,
% Rez: o)

% Model matematic
% conseqSeqHelp(l1…ln, w1….wm, lenW, c1….cp, lenC) =
% myReverse(c1….cp), n == 0 and lenC > lenW
% myReverse(w1….wm), n == 0
% conseqSeqHelp(l2…ln, w1….wm, lenW, [H], 1), lenC == 0 and l1 mod 2 == 0
% conseqSeqHelp(l2…ln, w1….wm, lenW, [], 0), lenC == 0 and l1 mod 2 != 0
% conseqSeqHelp(l2…ln, w1…wm, lenW, l1 U c1….cp, lenC + 1), l1 == c1 + 2
% conseqSeqHelp(l2…ln, c1…cp, lenC, [l1], 1), l1 != c1 + 2, l1 mod 2 == 0, lenC > lenW
% conseqSeqHelp(l2…ln, w1….wm, lenW, [l1], 1), l1 != c1 + 2, l1 mod 2 == 0
% conseqSeqHelp(l2…ln, c1…cp, lenC, [], 0), l1 != c1 + 2, l1 mod 2 != 0, lenC > lenW
% conseqSeqHelp(l2…ln, w1….wm, lenW, [], 0), l1 != c1 + 2, l1 mod 2 != 0,

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


% consecSeq(L: list, R: list)
% consecSeq(L: input, R: output)

% model matematic
% consecSeq(l1…ln) =
% consecSeq(l2…ln), l1 mod 2 != 0
% conseqSecHelp(l1…ln, [], 0, [l1], 1), l1 mod 2 == 0

consecSeq([], []).
consecSeq([H | T], Rez) :- H mod 2 =\= 0,
consecSeq(T, Rez).
consecSeq([H | T], Rez) :- H mod 2 =:= 0,
conseqSeqHelp(T, [], 0, [H], 1, Rez).



% Point b

% myIsList(L: )
% myIsList(i)
% returns true f param is list

% Model matematic
% myIsList(l1…ln) =
% fail, var(l1….ln) fails,
% true, n == 0
% myIsList(l2….ln)

myIsList(X) :-
var(X), !,
fail.
myIsList([]).
myIsList([_|T]) :-
myIsList(T).


% parseHetList(L:list, R: list)
% parseHetList(L: input, R: output)

% Model matematic
% parseHetList(l1….ln)
% [], n == 0
% consecSeq(l1) U parseHetList(l2…ln), myIsList(l1) == true
% l1 U parse

parseHetList([], []).

parseHetList([H | T], R) :- myIsList(H),
consecSeq(H, RezH),
parseHetList(T, RezT),
R = [RezH | RezT].

parseHetList([H | T], R) :- \+ myIsList(H),
parseHetList(T, RezT),
R = [H | RezT].

