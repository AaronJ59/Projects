

def download_image_data(source: str,
                        destination: str) -> Path:
    """
    Downloads a zip dataset from source and imports/unzips it to destination.

    source (str): Link to the file
    destination (str): Name of the directory that you want the zip file to be unzipped to

    """

    data_path = Path("data/")
    image_path = data_path / destination

    if image_path.is_dir():
      print(f"{image_path} already exists, skipping download")
    else:
      image_path.mkdir(parents=True, exist_ok=True)
      zip_file = Path(source).name
      
      with open(data_path / zip_file, "wb") as f:
        request = requests.get(source)
        print("Writing zip file to data/")
        f.write(request.content)
      
      with zipfile.ZipFile(data_path / zip_file, "r") as zObject:

        zObject.extractall(image_path)

      os.remove(data_path / zip_file) 
