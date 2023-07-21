from typing import List, Tuple
from django.db import models
import enum


class BaseEnum(str, enum.Enum):
    @classmethod
    def get_django_choices(cls) -> List[Tuple[str, str]]:
        return [(x.value, x.name) for x in cls]


class PgOrderStatusTypeField(models.CharField):
    def db_type(self, connection):
        return 'order_status_type'

class PgOrderStatusTypeEnum(BaseEnum):
    EnRoute = 'EnRoute'
    Suspended = 'Suspended'
    Canceled = 'Canceled'
    Shipped = 'Shipped'
    Error = 'Error'
    PaymentPending = 'PaymentPending'
    PaymentFailed = 'PaymentFailed'
    InDispute = 'InDispute'

class PgPaymentStatusTypeField(models.CharField):
    def db_type(self, connection):
        return 'payment_status_type'

class PgPaymentStatusTypeEnum(BaseEnum):
    CanceledSeller = 'Canceled-Seller'
    RejectedSeller = 'Rejected-Seller'
    CapturedManual = 'Captured-Manual'
    CapturedPP = 'Captured-PP'
    CapturedCC = 'Captured-CC'
    AuthorizedCC = 'Authorized-CC'
    RejectedAdmin = 'Rejected-Admin'
    Chargeback = 'Chargeback'
    CanceledAdmin = 'Canceled-Admin'
    PaymentPending = 'Payment-Pending'
    PaymentFailed = 'Payment-Failed'