def count_words_in_file(file_name):
    try:
        with open('file.txt', 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

if __name__ == "__main__":
    file_name = input("Enter the file name: ")
    word_count = count_words_in_file(file_name)

    if word_count != -1:
        print(f"The number of words in the file '{file_name}' is: {word_count}")
