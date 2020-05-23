"""Errors used in pyavanza."""


class AvanzaError(Exception):
    """Base error class for all pyavanza errors."""

    pass


class AvanzaRequestError(AvanzaError):
    """Raised when there is a request error."""

    pass


class AvanzaResponseError(AvanzaError):
    """Raised when there is a response error."""

    pass


class AvanzaParseError(AvanzaError):
    """Raised when there is a parse error."""

    pass
