# 🚦 Traffic Sign Detection

**👨‍💻 Author:** Bhunith Kumar k
**🔗 GitHub:** [https://github.com/bhunith058/traffic-sign-detection](https://github.com/bhunith058/traffic-sign-detection)

---

## 🌟 Overview

Traffic Sign Detection is a **web-based system** that uses Convolutional Neural Networks (CNNs) to detect traffic signs in real-time. Users can upload an image, and the app predicts the traffic sign along with the probability of the prediction. 🖼️🚗

---

## ✨ Features

* 🛑 Detects multiple traffic signs: Stop, Yield, Speed Limit, No Entry, Keep Left/Right, etc.
* 💻 Clean and interactive web interface for image upload.
* 🎯 High prediction accuracy with a pre-trained CNN model.
* 📊 Shows probability of prediction.

---

## 📁 Project Structure

traffic-sign-detection/

* 📝 app.py                 # Flask backend
* 📦 requirements.txt       # Python dependencies
* 📂 model/

  * 📓 model.ipynb          # Training notebook
  * 🧠 traffic.h5           # Pre-trained CNN model
* 🖼️ static/                # Images, CSS, JS, assets
* 🌐 templates/             # HTML templates
* 🧪 test_data/             # Sample traffic sign images
* 📄 README.md              # Project documentation

---

## ⚡ Installation & Setup

1. **Clone the repository**

```
git clone https://github.com/bhunith058/traffic-sign-detection.git
cd traffic-sign-detection
```

2. **Create a virtual environment**

```
python -m venv venv
```

3. **Activate the virtual environment**

* Windows: `venv\Scripts\activate`
* Linux / MacOS: `source venv/bin/activate`

4. **Install dependencies**

```
pip install -r requirements.txt
```

---

## 🚀 Usage

1. Run the Flask app:

```
python app.py
```

2. Open your browser and go to:

```
http://127.0.0.1:5000/
```

3. Upload a traffic sign image and see the prediction instantly! 🖼️🔍

---

## 📸 Example Output

**Input Image:** STOP

Prediction Result:

* 🛑 predicted traffic sign is : stop


Another Example:

**Input Image:** Speed Limit 30 km/h
Prediction Result:

* 🏎️ redicted traffic sign is : Speed Limit 30 km/h

---
OUTPUT IMAGE:
<img width="1881" height="965" alt="image" src="https://github.com/user-attachments/assets/a26f5ba2-66cb-4f05-bb16-7dbda86da110" />

---

## ⚠️ Note


* ✅ Make sure all dependencies from `requirements.txt` are installed to run the app properly.

---

## 🛠️ Tech Stack

* 🐍 Backend: Python, Flask
* 🤖 Machine Learning: TensorFlow, Keras, CNN
* 🌐 Frontend: HTML, CSS, JavaScript
* 🛠️ Tools: Git, GitHub
