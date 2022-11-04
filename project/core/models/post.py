from project.core.models import Base
from sqlalchemy import Integer, String, DateTime, Column, ForeignKey
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(2000), nullable=False)
    post_image = Column(String(500), nullable=True)
    created_at = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", backref="posts", foregin_keys=[user_id])