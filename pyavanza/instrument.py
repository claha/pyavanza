"""Representation of an Instrument."""
from typing import Any, Dict, List

from pyavanza.const import InstrumentType
from pyavanza.error import AvanzaParseError


class Instrument:
    """Instrument object."""

    def __init__(self, type_: InstrumentType, json_data: Dict[str, Any]) -> None:
        """Initialize instrument object using json data."""
        self._type = type_
        try:
            self._id: str = json_data["id"]
            self._name: str = json_data["name"]
            self._ticker_symbol: str = json_data["tickerSymbol"]
            self._tradable: bool = json_data["tradable"]
        except KeyError as exception:
            raise AvanzaParseError(exception.args[0]) from exception

    def __str__(self) -> str:
        """Print the object as a string."""
        return "Instrument[{}]: {}".format(self._id, self._name)

    @property
    def type(self) -> InstrumentType:
        """Get type."""
        return self._type

    @property
    def id(self) -> str:
        """Get id."""
        return self._id

    @property
    def name(self) -> str:
        """Get name."""
        return self._name

    @property
    def ticker_symbol(self) -> str:
        """Get ticker symbol."""
        return self._ticker_symbol

    @property
    def tradable(self) -> bool:
        """Get tradable."""
        return self._tradable


def parse_instruments(json_data: Dict[str, Any]) -> List[Instrument]:
    """Parse json data into list of instruments."""
    instruments = []
    for search in json_data["hits"]:
        if "topHits" in search:
            for json_instrument in search["topHits"]:
                instruments.append(
                    Instrument(
                        InstrumentType[search["instrumentType"]], json_instrument
                    )
                )
    return instruments
