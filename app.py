from flask import Flask, render_template, request, redirect, flash, send_file
import base64, os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import *

from core.key_loader import load_private_key, load_public_key
from core.signature import sign_data, verify_data

app = Flask(__name__)
app.secret_key = "supersecret"

os.makedirs("keys", exist_ok=True)


# 🔑 GENERATE KEYS
@app.route("/generate_keys")
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    with open("keys/private.pem", "wb") as f:
        f.write(private_key.private_bytes(
            Encoding.PEM,
            PrivateFormat.PKCS8,
            NoEncryption()
        ))

    with open("keys/public.pem", "wb") as f:
        f.write(public_key.public_bytes(
            Encoding.PEM,
            PublicFormat.SubjectPublicKeyInfo
        ))

    return render_template("keys.html")


# 📥 DOWNLOAD KEYS
@app.route("/download/<filename>")
def download_file(filename):
    return send_file(os.path.join("keys", filename), as_attachment=True)


@app.route("/")
def home():
    return render_template("index.html")


# ✍️ SIGN
@app.route("/sign", methods=["POST"])
def sign():
    text = request.form.get("text")
    key_file = request.files.get("private_key")

    if not key_file:
        flash("Private key required!", "danger")
        return redirect("/")

    try:
        private_key = load_private_key(key_file.read())
    except:
        flash("Invalid private key!", "danger")
        return redirect("/")

    data = text.encode()

    signature, hashed = sign_data(private_key, data)

    return render_template(
        "result.html",
        mode="sign",
        data=text,
        hash_val=hashed.hex(),
        signature=base64.b64encode(signature).decode()
    )


# ✔ VERIFY
@app.route("/verify", methods=["POST"])
def verify():
    text = request.form.get("text")
    sig = request.form.get("signature")
    pub_file = request.files.get("public_key")

    if not pub_file:
        flash("Public key required!", "danger")
        return redirect("/")

    public_key = load_public_key(pub_file.read())
    signature = base64.b64decode(sig)

    valid, hashed = verify_data(public_key, text.encode(), signature)

    return render_template(
        "result.html",
        mode="verify",
        valid=valid,
        hash_val=hashed.hex()
    )


if __name__ == "__main__":
    app.run(debug=True)