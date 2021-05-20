import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + 'password123'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':')for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
        return 0


def pwned_api_check(password):
    #check passowrd if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    #sha1password = hashlib.sha1(password.encode('utf-8'))
    first5_char, tail = sha1password[:5], sha1password[5:]
    respon = requests_api_data(first5_char)
    print(response)
    return get_password_leaks_count(respon, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{passowrd} was found {count} times... you should probably change your password')
        else:
            print(f'{password} was NOT found. Carry on!')
    return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))