% main(L: list, R: list)
% main(i, o)
% main(l1...ln) =
% empty list, if n == 0
% l1 U main(l2...ln), if l1 is a perfect square
% main(l2...ln), if l1 is not a perfect square

main([], []).
main([H | T], REZ) :- isPerfectSquareWrap(H),
    main(T, REZINT),
    REZ = [H | REZINT].
main([H | T], REZ) :- \+ isPerfectSquareWrap(H),
    main(T, REZ).
