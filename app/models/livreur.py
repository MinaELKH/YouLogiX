from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Livreur(Base):
    __tablename__ = "livreurs"
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    prenom = Column(String)
    telephone = Column(String)
    vehicule = Column(String)
    zone_assignee = Column(String)

    colis = relationship("Colis", back_populates="livreur")