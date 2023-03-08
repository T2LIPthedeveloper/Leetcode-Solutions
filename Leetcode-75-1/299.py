class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # secret and guess are strings of digits
        # return a string with the number of bulls and cows
        # bulls are digits that are in the correct position
        # cows are digits that are in the wrong position
        # the digits must be unique
        # the length of secret and guess are the same
        # the length of secret and guess are between 1 and 1000
        # the digits in secret and guess are between 0 and 9
        # the digits in secret and guess are unique
        dict_secret, dict_guess, bulls, cows = {}, {}, 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
                # directly counting bulls
            else:
                if secret[i] in dict_secret:
                    dict_secret[secret[i]] += 1
                # if the digit is already in the dictionary, increment the value
                else:
                    dict_secret[secret[i]] = 1
                # if the digit is not in the dictionary, add it with a value of 1
                # we're not adding bulls to the dictionary because they're already counted
                if guess[i] in dict_guess:
                    dict_guess[guess[i]] += 1
                # dict guess stores the number of times a digit appears in guess
                else:
                    dict_guess[guess[i]] = 1
        for key in dict_secret:
            if key in dict_guess:
                cows += min(dict_secret[key], dict_guess[key])
                # cows are the minimum of the number of times a digit appears in secret and guess
                # this is because the digits must be unique
        return str(bulls) + 'A' + str(cows) + 'B'
