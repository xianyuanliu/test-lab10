import os
import requests

def download_pykale(save_dir):
    url = "https://github.com/pykale/pykale/archive/refs/heads/main.zip"
    response = requests.get(url)
    
    if response.status_code == 200:
        os.makedirs(save_dir, exist_ok=True)
        file_path = os.path.join(save_dir, "pykale-main.zip")
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"PyKale has been downloaded and saved to {file_path}")
    else:
        print("Failed to download PyKale")
