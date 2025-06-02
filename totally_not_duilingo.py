import random
from fuzzywuzzy import fuzz

def main():
    translations = {
        "hello": ["konnichiwa", "yaho", "osu", "yo"],
        "cat": ["neko"],
        "power": ["chikara", "pawa"],
        "family": ["kazoku"],
        "magic": ["maho", "majutsu"],
        "ice cream": ["aisu kuriimu", "aisu"],
        "strong": ["tsuyoi", "jobu", "katai"],
        "water": ["mizu"],
        "bag": ["kaban", "baggu"],
        "dad (my dad)": ["chichi", "otosan", "oyaji"],
        "mom (my mom)": ["haha", "okasan", "okaachan"],
        "umbrella": ["kasa"],
        "I": ["watashi", "boku", "ore", "atashi"],
        "dumb": ["baka", "baaka", "aho"],
        "please": ["kudasai", "onegai"],
        "good/nice": ["ii", "yoi", "suteki"],
        "phone": ["sumaho", "denwa", "keitai"],
        "bye": ["jaane", "sayonara", "mata ne", "bai bai"]
    }
    score = 0
    streak = 0
    mistakes = []
    corrected_mistakes = []

    my_list = ['hello', 'cat', 'power', 'family', 'magic', 'ice cream', 'strong', 'water', 'bag', 'dad (my dad)',
    'mom (my mom)', 'umbrella', 'I', 'dumb', 'please', 'good/nice', 'phone', 'bye']
    print('welcome to totally not duolingo! Here you can practice your japanese skills and come out stronger!!')
    print()
    print('if you are new to Japanese its recommended to take a look at list of words and their translations that you are going to be quizzed on by saying practice.')
    print()
    print('but if you decide you are too good for that you can hop straight into it by saying quizz.')
    print()
    user_choice = input().strip().lower()
    if user_choice == 'practice':
        for word, translation_list in translations.items():
            print(f"{word}: {', '.join(translation_list)}")
        print()
        user_choice = input('wanna give it a try now? say quizz!').strip().lower()
    else:
        while user_choice not in ['practice', 'quizz']:

            user_choice = input('Please enter a valid choice -  either "practice" or "quizz".')
    if user_choice == 'quizz':
        for i in range (1000):
            print()
        while my_list:
            match = False
            perfect_match = False
            random_word = random.randint(0, len(my_list) - 1)
            x = my_list.pop(random_word)
            translation = translations.get(x)

            if isinstance(translation, str):
                translation = [translation]

            users_answer = input(f'What is the Japanese translation/pronunciation for {x}? ')
            if users_answer.strip().lower() in [word.lower() for word in translation]:
                perfect_match = True
            for word in translation:
                if fuzz.ratio(word.lower(), users_answer.lower()) > 70:
                    match = True
                    break


            if perfect_match:
                print('That is correct!')
                print()
                score += 1
                streak += 1
                if streak%5 == 0:
                    print(f"Congratulations! You guessed {streak} in row!")
                    print()
            elif match :
                print(f'Correct, but misspelled, correct answer was: {", or ".join(translation)}')
                print()
                score += 1
                streak += 1
            else:
                print(f'That is incorrect, the Japanese translation/pronunciation for {x} is {", or ".join(translation)}.')
                print()
                mistakes.append(x)
                streak = 0

        print(f'You got {score}/18 words correct, come study again soon!')
        print()
        while mistakes:
            user_retry = input('wanna correct your mistake(s)? then type "retry".')
            if user_retry == 'retry':
                print("Correct the mistake(s): ")
                mistakes_amount = len(mistakes)
                while mistakes:
                    random.shuffle(mistakes)
                    x = mistakes.pop()
                    translation = translations.get(x)  # FIXED
                    match = False  # FIXED
                    perfect_match = False  # FIXED

                    users_answer = input(f'What is the Japanese translation/pronunciation for {x}? ')

                    if users_answer.strip().lower() in [word.lower() for word in translation]:
                        perfect_match = True

                    for word in translation:
                        if fuzz.ratio(word.lower(), users_answer.lower()) > 70:
                            match = True
                            break

                    if perfect_match:
                        print('That is correct!')
                        print()
                        corrected_mistakes.append(x)

                    elif match:
                        print(f'Correct, but misspelled, correct answer was: {", or ".join(translation)}')
                        print()
                        corrected_mistakes.append(x)

                    else:
                        print(
                            f'That is incorrect, the Japanese translation/pronunciation for {x} is {", or ".join(translation)}.')
                        print()

                corrected_mistakes_amount = len(corrected_mistakes)
                if corrected_mistakes_amount == mistakes_amount:
                    print("Congratulations! You've corrected all your mistake(s)!")
                else:
                    print(f"You corrected {corrected_mistakes_amount}/{mistakes_amount} mistakes. Keep practicing!")






    else:
        print('Please enter a valid choice -  either "practice" or "quizz".')

    users_end = input('if you wish to end the code please press "enter", or if you wish to restart, please submit ".".')
    if users_end == '':
        print('Goodbye!')
    if users_end == '.':
        for i in range(100):
            print()
        main()


if __name__ == '__main__':
    main()
