import itertools

def calculate_response(guess, answer):
    response = 1
    for x in range(5):
        a = ord(guess[x]) - ord('a')
        b = ord(answer[x]) - ord('a')
        response = (response * (a-b)) % 31
    return response

#wordlist = open('sgb-words.txt', 'r').read().split('\n')

def generate_wordlist():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    wordlist = [''.join(w) for w in itertools.product(alphabet, repeat=5)]
    return wordlist

def filter_words(possible_words, last_guess, last_response):
    filtered_words = []
    for word in possible_words:
        if calculate_response(last_guess, word) == last_response:
            filtered_words.append(word)
    return filtered_words

def main():
    possible_words = generate_wordlist()
    guesses = []
    responses = []

    for _ in range(6):  # Assuming the original program allows 3 attempts
        last_guess = input("Last guess: ").lower()
        last_response = int(input("Last response: "))
        guesses.append(last_guess)
        responses.append(last_response)

        if last_guess:
            possible_words = filter_words(possible_words, last_guess, last_response)
        else:
            print("Invalid guess. Please provide a valid guess.")

        print("Possible words remaining:", possible_words)

        if len(possible_words) == 1:
            print("The word is:", possible_words[0])
            break

if __name__ == "__main__":
    main()
