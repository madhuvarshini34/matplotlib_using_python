from sqlalchemy import Column, Integer, String, Date, Enum, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    dob = Column(Date, nullable=False)
    gender = Column(Enum('Male', 'Female', 'Other'), nullable=False)
    department = Column(String(100), nullable=False)
    phonenumber = Column(String(15), unique=True, nullable=False)
    emailId = Column(String(100), unique=True, nullable=False)
    regNumber = Column(String(50), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
