

---

# Multiple Disease Prediction System

![Streamlit App](https://img.shields.io/badge/Streamlit-App-blue) ![Python](https://img.shields.io/badge/Python-3.8+-yellow) ![License](https://img.shields.io/badge/License-MIT-green)

A web-based application built with **Streamlit** to predict the likelihood of **Diabetes**, **Heart Disease**, and **Parkinson's Disease** using machine learning models. This project leverages pre-trained models (`scikit-learn`) and provides an intuitive interface for users to input medical data and receive predictions.

---

## 📖 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## 📋 Project Overview
This application allows users to input relevant medical data to predict the presence of **Diabetes**, **Heart Disease**, or **Parkinson's Disease** using pre-trained machine learning models. The app is built using **Streamlit** for the frontend and **scikit-learn** for the backend models, with a user-friendly sidebar navigation to switch between disease prediction modules.

The models were trained on publicly available datasets and saved as `.sav` files using `pickle`. The app is designed for educational purposes and should not be used for actual medical diagnosis.

---

## ✨ Features
- **Multi-Disease Prediction**: Predicts Diabetes, Heart Disease, and Parkinson's Disease.
- **Interactive UI**: Built with Streamlit for easy data input and result visualization.
- **Sidebar Navigation**: Seamlessly switch between disease prediction modules.
- **Pre-trained Models**: Uses SVM and other ML models trained on standard datasets.
- **Portable**: Can be run locally or deployed to platforms like Streamlit Cloud.

---

## 📊 Dataset
The project uses the following datasets:
- **Diabetes**: [PIMA Indians Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database)
- **Heart Disease**: [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/Heart+Disease)
- **Parkinson's Disease**: [UCI Parkinson's Dataset](https://archive.ics.uci.edu/ml/datasets/Parkinsons)

The datasets are stored in the `dataset/` folder and were used to train the models saved in the `saved_models/` folder.

---

## 🛠 Installation
Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/multiple-disease-prediction-streamlit-app.git
   cd multiple-disease-prediction-streamlit-app
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   Ensure you have Python 3.8+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Required Packages**:
   The `requirements.txt` includes:
   ```
   streamlit
   scikit-learn
   pandas
   numpy
   streamlit-option-menu
   ```

5. **Run the Streamlit App**:
   ```bash
   streamlit run app.py
   ```
   This will start a local server, and your browser will open to `http://localhost:8501`.

---

## 🚀 Usage
1. **Start the App**:
   Run `streamlit run app.py` in your terminal.

2. **Navigate the App**:
   - Use the sidebar to select a disease prediction module: **Diabetes**, **Heart Disease**, or **Parkinson's**.
   - Enter the required medical data in the input fields (e.g., Glucose Level, Blood Pressure, MDVP:Fo(Hz), etc.).
   - Click the respective **Test Result** button to see the prediction.

3. **Interpret Results**:
   - The app will display a message indicating whether the person is likely to have the disease (e.g., "The person is diabetic" or "The person does not have Parkinson's disease").
   - **Note**: These predictions are for demonstration purposes only and should not be used for medical decisions.

---

## 📂 Project Structure
```plaintext
multiple-disease-prediction-streamlit-app/
├── dataset/
│   ├── diabetes.csv
│   ├── heart.csv
│   └── parkinsons.csv
├── saved_models/
│   ├── diabetes_model.sav
│   ├── heart_disease_model.sav
│   └── parkinsons_model.sav
├── colab_files_to_train_models/
├── app.py
├── requirements.txt
└── README.md
```
- **`dataset/`**: Contains the datasets used for training the models.
- **`saved_models/`**: Stores the pre-trained `.sav` model files.
- **`colab_files_to_train_models/`**: Jupyter notebooks or scripts used to train the models.
- **`app.py`**: Main Streamlit application script.
- **`requirements.txt`**: Lists Python dependencies.
- **`README.md`**: Project documentation.

---

## 🌐 Deployment
You can deploy this app to **Streamlit Cloud** (or other platforms like Render or Heroku) for public access:

### Deploy to Streamlit Cloud
1. Push your repository to GitHub.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.
3. Click **New App** > **From GitHub Repo** and select your repository.
4. Specify the main file as `app.py`.
5. Click **Deploy**. Streamlit Cloud will handle the rest, installing dependencies from `requirements.txt`.

### Local Testing
Run `streamlit run app.py` to test locally before deployment.

---

## 🤝 Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to your fork (`git push origin feature-branch`).
5. Open a Pull Request.

Please ensure your code follows the project's style and includes appropriate documentation.

---

## 📜 License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute as per the license terms.

---

## 🙏 Acknowledgements
- [Streamlit](https://streamlit.io/) for the awesome web framework.
- [scikit-learn](https://scikit-learn.org/) for machine learning tools.
- UCI Machine Learning Repository and Kaggle for providing the datasets.
- The open-source community for inspiration and support.

---

⭐ **If you find this project useful, please give it a star on GitHub!**

For any questions or suggestions, feel free to open an issue or contact me at `<soumyajitb0912@gmailcom>`.

---

