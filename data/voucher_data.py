from dataclasses import dataclass


@dataclass
class Voucher:
    from_name: str = None
    from_email: str = None
    to_name: str = None
    to_email: str = None
    amount: int = None
    code: str = None
