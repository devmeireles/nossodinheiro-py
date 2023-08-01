import os
import zipfile
import requests


def download_and_extract_file(url, output_dir="."):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Extract the filename from the URL
    filename = url.split("/")[-1]

    # Download the file
    file_path = os.path.join(output_dir, filename)
    with requests.get(url, stream=True) as response:
        response.raise_for_status()
        with open(file_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

    # Extract the contents of the zip file
    with zipfile.ZipFile(file_path, "r") as zip_ref:
        zip_ref.extractall(output_dir)

    # Remove the zip file after extraction
    os.remove(file_path)
