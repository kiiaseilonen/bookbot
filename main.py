def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    def count_words():
        words = file_contents.split()
        
        return (len(words))
        
    count_words()

    def count_characters():
        words = file_contents
        character_log = {}

        for low_character in words:
            low_character = low_character.lower()
                
            if low_character not in character_log:
                character_log[low_character] = 1

            else: 
                character_log[low_character] += 1

        return character_log
        

    def sort_on(character_log):
        return character_log["num"]
    
    char_list = []
    characters = count_characters()

    for char, num in characters.items():
        if char.isalpha():
            char_dict = {"char": char, "num": num}
            char_list.append(char_dict)

    char_list.sort(key=lambda char_log: char_log["char"])
  
    print("--- Begin report ---")

    for char_log in char_list:
        print(f"The '{char_log['char']}' character was found {char_log['num']} times")

    print("--- End report ---")


main()