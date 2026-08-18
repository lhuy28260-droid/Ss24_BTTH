from enum import Enum

class Role(str, Enum):
    ADMIN = "ADMIN"
    HR = "HR"
    STAFF = "STAFF"