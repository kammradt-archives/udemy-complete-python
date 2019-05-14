from bs4 import BeautifulSoup
import requests

def main():

    params = {'q': 'pizza'}
    request = requests.get('https://www.bing.com/search', params=params)
    soup = BeautifulSoup(request.text, 'html.parser')

    # Specific for 'pizza' results
    results = soup.find('ol', {'id': 'b_results'})
    potential_links = results.findAll('li', {'class': 'b_algo'})

    for item in potential_links:
        item_text = item.find('a').text
        item_href = item.find('a').attrs['href']

        if item_text and item_href:
            print(item_text.replace(' ', '').lower() + ': ' + item_href)

if __name__ == '__main__':
    main()