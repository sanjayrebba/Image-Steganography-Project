# Crypto-Steganography Tool

A simple and secure Python tool to hide encrypted text messages inside PNG images using Least Significant Bit (LSB) steganography and AES-128 (Fernet) encryption.

---

## 📂 Project Structure

* `.venv/` - Local virtual environment.
* `.python-version` - Target Python version file.
* `pyproject.toml` - Project settings and dependencies.
* `uv.lock` - Locked dependency file.
* `main.py` - Core script containing the hide/retrieve logic.
* `README.md` - Project documentation.

---

## Setup & Installation

You can set up this project using **Standard Python (pip)** or **uv**.

### Option A: Standard Python (No uv required)
1. Open your terminal in the project directory.
2. Install the required packages:
   ```bash
   pip install pillow numpy cryptography

Run the application:

Bash
python main.py

Option B: Using uv (If installed)
Open your terminal in the project directory.

Sync the environment:

Bash
uv sync
Run the application:

Bash
uv run main.py
💻 How to Use
1. Hide a Message
Choose option 0 when prompted.

Enter the path to your source image (e.g., cover.jpg).

Type the secret message you want to hide.

Enter a name for your output image (it must end in .png, e.g., secret.png).

Important: Copy and save the long key printed at the end. You need this to read the message later!

2. Retrieve a Message
Choose option 1 when prompted.

Enter the path to your secret PNG image (e.g., secret.png).

Paste the exact key you saved during the hiding process.

Your decrypted secret message will appear in the terminal.

⚠️ Key Rules
Never convert the output image to JPG: Only use .png. Compression from formats like JPG or sending the image over compressed chat apps (like WhatsApp) will destroy the hidden data.

Don't lose the key: The message is strongly encrypted; it cannot be recovered without the generated master key.