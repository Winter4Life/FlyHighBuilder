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
    skills_resonances = relationship("SkillsResonance", backref="character")
    skills = relationship("Skills", backref="character")
    
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
        UniqueConstraint('char_id', 'resonance_level', name='uix_char_resonance'),
    )
    
class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    char_id = Column(Integer, ForeignKey('characters.id'))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    skilltags = relationship("SkillTag", backref="skill")
    
class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    tag = Column(String, nullable=False, unique=True)
    
    skilltags = relationship("SkillTag", backref="tag")

class SkillTag(Base):
    __tablename__ = "skill_tags"
    
    id = Column(Integer, primary_key=True, index=True)
    skill_id = Column(Integer, ForeignKey('skills.id'))
    tag_id = Column(Integer, ForeignKey('tags.id'))
    
    # No duplicate tag pair
    __table_args__ = (
        UniqueConstraint('skill_id', 'tag_id', name='uix_skill_tag'),
    )