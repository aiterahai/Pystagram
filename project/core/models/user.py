from project.core.models import Base
from sqlalchemy import Column, String, CHAR, Integer


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    account_id = Column(String(20), nullable=False, index=True)
    password = Column(CHAR(60), nullable=False)
    phone_number = Column(CHAR(11), nullable=False)
    profile_image = Column(String(500), nullable=True)