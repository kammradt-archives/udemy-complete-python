import requests


def main():
    value = input('What do you want to search? ')
    params = {'q': value}

    response = requests.get('http://google.com/search', params=params)
    print(response.url)


if __name__ == '__main__':
    main()
