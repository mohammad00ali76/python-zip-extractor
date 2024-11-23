import zipfile
import os

def extract_zip(zip_file_path, extract_to):
    # Check if the zip file exists
    if not os.path.exists(zip_file_path):
        print(f"The file {zip_file_path} does not exist.")
        return

    # Create the extraction directory if it doesn't exist
    os.makedirs(extract_to, exist_ok=True)

    # Extract the zip file
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    print(f"Extracted {zip_file_path} to {extract_to}")

# Example usage
zip_file_path = r'D:\dars\book1\nazaryeh.zip'  # Replace with your zip file path
extract_to = r'D:\dars\book1'  # Replace with your extraction directory
extract_zip(zip_file_path, extract_to)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
