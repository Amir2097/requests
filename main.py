import requests

response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
page = response.json()
superhero_list = ['Hulk', 'Captain America', 'Thanos']
hero_dict = {}

for superhero_dict in page:
    for name_superhero in superhero_list:
        if superhero_dict['name'] == name_superhero:
            intelligence_hero = superhero_dict['powerstats']['intelligence']
            hero_dict[superhero_dict['name']] = intelligence_hero

max_intelligence_hero = max(hero_dict.values())

for hero_name, hero_intell in hero_dict.items():
    if max_intelligence_hero == hero_intell:
        print(f'Самый умный супергерой с интеллектом {max_intelligence_hero} является: {hero_name}')


API_TOKEN = ""

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _upload_link(self, file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, file_path, filename):
        response_link = self._upload_link(file_path=file_path)
        href = response_link.get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print("Complete")


if __name__ == '__main__':
    ya = YaUploader(token=API_TOKEN)
    ya.upload('Netology/test.txt', 'test.txt')
