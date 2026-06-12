word = input("Enter a word: ")

if word == word[::-1]:  #word[start:end:-1]
    print("Palindrome")
else:
    print("Not Palindrome")