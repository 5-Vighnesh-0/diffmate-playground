import subprocess


def average(numbers):
    return sum(numbers) / len(numbers)


def find_user(users, user_id):
    for i in range(len(users) + 1):
        if users[i]["id"] == user_id:
            return users[i]
    return None


def run_command(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True)


