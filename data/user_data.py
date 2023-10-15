from dataclasses import dataclass


@dataclass
class User:
    first_name: str = None
    last_name: str = None
    email: str = None
    phone: str = None
    password: str = None
    address: str = None
    city: str = None
    country_id: any = None
    zone_id: any = None
