# PRODIGY_GA_02

# 🧠 AI Image Generator (Text-to-Image Flask App)

Transform your imagination into stunning visuals.

![AI Image Generator UI](Screenshot%202025-07-09%20180729.png)

---

## ✨ Features

- 🧾 Prompt-based image generation
- 🤖 Powered by Hugging Face Inference API (`ZB-Tech/Text-to-Image`)
- 🖼️ Base64 image rendering without saving files
- 💡 Easy to use Flask web interface

---

## 📁 Project Structure

```
text-to-image-flask/
├── app.py               # Flask backend
├── templates/
│   └── index.html       # Frontend UI
├── .env                 # (optional) Environment file for API key
├── Screenshot 2025-07-09 180729.png
└── README.md            # You're here!
```

---

## 🚀 Getting Started

### 1. Clone the Project

```bash
git clone https://github.com/your-username/text-to-image-flask.git
cd text-to-image-flask
```

### 2. Install Dependencies

```bash
pip install flask pillow requests python-dotenv
```

### 3. Get a Hugging Face API Token

1. Visit [HuggingFace Tokens](https://huggingface.co/settings/tokens)
2. Click **New token**
3. Check ✅ `Access Inference Endpoints`
4. Copy the token

---

## 🔐 Setup API Token

### Option A: Set in terminal

```bash
# CMD
set HF_API_KEY=your_real_token

# PowerShell
$env:HF_API_KEY="your_real_token"

# Linux/macOS
export HF_API_KEY=your_real_token
```

### Option B: Use `.env` file

Create `.env`:

```
HF_API_KEY=your_real_token
```

Add this line at the top of `app.py`:

```python
from dotenv import load_dotenv
load_dotenv()
```

---

## 🧠 Usage

### Run the app:

```bash
python app.py
```

Visit in browser:

```
http://127.0.0.1:5000
```

---

## 🌈 Example Prompt

> `"Astronaut riding a horse in a futuristic city"`

Will generate a stunning AI image and display it directly on the page.

---

## 📸 UI Preview

![UI](Screenshot%202025-07-09%20180729.png)

---

## 📜 License

MIT License © 2025

---

## 🙌 Acknowledgements

- Built with [Flask](https://flask.palletsprojects.com/)
- Powered by [Hugging Face](https://huggingface.co/inference-api)
