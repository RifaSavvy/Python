def count_vowels_in_file(file_path):
    with open(file_path, 'r') as file:
        return sum(1 for char in file.read().lower() if char in 'aeiou')

# Example usage
print(count_vowels_in_file('sample.txt'))

