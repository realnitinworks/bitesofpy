import random 


MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        try:
            guess_number = int(input(f"Guess a number between {START} and {END}"))
        except ValueError:
            print("Should be a number")
            raise ValueError('Should be a number')
        except TypeError:
            print("Please enter a number")
            raise ValueError("Please enter a number")
        else:
            if not START <= guess_number <= END:
                print("Number not in range")
                raise ValueError("Number not in range")

        if guess_number in self._guesses:
            print("Already guessed")
            raise ValueError("Already guessed")

        self._guesses.add(guess_number)
        return guess_number

    def _validate_guess(self, guess):
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""

        if self._answer == guess:
            print(f"{guess} is correct!")
            return True
        elif guess < self._answer:
            print(f"{guess} is too low")
        else:
            print(f"{guess} is too high")
        return False

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while len(self._guesses) < MAX_GUESSES:
            try:
                guess_number = self.guess()
            except ValueError:
                continue

            if self._validate_guess(guess_number):
                self._win = True
                break

        if not self._win:
            print(f"Guessed {MAX_GUESSES} times, answer was {self._answer}")


if __name__ == '__main__':
    game = Game()
    game()
