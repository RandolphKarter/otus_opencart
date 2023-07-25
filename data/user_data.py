from dataclasses import dataclass


@dataclass
class User:
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    password: str = None
