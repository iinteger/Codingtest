def solution(n, words):
    using_word = []
    last_alphabet = words[0][0]

    for i, word in enumerate(words):
        print(word)
        if word in using_word or word[0] != last_alphabet:
            return [i % n + 1, i // n + 1]

        using_word.append(word)
        last_alphabet = word[-1]

    return [0, 0]

# 쉬운 문제