from database import engine, Base
from models import Character, CharacterSpecialty, SkillsResonance, Skill, Tag, SkillTag

Base.metadata.create_all(bind=engine)
print("Tables created successfully!")   # Testing