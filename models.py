from sqlalchemy import Column, ForeignKey, Integer, String
from database import Base, relationship

class Character(Base):
    __tablename__ = 'characters'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    rarity = Column(String, nullable=False)
    school = Column(String, nullable=False)
    position = Column(String, nullable=False)
    
    # Relationship
    character_specialties = relationship("CharacterSpecialty", backref="character") # reverses relationship
    
class CharacterSpecialty(Base):
    __tablename__ = 'character_specialties'
    
    id = Column(Integer, primary_key=True, index=True)
    char_id = Column(Integer, ForeignKey('characters.id'))
    specialty = Column(String, nullable=False)
