def character_frequency(string):
    
    frequency = {}
    for char in string:
        if char.isalpha():
            char = char.lower()
            frequency[char] = frequency.get(char, 0) + 1
    return frequency


if __name__ == "__main__":
    string = "Python is funny"
    frequency = character_frequency(string)
    print(frequency)