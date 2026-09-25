# 🩺 Smart Medical Diagnosis System

An AI-powered **Smart Medical Diagnosis System** that predicts possible diseases based on user-provided symptoms using Machine Learning.

The project implements a complete machine learning pipeline including data preprocessing, duplicate handling, model training, evaluation, and disease prediction through an interactive **Streamlit web application**.

## 🚀 Live Demo

🔗 **[Try Smart Medical Diagnosis System](https://smart-medical-diagnosis-system.streamlit.app/)**

---

## 📌 Project Overview

The Smart Medical Diagnosis System demonstrates how Machine Learning can be applied to symptom-based disease prediction.

Users can select symptoms through the web interface, and the trained Machine Learning model processes the selected inputs to generate a predicted disease.

The project focuses on building an **end-to-end Machine Learning application**, from dataset preprocessing and model training to evaluation, prediction, and web deployment.

---

## ✨ Key Features

* 🩺 Symptom-based disease prediction
* 🤖 Machine Learning-based prediction system
* 📊 Evaluation of multiple ML algorithms
* 🧹 Data cleaning and preprocessing
* 🔄 Duplicate data handling
* 📈 Model performance evaluation
* 🧠 Interactive Streamlit interface
* 📋 Dedicated model insights page
* ⚡ Real-time prediction through the web application
* 📱 Responsive and user-friendly interface

---

## 🔬 Machine Learning Pipeline

```text
Dataset
   ↓
Data Cleaning
   ↓
Duplicate Handling
   ↓
Data Preparation
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Best Model Selection
   ↓
Disease Prediction
   ↓
Streamlit Web Application
```

---

## 📂 Dataset

The dataset contains symptom-based records used for supervised machine learning.

### Dataset Details

* **Training samples:** 4,920
* **Testing samples:** 42
* **Input features:** 132 symptoms/features
* **Learning type:** Supervised Learning
* **Target:** Disease

During preprocessing, duplicate records were identified and handled before model training.

---

## 🤖 Machine Learning Models Evaluated

The project evaluates multiple classification algorithms:

1. Logistic Regression
2. Random Forest
3. Support Vector Machine (SVM)
4. K-Nearest Neighbors (KNN)

The models were evaluated using standard classification metrics.

### Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## 🏆 Selected Model

### Logistic Regression

Logistic Regression was selected as the final model based on the evaluation results obtained during the project.

The trained model was integrated with the prediction pipeline and used by the Streamlit application.

### Model Performance

| Metric    | Score |
| --------- | ----: |
| Accuracy  |  100% |
| Precision |  100% |
| Recall    |  100% |
| F1-Score  |  100% |

> **Note:** These scores are based on the project's processed dataset and evaluation setup. They should not be interpreted as clinical validation or real-world medical accuracy.

---

## 🧠 Why Logistic Regression?

Logistic Regression was selected because it provides:

* Efficient classification for structured symptom data
* Fast prediction
* Simple and interpretable model behavior
* Good suitability for high-dimensional input features
* Easy integration into a web-based prediction application

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Web Application

* Streamlit

### Development Environment

* Google Colab
* VS Code

### Version Control & Deployment

* Git
* GitHub
* Streamlit

---

## 📁 Project Structure

```text
Smart-Medical-Diagnosis-System/
│
├── Dataset/
│   ├── Training.csv
│   └── Testing.csv
│
├── Model/
│   └── Trained model files
│
├── VS_code/
│   ├── app.py
│   └── frontend_preview/
│       ├── index.html
│       ├── style.css
│       ├── script.js
│       ├── diagnosis.html
│       └── model_insights.html
│
├── Colab/
│   └── Smart_Medical_Diagnosis_System.ipynb
│
├── Screenshots/
│
└── README.md
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project

```bash
cd Smart-Medical-Diagnosis-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If a requirements file is not available, install the main packages:

```bash
pip install streamlit pandas numpy scikit-learn matplotlib seaborn
```

### 4. Run the Streamlit Application

```bash
streamlit run VS_code/app.py
```

### 5. Open the Application

The application will normally be available at:

```text
http://localhost:8501
```

---

## 🖥️ Application Pages

### 🏠 Home

Introduces the Smart Medical Diagnosis System and provides access to the diagnosis functionality.

### 🩺 Diagnosis

Allows users to provide symptoms and receive a Machine Learning-based disease prediction.

### 📊 Model Insights

Displays technical information about:

* Number of input features
* Machine Learning models evaluated
* Selected model
* ML pipeline
* Model comparison
* Evaluation metrics
* Confusion matrix
* Technology stack

---

## 📊 Model Insights

The project evaluates the complete Machine Learning workflow instead of relying on a single algorithm.

```text
132 Input Features
        ↓
Data Preprocessing
        ↓
Duplicate Handling
        ↓
4 ML Models Evaluated
        ↓
Performance Comparison
        ↓
Logistic Regression Selected
        ↓
Prediction
```

---

## 🎯 Project Objectives

* Build an end-to-end Machine Learning application.
* Understand data preprocessing and cleaning.
* Handle duplicate records in a dataset.
* Train and compare multiple classification algorithms.
* Evaluate models using standard classification metrics.
* Integrate a trained ML model with a web application.
* Deploy the application using Streamlit.
* Demonstrate practical implementation of Machine Learning.

---

## 🔮 Future Enhancements

* Integration with a larger and more diverse medical dataset
* Improved model validation using cross-validation
* Explainable AI for prediction reasoning
* Patient history management
* Prediction history and report generation
* Authentication and secure user management
* Cloud database integration
* Advanced medical NLP capabilities

---

## ⚠️ Medical Disclaimer

This project is developed **for educational and demonstration purposes only**.

The predictions generated by this application are not a substitute for professional medical diagnosis, treatment, or medical advice. Users should consult a qualified healthcare professional for actual medical concerns.

---

## 👩‍💻 Author

**Shrabani Bhutia**

B.Sc. Information Technology & Management

### Skills Demonstrated

`Python` • `Machine Learning` • `Scikit-learn` • `Pandas` • `NumPy` • `Streamlit` • `Data Preprocessing` • `Model Evaluation` • `GitHub`

---

⭐ **If you find this project interesting, feel free to explore the repository and try the live demo.**
