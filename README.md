# AI CV Analyzer

An AI-powered Resume Analysis platform that evaluates resumes using ATS scoring, job matching, GitHub profile analysis, and personalized career recommendations. The application helps candidates understand how well their resume aligns with a target job description and provides actionable suggestions for improvement. A good README should clearly explain what the project does, how to run it, and where to access it. :contentReference[oaicite:0]{index=0}

## 🌐 Live Demo

**Frontend:**  
https://cv-analyzer-iq77ro1qk-byniemoser07s-projects.vercel.app/

**Backend API:**  
https://cv-analyzer-3p31.onrender.com

**API Documentation (Swagger):**  
https://cv-analyzer-3p31.onrender.com/docs

---

## ✨ Features

- Resume Upload (PDF)
- Resume Parsing
- ATS Score Analysis
- Resume Completeness Check
- Resume Grade
- Resume Feedback & Suggestions
- Job Description Matching
- Keyword Matching
- Semantic Resume Matching
- Skill Gap Analysis
- Missing Skills Priority
- GitHub Profile Analysis
- GitHub Score
- Recommended Job Roles
- Learning Roadmap
- Hiring Recommendation
- Candidate Ranking
- Salary Prediction
- Interview Readiness Score
- Personalized Interview Questions
- Dashboard Analytics
- Resume Improvement Tips

---

## 🛠 Tech Stack

### Frontend
- React.js
- Vite
- Axios
- CSS

### Backend
- FastAPI
- Python

### AI / NLP
- Sentence Transformers
- Scikit-learn
- spaCy
- Regular Expression based Resume Parsing

### APIs
- GitHub REST API

### Deployment
- Vercel
- Render

---

## 📁 Project Structure

```
cv-analyzer/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── analyzers/
│   │   ├── parser/
│   │   ├── routers/
│   │   ├── github/
│   │   ├── nlp/
│   │   └── main.py
│   │
│   ├── uploads/
│   ├── requirements.txt
│   └── runtime.txt
│
└── README.md
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/byniemoser07/cv-analyzer.git

cd cv-analyzer
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download the spaCy model

```bash
python -m spacy download en_core_web_sm
```

Run the backend

```bash
uvicorn app.main:app --reload
```

Backend runs on

```
http://localhost:8000
```

---

## Frontend Setup

```bash
cd frontend

npm install
```

Create a `.env` file

```env
VITE_API_URL=http://localhost:8000
```

Run

```bash
npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/analyze-profile` | Analyze Resume |
| GET | `/docs` | Swagger Documentation |
| GET | `/about` | Project Information |
| GET | `/` | API Status |

---

## Sample Workflow

1. Upload Resume (PDF)
2. Enter Target Job Description
3. Enter GitHub Username (Optional)
4. Click **Analyze**
5. View:
   - ATS Score
   - Job Match
   - Skill Gap
   - GitHub Analysis
   - Interview Questions
   - Learning Roadmap
   - Resume Feedback
   - Recommended Roles

---

## Future Improvements

- Authentication
- Resume Version History
- Multiple Resume Comparison
- Cover Letter Generator
- AI Chat Assistant
- LinkedIn Profile Analysis
- Export Report as PDF

---

## Author

**Akarshit Singh**

GitHub: https://github.com/byniemoser07

LinkedIn: https://www.linkedin.com/in/akarshit-singh/

---

## License

This project is intended for educational and internship assignment purposes.
