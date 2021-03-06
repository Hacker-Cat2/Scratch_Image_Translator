# Scratch_Image_Translator
About:
1. This is a simple program that is meant to convert images into the HSV colour format so Scratch can more easily draw them using the pen extension.
2. It uses the imageio library to open images, the colorsys library to convert the rgb values of the image to hsv, and the os library to check before overwriting existing files.
3. There are two functions within the "imageToCode" class. The first is "printCode", and the second is "saveToFile". "printCode" will print the output image "code" into the command line, and "saveToFile" will require an aditional file path to save the code to. Both will require the directory of whatever image you are trying to convert.
4. "Image_Translator.py" is the converter itself, and the other file "Interface.py" is a simple command line interface to convert images using the "imageToCode" class in the previously mentioned "Image_Translator.py" file.
5. All output code files will be stored in the .txt file type.

Instuctions for use:
1. Save the "Image_Translator.py" and the optional "Interface.py" files to wherever you're running them from.
2. Incorperate them into your own projects however needed, or use as-is.
3. Use the decoder in my project on Scratch here: https://scratch.mit.edu/projects/589671111/
4. Create your own project that uses these scripts.
5. Have fun!

Troubleshooting:
1. Make sure all required libraries are up to date
2. Check for syntax errors
3. Contact me on Scratch (or here?)

I would really appreciate it if you credit me, both for the programs here on Github, and the decoder on Scratch using my username (@Hacker-Cat2 on both websites: https://scratch.mit.edu/users/Hacker-Cat2/ - Scratch, https://github.com/Hacker-Cat2/ - Github).
