import time
import psutil
import asyncio

class PasswordCracker:
    def __init__(self, correct_password, password_files):
        self.correct_password = correct_password
        self.password_list = self.load_passwords(password_files)

    def load_passwords(self, filenames):
        passwords = []
        for filename in filenames:
            with open(filename, 'r', encoding="utf8", errors='ignore') as file:
                passwords.extend([line.strip() for line in file])
        return passwords

    def check_password(self, given_password):
        return given_password == self.correct_password

    async def crack_password(self):
        start_time = time.time()
        start_cpu_usage = psutil.cpu_percent(interval=None)

        found_password = None
        number_of_attempts = 0

        for password in self.password_list:
            number_of_attempts += 1
            if self.check_password(password):
                found_password = password
                print(f"\nCracked the password: {found_password} after {number_of_attempts} attempts.")
                break
            if number_of_attempts % 1000 == 0:
                print(f"\rAttempted {number_of_attempts:,} times", end="")
        if not found_password:
            print("\nPassword not found")

        end_time = time.time()
        end_cpu_usage = psutil.cpu_percent(interval=None)
        time_taken = end_time - start_time
        cpu_usage = end_cpu_usage - start_cpu_usage

        print("Duration: ", time_taken , " secs")
        print("CPU usage: ", cpu_usage, " %")

async def main():
    secret_password = input("Enter your password: ")
    password_files = input("Enter the paths to your password files, separated by a comma: ").split(",")
    cracker = PasswordCracker(secret_password, password_files)
    await cracker.crack_password()

asyncio.run(main())