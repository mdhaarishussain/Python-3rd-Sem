def print_lines_in_reverse(file_name):
    try:
        with open('file.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                reversed_line = line.strip()[::-1]  
                print(reversed_line)
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    print_lines_in_reverse(file_name)
