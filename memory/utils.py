def convert_to_single_word(text):
    # Split the text into words
    words = text.split()
    
    # Capitalize each word and join them without spaces
    single_word = ''.join(word.capitalize() for word in words)
    
    return single_word 