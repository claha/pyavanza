"""Errors used in pyavanza."""


class AvanzaError(Exception):
    """Base error class for all pyavanza errors."""


class AvanzaRequestError(AvanzaError):
    """Raised when there is a request error."""


class AvanzaResponseError(AvanzaError):
    """Raised when there is a response error."""


class AvanzaParseError(AvanzaError):
    """Raised when there is a parse error."""
