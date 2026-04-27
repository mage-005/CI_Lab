male(motilal).
male(jawaharlal).
male(rajiv).
male(sanjay).
male(rahul).

female(kamala).
female(indira).
female(sonia).
female(priyanka).
female(vijayalakshmi).
female(krishna).

parent(motilal, jawaharlal).
parent(motilal, vijayalakshmi).
parent(motilal, krishna).
parent(jawaharlal, indira).
parent(kamala, indira).
parent(indira, rajiv).
parent(indira, sanjay).
parent(rajiv, rahul).
parent(rajiv, priyanka).
parent(sonia, rahul).
parent(sonia, priyanka).

father(X,Y) :- parent(X,Y), male(X).
mother(X,Y) :- parent(X,Y), female(X).

grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
grandfather(X,Y) :- grandparent(X,Y), male(X).
grandmother(X,Y) :- grandparent(X,Y), female(X).

sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \= Y.
brother(X,Y) :- sibling(X,Y), male(X).
sister(X,Y) :- sibling(X,Y), female(X).

ancestor(X,Y) :- parent(X,Y).
ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y).