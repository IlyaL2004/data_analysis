import datetime
from app.core.datagase import Base
from sqlalchemy.orm import Mapped, mapped_column


class Visits(Base):
    __tablename__ = "visits"
    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    user_email: Mapped[str]
    site_id: Mapped[int]
    date: Mapped[datetime.datetime]
    admin_name: Mapped[str]