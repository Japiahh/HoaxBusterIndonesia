# Hoax Buster Indonesia

**TF-IDF + SVM**

---

## About the Project

**Hoax Buster Indonesia** is a web-based application designed to detect whether a news article or official document (including PDF circular letters) is **Fact** or **Hoax**. 

This project combines traditional Natural Language Processing (NLP) techniques with Machine Learning and Generative AI to provide fast, accurate classification and explainable results.

## Background

The rapid spread of information in the digital era has a negative side: the uncontrolled dissemination of **hoax news**. Hoaxes can cause significant harm to individuals, communities, and even national stability. 

This project leverages **Machine Learning** as a solution to automatically and quickly classify news articles, helping improve digital literacy and maintain information integrity.

## Objectives

- Build an accurate hoax detection model using Machine Learning.
- Develop a user-friendly web application with an intuitive interface.
- Provide explainable AI features to help users understand the classification results.
- Support digital literacy efforts in Indonesia.

## Dataset

- **Source**: [Dataset Deteksi Berita Hoaks Indonesia](https://www.kaggle.com/datasets/mochamadabdulazis/deteksi-berita-hoaks-indo-dataset) by Mochamad Abdul Azis
- **Total Samples**: 23,944 news articles
- **Sources**: TurnBackHoax.id, Antaranews, Kompas, Detik.com
- **Labels**: Binary (1 = Hoax, 0 = Fact)
- **Features Used**: `narasi` (narrative/content) and `label`

---

## Methodology

### 1. Data Preprocessing
- Case folding (lowercasing)
- Removal of brackets `[]`, punctuation, numbers, and newlines
- Text cleaning and feature selection

### 2. Data Splitting
- Train : 80% (19,155 samples)
- Validation : 10% (2,394 samples)
- Test : 10% (2,394 samples)

### 3. Feature Extraction
- **TF-IDF Vectorizer** with maximum 10,000 features

### 4. Model
- **Algorithm**: Support Vector Machine (SVM)
- **Kernel**: Linear
- **C (Regularization)**: 1.0
- **Random State**: 42

**Why Linear Kernel?**  
With high-dimensional text data (10,000 features), the data is usually linearly separable. Linear SVM is faster and more effective at preventing overfitting on large text datasets.

---

## Model Performance

- **Training Score**: 99.7%
- **Validation Score**: 98.5%
- **Test F1-Score**: **98.5%**
- **Final Accuracy**: 98.5%

## Application Features

**Hoax Buster Indonesia** is built using **Streamlit** and has the following capabilities:

- Detect hoax/fact from **text input**
- Analyze **PDF documents** (e.g., official circular letters)
- Display classification result (Fact / Hoax)
- Provide **explanation** using Gemini 2.0 Flash Lite as Explainable AI (XAI)
- Clean and modern user interface

> **Note**: You need a Google Gemini API key to enable the explanation feature.

## Tech Stack

- **Programming Language**: Python
- **Web Framework**: Streamlit
- **Machine Learning**: Scikit-Learn (SVM + TF-IDF)
- **PDF Processing**: PyPDF2
- **Explainable AI**: Google Gemini 2.0 Flash Lite API
- **Data Processing**: Pandas, NumPy

## SDG Alignment

This project contributes to the United Nations Sustainable Development Goals (SDGs):

- **Goal 4.7**: Quality Education – Digital Literacy
- **Goal 9.b**: Industry, Innovation, and Infrastructure – Local Technological Innovation
- **Goal 16.10**: Peace, Justice, and Strong Institutions – Information Integrity
- **Goal 17.16**: Partnerships for the Goals

---

## Core Contributors

**Kupat Tahu Padalarang**  

- Japiahh
- Xyuuzu

---

## Conclusion

The combination of **TF-IDF + Linear SVM** has proven to be highly efficient for hoax news classification in Indonesian language. The deployment using Streamlit makes the project easy to use and suitable for experimental and educational purposes.

This application can serve as a practical tool to increase public awareness and digital literacy regarding hoax news in Indonesia.

---

**Made with ❤️ for a more informed Indonesia**
