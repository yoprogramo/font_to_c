# Convert raw image file to c

This program is intended to generate a .h file based on a raw image in black and white.

The image should have the height of the font (8 pixels in this case) and all the characters
you are going to use in your device with no space between (in the example the first 95 ASCII 
characters starting from the space 0x20)

You have to generate the image in b/w indexed colors (max 2) and export using gimp as raw
or data file (.data included for the example). Modify the name of the input and output files
in the program and execute it with python3.