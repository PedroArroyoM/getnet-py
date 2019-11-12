from datetime import datetime
from typing import Union

from dateutil import parser

from getnet.services.payments.credit.credit import Credit


class CreditResponse(Credit):
    authorization_code: str
    authorized_at: datetime
    reason_code: int
    reason_message: str
    acquirer: str
    acquirer_transaction_id: str
    terminal_nsu: str
    transaction_id: str
    brand: str

    def __init__(
        self,
        authorization_code: str,
        authorized_at: Union[datetime, str],
        reason_code: int,
        reason_message: str,
        acquirer: str,
        acquirer_transaction_id: str,
        terminal_nsu: str,
        transaction_id: str,
        brand: str,
        **kwargs,
    ):
        self.authorization_code = authorization_code
        self.authorized_at = (
            authorized_at
            if isinstance(authorized_at, datetime)
            else parser.isoparse(authorized_at)
        )
        self.reason_code = reason_code
        self.reason_message = reason_message
        self.acquirer = acquirer
        self.acquirer_transaction_id = acquirer_transaction_id
        self.terminal_nsu = terminal_nsu
        self.transaction_id = transaction_id
        self.brand = brand
        kwargs.update({"card": None})
        super(CreditResponse, self).__init__(**kwargs)
