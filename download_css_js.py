import os
import csv
import requests
from urllib.parse import urlparse
from random import randint
from time import sleep

def download_file(url, output_dir):
    # Parse URL to extract path
    parsed_url = urlparse(url)
    path = parsed_url.path

    # Remove leading slash if present
    if path.startswith('/'):
        path = path[1:]

    # Create directories if they don't exist
    download_dir = os.path.join(output_dir, os.path.dirname(path))
    os.makedirs(download_dir, exist_ok=True)

    # Extract filename from URL
    filename = os.path.basename(path)

    # Download file
    response = requests.get(url)
    if response.status_code == 200:
        # Write file to disk
        with open(os.path.join(download_dir, filename), 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

def main():
    # Current working directory
    current_dir = os.getcwd()

    # Paths to CSV files
    js_csv_path = 'js_files.txt'
    css_csv_path = 'css_files.txt'
    # Output directories
    output_dir = os.path.join(current_dir, 'downloaded')

    # Process CSS URLs
    print("Processing CSS files...")
    with open(css_csv_path, 'r', encoding='utf-8-sig') as css_file:
        reader = csv.reader(css_file)
        for row in reader:
            print("Processing:", row[0])
            download_file(row[0], output_dir)

    # Process JavaScript URLs
    print("\nProcessing JavaScript files...")
    with open(js_csv_path, 'r', encoding='utf-8-sig') as js_file:
        reader = csv.reader(js_file)
        for row in reader:
            print("Processing:", row[0])
            download_file(row[0], output_dir)
            
if __name__ == "__main__":
    main()
