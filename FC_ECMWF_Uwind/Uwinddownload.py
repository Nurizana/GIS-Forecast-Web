import os
import requests
from bs4 import BeautifulSoup

def download_u_wind():
    # URL for U wind data
    url = "http://hpfx.collab.science.gc.ca/~swpm001/WP-MIP/forecasts/oic/ecmf/pm_00/u/"
    save_dir = "FC_ECMWF_Uwind"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all .grib2 files
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.endswith('.grib2'):
            file_url = url + href
            file_path = os.path.join(save_dir, href)
            
            print(f"Downloading {href}...")
            # Stream the download and overwrite if it exists
            with requests.get(file_url, stream=True) as r:
                r.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): 
                        f.write(chunk)
            print(f"Saved to {file_path}")

if __name__ == "__main__":
    download_u_wind()
