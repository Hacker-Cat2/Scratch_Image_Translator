# Scratch_Image_Translator
About:
• This is a simple program that is meant to convert images into the HSV colour format so Scratch can more easily draw them using the pen extension.
• It uses the imageio library to open images, the colorsys library to convert the rgb values of the image to hsv, and the os library to check before overwriting existing files.
• There are two functions within the "imageToCode" class. The first is "printCode", and the second is "saveToFile". "printCode" will print the output image "code" into the command line, and "saveToFile" will require an aditional file path to save the code to. Both will require the directory of whatever image you are trying to convert.
• "Image_Translator.py" is the converter itself, and the other file "Interface.py" is a simple command line interface to convert images using the "imageToCode" class in the previously mentioned "Image_Translator.py" file.
• All output code files will be stored in the .txt file type.

Instuctions for use:
1. Save the "Image_Translator.py" and the optional "Interface.py" files to wherever you're running them from.
2. Incorperate them into your own projects however needed, or use as-is.
3. Use the decoder in my project on Scratch here: https://scratch.mit.edu/projects/589671111/
4. Create your own project that uses these scripts.
5. Have fun!

I would really appreciate it if you credit me, both for the "translator" here on Github, and the decoder on Scratch.
