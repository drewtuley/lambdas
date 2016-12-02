import math
import string
from itertools import combinations
from functools import reduce
import operator
import time


def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n) + 1)):
        if n != x and n % x == 0:
            return False
    return True

start=time.time()
primes = [p for p in range(3, 150) if is_prime(p)]


def calculate_prime_value(string_value):
    prod = -1
    for l in string_value:
        try:
            idx = string.ascii_lowercase.index(l)
            prime_value = primes[idx]
        except Exception:
            # print('Trouble with: {} in {} because {}'.format(l, str, ex))
            prime_value = 0
        if prod < 0:
            prod = prime_value
        else:
            prod *= prime_value
    return prod


# reverse lookup dictionary - anagrams with same value keyed by value
anagram_primes_reverse = [{}, {}, {}, {} ,{}]
min_prime = 100
max_prime = 0
prime_pots = [0, 0, 0, 0, 0]

with open('brit-a-z.txt') as fd:
    complete = False
    loaded_words = []
    while not complete:
        try:
            for line in fd:
                word = line.strip()
                if "'" not in word and word not in loaded_words:
                    loaded_words.append(word)
                    prime = calculate_prime_value(word)
                    if prime != 0:
                        # print('{} {}'.format(word, prime))
                        if prime > max_prime:
                            max_prime = prime
                        if -1 < prime < min_prime:
                            min_prime = prime
                        prime_idx = ((prime % 10)-1)/2
                        pot = prime_pots[prime_idx]
                        pot += 1
                        prime_pots[prime_idx] = pot
                        if prime in anagram_primes_reverse[prime_idx]:
                            words = anagram_primes_reverse[prime_idx][prime]
                            words.append(word)
                        else:
                            words = list()
                            words.append(word)
                        anagram_primes_reverse[prime_idx][prime] = words
        except UnicodeDecodeError as err:
            print('error {} '.format(err))
            pass
        else:
            complete = True

print('prime range: min {} max {}'.format(min_prime, max_prime))
for idx in prime_pots:
    print('{}'.format(idx))

with open('anagrams_reverse.py', 'w') as fd:
    fd.write("import time\nstart = time.time()\n")
    idx=1
    dict_names=[]
    for reverse in anagram_primes_reverse:
        dict_name = 'anagram_primes_{}'.format(idx)
        fd.write('{}={}\n'.format(dict_name, reverse))
        dict_names.append(dict_name)
        idx += 1
    fd.write('anagram_primes_reverse=[{}]\n'.format(",".join(dict_names)))
    fd.write("\nend = time.time()\n")
    fd.write("print('start {} end {} duration {}'.format(start, end, end-start))\n")


end=time.time()
print('start={} end={} elapsed={}'.format(start, end, end-start))