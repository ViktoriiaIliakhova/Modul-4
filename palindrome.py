def palindrome_fun(word="x"):
    """
            Verifies if the word is a palindrome or not
            Optional argument:
            word
        """
    new_word = word[::-1]
    if word == new_word:
      print("Palindrome")
    else:
      print("Not Palindrome")
palindrome_fun()