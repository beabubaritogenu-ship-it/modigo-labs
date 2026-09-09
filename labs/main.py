def has_all_vowels(word):
    required = {"a", "e", "i", "o", "u"}
    word = word.lower()
    # TODO: build a set of vowels actually found in `word`,
    # then check if it contains all of `required`
    return required <= set(word)