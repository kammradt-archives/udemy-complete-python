def main():
    file = open('newfile.txt', 'w+')
    text = 'This is my text'

    file.write(text)


if __name__ == '__main__':
    main()
