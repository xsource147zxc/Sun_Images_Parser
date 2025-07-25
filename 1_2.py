import json
import requests
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
save_to_folder="IMG"
os.makedirs(save_to_folder, exist_ok=True)

def get_file_link(json):
    links_fnames = {}
    for i in range(len(json["data"])):
        url = json["url"]
        path = json["data"][i]["path"]
        fname = json["data"][i]["fname"]
        file_link = url+path+fname
        links_fnames[file_link] = fname
    return links_fnames

def download_file(dict1):
    for i in dict1.items():
        link, fname = i
        r = requests.get(link, stream=True)
        file_path = os.path.join(script_dir,save_to_folder,fname)
        with open(file_path, 'wb') as file_data:
            for chunk in r.iter_content(chunk_size=128):
                file_data.write(chunk)
            print(f"Скачан файл {fname}")


json1 = requests.get('https://xras.ru/txt/sun_RAL5_171.json').json()
download_file(get_file_link(json1))
print("Загрузка изображений завершена!")
