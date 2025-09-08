import os
import requests
from urllib.parse import urlparse
import uuid
import hashlib

# Directory for fetched images
DIRECTORY = "Fetched_Images"
os.makedirs(DIRECTORY, exist_ok=True)

# Maximum file size (e.g., 10 MB for safety)
MAX_FILE_SIZE = 10 * 1024 * 1024


def generate_filename(url, content_type):
    """Extract filename from URL or generate one based on UUID and content type."""
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    if not filename or "." not in filename:
        # Guess extension from content type
        ext = content_type.split("/")[-1] if "/" in content_type else "jpg"
        filename = f"image_{uuid.uuid4().hex}.{ext}"

    return filename


def get_file_hash(content):
    """Generate SHA256 hash of file content to detect duplicates."""
    return hashlib.sha256(content).hexdigest()


def fetch_image(url, existing_hashes):
    """Fetch and save a single image from URL."""
    try:
        # Request image
        response = requests.get(url, timeout=10, stream=True)
        response.raise_for_status()

        # Check headers for content-type
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"⚠️ Skipped (not an image): {url}")
            return

        # Check file size limit
        content_length = response.headers.get("Content-Length")
        if content_length and int(content_length) > MAX_FILE_SIZE:
            print(f"⚠️ Skipped (file too large): {url}")
            return

        # Read content
        content = response.content

        # Duplicate check
        file_hash = get_file_hash(content)
        if file_hash in existing_hashes:
            print(f"⚠️ Skipped duplicate image: {url}")
            return
        existing_hashes.add(file_hash)

        # Generate filename
        filename = generate_filename(url, content_type)
        filepath = os.path.join(DIRECTORY, filename)

        # Save file
        with open(filepath, "wb") as f:
            f.write(content)

        print(f"✅ Image saved: {filepath}")

    except requests.exceptions.MissingSchema:
        print(f"❌ Invalid URL (missing http/https): {url}")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP error {e.response.status_code} for {url}")
    except requests.exceptions.ConnectionError:
        print(f"❌ Connection error for {url}")
    except requests.exceptions.Timeout:
        print(f"❌ Timeout fetching {url}")
    except Exception as e:
        print(f"❌ Unexpected error for {url}: {e}")


def main():
    # Prompt for multiple URLs separated by commas or spaces
    urls = input("Enter image URLs (separated by spaces or commas): ").replace(",", " ").split()
    
    # Track hashes to prevent duplicate downloads
    existing_hashes = set()

    for url in urls:
        fetch_image(url.strip(), existing_hashes)


if __name__ == "__main__":
    main()
