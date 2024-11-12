def process_file():
    """
    Reads a file, modifies its content, and writes to a new file
    with comprehensive error handling.
    """
    while True:
        input_filename = input("Enter the input filename: ")
        
        try:
            with open(input_filename, 'r') as input_file:
                content = input_file.read()
                
                # Modify content (for example, convert to uppercase and add line numbers)
                modified_content = []
                for i, line in enumerate(content.split('\n'), 1):
                    modified_content.append(f"{i}. {line.upper()}")
                
                # Get output filename
                output_filename = input("Enter the output filename: ")
                
                # Write modified content to new file
                with open(output_filename, 'w') as output_file:
                    output_file.write('\n'.join(modified_content))
                
                print(f"\nSuccess! Modified content written to {output_filename}")
                print(f"Processed {len(modified_content)} lines")
                break
                
        except FileNotFoundError:
            print(f"Error: The file '{input_filename}' was not found.")
            retry = input("Would you like to try another filename? (yes/no): ")
            if retry.lower() != 'yes':
                print("Operation cancelled.")
                break
                
        except PermissionError:
            print(f"Error: Permission denied accessing '{input_filename}'.")
            print("Please check file permissions and try again.")
            break
            
        except IOError as e:
            print(f"Error: An I/O error occurred: {e}")
            break
            
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break

if __name__ == "__main__":
    print("File Processing Program")
    print("----------------------")
    print("This program will read a file, convert its contents to uppercase,")
    print("add line numbers, and write the result to a new file.")
    print("----------------------\n")
    
    process_file()