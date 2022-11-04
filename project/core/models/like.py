from project.core.models import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Like(Base):
    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("post.id"), primary_key=True, index=True)

    user = relationship("User", backref="liked_post", foreign_key=[user_id])
    post = relationship("Post", backref="liked_users", foreign_key=[post_id])