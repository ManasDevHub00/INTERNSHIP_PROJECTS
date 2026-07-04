# 🌾 Farmer Guider App

A Machine Learning-based web application built with **Flask** that helps farmers make informed agricultural decisions by recommending the most suitable **Crop** and **Fertilizer** based on soil and environmental conditions.

The project includes two intelligent prediction systems:

- 🌱 Crop Recommendation
- 🧪 Fertilizer Recommendation

Both models are trained using the **Random Forest Classifier** algorithm and deployed through a Flask web application.

---

## 🚀 Features

- 🌱 Predict the most suitable crop based on soil nutrients and weather conditions.
- 🧪 Recommend the appropriate fertilizer based on soil and crop information.
- User-friendly web interface built with HTML and CSS.
- Fast prediction using trained Machine Learning models.
- Separate modules for Crop and Fertilizer Recommendation.
- Models saved using Pickle for deployment.
- Single result page for displaying predictions.

---

## 🛠️ Tech Stack

- Python 3.11.5
- Flask
- Pandas
- NumPy
- Scikit-learn
- HTML5
- CSS3
- Pickle

---

## 🤖 Machine Learning Algorithm

The application uses the following Machine Learning algorithm for both prediction modules:

- **Random Forest Classifier**

---

## 📁 Project Structure

```text
Farmer_Guider_app/
│
├── dataset/
│   ├── Crop_recommendation.csv
│   └── fertilizer_recommendation_dataset.csv
│
├── model/
│   ├── Crop_recom_model.pkl
│   ├── crop_recom_encoder.pkl
│   ├── crop_recom_scaler.pkl
│   ├── fertilizer_model.pkl
│   ├── le_crop.pkl
│   ├── le_soil.pkl
│   ├── le_target.pkl
│   └── scaler.pkl
│
├── Notebook/
│   ├── train_Crop.ipynb
│   └── train_Fertilizer.ipynb
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── crop.html
│   ├── fertilizer.html
│   └── result.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 🏗️ Project Architecture

```

```

---

## ⚙️ Workflow

1. Open the Flask application.
2. Select either **Crop Recommendation** or **Fertilizer Recommendation**.
3. Enter the required agricultural information.
4. The application preprocesses the input data.
5. The trained Random Forest model predicts the result.
6. The prediction is displayed on the Result page.

---

## 🌱 Crop Recommendation Inputs

The Crop Recommendation model predicts the best crop using:

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall

### Output

- Recommended Crop

---

## 🧪 Fertilizer Recommendation Inputs

The Fertilizer Recommendation model predicts the most suitable fertilizer using:

- Temperature
- Moisture
- Rainfall
- pH
- Nitrogen
- Phosphorus
- Potassium
- Carbon
- Soil Type
- Crop Type

### Output

- Recommended Fertilizer

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Farmer_Guider_app.git
```

### Navigate to the Project Directory

```bash
cd Farmer_Guider_app
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### Install Required Packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 📦 Model Files

### Crop Recommendation

- Crop_recom_model.pkl
- crop_recom_encoder.pkl
- crop_recom_scaler.pkl

### Fertilizer Recommendation

- fertilizer_model.pkl
- le_crop.pkl
- le_soil.pkl
- le_target.pkl
- scaler.pkl

---

## 🎯 Future Improvements

- 🌦️ Weather API Integration
- 🌾 Crop Disease Prediction
- 🤖 AI Chatbot for Farmers
- 📍 Location-based Recommendations
- 🌐 Multilingual Support
- 📱 Mobile Application

---

## 👨‍💻 Author

**Manas Sharma**

- 🎓 Engineering Student
- 💻 Machine Learning & AI Enthusiast
- 🌱 Interested in AI for Agriculture

---

## 📄 License

This project is developed for educational and learning purposes.