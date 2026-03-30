# Run Commands

## Step 1 - Start Backend

```powershell
cd backend
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8010
```

Or:

```powershell
cd backend
uvicorn app.main:app --reload
```

