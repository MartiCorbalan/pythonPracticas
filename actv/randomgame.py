import random

def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('you are a genius')
            return True
        else:
            print('hey, i say 1 to 10')
            return False
#generate number 1 to 10

#input from user

#chck that input is a number 1 to 10
if __name__ == '__main__':
    answer = random.randint(1,10)
    while True:
        try:
            guess = int(input('guess a number 1 to 10: '))
            if (run_guess(guess, answer)):
                break
        except ValueError:
            print('please enter a number')
            continue
    #check if number is right guess. otherwise ask again
