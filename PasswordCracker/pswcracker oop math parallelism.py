import itertools
import string
import time
import psutil
import math
import asyncio

class PasswordCracker:
    def __init__(self, correct_password):
        self.correct_password = correct_password
        self.characters = string.printable[:-5]

    def generate_permutations(self):
        return (itertools.product(self.characters, repeat=len)
                for len in range(1, len(self.correct_password) + 1))

    def check_password(self, given_password):
        return ''.join(given_password) == self.correct_password

    def skip_unlikely_permutations(self, length):
        return len(self.characters)**(length-1)

    async def crack_password(self):
        start_time = time.time()
        start_cpu_usage = psutil.cpu_percent(interval=None)

        permutations = self.generate_permutations()

        found_password = None
        number_of_attempts = 0

        for set_of_permutations in permutations:
            length_of_permutation = len(next(iter(set_of_permutations)))
            if math.log10(self.skip_unlikely_permutations(length_of_permutation)) > len(self.correct_password):
                number_of_attempts += self.skip_unlikely_permutations(length_of_permutation)
                continue
            for permutation in set_of_permutations:
                number_of_attempts += 1
                if self.check_password(permutation):
                    found_password = ''.join(permutation)
                    print(f"\nCracked the password: {found_password} after {number_of_attempts} attempts.")
                    break
                if number_of_attempts % 1000 == 0:
                    print(f"\rAttempted {number_of_attempts:,} times", end="")
            if found_password:
                break

        end_time = time.time()
        end_cpu_usage = psutil.cpu_percent(interval=None)
        time_taken = end_time - start_time
        cpu_usage = end_cpu_usage - start_cpu_usage

        print("Duration: ", time_taken , " secs")
        print("CPU usage: ", cpu_usage, " %")


async def main():
    secret_password = input("Enter your password: ")
    cracker = PasswordCracker(secret_password)
    await cracker.crack_password()

asyncio.run(main())