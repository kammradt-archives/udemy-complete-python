import simplejson as json
import os


def main():
    exist = os.path.isfile('file.json')

    if exist:
        file = open('file.json', 'r+')
        data = json.loads(file.read())
        people = data.get('people')

        for person in people:
            print(person)

    else:
        new_file = open('file.json', 'w+')
        data = {
          "people": [
            {
              "name": "Vinicius",
              "age": 19,
              "salary": 1000.0
            },
            {
              "name": "Kammradt",
              "age": 20,
              "salary": 2000.0
            },
            {
              "name": "Jose",
              "age": 10,
              "salary": 0
            },
            {
              "name": "Maria",
              "age": 30,
              "salary": 6000.0
            },
            {
              "name": "Fernanda",
              "age": 25,
              "salary": 10000.0
            }
          ]
        }
        new_file.write(json.dumps(data))


if __name__ == '__main__':
    main()
