def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    output = "--- Begin report of books/frankenstein.txt ---\n"
    #print(text)
    word_count = get_word_count(text)
    output += f"{word_count} words found in the document\n\n"
    #print(word_count)
    character_count = get_character_count(text)
    sorted_characters = get_sorted_characters(character_count)
    for char in sorted_characters:
       output+= f"The '{char["name"]}' character was found {char["num"]} times\n"
    output += "--- End report ---"
    #print(character_count)
    print(output)


def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_sorted_characters(unsorted_dict):
    unsorted_list =[]
    for entry in unsorted_dict:
        if entry.isalpha():
            unsorted_list.append({"name":entry, "num":unsorted_dict[entry]})
    #print(unsorted_list)
    unsorted_list.sort(reverse=True,key=sort_on)
    return unsorted_list

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