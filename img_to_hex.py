from PIL import Image

def img_to_hex(image_path, output_file):
    # Open the image
    with Image.open(image_path) as img:
        # Convert the image to RGB if it's not
        img = img.convert("RGB")
        pixels = list(img.getdata())

        # Convert each pixel (R, G, B) to hexadecimal and remove the '0x' prefix
        hex_pixels = ['{:02x}{:02x}{:02x}'.format(r, g, b) for r, g, b in pixels]

        # Join all hexadecimal values into a single string
        hex_string = ''.join(hex_pixels)

        # Write the hex string to the output file
        with open(output_file, 'w') as f:
            f.write(hex_string)

# Example usage
img_to_hex('pi_million_image.png', 'pi_million_conv.txt')
