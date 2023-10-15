from dataclasses import dataclass


@dataclass
class Coupon:
    coupon_name: str = None
    coupon_code: int = None
    coupon_type: str = None
    coupon_discount: float = None
    coupon_logged: int = None
    coupon_shipping: int = None
    coupon_total: float = None
    coupon_date_start: str = None
    coupon_date_end: str = None
    coupon_uses_total: int = None
    coupon_uses_customer: int = None
    coupon_status: int = None
    coupon_date_added: str = None
