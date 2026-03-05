from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint, Enum, Float
from database import Base, relationship

class Character(Base):
    __tablename__ = "characters"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    rarity = Column(
        Enum("SP", "UR", "SSR", "SR", name="character_rarity"), 
        nullable=False
    )
    school = Column(String, nullable=False)
    position = Column(String, nullable=False)
    
    # Relationships
    specialties = relationship("CharacterSpecialty", back_populates="character", cascade="all, delete") # reverses relationship
    stats = relationship("CharacterStat", back_populates="character", cascade="all, delete")
    skills = relationship("Skill", back_populates="character", cascade="all, delete")
    skill_resonances = relationship("SkillsResonance", back_populates="character", cascade="all, delete")
    
class CharacterStat(Base):
    __tablename__ = "character_stats"

    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey("characters.id"), nullable=False)
    stat_id = Column(Integer, ForeignKey("stats.id"), nullable=False)
    level = Column(Float, nullable=False)
    value = Column(Float, nullable=False)

    character = relationship("Character", back_populates="stats")
    stat = relationship("Stat", back_populates="character_stats")

    __table_args__ = (
        UniqueConstraint("char_id", "stat_id", name="uix_character_stat"),
    )
    
class CharacterSpecialty(Base):
    __tablename__ = 'character_specialties'
    
    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    specialty = Column(String, nullable=False)
    
    character = relationship("Character", back_populates="specialties")
    
    __table_args__ = (
        UniqueConstraint("char_id", "specialty", name="uix_char_specialty"),
    )

class SkillsResonance(Base):
    __tablename__ = 'skills_resonances'
    
    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    resonance_level = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    
    character = relationship("Character", back_populates="skill_resonances")
    
    # Only one row per resonance level
    __table_args__ = (
        UniqueConstraint('char_id', 'resonance_level', name='uix_char_resonance'),
    )
    
class Skill(Base):
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True)
    char_id = Column(Integer, ForeignKey('characters.id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    
    character = relationship("Character", back_populates="skills")
    skill_tags = relationship("SkillTag", back_populates="skill", cascade="all, delete")
    
class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True)
    tag = Column(String, nullable=False, unique=True)
    
    skill_tags = relationship("SkillTag", back_populates="tag", cascade="all, delete")

class SkillTag(Base):
    __tablename__ = "skill_tags"
    
    id = Column(Integer, primary_key=True)
    skill_id = Column(Integer, ForeignKey('skills.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tags.id'), nullable=False)
    
    skill = relationship("Skill", back_populates="skill_tags")
    tag = relationship("Tag", back_populates="skill_tags")
    
    # No duplicate tag pair
    __table_args__ = (
        UniqueConstraint('skill_id', 'tag_id', name='uix_skill_tag'),
    )
    
class Potentials(Base):
    __tablename__ = "potentials"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    color = Column(
        Enum("Gold", "Purple", "Blue", name="pot_color"),
        nullable=False
    )
    effect_2pc = Column(String, nullable=False)
    effect_4pc = Column(String, nullable=False)
    
class Stat(Base):
    __tablename__ = "stats"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    
    memory_stats = relationship("MemoryStat", back_populates="stat")
    character_stats = relationship("CharacterStat", back_populates="stat")
    
class Memory(Base):
    __tablename__ = "memories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    rarity = Column(
        Enum("SP", "UR", "SSR", "SR", name="memory_rarity"), 
        nullable=False
    )
    
    stats = relationship("MemoryStat", back_populates="memory", cascade="all, delete")
    tiers = relationship("MemoryTier", back_populates="memory", cascade="all, delete")
    
class MemoryStat(Base):
    __tablename__ = "memory_stats"
    
    id = Column(Integer, primary_key=True)
    memory_id = Column(Integer, ForeignKey("memories.id"), nullable=False)
    stat_id = Column(Integer, ForeignKey("stats.id"), nullable=False)
    
    level = Column(Integer, nullable=False)  # 1 or 80
    value = Column(Float, nullable=False)
    
    memory = relationship("Memory", back_populates="stats")
    stat = relationship("Stat", back_populates="memory_stats")

    __table_args__ = (
        UniqueConstraint('memory_id', 'stat_id', 'level', name='uix_memory_stat_level'),
    )
    
class MemoryTier(Base):
    __tablename__ = "memory_tiers"
    
    id = Column(Integer, primary_key=True)
    memory_id = Column(Integer, ForeignKey("memories.id"), nullable=False)
    tier = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    
    memory = relationship("Memory", back_populates="tiers")

    __table_args__ = (
        UniqueConstraint('memory_id', 'tier', name='uix_memory_tier'),
    )