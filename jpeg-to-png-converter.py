import os
from PIL import Image

def is_valid_jpeg(file_path):
    try:
        with Image.open(file_path) as img:
            return img.format == 'JPEG'
    except:
        return False

def convert_jpeg_to_png(input_file):
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return

    if not is_valid_jpeg(input_file):
        print("Error: The file is not a valid JPEG image.")
        return

    try:
        with Image.open(input_file) as img:
            # Get the filename without extension
            filename = os.path.splitext(os.path.basename(input_file))[0]
            
            # Create the output filename
            output_file = f"{filename}.png"
            
            # Save as PNG
            img.save(output_file, 'PNG')
        
        print(f"Conversion successful. Image saved as '{output_file}'")
    except Exception as e:
        print(f"Error during conversion: {str(e)}")

def main():
    while True:
        input_file = input("Enter the path to the JPEG file (or 'q' to quit): ")
        
        if input_file.lower() == 'q':
            print("Exiting the program.")
            break

        convert_jpeg_to_png(input_file)
        print("\n")  # Add a newline for better readability

if __name__ == "__main__":
    main()
