def reverse_file_content(input_file, output_file):
    try:
        with open('file.txt', 'r') as input_file:
            content = input_file.read()
            reversed_content = content[::-1]

        with open('file2.txt', 'w') as output_file:
            output_file.write(reversed_content)

        print(f"Content reversed and stored in '{output_file.name}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file_name = input("Enter the input file name: ")
    output_file_name = input("Enter the output file name: ")

    reverse_file_content(input_file_name, output_file_name)

    # Print the content of the output file
    try:
        with open('file2.txt', 'r') as output_file:
            output_content = output_file.read()
            print(f"Content of '{output_file.name}':")
            print(output_content)
    except FileNotFoundError:
        print(f"Error: The file '{output_file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
