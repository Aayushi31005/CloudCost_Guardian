from app.db.base import Base
from app.db.session import engine
from app.db.models import usage  # ensure table registration
from app.db.models import cost
def init_db():
    Base.metadata.create_all(bind=engine)
    
