mergeLists([],[],[]).
mergeLists([], L, L).
mergeLists(L, [], L).
mergeLists([H1|T1], [H2|T2], R):-
    H1 < H2,
    mergeLists(T1, [H2|T2], RT),
    R = [H1|RT].
mergeLists([H1|T1], [H2|T2], R):-
    mergeLists([H1|T1], T2, RT),
    R = [H2|RT].


removeDuplicatesSorted([H1, H2 | T], R) :-
    H1 =:= H2,
    removeDuplicatesSorted([H2 | T], R).
removeDuplicatesSorted([H1, H2 | T], R) :-
    removeDuplicatesSorted([H2 | T], RT),
    R = [H1 | RT].
removeDuplicatesSorted([H1|_], [H1]).



main(L1, L2, R) :-
    mergeLists(L1, L2, RL),
    removeDuplicatesSorted(RL, R).

hetMain([], []).
hetMain([H|T],R) :-
    is_list(H),
    hetMain(T, RT),
    main(H, RT, R).
hetMain([H|T], R) :-
    hetMain(T, RT),
    main([H], RT, R).
