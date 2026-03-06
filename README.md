🦠 Malaria Detection Using Deep Learning

An AI-based system that detects malaria parasites in blood smear images using Deep Learning (CNN).
This project helps automate malaria diagnosis and assist healthcare professionals in detecting infected blood cells quickly and accurately.

👨‍💻 Author

Name: Gajender Kumar
GitHub: https://github.com/gajenderyadav644-spec

Project: Malaria Detection Using Deep Learning
Team ID: SWTID-2026-8818

📌 Project Overview

Malaria is a serious infectious disease caused by parasites transmitted through mosquito bites.
Traditional diagnosis involves manual examination of blood smear images under a microscope, which is time-consuming and dependent on expert analysis.

This project uses Deep Learning and Computer Vision to automatically classify blood cell images into two categories:

Parasitized

Uninfected

Users can upload blood smear images through a web interface, and the system predicts whether malaria parasites are present.

🚀 Features

Deep Learning based malaria detection

CNN image classification model

Web interface using Flask

Image upload and prediction system

Fast AI-based diagnosis support

🛠 Technologies Used
Technology	Purpose
Python	Programming language
TensorFlow / Keras	Deep learning framework
CNN	Image classification
Flask	Web application
NumPy	Numerical computation
OpenCV / Pillow	Image processing
📂 Project Structure
malaria-detection/
│
├── static/
│   ├── css/
│   └── uploads/
│
├── templates/
│   └── index.html
│
├── cell_images/
│   ├── Parasitized/
│   └── Uninfected/
│
├── app.py
├── train.py
├── malaria_model.h5
├── requirements.txt
└── README.md
⚙️ Installation
Clone the Repository
git clone https://github.com/gajenderyadav644-spec/malaria-detection.git
cd malaria-detection
Install Dependencies
pip install -r requirements.txt
Run the Application
python app.py
🧪 Model Training

To train the deep learning model:

python train.py

The trained model will be saved as:

malaria_model.h5
🖥 Usage

Start the Flask application

Open browser

http://127.0.0.1:5000

Upload a blood smear image

The system predicts:

Parasitized

Uninfected

📊 Dataset

Dataset used for training:

NIH Malaria Cell Images Dataset

Classes:

Parasitized

Uninfected

📈 Model Performance

Evaluation metrics used:

Accuracy

Precision

Recall

F1 Score

These metrics measure how accurately the model detects malaria parasites.

📌 Advantages

Faster malaria detection

Reduced human error

Automated blood smear analysis

Helpful in rural healthcare centers

⚠ Limitations

Depends on image quality

Requires large dataset

Not a replacement for professional diagnosis

🔮 Future Improvements

Mobile application development

Cloud deployment

Real-time microscope integration

Larger dataset training

📜 License

This project is developed for educational and research purposes.
