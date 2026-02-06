

# 📰 Task 1: News Topic Classification using BERT

## 📌 Objective

The goal of this task is to build a **news topic classification system** using a **Transformer-based model (BERT)**.
The model classifies news headlines into predefined categories using **transfer learning and fine-tuning**.

This project demonstrates hands-on experience with **Natural Language Processing (NLP)**, **transformer models**, and **model deployment**.

---

## 📊 Dataset

**AG News Dataset**

The AG News dataset contains news articles categorized into four classes:

* 🌍 World
* 🏅 Sports
* 💼 Business
* 🔬 Science & Technology

Each sample consists of:

* News title
* News description
* Corresponding label

🔹 *For faster experimentation and training efficiency, a randomized subset of the dataset was used while preserving class balance.*

---

## 🛠️ Technologies Used

* Python
* PyTorch
* Hugging Face Transformers
* Scikit-learn
* Pandas
* Gradio
* BERT (`bert-base-uncased`)

---

## 🔄 Methodology / Approach

### 1. Data Preprocessing

* Loaded AG News dataset from public CSV source
* Combined **title + description** into a single text field
* Converted labels to zero-based indexing
* Split data into:

  * Training set
  * Validation set
  * Test set

### 2. Tokenization

* Used **BERT tokenizer**
* Applied:

  * Padding
  * Truncation
  * Fixed maximum sequence length

### 3. Model Training

* Pre-trained **BERT Base (Uncased)** model
* Fine-tuned for **multi-class classification**
* Optimizer: **AdamW**
* Loss Function: **CrossEntropyLoss**
* Trained for a small number of epochs for efficiency

### 4. Model Evaluation

The model was evaluated on the test set using:

* **Accuracy**
* **Weighted F1-score**

### 5. Deployment

* Built an interactive web interface using **Gradio**
* Users can input a news headline and get the predicted topic in real time

---

## 📈 Results

* **Test Accuracy:** ~94%
* **Weighted F1-score:** ~94%

The model performs consistently well across all four categories.

---

## 🌐 Deployment

The trained model is deployed using **Gradio**, allowing real-time interaction through a web interface.

Users can:

* Enter a news headline
* Instantly receive the predicted topic

---

## ✅ Key Skills Gained

* NLP using Transformer models
* Fine-tuning pre-trained LLMs
* Text classification evaluation metrics
* Model deployment with Gradio
* Efficient dataset handling for faster training

---

## 📌 Conclusion

This task demonstrates how **pre-trained transformer models** like BERT can be effectively fine-tuned for real-world NLP tasks such as news classification.
The project highlights both **model performance** and **practical deployment**, making it suitable for production-style applications.

