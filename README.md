# Crypto-Steganography Tool

A simple and secure Python tool to hide encrypted text messages inside PNG images using Least Significant Bit (LSB) steganography and AES-128 (Fernet) encryption.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [How to Use](#how-to-use)
- [Key Rules](#️-key-rules)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

- 🔒 Encrypts your message with AES-128 (via `cryptography`'s Fernet) before hiding it
- 🖼️ Hides the encrypted payload inside a PNG using LSB steganography
- 🔑 Generates a unique key per message — without it, the data can't be decrypted
- ⚡ Works with either plain `pip` or `uv` for setup

---

## Project Structure

| File / Folder      | Description                              |
|---------------------|-------------------------------------------|
| `.venv/`            | Local virtual environment                 |
| `.python-version`   | Target Python version file                |
| `pyproject.toml`    | Project settings and dependencies         |
| `uv.lock`           | Locked dependency file                    |
| `main.py`           | Core script containing the hide/retrieve logic |
| `README.md`         | Project documentation                     |

---

## Setup & Installation

**Prerequisites:** Python 3.9+ installed on your system.

You can set up this project using **standard Python (pip)** or **uv**.

### Option A: Standard Python (pip)

1. Open your terminal in the project directory.
2. Install the required packages:
   ```bash
   pip install pillow numpy cryptography
   ```
3. Run the application:
   ```bash
   python main.py
   ```

### Option B: Using uv

1. Open your terminal in the project directory.
2. Sync the environment:
   ```bash
   uv sync
   ```
3. Run the application:
   ```bash
   uv run main.py
   ```

---

## How to Use

### 1. Hide a Message

1. Choose option `0` when prompted.
2. Enter the path to your source image (e.g., `cover.png`).
3. Type the secret message you want to hide.
4. Enter a name for your output image — it **must** end in `.png` (e.g., `secret.png`).
5. **Important:** Copy and save the long key printed at the end. You'll need it to read the message later — it cannot be regenerated or recovered.

### 2. Retrieve a Message

1. Choose option `1` when prompted.
2. Enter the path to your secret PNG image (e.g., `secret.png`).
3. Paste the exact key you saved during the hiding process.
4. Your decrypted secret message will appear in the terminal.

---

## ⚠️ Key Rules

- **Never convert the output image to JPG.** Only use `.png`. Lossy compression — including from formats like JPG or from sending the image over compressed chat apps (e.g., WhatsApp) — will destroy the hidden data.
- **Don't lose the key.** The message is strongly encrypted and cannot be recovered without the generated key.
- **Use a large enough source image.** The cover image must have enough pixels to hold your message; very short messages need only a small image, but longer messages require a proportionally larger one.
- **Keep your key private.** Anyone with the key and the image can decrypt the hidden message.

---

## Troubleshooting

| Issue | Likely Cause |
|---|---|
| Output image looks corrupted or won't open | Message may be too large for the source image |
| Decryption fails / garbled output | Key was copied incorrectly, or the image was re-compressed/edited after hiding |
| `ModuleNotFoundError` on run | Dependencies not installed — rerun the install step for your chosen setup option |

---

## License

Specify your project's license here (e.g., MIT, Apache 2.0).
