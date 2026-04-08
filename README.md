# HASH-LIB
🔐 PyHashPass
Securely hash password inputs using Python's hashlib — supporting SHA-256, SHA-512, MD5, and more.
📖 Overview
PyHashPass is a lightweight Python tool that takes a password input from the user and converts it into a cryptographic hash. Built on Python's built-in hashlib library — no external dependencies required.
Whether you're learning cryptography basics or need a quick hashing utility, this project has you covered.
✨ Features
🔑 Accepts password input securely (hidden from terminal)
🔒 Supports multiple hashing algorithms: SHA-256, SHA-512, SHA-1, MD5
⚡ Zero external dependencies — pure Python stdlib
🧂 Optional salt support to prevent rainbow table attacks
📋 Displays hex digest output ready to store or compare
🚀 Quick Start
              -----Requirements-----
Python 3.6+
Clone the repo
git clone https://github.com/sk4mx/pyhashpass.git
cd pyhashpass
Run
python hash_password.py
