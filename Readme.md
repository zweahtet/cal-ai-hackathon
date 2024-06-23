# Getting Started
**Install Python Virtual Environment**
```bash
pip install virtualenv
```

**Start python virtual environment**
```bash
python3 -m venv venv
```

**Activate python virtual environment**
```bash
source venv/bin/activate
```

**Install required packages**
```bash
pip install -r requirements.txt
```

**Add the following environment variables to the .env file**
```bash
HUME_API=<your_hume_api_key>
GROQ_API=<your_groq_api_key>
SERP_API=<your_serp_api_key>
```

**Run the application**
```bash
streamlit run app.py
```