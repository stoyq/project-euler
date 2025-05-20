import time
from datetime import datetime

# first let's define some common words
words = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            100: 'one hundred',
            1000: 'one thousand'
            }

# Precondition:   1 <= n <= 1000
# Post-condition: Return British English equivalent, along with number of letters
def countLetters(n):
    # check if it's pre-defined
    if n in words:
        return words[n], len(''.join(words[n].split()))

    # rule for 21 to 99
    elif n >= 21 and n <= 99:
        tens = 10 * (n // 10)
        ones = n % 10

        english = words[tens] + " " + words[ones]
        return english, len(''.join(english.split()))

    # rule for 101 to 999
    elif n >= 101 and n <= 999:
        huns = n // 100
        remainder = n % 100

        if remainder == 0:
            english = words[huns] + " hundred"
            return english, len(''.join(english.split()))
        
        else:
            a, b = countLetters(remainder)

            english = words[huns] + " hundred and " + a
            return english, len(''.join(english.split()))


    else:
        return "********************************** invalid", -1

# rules for 



def main():
    total = 0
    for i in range(1, 1001):
        english, num_letters = countLetters(i)
        print(i,":",english,",",num_letters)
        total += num_letters
    
    print("total",total)

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    now = datetime.now()
    print()
    print("Last ran:", now.strftime("%H:%M"))
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.6f} seconds")
