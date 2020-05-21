"""Constants used in pyavanza."""
from enum import Enum

AVANZA_API_BASE_URL = "https://www.avanza.se/_mobile/market"
AVANZA_API_STOCK_URL = AVANZA_API_BASE_URL + "/stock/{id}"
AVANZA_API_SEARCH_URL = AVANZA_API_BASE_URL + "/search?query={query}&limit={limit}"
AVANZA_API_SEARCH_INSTRUMENT_URL = (
    AVANZA_API_BASE_URL + "/search/{instrument}?query={query}&limit={limit}"
)


class Instrument(Enum):
    """Instrument types."""

    ANY = "ANY"
    BOND = "BOND"
    CERTIFICATE = "CERTIFICATE"
    CONVERTIBLE = "CONVERTIBLE"
    EQUITY_LINKED_BOND = "EQUITY_LINKED_BOND"
    EXCHANGE_TRADED_FUND = "EXCHANGE_TRADED_FUND"
    FUND = "FUND"
    FUTURE_FORWARD = "FUTURE_FORWARD"
    INDEX = "INDEX"
    OPTION = "OPTION"
    PREMIUM_BOND = "PREMIUM_BOND"
    RIGHT = "RIGHT"
    STOCK = "STOCK"
    SUBSCRIPTION_OPTION = "SUBSCRIPTION_OPTION"
    WARRANT = "WARRANT"
