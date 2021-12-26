import os
import converter

run = True
while run:
    image_path = input("Type the file path of the image you want to encode here. Make sure to include the file extension!: ")
    output_dir = input("Type the directory you would like to save the code to: ")
    if not output_dir:
        output_dir = '.'
    output_path = os.path.join(output_dir, os.path.basename(image_path) + '_hsv.txt')
    success, result = converter.convert(image_path)
    if success is False:
        print(result)
    elif success is True:
        print("Saving file...")
        try:
            with open(output_path, 'x') as output_file:
                output_file.write(result)
            print(f"Succesfully saved file '{output_path}'")
        except Exception as exception:
            print(f"Error: {exception}")
            print("Image code:")
            print(result)
    run = input("Enter 'r' to encode another image, or anything else to close: ") == 'r'
