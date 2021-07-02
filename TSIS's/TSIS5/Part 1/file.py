from itertools import islice
from itertools import count
from collections import Counter
import os
import random
import os.path

# Enter requests
print('\nWorking with a file.')
print('1. Read file.')
print('2. Read first n lines.')
print('3. Add text to file.')
print('4. Read last n lines.')
print('5. Read a file and save to list.')
print('6. Read a file and save to a variable.')
print('7. Read a file and save to an array.')
print('8. Find the longest word.')
print('9. Number of lines in the file.')
print('10. Number of words in a file.')
print('11. Check file size.')
print('12. Write a list to a file.')
print('13. Copy the contents of a file to another file.')
print('14. Combine each line from first file with the corresponding line in second file.')
print('15. Read a random line from a file.')
print('16. Checking for file existence.')
print('17. Remove newline characters from a file.')
print('18. Find number of words in file.')
print('19. Create a list with all words from the text.')
print('20. Create 26 txt files named A-Z.txt.')
print('21. Create a file where all letters of English alphabet are listed by n number of letters on each line.')
print('\nEnter your request(number):')

Request_number = input()

if Request_number.isdigit():
    Request_number = int(Request_number)
else:
    print('Wrong input. Try again.')
    exit()

if Request_number > 21 or Request_number < 1:
    print('Wrong input. Try again.')
else:
    def cnt_line():
        with open('raw.txt') as txt:
            cnt = 0
            for line in txt:
                cnt += 1
        return cnt

    # Read files
    if Request_number == 1:
        print(open('raw.txt').read())

    # Read first n lines
    if Request_number == 2:
        print('Enter n:')
        with open('raw.txt') as start:
            for line in islice(start, int(input())):
                print(line)

    # Add text to file
    if Request_number == 3:
        print('Enter your txt:')
        with open('raw.txt', 'a') as txt:
            txt.write('\n' + input())
        with open('raw.txt') as txt:
            print('\n' + txt.read())

    # Read last n lines
    if Request_number == 4:
        print('Enter n:')
        n = int(input())

        with open('raw.txt') as end:
            for line in islice(end, cnt_line() - n, cnt_line()):
                print(line, end='')

    # Read a file and save to list
    if Request_number == 5:
        with open('raw.txt') as txt:
            txt_list = []
            for line in txt:
                txt_list += line.split('\n')
        print(txt_list)

    # Read a file and save to a variable
    if Request_number == 6:
        with open('raw.txt') as txt:
            print(txt.readlines())

    # Read a file and save to an array
    if Request_number == 7:
        with open('raw.txt') as txt:
            arr = []
            for i in txt:
                arr += (i.split('\n'))
                arr = list(filter(None, arr))
        print(arr)

    # Find the longest word
    if Request_number == 8:
        with open('raw.txt') as txt:
            txt_list = []
            first_longest_word = ''
            last_longest_word = ''
            for i in txt:
                i = i.replace(' ', '\n')
                txt_list += i.split('\n')
                txt_list = list(filter(None, txt_list))

            for i in range(len(txt_list)):
                if len(txt_list[i]) > len(first_longest_word):
                    first_longest_word = txt_list[i]

                if len(txt_list[i]) >= len(last_longest_word):
                    last_longest_word = txt_list[i]

        if first_longest_word != last_longest_word:
            print(
                f'First longest word in file: {first_longest_word}\nLast longest word in file: {last_longest_word}')
        else:
            print(f'Longest word in file: {first_longest_word}')

    # Number of lines in the file
    if Request_number == 9:
        print(cnt_line())

    # Number of words in a file
    if Request_number == 10:
        with open('raw.txt') as txt:
            txt_list = []
            cnt_words = 0
            for i in txt:
                i = i.replace(' ', '\n')
                txt_list += i.split('\n')
                txt_list = list(filter(None, txt_list))

            for i in txt_list:
                cnt_words += 1
        print('Number of words in file:', cnt_words, 'words\n')

        with open('raw.txt') as txt:
            for i, j in Counter(txt.read().split()).items():
                print(f'{i}: {j} word')

    # Check file size
    if Request_number == 11:
        print(os.path.getsize('raw.txt'))

    # Write a list to a file
    if Request_number == 12:
        with open('raw.txt', 'a') as txt:
            txt.write('\n' + str(list(map(int, input().split()))))

        with open('raw.txt') as txt:
            print(txt.read())

    # Copy the contents of a file to another file
    if Request_number == 13:
        with open('copy.txt', 'w') as copy_txt:
            with open('raw.txt') as raw_txt:
                copy_txt.write(str(raw_txt.read()))
        with open('copy.txt') as copy_txt:
            print(copy_txt.read())

    # Combine each line from first file with the corresponding line in second file.
    if Request_number == 14:
        with open('copy.txt') as copy, open('raw.txt') as raw:
            for copy_line, raw_line in zip(copy, raw):
                print(copy_line, raw_line, end='')

    #  Read a random line from a file
    if Request_number == 15:
        with open('raw.txt') as raw:
            lines = raw.read().splitlines()
            print(random.choice(lines))

    # Checking for file existence
    if Request_number == 16:
        print('Enter file name:')
        print('File exists!') if os.path.exists(
            input()) else print("File doesn't exists.")

    # Remove newline characters from a file
    if Request_number == 17:
        with open('raw.txt') as raw:
            lines = raw.readlines()
            for i in lines:
                print(i.rstrip('\n'), end=' ')

    # Number of words in file
    if Request_number == 18:
        with open('raw.txt') as txt:
            txt_list = []
            cnt_words = 0
            for i in txt:
                i = i.replace(' ', '\n')
                txt_list += i.split('\n')
                txt_list = list(filter(None, txt_list))

            for i in txt_list:
                cnt_words += 1
        print('Number of words in file:', cnt_words, 'words\n')

    # Create a list with all words from the text
    if Request_number == 19:
        with open('raw.txt') as raw:
            raw_list = []
            for i in raw:
                i = i.replace(' ', '\n')
                raw_list += i.split('\n')
                raw_list = list(filter(None, raw_list))
        print(raw_list)

    # Create 26 txt files named A-Z.txt
    if Request_number == 20:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        if os.path.exists('Letters'):
            pass
        else:
            os.mkdir('Letters')

        for letters in alphabet:
            with open(letters + '.txt', 'w+') as text_file:
                text_file.write(letters)

        for letters in alphabet:
            os.replace(letters + '.txt', 'Letters/' + letters + '.txt')
        print('Files created!')

    # Create a file where all letters of English alphabet are listed by n number of letters on each line.
    if Request_number == 21:
        print('Enter n:')
        n = int(input())

        if os.path.exists('Letters'):
            pass
        else:
            os.mkdir('Letters')

        with open('Letters.txt', 'w') as Letters_file:
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            letters = [alphabet[i:i + n] +
                       "\n" for i in range(0, len(alphabet), n)]
            Letters_file.writelines(letters)

        os.replace('Letters.txt', 'Letters/Letters.txt')
        print('File created!')
