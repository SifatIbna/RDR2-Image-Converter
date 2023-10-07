def get_metadata(file_path):
    with open(file_path, "rb") as file:
        data = file.read()
        metadata_bytes = data[20:54]
        metadata_str = "".join([chr(b) for b in metadata_bytes if b > 31])
        date, time = metadata_str.split()
        year, month, day = date.split("/")
        hour, minute, second = time.split(":")
    return f"{year}-{month}-{day} {hour}.{minute}.{second}"

def convert_file(file_path, save_location):
    with open(file_path, "rb") as f:
        data = f.read()
    new_data = data[300:]
    metadata = get_metadata(file_path)
    filename = f"{metadata} PRDR.jpg"
    save_path = os.path.join(save_location, filename)
    with open(save_path, "wb") as f:
        f.write(new_data)
    return save_path

if __name__ == "__main__":
    file_path = input("Enter the path to the PRDR file: ").strip()
    save_location = input("Enter the directory to save the converted JPG: ").strip()

    save_path = convert_file(file_path, save_location)
    print(f"Conversion completed! JPG saved at: {save_path}")
