"""This module implement API environment enum"""
from enum import Enum, unique

API_URLS = {
    0: "https://checkout.test.getnet.cl",
    1: "",
    2: "https://checkout.getnet.cl",
}


@unique
class Environment(Enum):
    """Environment represents the API envinments specs"""

    SANDBOX = 0
    HOMOLOG = 1
    PRODUCTION = 2

    def base_url(self) -> str:
        return API_URLS[self.value]
