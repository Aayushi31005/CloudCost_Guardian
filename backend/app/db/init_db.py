from app.db.base import Base
from app.db.session import engine
from app.db.models import usage  # ensure table registration

def init_db():
    Base.metadata.create_all(bind=engine)
    
