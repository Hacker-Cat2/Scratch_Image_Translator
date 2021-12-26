# Scratch Image Converter
## About
- This is a simple program to convert images into the HSV colour format so Scratch can more easily draw them using the pen extension
- It uses the `pillow` library to open images, the `colorsys` library to convert the rgb values of the image to hsv, and the `os` library to check before overwriting existing files
- The `converter.py` file includes one function named `convert()` which will return the "image code" as a string
- `ui.py` is the command line user interface that will save the converted "image code" to a text file

## Usage
1. Download the files from this repository
2. Open a terminal and navigate to the directory containing the downloaded files
3. Run the command `python ui.py` to use the included user interface
4. Enter the full file path of the image you want to convert
5. Enter an output directory, the default is the current working directory
6. Open the created text file and copy the contents
7. You can now use the image code in my [decoder](https://scratch.mit.edu/projects/589671111/) on Scratch

You can also integrate `converter.py` into your own projects.

## Troubleshooting
- Make sure all required libraries are up to date
- Check for syntax errors
- Contact me on Scratch or GitHub

I would really appreciate it if you credit me, both for the programs here on Github, and the decoder on Scratch using my username @Hacker-Cat2 on both websites: [Scratch](https://scratch.mit.edu/users/Hacker-Cat2/) and [GitHub](https://github.com/Hacker-Cat2/).

## License
[MIT License](https://choosealicense.com/licenses/mit/)
