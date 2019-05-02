import requests


def main():
    r = requests.get("http://google.com/")
    print(r.text)


if __name__ == '__main__':
    main()
