
isSet([]).
isSet([X|Y]):- not(member(X,Y)),isSet(Y).

subset([],Z).
subset([X|Y],Z):- member(X,Z),subset(Y,Z).
	
union([],X,X):-!.
union([X|W],Y,Z):- member(X,Y),union(W,Y,Z),!.
union([X|W],Y,[X|Z]):- union(W,Y,Z).
	
intersect([],X,[]):- !.
intersect([X|W],Y,[X|Z]):- member(X,Y),intersect(W,Y,Z),!.
intersect([X|W],Y,Z):- intersect(W,Y,Z).



tally(_,[],0).
tally(X,[X|Y],N):- !,tally(X,Y,N1),N is N1+1.
tally(X,[_|Y],N):- tally(X,Y,N). 

subst(X,Y,[],[]):- !.
subst(X,Y,[X|W],[Y|Z]):- subst(X,Y,W,Z),!.
subst(X,Y,[V|W],[V|Z]):- subst(X,Y,W,Z).

insert(X, [], [X]).
insert(X, [Y|Z], [X,Y|Z]) :-
    X @< Y, !.
insert(X, [Y|Z0], [Y|Z]) :-
    insert(X, Z0, Z).
	
accRev([H|T],A,R):-  accRev(T,[H|A],R).
accRev([],A,A). 