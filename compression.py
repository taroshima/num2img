import brotli
import os

def compress_file(input_file):
    # Generate the output file name by appending '_compressed' to the input file name
    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name}_compressed{ext}"
    
    # Read the contents of the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Compress the content using Brotli
    compressed_data = brotli.compress(content.encode('utf-8'), quality=11)
    
    # Write the compressed data to the output file in binary mode
    with open(output_file, 'wb') as f:
        f.write(compressed_data)
    
    print(f"Compressed file saved as: {output_file}")

# Example usage:
compress_file('pi_million_conv.txt')
