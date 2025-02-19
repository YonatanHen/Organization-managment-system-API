from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column, declarative_base
from typing import List

Base = declarative_base()

class Organization(Base):
    __tablename__ = "organizations"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    endpoints: Mapped[List['Endpoint']] = relationship(backref='organization', cascade="all, delete-orphan")
    
class Endpoint(Base):
    __tablename__ = "endpoints"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    organization_id: Mapped[int] = mapped_column(ForeignKey('organizations.id', ondelete='CASCADE'))
    users: Mapped[List['User']] = relationship(backref='endpoint', cascade="all, delete-orphan")
    
    # Allows the same name to exist in multiple organizations, but it prevents duplicate endpoint names within the same organization.
    __table_args__ = (UniqueConstraint('name', 'organization_id', name='uq_name_organization'),)

    
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    endpoint_id: Mapped[int] = mapped_column(ForeignKey('endpoints.id', ondelete='CASCADE'))