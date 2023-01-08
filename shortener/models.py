from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from extensions import db
import random
import string
import datetime
from dateutil.relativedelta import relativedelta
from sqlalchemy_serializer import SerializerMixin


class Url(db.Model, SerializerMixin):
    """Data model for shortened urls."""

    __tablename__ = "urls"

    serialize_rules = ("-id", "-user_id", "-user")

    id = Column(Integer, primary_key=True)
    url_long = Column(String(2048), nullable=False)
    url_short = Column(String(8), unique=True, nullable=False)
    expiration = Column(DateTime)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref="url", foreign_keys=[user_id])

    def __init__(self, **kwargs):

        self.url_long = kwargs.get("url_long")
        self.url_short = kwargs.get("url_short")
        self.expiration = kwargs.get(
            "expiration", datetime.datetime.today() + relativedelta(months=12)
        )
        self.user_id = kwargs.get("user_id")

    def __repr__(self):

        return f"<Url {self.url_short}>"

    def hash_url(self, length: int = 8):
        """
        Hash url from url_long field and store it inside url_short field.
        """

        self.url_short = "".join(
            random.SystemRandom().choice(
                string.ascii_uppercase + string.ascii_lowercase + string.digits
            )
            for _ in range(length)
        )
