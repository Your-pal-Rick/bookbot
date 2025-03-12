def get_word_count(string):
    word_count = len(string.split())
    return word_count

def get_character_count(string):
    character_count = {}
    for character in string:
        if character.lower() not in character_count:
            character_count[character.lower()] = 0
        character_count[character.lower()] += 1
    return character_count

def sort_characters_by_count(character_count):
    sorted_character_count = []
    for character in character_count:
        sorted_character_count.append({"character": character, "count": character_count[character]})
    sorted_character_count.sort(reverse = True, key = lambda dictionary: dictionary["count"])
    return sorted_character_count
