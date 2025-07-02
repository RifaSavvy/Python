def reverse_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        content = infile.read()
    with open(output_file, 'w') as outfile:
        outfile.write(content[::-1])

# Example usage
reverse_file('input.txt', 'reversed_output.txt')

