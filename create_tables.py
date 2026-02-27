from database import engine, Base
from models import Character, CharacterSpecialty

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")   # Testing