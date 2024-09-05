import brotli
import os

def decompress_file(input_file):
    # Generate the output file name by replacing '_compressed' with '_decompressed'
    base_name, ext = os.path.splitext(input_file)
    output_file = f"{base_name.replace('_compressed', '_decompressed')}{ext}"
    
    # Read the compressed data from the input file
    with open(input_file, 'rb') as f:
        compressed_data = f.read()
    
    # Decompress the data using Brotli
    decompressed_data = brotli.decompress(compressed_data).decode('utf-8')
    
    # Write the decompressed data to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(decompressed_data)
    
    print(f"Decompressed file saved as: {output_file}")

# Example usage:
decompress_file('pi_million_conv_compressed.txt')
