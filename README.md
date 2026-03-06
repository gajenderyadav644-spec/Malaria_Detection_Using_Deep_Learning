🦠 Malaria Detection Using Deep Learning

An AI-powered system that detects malaria parasites in blood smear images using Deep Learning (CNN).
This project helps automate malaria diagnosis and assists healthcare professionals in detecting infected blood cells quickly.

📌 Project Overview

Malaria is a life-threatening disease caused by parasites transmitted through mosquito bites.
Traditional diagnosis involves manual examination of blood smear images under a microscope, which can be time-consuming and error-prone.

This project uses Deep Learning and Computer Vision to automatically classify blood cell images into:

Parasitized

Uninfected

The system allows users to upload a blood smear image through a web interface and receive an AI-based prediction.

🚀 Features

🧠 Deep Learning based malaria detection

🖼 Image classification using CNN

🌐 Web interface using Flask

⚡ Fast prediction results

📊 Helps assist medical diagnosis

🛠 Technologies Used
Technology	Purpose
Python	Programming language
TensorFlow / Keras	Deep learning framework
CNN	Image classification model
Flask	Web application framework
NumPy	Numerical operations
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
1️⃣ Clone the repository
git clone https://github.com/yourusername/malaria-detection.git
cd malaria-detection
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the application
python app.py
🧪 Model Training

To train the CNN model using the malaria dataset:

python train.py

The trained model will be saved as:

malaria_model.h5
🖥 Usage

Start the Flask application.

Open the browser and go to:

http://127.0.0.1:5000

Upload a blood smear image.

The system will classify the image as:

Parasitized

Uninfected

📊 Dataset

The dataset contains microscopic images of blood cells divided into two categories:

Parasitized

Uninfected

Dataset commonly used:

NIH Malaria Dataset
📈 Model Performance

Typical CNN model evaluation metrics include:

Accuracy

Precision

Recall

F1 Score

These metrics help evaluate the model's ability to correctly detect malaria-infected cells.

📌 Advantages

Faster malaria detection

Reduces human error

Supports healthcare professionals

Useful in remote areas

⚠ Limitations

Model accuracy depends on image quality

Requires large dataset for better performance

Not a replacement for professional medical diagnosis

🔮 Future Improvements

Mobile application integration

Cloud deployment

Real-time microscope integration

Larger dataset training

👨‍💻 Author

Gajender Kumar
Project: Malaria Detection Using Deep Learning
Team ID: SWTID-2026-8818

📜 License

This project is for educational and research purposes.

✅ Agar chaho to main tumhe GitHub ke liye aur powerful README bhi bana sakta hoon jisme:

📸 Project screenshots

🎥 Demo GIF

📊 Model architecture diagram

⭐ Badges (Python, TensorFlow, Flask)
