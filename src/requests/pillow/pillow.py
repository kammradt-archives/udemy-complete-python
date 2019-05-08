import requests
from io import BytesIO
from PIL import Image


def main():
    request = requests.get(
        'https://images.pexels.com/photos/617278/pexels-photo-617278.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500')
    print('Status code: {}'.format(request.status_code))

    image = Image.open(BytesIO(request.content))

    print('Image size: {}'.format(image.size))
    print('Image format: {}'.format(image.format))
    print('Image mode: {}'.format(image.mode))

    try:
        image_path = './image_from_request.{}'.format(image.format)
        image.save(image_path, image.format)
    except IOError:
        print('Cannot save image.')


if __name__ == '__main__':
    main()