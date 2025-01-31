def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    #word_count = get_word_count(text)
    #print(word_count)
    character_count = get_character_count(text)
    print(character_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lowercase_text = text.lower()
    char_dict = {}
    for char in lowercase_text:
        if char in char_dict:
            char_dict[char] +=1
        else:
            char_dict[char] =1
    return char_dict

main()