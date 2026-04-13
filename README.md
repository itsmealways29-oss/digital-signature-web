<div align="center">
  <h1>🔐 Digital Signature Web Interface</h1>
  <p>
    <strong>A robust, secure, and intuitive web application demonstrating RSA digital signatures in action.</strong>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version" />
    <img src="https://img.shields.io/badge/Flask-2.x-lightgrey.svg" alt="Flask Framework" />
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License" />
    <img src="https://img.shields.io/badge/Status-Active-success.svg" alt="Status" />
  </p>
</div>

---

## 📖 Overview

In today's digital landscape, ensuring data integrity and non-repudiation is paramount. The **Digital Signature Web Interface** is a lightweight yet powerful full-stack application built with Python and Flask. It provides a seamless user experience for performing foundational cryptographic operations: generating RSA 2048-bit key pairs, digitally signing data, and cryptographically verifying those signatures.

This project serves as an excellent reference implementation for developers looking to understand public-key cryptography and as a practical utility for rapid signature operations.

## ✨ Core Features

- **Asymmetric Key Generation**: Generate mathematically secure 2048-bit RSA Private and Public key pairs instantly. Keys are exportable directly to your local file system (`.pem` format).
- **Cryptographic Signing (SHA-256 + RSA)**: Input any sensitive message, and use your private key to compute a unique, verifiable digital signature. The application utilizes industry-standard SHA-256 hashing schemas under the hood.
- **Signature Verification**: Validate the integrity and source of the signed data. By uploading the original message, the corresponding signature, and the author's public key, the system can definitively confirm whether the data remains untampered since it was signed.
- **Production-Ready Configuration**: Built with a WSGI-compliant `gunicorn` setup, ensuring the application is deployment-ready for modern PaaS providers like Render or Heroku.

## ⚙️ How It Works

1. **Hashing:** When data is signed, it is first passed through a one-way hashing algorithm (SHA-256) to create a fixed-size digest.
2. **Encryption:** This digest is then encrypted using the sender's Private Key. This encrypted digest *is* the digital signature.
3. **Verification:** The receiver uses the sender's Public Key to decrypt the signature, retrieving the original hash. The receiver then independently hashes the received data. If both hashes match, the signature is mathematically valid!

## 🚀 Getting Started

Follow these instructions to set up the project on your local machine for development and testing.

### Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/itsmealways29-oss/digital-signature-web.git
   cd digital-signature-web
   ```

2. **Set up a virtual environment (Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the local server**
   ```bash
   python app.py
   ```
   *The application will now be accessible at `http://127.0.0.1:5000/`.*

## 📂 Project Structure

```text
digital-signature-web/
├── app.py                     # Main Flask application and routing
├── generate_keys.py           # Standalone key generation script
├── requirements.txt           # Project dependencies (Flask, Cryptography, Gunicorn)
├── core/
│   ├── hashing.py             # SHA-256 hashing infrastructure
│   ├── key_loader.py          # Utilities for parsing PEM key files
│   └── signature.py           # Core RSA signing and verification logic
├── keys/                      # Auto-generated directory for stored keys
└── templates/                 # HTML UI layouts rendered by Jinja2
    ├── base.html              # Main application wrapper
    ├── index.html             # Homepage / Entry point
    ├── keys.html              # Key generation UI
    └── result.html            # Success/Failure reporting screens
```

## 🌍 Production Deployment

This project is configured out-of-the-box for cloud platforms like **Render**, **Railway**, or **Heroku**.

**For Render Deployment:**
- Connect your GitHub repository to a new "Web Service".
- Set the **Build Command** to: `pip install -r requirements.txt`
- Set the **Start Command** to: `gunicorn app:app`
- No specialized environment variables are required to achieve a successful build.

## 🛡️ Security Disclaimer
> **CRITICAL:** **Never distribute or share your `private.pem` file.**
> The security of RSA cryptography relies entirely on the secrecy of the private key. Your private key represents your absolute digital identity. You should only share your `public.pem` key file with external parties.

## 🤝 Contributing

Contributions, issues, and feature requests are always welcome! Feel free to check the [issues page](https://github.com/itsmealways29-oss/digital-signature-web/issues) if you want to contribute.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---
<div align="center">
  <b>Developed by <a href="https://github.com/itsmealways29-oss">itsmealways29-oss</a></b>
</div>
