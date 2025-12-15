def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count


def count_consonants(s):
    count = 0
    for ch in s:
        if ch.isalpha() and ch not in "aeiouAEIOU":
            count += 1
    return count


def vowel_consonant_ratio(vowels, consonants):
    if consonants == 0:
        return "Consonants count is zero, ratio not possible"
    return vowels / consonants


# Main Program
text = input("Enter a string: ")

v = count_vowels(text)
c = count_consonants(text)

ratio = vowel_consonant_ratio(v, c)

print("Number of vowels:", v)
print("Number of consonants:", c)
print("Ratio of vowels to consonants:", ratio)