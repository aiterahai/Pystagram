from project.core.models import Base
from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    parent_id = Column(Integer, ForeignKey("parent.id"), nullable=True)

    post = relationship("Post", backref="comments", foreign_key=[post_id])
    user = relationship("User", foreign_key=[user_id])
    parent = relationship("Comment", foreign_key=[parent_id])