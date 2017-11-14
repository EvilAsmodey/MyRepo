import random
import math


class RSAEncDec(object):

    def __init__(self, bit_length = 32):
        for bit in range(bit_length, 2, -1):
            try:
                p, q = self._find_primes(bit)
                #public key
                self.n = p * q
                #exponent
                self.e = self._find_exponent((p - 1) * (q - 1))
                #primary key
                self.d = self._find_private_key((p - 1) * (q - 1), self.e)
                break
            except:
                pass

    def get_max_value_to_encrypt(self):
        return self.n - 1
        
    def get_public_key(self):
        return (self.n, self.e)
    
    def get_private_key(self):
        return (self.n, self.d)
        
    def encrypt(self, message):
        return pow(message, self.e, self.n)
        
    def decrypt(self, message):
        return pow(message, self.d, self.n)


    def _get_primes(self, begin, end):
        if end <= begin:
                return []
        primes_number = [2]

        #find all primes number from 3 (prime number '2' already in array) to last range element
        for prime_candidate in range(3, end + 1, 2):
            is_prime = True
            for already_prime in primes_number:
                if prime_candidate % already_prime == 0:
                    is_prime = False
                    break
            if is_prime:
                primes_number.append(prime_candidate)

        #delete all prime number that less that begin range element
        while primes_number and primes_number[0] < begin:
            del primes_number[0]

        return primes_number

    def _are_primes_relatively(self, first_prime, second_prime):
        min_prime = min(first_prime, second_prime)
        for value in range(2, int(math.sqrt(min_prime)) + 1):
            if first_prime % value == second_prime % value == 0:
                return False
        return True

    def _find_primes(self, bit_length):
        #f.e bit_length = 8, then public key must be in range:
        #n_min = 1 << 7 = 128
        #n_max = 1 << 8 - 1 = 255
        
        n_min = 1 << (bit_length - 1)
        n_max = (1 << bit_length) - 1

        #so, primes must be in range for this case: [8, 32]
        begin_range = 1 << (bit_length // 2 - 1)
        end_range = 1 << (bit_length // 2 + 1)
        prime_numbers = self._get_primes(begin_range, end_range)

        #random check two prime number
        while prime_numbers:
            p = random.choice(prime_numbers)
            prime_numbers.remove(p)
            q_candidates = [q for q in prime_numbers if n_min <= p * q <= n_max]
            if q_candidates:
                q = random.choice(q_candidates)
                return p, q


    def _find_exponent(self, max_value):
        for e in range (3, max_value, 2):
            if self._are_primes_relatively(e, max_value):
                return e

    def _find_private_key(self, max_value, exp):
        for d in range(3, max_value, 2):
            if d * exp % max_value == 1:
                return d


    
