from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
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
    SkillsResonance = relationship("SkillsResonance", backref="character")
    
class CharacterSpecialty(Base):
    __tablename__ = 'character_specialties'
    
    id = Column(Integer, primary_key=True, index=True)
    char_id = Column(Integer, ForeignKey('characters.id'))
    specialty = Column(String, nullable=False)

class SkillsResonance(Base):
    __tablename__ = 'skills_resonances'
    
    id = Column(Integer, primary_key=True, index=True)
    char_id = Column(Integer, ForeignKey('characters.id'))
    resonance_level = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    
    # Only one row per resonance level
    __table_args__ = (
        UniqueConstraint('char_id', 'resonance_level', name='uix_char_resonance')
    )