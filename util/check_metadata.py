# Copyright (c) 2025 takotime808

from PIL import Image
from PIL.ExifTags import TAGS
import sys

def print_image_metadata(image_path: str):
    """
    Print EXIF metadata from an image file.

    Parameters
    ----------
    image_path : str
        Path to the image file from which metadata will be extracted.

    Notes
    -----
    - This function uses the Python Imaging Library (Pillow) to read EXIF metadata.
    - If no EXIF metadata is present, a message is printed.
    - Metadata tag names are converted to human-readable strings when possible.
    - Some image formats (e.g., PNG) may not contain EXIF metadata.

    Examples
    --------
    >>> print_image_metadata("example.jpg")
    ImageWidth               : 1920
    ImageLength              : 1080
    DateTime                 : 2025:08:14 15:22:10
    """
    try:
        # Open the image
        image = Image.open(image_path)

        # Extract EXIF data
        exif_data = image._getexif()

        if not exif_data:
            print("No EXIF metadata found.")
            return

        # Loop through EXIF data and print in readable format
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag:25}: {value}")

    except Exception as e:
        print(f"Error reading metadata: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    print_image_metadata(image_path)
