def sed(pattern, replacement, input_filename, output_filename):
    try:
        with open('/Users/prajaktapohare/Library/CloudStorage/OneDrive-ILStateUniversity/BIS420/Week 14/input.txt', 'r') as infile:
            content = infile.read()
        
        new_content = content.replace(pattern, replacement)
        
        with open('/Users/prajaktapohare/Library/CloudStorage/OneDrive-ILStateUniversity/BIS420/Week 14/output.txt', 'w') as outfile:
            outfile.write(new_content)

        print(f"Replacements complete. Output written to '{'output.txt'}'.")

    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except IOError as e:
        print(f"IO error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def main():
    pattern = '\\ '
    replacement = ' '
    input_filename = '/Users/prajaktapohare/Library/CloudStorage/OneDrive-ILStateUniversity/BIS420/Week 14/input.txt'
    output_filename = '/Users/prajaktapohare/Library/CloudStorage/OneDrive-ILStateUniversity/BIS420/Week 14/output.txt'
    sed(pattern, replacement, input_filename, output_filename)

main()