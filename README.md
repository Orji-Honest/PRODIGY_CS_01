# 🔐 Caesar Cipher Tool

## 📋 Project Overview
A Python implementation of the classic Caesar Cipher encryption algorithm, developed as **Task 01** of my Cybersecurity Internship at PRODIGY. This tool provides both encryption and decryption capabilities using the historical Caesar shift technique.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

## ✨ Features
- ✅ **Encrypt** plain text with customizable shift values
- ✅ **Decrypt** cipher text with known shift values
- ✅ **Preserves case** (uppercase/lowercase remain as is)
- ✅ **Handles special characters** (numbers, symbols remain unchanged)
- ✅ **Interactive command-line interface** with menu system
- ✅ **File encryption/decryption** support
- ✅ **Input validation** and error handling
- 
## How It Works
The program shifts alphabetic characters forward (encryption) or backward (decryption) by a user-specified number.
Uppercase and lowercase letters are preserved.
Non-letter characters (spaces, punctuation) remain unchanged.
Decryption is handled by reversing the shift.
Testing Examples
Encrypt "orji" with shift 3 → Output: "kuml"
Decrypt "kuml" with shift 3 → Output: "orji"
Encrypt "orji honest" with shift 4 → Output: "svnm lsriwx"
## Security Note
The Caesar cipher is outdated and vulnerable to brute force attacks.
This project is a learning tool for basic understanding encryption basics.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- No external dependencies required

### Installation
```bash
# Clone the repository
git clone https://github.com/Orji-Honest/PRODIGY_CS_01.git

# Navigate to project directory
cd PRODIGY_CS_01

# Run the program
python caesar_cipher.py
