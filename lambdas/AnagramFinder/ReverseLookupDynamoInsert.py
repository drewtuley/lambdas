import math
import string
import time
import boto3


def is_prime(n):
    if n > 2 and n % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(n) + 1)):
        if n != x and n % x == 0:
            return False
    return True


start = time.time()
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
anagram_primes_reverse = {}
wordlist = 'brit-a-z.txt'
print('Processing word list {}'.format(wordlist))
with open(wordlist) as fd:
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
                        if prime in anagram_primes_reverse:
                            words = anagram_primes_reverse[prime]
                            words.append(word)
                        else:
                            words = list()
                            words.append(word)
                        anagram_primes_reverse[prime] = words
        except UnicodeDecodeError as err:
            print('error {} '.format(err))
            pass
        else:
            complete = True

    print('Connecting to Dynamodb')
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-1',
                              endpoint_url="https://dynamodb.eu-west-1.amazonaws.com")

    table = dynamodb.Table('prime_anagram')

    print('Uploading reverse prime anagrams')
    x = 0
    upload = False
    for reverse in anagram_primes_reverse:
        if upload is False and reverse == 556569:
            upload = True
        if upload is True:
            t1 = time.time()
            response = table.put_item(
                Item={
                    'prime': reverse,
                    'words': ",".join(anagram_primes_reverse[reverse])
                }
            )
            t2 = time.time()
            uploadtime = (t2 - t2) * 1000
            if uploadtime < 200:
                time.sleep((200 - uploadtime) / 1000)
            x += 1
            if x % 100 == 0:
                print('Uploaded {} items'.format(x))

end = time.time()
print('start={} end={} elapsed={}'.format(start, end, end - start))
