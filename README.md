⭐💲 Star-Dollar Algorithm with LSB Image Steganography

This project demonstrates how the Star-Dollar Algorithm can be combined with Least Significant Bit (LSB) Image Steganography to securely embed hidden codes into images.

The main idea is to use the Star-Dollar Algorithm (a gesture/matching algorithm) as a layer of encoding for secret messages, and then hide those encoded values inside an image using LSB steganography, making the data imperceptible to the human eye while still retrievable by the algorithm.

🚀 Features

Implementation of the Star-Dollar Algorithm for generating unique encoded representations of secret codes.

LSB Image Steganography for hiding codes inside image pixel values.

Ability to embed secret messages (codes, keys, or data) into an image.

Functionality to extract and decode the hidden information from the stego-image.

Lightweight and easy-to-extend Python project.

🛠️ Technologies Used

Python 3.x

PIL / Pillow – for image manipulation.

NumPy – for handling pixel operations efficiently.

Custom Star-Dollar Algorithm Implementation

Star-dollar-algorithm-with-lsb-image-steganography/
│── star_dollar.py        # Star-Dollar Algorithm logic
│── lsb_stego.py          # LSB steganography functions
│── main.py               # Main script to run embedding & extraction
│── utils.py              # Helper functions
│── samples/              # Sample images (cover & stego images)
│── README.md             # Project documentation

🔑 How It Works

Input: A secret code (text/numeric).

Encoding: The Star-Dollar Algorithm transforms the code into a structured representation.

Embedding: The encoded values are hidden inside the least significant bits of a cover image.

Output: A stego-image visually identical to the original but containing hidden data.

Decoding: Extraction of the hidden codes from the image, followed by decoding using the Star-Dollar Algorithm.

▶️ Usage
1. Clone the repository
git clone https://github.com/your-username/Star-dollar-algorithm-with-lsb-image-steganography.git
cd Star-dollar-algorithm-with-lsb-image-steganography

2. Install dependencies
pip install -r requirements.txt

3. Run the program

Embedding data

python main.py --mode embed --input cover.png --output stego.png --secret "MyHiddenCode123"


Extracting data

python main.py --mode extract --input stego.png

📸 Example

Cover Image →

Stego Image →

Hidden Code → MyHiddenCode123

🔮 Future Improvements

Add GUI for easier use.

Support for audio/video steganography.

Encryption layer before embedding.

Integration with machine learning for enhanced robustness.
