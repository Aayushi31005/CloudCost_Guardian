cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
or 
uvicorn app.main:app --reload
