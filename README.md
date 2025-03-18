# 🧐 fc-gpt: AI Fact Verifier

## 📌 Overview
**fc-gpt** is an AI-powered fact verification system that checks the truthfulness of a claim by retrieving evidence and analyzing it using **GPT-3.5 Turbo** and **RoBERTa-based Natural Language Inference (NLI)**.  

The system is designed to be **accurate, strict, and reliable**, reducing false positives while correctly verifying factual claims.

---

## ⚡ Features
👉 **AI Fact-Checking** – Uses **GPT-3.5 Turbo** and **NLI (RoBERTa-large-mnli)**  
👉 **Strict Verification** – Only confirms claims **with strong supporting evidence**  
👉 **Hybrid AI Model** – GPT-3.5 checks first, NLI acts as a backup  
👉 **Web-Based Interface** – Easy-to-use **Streamlit frontend**  
👉 **FastAPI Backend** – High-performance fact-checking API  

---

## 🏗️ Project Structure
```
fc-gpt/
│-- backend/            # FastAPI backend
│   ├-- main.py         # API server handling requests
│   ├-- retrieval.py    # Retrieves evidence from the web
│   ├-- explanation.py  # Fact-checking using GPT & NLI
│   ├-- config.py       # Stores API keys
│   ├-- requirements.txt # Backend dependencies
│-- frontend/           # Streamlit-based UI
│   ├-- app.py         # Main frontend file
│   ├-- requirements.txt # Frontend dependencies
│-- README.md           # Documentation
```

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/fc-gpt.git
cd fc-gpt
```

### **2️⃣ Set Up the Backend**
```sh
cd backend
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate      # For Windows
pip install -r requirements.txt
```
- **Set up your API keys** in `config.py`:
```python
OPENAI_API_KEY = "your-openai-api-key"
SERPAPI_KEY = "your-serpapi-key"
```

### **3️⃣ Run FastAPI Backend**
```sh
uvicorn main:app --reload
```
- **Backend runs at**: `http://127.0.0.1:8000`
- **Test API**:
  ```sh
  curl -X POST "http://127.0.0.1:8000/fact-check" -H "Content-Type: application/json" -d '{"claim": "The Eiffel Tower is in Paris."}'
  ```

---

## 🎨 Running the Frontend (Streamlit UI)
### **1️⃣ Set Up the Frontend**
```sh
cd frontend
pip install -r requirements.txt
```

### **2️⃣ Run the UI**
```sh
streamlit run app.py
```
- **Frontend runs at**: `http://localhost:8501`
- Enter a claim in the text box and click **"Verify Claim"** to see results.

---

## 🔍 How It Works

### **1️⃣ Evidence Retrieval**
- Uses **SerpAPI (Google Search API)** to find **relevant sources**.
- Extracts the most relevant snippet of **factual information**.

### **2️⃣ Fact-Checking with AI**
- **First Step:** **GPT-3.5 Turbo** analyzes whether the claim is **fully supported**, **contradicted**, or **inconclusive**.
- **Second Step (if needed):** **RoBERTa (NLI)** checks if the evidence **entails, contradicts, or is neutral** to the claim.
- If both models are unsure, it **returns "Unknown".**

### **3️⃣ Response Format**
The system provides:
- **Claim:** What the user entered.
- **Evidence:** The most relevant factual snippet.
- **Result:** ✅ **True**, ❌ **False**, ⚠️ **Unknown**

---

## 📜 API Reference

### **1️⃣ Fact-Check Endpoint**
#### **`POST /fact-check`**
Verifies a claim's accuracy based on evidence.

📌 **Example Request:**
```json
{
  "claim": "The Eiffel Tower is in Paris."
}
```

📌 **Example Response:**
```json
{
  "claim": "The Eiffel Tower is in Paris.",
  "evidence": "The Eiffel Tower is a famous landmark located in Paris, France.",
  "is_true": true
}
```

---

## 🛠️ Troubleshooting

### **Backend Not Starting?**
- Ensure you've installed dependencies:
  ```sh
  pip install -r backend/requirements.txt
  ```
- Make sure your API keys are correctly set in `config.py`.

### **Frontend Not Loading?**
- Ensure **FastAPI is running** first before launching Streamlit.
- Check for any errors in the **backend terminal**.

---

## 📌 Future Improvements
✅ **Improve Accuracy** – Tune GPT and NLI models for better fact-checking.  
✅ **Customizable Model Selection** – Allow users to choose different AI models.  
✅ **More Data Sources** – Expand retrieval to Wikipedia, News APIs, and more.  
✅ **Mobile Support** – Improve UI for better usability on mobile devices.  

---

## 👨‍💻 Contributors
- **Your Name** – *Developer & Researcher*
- **Other Contributors** – *Optional*

Feel free to contribute! Open a pull request or create an issue.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## ⭐ Support & Feedback
If you find this project useful, consider **starring** the repository on GitHub! 🌟  
For any questions, open an **issue** or contact me.

---

