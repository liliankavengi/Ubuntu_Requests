# Ubuntu Image Fetcher 🌍

*"I am because we are" - Ubuntu Philosophy*

A Python tool for mindfully collecting images from the web community, embodying Ubuntu principles of community, respect, sharing, and practicality.

## 🌟 Features

- **Community Connection**: Respectfully connects to the global web community
- **Intelligent Validation**: Checks file types, sizes, and headers before downloading
- **Duplicate Prevention**: MD5 hash tracking prevents re-downloading identical images
- **Batch Processing**: Handle multiple URLs with respectful delays
- **Security First**: Content validation and safe filename handling
- **Graceful Error Handling**: Ubuntu principle of respect in action

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- `requests` library

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/liliankavengi/Ubuntu_Requests.git
   cd Ubuntu_Requests
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program**:
   ```bash
   python ubuntu_image_fetcher.py
   ```

## 🔧 Usage

### Single Image Download
```bash
python ubuntu_image_fetcher.py
# Choose option 1
# Enter image URL when prompted
```

### Multiple Images (Batch)
```bash
python ubuntu_image_fetcher.py
# Choose option 2  
# Enter multiple URLs (one per line)
# Press Enter on empty line to start processing
```

### Example URLs for Testing
- `https://httpbin.org/image/jpeg`
- `https://httpbin.org/image/png`
- `https://picsum.photos/800/600`

## 🏗️ Project Structure

```
Ubuntu_Requests/
├── ubuntu_image_fetcher.py    # Main application
├── requirements.txt           # Python dependencies
├── README.md                 # This file
└── Fetched_Images/           # Created automatically
    └── .image_hashes.txt     # Duplicate prevention tracking
```

## 🤝 Ubuntu Principles Implementation

### 1. Community 🌐
- Connects respectfully to the global web
- Uses proper User-Agent identification
- Supports batch processing for community resource gathering

### 2. Respect 🤝
- Comprehensive error handling without crashes
- Respectful delays between requests (2-second intervals)
- Validates content before downloading
- Graceful handling of server responses

### 3. Sharing 📁
- Organizes images in dedicated directory structure
- Maintains metadata for future reference and sharing
- Prevents wasteful duplicate downloads

### 4. Practicality 🔧
- Addresses real-world security concerns
- File size limits (50MB max)
- Content-Type validation
- Automatic filename generation and conflict resolution

## 🛡️ Security Features

- **Content Validation**: Ensures URLs serve actual images
- **File Size Limits**: Prevents downloading oversized files (50MB limit)
- **Safe Filenames**: Sanitizes filenames to prevent directory traversal
- **Timeout Protection**: Prevents hanging on unresponsive servers
- **Duplicate Detection**: MD5 hash comparison prevents redundant downloads

## 🔍 Advanced Features

### Duplicate Prevention
The system tracks MD5 hashes of downloaded images in `.image_hashes.txt` to prevent downloading the same image multiple times.

### Smart Filename Generation
- Extracts filenames from URLs when available
- Generates timestamped names when URL doesn't contain filename
- Handles filename conflicts with automatic numbering
- Sanitizes filenames for cross-platform compatibility

### Respectful Web Crawling
- Implements 2-second delays between requests
- Uses descriptive User-Agent string
- Validates headers before downloading content
- Handles HTTP errors gracefully

## 🎯 Assignment Completion

This project fulfills all assignment requirements:

✅ **Basic Requirements**
- Prompts user for image URLs
- Creates "Fetched_Images" directory automatically  
- Downloads images using `requests` library
- Handles errors gracefully
- Extracts/generates appropriate filenames
- Saves images in binary mode

✅ **Challenge Questions Addressed**
1. **Multiple URLs**: Batch processing with respectful delays
2. **Security Precautions**: Content validation, size limits, safe filename handling  
3. **Duplicate Prevention**: MD5 hash tracking system
4. **HTTP Headers**: Content-Type and Content-Length validation

✅ **Ubuntu Principles**
- **Community**: Web connectivity and resource sharing
- **Respect**: Error handling and server-friendly requests
- **Sharing**: Organized file structure for future use
- **Practicality**: Real-world security and usability features

## 🤖 Example Session

```
============================================================
🌍 Welcome to the Ubuntu Image Fetcher 🌍
A tool for mindfully collecting images from the web
"I am because we are" - Ubuntu Philosophy
============================================================

🔧 Choose your approach:
1. Fetch a single image
2. Fetch multiple images (one per line)
3. Exit

Enter your choice (1-3): 1

🔗 Please enter the image URL: https://picsum.photos/800/600

🌐 Connecting to: https://picsum.photos/800/600
✅ Headers validated successfully
📥 Downloading image...
✅ Successfully fetched: ubuntu_image_1725552123.jpg
📁 Saved to: Fetched_Images/ubuntu_image_1725552123.jpg  
📊 Size: 0.45MB
🤝 Connection strengthened. Community enriched.
```

## 🛠️ Development

### Requirements
- Python 3.7+
- requests library

### Contributing
This project embodies Ubuntu philosophy - contributions that strengthen community connections and respect are welcome.

## 📜 License

This project is created for educational purposes, embodying the Ubuntu principle that knowledge belongs to the community.

## 🙏 Acknowledgments

- Ubuntu Philosophy for inspiration
- The global web community for shared resources
- Python and requests library maintainers

---

*"A person is a person through other persons." - Ubuntu philosophy*  
*This program connects you to the work of others across the web.*
