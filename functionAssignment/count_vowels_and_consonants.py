def count_vowels_and_consonants(s):
    """Count the number of vowels and consonants in a string."""
    return (len([c for c in s if c.lower() in 'aeiou']),len([c for c in s if c.lower() not in 'aeiou']))

s = input("Enter String : ")
count_vowels, count_cons= count_vowels_and_consonants(s)
print(f'Number of vowels in string "{s}" is {count_vowels} and number of consonants are {count_cons}')