import gmpy2
import math
from PIL import Image
import time

def number_to_hex_with_gmpy2(input_filename):
    with open(input_filename, 'r') as input_file:
        numeric_string = input_file.read().strip()

    # Convert the numeric string to a large integer using gmpy2
    num = gmpy2.mpz(numeric_string)
    # Convert to hexadecimal string
    hex_string = num.digits(16)  # gmpy2's method to get hex string
    
    return hex_string

def hex_to_image(hex_string, output_filename):
    padding_needed = (6 - len(hex_string) % 6) % 6
    hex_string = '0' * padding_needed + hex_string
    
    total_chars = len(hex_string)
    pixels = total_chars // 6
    
    width = int(math.sqrt(pixels))
    height = (pixels + width - 1) // width

    image_data = []

    for i in range(0, total_chars, 6):
        hex_chunk = hex_string[i:i+6]
        r = int(hex_chunk[0:2], 16)
        g = int(hex_chunk[2:4], 16)
        b = int(hex_chunk[4:6], 16)
        image_data.append((r, g, b))
    
    image_data += [(0, 0, 0)] * (width * height - len(image_data))
    
    try:
        image = Image.new("RGB", (width, height))
        image.putdata(image_data)
        image.save(output_filename)
        print(f"Image successfully saved as {output_filename}")
    except Exception as e:
        print(f"An error occurred while creating the image: {e}")

def main():
    input_filename = "pi_million.txt"
    output_filename = "pi_million_hex.txt"
    output_image = "pi_million_image.png"

    # Start timing
    start_time = time.time()

    # Convert the numeric string to a hexadecimal string
    hex_string = number_to_hex_with_gmpy2(input_filename)

    # Save the hexadecimal string to an output file
    with open(output_filename, 'w') as output_file:
        output_file.write(hex_string)

    # Convert the hexadecimal string to an image
    hex_to_image(hex_string, output_image)

    # End timing
    end_time = time.time()
    duration = end_time - start_time

    print(f"Hexadecimal conversion saved to {output_filename}")
    print(f"Image saved as {output_image}")
    print(f"Time taken: {duration:.4f} seconds")

if __name__ == "__main__":
    main()
