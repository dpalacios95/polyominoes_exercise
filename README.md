# Polyominoes

There's a background introduction on [Wikipedia](https://en.wikipedia.org/wiki/Polyomino):

> A polyomino is a plane geometric figure formed by joining one or more equal squares edge to edge. It is a polyform whose cells are squares. It may be regarded as a finite subset of the regular square tiling.

We're interested specifically in one-sided polyominoes (pieces can be rotated or translated, but not flipped.)

There is only one 2-ominoe (or "domino", a block with 2 pieces):

    XX

There are 2 3-ominoes:

    XX   XXX
    X

There are 7 4-ominoes, which you'll recognise as the pieces from tetris:

    XXXX  XXX  XXX  XXX  XX  XX    XX
          X      X   X   XX   XX  XX

There are 196 7-ominoes.


## Coding Problems

  * Answer "how many 9-ominoes are there?"
  * Provide a program that calculates the number of _N_-ominoes for any whole number _N_.
  * Print out all the _N_-ominoes for any _N_.
  * Optimise for either speed or memory for large values of _N_ (greater than 10).
