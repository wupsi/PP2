from collections import Counter

word, cnt = input(), 0
word_amount = dict(Counter(word))

if word != word[::-1]:
    print('NotPalindrome')

else: 
    for i in word_amount.values():
        if i % 2 == 1:
            cnt += 1

    print('NotGoodPalindrome' if cnt == 1 else 'GoodPalindrome')