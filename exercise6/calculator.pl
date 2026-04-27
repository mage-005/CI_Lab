start :-
    write('Enter first number: '), nl,
    read(X),
    write('Enter second number: '), nl,
    read(Y),
    write('Choose operation: add / subtract / multiply / divide / modulus / power'), nl,
    read(Op),
    calculate(Op, X, Y, R),
    write('Result is: '), write(R), nl.
    
calculate(add, X, Y, R) :- R is X + Y.
calculate(subtract, X, Y, R) :- R is X - Y.
calculate(multiply, X, Y, R) :- R is X * Y.
calculate(divide, X, Y, R) :- Y \= 0, R is X / Y.
calculate(modulus, X, Y, R) :- R is X mod Y.
calculate(power, X, Y, R) :- R is X ** Y.