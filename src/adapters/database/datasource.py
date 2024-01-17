from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/condoledger", echo=True
)


def get_session():
    with Session(engine) as session:
        yield session
