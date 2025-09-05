import requests
import os
import hashlib
import mimetypes
from urllib.parse import urlparse, unquote
from pathlib import Path
import time
from typing import List, Optional


class UbuntuImageFetcher:
    """
    A respectful image fetcher that embodies Ubuntu principles
    """
    
    def __init__(self, download_dir: str = "Fetched_Images"):
        self.download_dir = Path(download_dir)
        self.downloaded_hashes = set()
        self.session = requests.Session()
        # Set a respectful User-Agent
        self.session.headers.update({
            'User-Agent': 'Ubuntu-Image-Fetcher/1.0 (Educational Purpose; Respectful Bot)'
        })
        
        self.download_dir.mkdir(exist_ok=True)
        
        self._load_existing_hashes()
    
    def _load_existing_hashes(self):
        """Load hashes of existing images to prevent duplicates"""
        hash_file = self.download_dir / ".image_hashes.txt"
        if hash_file.exists():
            try:
                with open(hash_file, 'r') as f:
                    self.downloaded_hashes = set(line.strip() for line in f)
                print(f"📝 Loaded {len(self.downloaded_hashes)} existing image hashes")
            except Exception as e:
                print(f"⚠️ Could not load existing hashes: {e}")
    
    def _save_hash(self, file_hash: str):
        """Save hash of downloaded image"""
        hash_file = self.download_dir / ".image_hashes.txt"
        try:
            with open(hash_file, 'a') as f:
                f.write(f"{file_hash}\n")
            self.downloaded_hashes.add(file_hash)
        except Exception as e:
            print(f"⚠️ Could not save hash: {e}")
    
    def _get_file_hash(self, content: bytes) -> str:
        """Generate MD5 hash of file content"""
        return hashlib.md5(content).hexdigest()
    
    def _validate_image_headers(self, response: requests.Response) -> tuple[bool, str]:
        """
        Validate HTTP headers to ensure we're downloading an image
        Returns: (is_valid, message)
        """
        content_type = response.headers.get('Content-Type', '').lower()
        content_length = response.headers.get('Content-Length')
        
        if not content_type.startswith('image/'):
            return False, f"Content-Type '{content_type}' is not an image"
        

        if content_length:
            try:
                size_mb = int(content_length) / (1024 * 1024)
                if size_mb > 50:
                    return False, f"Image too large ({size_mb:.1f}MB). Limit: 50MB"
            except ValueError:
                pass
        
        return True, "Headers validated successfully"
    
    def _generate_filename(self, url: str, content_type: str) -> str:
        """
        Generate appropriate filename from URL and content type
        """
        parsed_url = urlparse(url)
        filename = os.path.basename(unquote(parsed_url.path))
        
        if not filename or '.' not in filename:
            # Get file extension from content type
            extension = mimetypes.guess_extension(content_type)
            if not extension:
                extension = '.jpg'  # Default fallback
            
            # Create filename with timestamp
            timestamp = int(time.time())
            filename = f"ubuntu_image_{timestamp}{extension}"
        
        # Ensure filename is safe
        filename = "".join(c for c in filename if c.isalnum() or c in '.-_')
        return filename
    
    def fetch_image(self, url: str) -> bool:
        """
        Fetch a single image with Ubuntu principles
        Returns: True if successful, False otherwise
        """
        print(f"\n🌐 Connecting to: {url}")
        
        try:
            # Send HEAD request first to check headers (respectful approach)
            head_response = self.session.head(url, timeout=10, allow_redirects=True)
            head_response.raise_for_status()
            
            # Validate headers
            is_valid, message = self._validate_image_headers(head_response)
            if not is_valid:
                print(f"❌ {message}")
                return False
            
            print(f"✅ {message}")
            
            # Now fetch the actual content
            print("📥 Downloading image...")
            response = self.session.get(url, timeout=30, stream=True)
            response.raise_for_status()
            
            # Get content
            content = response.content
            
            # Check for duplicates
            file_hash = self._get_file_hash(content)
            if file_hash in self.downloaded_hashes:
                print("🔄 Image already exists (duplicate detected)")
                return True
            
            # Generate filename
            content_type = response.headers.get('Content-Type', 'image/jpeg')
            filename = self._generate_filename(url, content_type)
            filepath = self.download_dir / filename
            
            # Handle filename conflicts
            counter = 1
            original_filepath = filepath
            while filepath.exists():
                stem = original_filepath.stem
                suffix = original_filepath.suffix
                filepath = self.download_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            
            # Save the image
            with open(filepath, 'wb') as f:
                f.write(content)
            
            # Save hash for duplicate prevention
            self._save_hash(file_hash)
            
            # Success message
            size_mb = len(content) / (1024 * 1024)
            print(f"✅ Successfully fetched: {filename}")
            print(f"📁 Saved to: {filepath}")
            print(f"📊 Size: {size_mb:.2f}MB")
            print("🤝 Connection strengthened. Community enriched.")
            
            return True
            
        except requests.exceptions.Timeout:
            print("⏰ Request timed out - the community is busy")
        except requests.exceptions.ConnectionError:
            print("🔌 Connection error - check your network")
        except requests.exceptions.HTTPError as e:
            print(f"🚫 HTTP error {e.response.status_code}: {e}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Request error: {e}")
        except OSError as e:
            print(f"💾 File system error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
        
        return False
    
    def fetch_multiple_images(self, urls: List[str]) -> dict:
        """
        Fetch multiple images with respectful delays
        Returns: Dictionary with results
        """
        results = {"successful": 0, "failed": 0, "total": len(urls)}
        
        print(f"\n🚀 Starting Ubuntu Image Fetching Session")
        print(f"📋 Processing {len(urls)} URLs")
        print("⏱️  Adding respectful delays between requests...\n")
        
        for i, url in enumerate(urls, 1):
            print(f"--- Processing {i}/{len(urls)} ---")
            
            success = self.fetch_image(url.strip())
            
            if success:
                results["successful"] += 1
            else:
                results["failed"] += 1
            
            # Respectful delay between requests (Ubuntu principle of respect)
            if i < len(urls):
                print("⏸️  Pausing respectfully...")
                time.sleep(2)
        
        return results


def main():
    """Main function implementing the Ubuntu Image Fetcher"""
    print("=" * 60)
    print("🌍 Welcome to the Ubuntu Image Fetcher 🌍")
    print("A tool for mindfully collecting images from the web")
    print('"I am because we are" - Ubuntu Philosophy')
    print("=" * 60)
    
    fetcher = UbuntuImageFetcher()
    
    while True:
        print("\n🔧 Choose your approach:")
        print("1. Fetch a single image")
        print("2. Fetch multiple images (one per line)")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            url = input("\n🔗 Please enter the image URL: ").strip()
            if url:
                fetcher.fetch_image(url)
            else:
                print("❌ Please provide a valid URL")
        
        elif choice == '2':
            print("\n📝 Enter image URLs (one per line, empty line to finish):")
            urls = []
            while True:
                url = input().strip()
                if not url:
                    break
                urls.append(url)
            
            if urls:
                results = fetcher.fetch_multiple_images(urls)
                print(f"\n📊 Session Summary:")
                print(f"✅ Successful: {results['successful']}")
                print(f"❌ Failed: {results['failed']}")
                print(f"📋 Total: {results['total']}")
                print("\n🤝 Ubuntu spirit maintained through respectful fetching")
            else:
                print("❌ No URLs provided")
        
        elif choice == '3':
            print("\n🙏 Thank you for using Ubuntu Image Fetcher")
            print("May the spirit of Ubuntu guide your digital journey")
            break
        
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3")


if __name__ == "__main__":
    main()
