
# 📝 Resume Screening Web App

Welcome to the **Resume Screening Web App** — a machine learning-powered application that automatically classifies resumes into predefined categories using NLP techniques and a trained model.

---

## 🚀 Overview

This web app allows users to upload a **resume (PDF format)**, automatically extracts the text, cleans it, vectorizes the content, and then classifies it into a specific job category using a trained **Scikit-learn** model.

Built with the help of:

- 🧠 **Scikit-learn** — for building and using the machine learning model  
- 📊 **Pandas** — for data handling and preprocessing  
- 📈 **Matplotlib** & **Seaborn** — for data visualization and EDA  
- 🌐 **Streamlit** — to make this app accessible via a beautiful web interface  

---

## 📂 Project Structure

```
resume-screening/
│
├── app.py                 # Streamlit web app
├── requirements.txt       # List of required Python packages
├── README.md              # You are here :)
|
├── data/
│   ├── resumes.csv        # (Optional) Raw dataset used for training
│   ├── model.pkl          # Trained ML model
│   ├── tfidf_vectorizer.pkl # TF-IDF vectorizer used for transforming input text
│
└── myenv/                 # Your virtual environment (not mandatory to include)
```

---

## 📥 How to Use

### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/resume-screening.git
cd resume-screening
```

### ✅ Step 2: Set Up the Environment

Make sure you're in the main project directory and install all dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### ✅ Step 3: Run the App

Start the Streamlit app by running:

```bash
streamlit run app.py
```

### ✅ Step 3: Analyze the notebook

Analyze the notebook to understand how we done what we did.

---

## 🔍 Features

- 📄 **PDF Resume Upload**
- 🧹 **Automatic Text Extraction & Cleaning**
- 📚 **TF-IDF Vectorization**
- 🎯 **Resume Category Prediction**
- ✨ **Simple & Clean Web Interface**

---

## 💡 How It Works

1. The user uploads a **PDF resume**.
2. The app extracts text from the PDF using a text extractor.
3. It cleans and vectorizes the text using a pre-trained **TF-IDF vectorizer**.
4. A **KNeighborsClassifier** (or other scikit-learn model) predicts the most relevant job category.
5. The predicted category is displayed on the web interface.

---

## 📦 Dependencies

All required packages are listed in `requirements.txt`. Install them with:

```bash
pip install -r requirements.txt
```

Some key libraries:
- `scikit-learn`
- `pandas`
- `matplotlib`
- `seaborn`
- `streamlit`

---

## 📬 Feedback

If you like the project or want to contribute, feel free to open issues or pull requests!  
Made with ❤️ by [Your Name].

---

## 🏁 Sample Output

> Upload your resume and the app will tell you if it's for:
> - 📊 Data Analyst  
> - 🧬 Machine Learning Engineer  
> - 💻 Software Developer  
> - 📱 Android Developer  
> - …and more!

---

Happy Screening! 🎉
