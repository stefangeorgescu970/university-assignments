% myMember(X: Int, L: list).
% myMember(i,i).
% Turn a list into a set, items ordered by their last appearances


myMember(X, [X|_]).
myMember(X, [_|T]) :- myMember(X, T).
