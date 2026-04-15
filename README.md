# Skill-Gap-Intelligence
made a batch script file
./start.sh

    created virtual environment and activate
    python -m venv venv
    venv\Scripts\activate
    deactivate

    To run 
    uvicorn backend.app.main:app --reload
    # main:app here main is file name and app is instance inside it 
```
skill-gap-intelligence/         # Root project folder
│
├── backend/                    # All backend code
│   ├── app/
│   │   ├── main.py             # FastAPI entrypoint
│   │
│   │   ├── api/
│   │   │   └── routes.py       # Future API endpoints
│   │
│   │   ├── services/           # Core Python modules
│   │   │   ├── resume_parser.py
│   │   │   ├── skill_extractor.py
│   │   │   ├── similarity_engine.py
│   │   │   ├── gap_analyzer.py
│   │   │   ├── pdf_generator.py      # Will implement later
│   │   │   └── email_sender.py       # Will implement later
│   │   │
│   │   ├── db.py
│   │   │                             # MongoDB connection
│   │   │
│   │   └── utils/
│   │       ├── logging_config.py    # Will implement later
│   │       └── config.py            # Environment/config variables
│
├── tests/                     # Unit tests (pytest)
│   ├── test_skill_extractor.py     # Will implement later
│   └── test_similarity.py          # Will implement later
│
├── docs/                      # Documentation
│   ├── architecture.md
│   └── api_docs.md
│
├── venv/                      # Virtual environment (auto-created)
│
├── requirements.txt           # Installed Python packages
├── Dockerfile                 # Container setup (later)
├── .gitignore                 # Ignore venv, pycache, env, etc.
├── README.md                  # Project overview & instructions
└── .env                       # Environment variables (MongoDB URI, etc.)
```

Redis, Doc and Pdf support, email incorporate, kafka if needed
