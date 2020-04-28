% myAppend(L1: list, L2: list, R: list)
% myAppend(i,i,o).
% Put the contents of L2 after the contents of L1 and store them in R


myAppend([],R,R).
myAppend([H|T],L2,[H|R]) :-myAppend(T,L2,R).
