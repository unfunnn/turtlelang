# turtlelang
## About:
turtlelang is an esolang (esoteric language) that uses a turtle as a "pointer" and a 2D 5x5 grid as a way to store variables. You may only output and input to the current position that you are in. The position system is based around an array, with position 00 being the top left corner and 44 being the bottom right.

This language does not need newlines or tabs, everything can be entered on one line

This language is not turning complete yet due to the lack of loops. 

Because it is a turtle that draws, you can use this to create monochrome pixel art if you wish

## CLI:
This language runs in a CLI (command line interface) which has some of it's own subcommands

exit: Exits the CLI and brings you back to wherever you were before

open: Lets you specifcy a file path to a .turt file which it will then attempt to run

compile: Compiles every instruction that you have entered so far into a single string

## Directionals:
\>: Moves right

<: Moves left

^: Moves up

v: Moves down

Directionals cannot be used while an operator is also in use

## Operators:
%: Sets that positions variable to whatever comes after (%3: would set the variable to 3)

@: Outputs the variable that you are currently on (@:, no arguments needed)

\$: Asks the user for input and stores it (\$:, no arguments needed)

|: Outputs a literal instead of a variable (|literal goes here:)

+,-,\*,/: Arithmetic operators, operate on your given positions and store it in your current one. They all have the same syntax (+00,01: would add the variables stored in pos00 and pos01 and store it)

?: Conditional, stores a variable dependant on the outcome (?00,01,=,yes,no: would check if pos00 and pos01 are equal, if so then store "yes", otherwise "no")
&: Stores a random number between given args (&1,5 would choose a random number between 1 and 5)

#: Comment, is ignored (#comment:)

.: Duplicates the pos you are currently on to another one of your choice (.00: would copy the data off whatever pos you're at to 00)

\[]: Loops are coming soon

You cannot use an operator while another operator is in use

Every operator needs a ":" after it to indicate that it needs to run and to end the instruction

## Other instructions:
\~: Toggles the "drawing" of the turtle on or off (~> would move to the right without drawing)

## Example Programs:
CAT program:
>$:@:

Program that adds (replace the + with -, \*, or / for that operator) two numbers inputted by the user together:
>$:>$:>+00,01:@:

Draw a spiral:
>vvvv>>>>^^^<<v

Random Number Guessing Game:
>&1,5:>$:>?00,01,=,correct,incorrect:@:<<<| correct guess was :@:

Fibonnaci (first 9 numbers)
>%0:@:| :>%1:@:| :>+00,01:@:| :<.00:>.01:+00,01:@:| :<.00:>.01:+00,01:@:| :<.00:>.01:+00,01:@:| :<.00:>.01:+00,01:@:| :<.00:>.01:+00,01:@:| :<.00:>.01:+00,01:@:| :<.00:>.01:
