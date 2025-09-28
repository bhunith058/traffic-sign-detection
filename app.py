from flask import *
import os
from werkzeug.utils import secure_filename
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import pyttsx3
import gdown  

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

MODEL_DIR = 'model'
MODEL_FILE = 'traffic.h5'
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILE)


MODEL_URL = "https://drive.google.com/uc?id=1pOEaI2rl3RSoI3cRNGyGm0sm4aXlZUM8"

def download_model_if_missing():
    if not os.path.exists(MODEL_PATH):
        print("Model not found locally. Downloading...")
        os.makedirs(MODEL_DIR, exist_ok=True)
        gdown.download(MODEL_URL, MODEL_PATH, quiet=False)
        print("Model downloaded successfully.")


download_model_if_missing()


model = load_model(MODEL_PATH)


classes = {
    0: 'Speed limit (20km/h)', 1: 'Speed limit (30km/h)', 2: 'Speed limit (50km/h)',
    3: 'Speed limit (60km/h)', 4: 'Speed limit (70km/h)', 5: 'Speed limit (80km/h)',
    6: 'End of speed limit (80km/h)', 7: 'Speed limit (100km/h)', 8: 'Speed limit (120km/h)',
    9: 'No passing', 10: 'No passing veh over 3.5 tons', 11: 'Right-of-way at intersection',
    12: 'Priority road', 13: 'Yield', 14: 'Stop', 15: 'No vehicles',
    16: 'Vehicle > 3.5 tons prohibited', 17: 'No entry', 18: 'General caution',
    19: 'Dangerous curve left', 20: 'Dangerous curve right', 21: 'Double curve',
    22: 'Bumpy road', 23: 'Slippery road', 24: 'Road narrows on the right',
    25: 'Road work', 26: 'Traffic signals', 27: 'Pedestrians', 28: 'Children crossing',
    29: 'Bicycles crossing', 30: 'Beware of ice/snow', 31: 'Wild animals crossing',
    32: 'End speed + passing limits', 33: 'Turn right ahead', 34: 'Turn left ahead',
    35: 'Ahead only', 36: 'Go straight or right', 37: 'Go straight or left',
    38: 'Keep right', 39: 'Keep left', 40: 'Roundabout mandatory',
    41: 'End of no passing', 42: 'End no passing vehicle > 3.5 tons', 43: 'No Sign Detected'
}

def image_processing(img_path):
    data = []
    with Image.open(img_path) as image:
        image = image.resize((30, 30))
        data.append(np.array(image))

    X_test = np.array(data)
    Y_pred = model.predict(X_test)
    Y_pred_class = np.argmax(Y_pred, axis=1)
    return Y_pred_class

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/first', methods=['GET'])
def first():
    return render_template('first.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)

        result = image_processing(file_path)
        s = [str(i) for i in result]
        a = int("".join(s))
        prediction_text = "Predicted Traffic Sign is: " + classes.get(a, "Unknown Sign")

        os.remove(file_path)

        engineio = pyttsx3.init()
        engineio.say(prediction_text)
        engineio.runAndWait()

        return render_template_string('{{ prediction }}', prediction=prediction_text)

    return redirect('/first')

@app.route('/performance')
def performance():
    return render_template("performance.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")

if __name__ == '__main__':
    app.run(port=5000, debug=True)
