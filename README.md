# Macheight

## What is it?

This is the code test for the company Macheight, it seeks to create a program that when executed asks for a number, this will look for the pairs of players whose height in inches is equal to the written number.

## How does it work?

1. First, all commands must be executed in the linux console, or windows cmd.
2. How to clone the repository.
```
    $ git clone https://github.com/jpcortesg1/macheight.git
```

3. Enter the project folder.
```
    $ cd macheight
```

4. Run the program
```
    $ python3 macheight.py
```
You can see something that says:
```
Insert any number to search for the pair of players that when adding their height is equal to the number, or write 'exit' to stop the program:
```

You must enter any number for the program to search for players.

For example if you enter the number 139, the output should be
```
Nate Robinson Mike Wilks
Nate Robinson Brevin Knight
```

For example if you enter an invalid value you should see.
```
Value must be numeric
```

If you enter a numeric value that has no matches
```
No matches found
```

The program does not stop executing, that is, at the end of the search with a number it continues to ask until the word 'exit' is entered, or press the key combination Ctrl + c (cmd in mac)