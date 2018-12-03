
words = ["gin", "zen", "gig", "msg"]

morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
         "...","-","..-","...-",".--","-..-","-.--","--.."]


def uniqueMorseRepresentations(words):
    x = set()

    for word in words:
        morse_word = ''

        for key in word:
            num = ord(key)-96
            morse_key = morse[num-1]
            morse_word = morse_word + morse_key

        x.add(morse_word)

    return len(x)

uniqueMorseRepresentations(words)