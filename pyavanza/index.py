"""Representation of a Index."""
from typing import Any, Dict

from pyavanza.error import AvanzaParseError


class Index:
    """Index object."""

    def __init__(self, json_data: Dict[str, Any]) -> None:
        """Initialize index object using json data."""
        try:
            self._change: float = json_data["change"]
            self._change_percent: float = json_data["changePercent"]
            self._currency: str = json_data["currency"]
            self._id: str = json_data["id"]
            self._name: str = json_data["name"]
            self._push_permitted: bool = json_data["pushPermitted"]
            self._quote_updated: str = json_data["quoteUpdated"]
        except KeyError as exception:
            raise AvanzaParseError(exception.args[0]) from exception

        self._description: str = json_data.get("description", None)
        self._flag_code: str = json_data.get("flagCode", None)
        self._highest_price: float = json_data.get("highestPrice", None)
        self._last_price: float = json_data.get("lastPrice", None)
        self._last_price_updated: str = json_data.get("lastPriceUpdated", None)
        self._lowest_price: float = json_data.get("lowestPrice", None)
        self._price_at_start_of_year: float = json_data.get("priceAtStartOfYear", None)
        self._price_five_years_ago: float = json_data.get("priceFiveYearsAgo", None)
        self._price_one_month_ago: float = json_data.get("priceOneMonthAgo", None)
        self._price_one_week_ago: float = json_data.get("priceOneWeekAgo", None)
        self._price_one_year_ago: float = json_data.get("priceOneYearAgo", None)
        self._price_six_months_ago: float = json_data.get("priceSixMonthsAgo", None)
        self._price_three_months_ago: float = json_data.get("priceThreeMonthsAgo", None)
        self._price_three_years_ago: float = json_data.get("priceThreeYearsAgo", None)
        self._title: str = json_data.get("title", None)

    def __str__(self) -> str:
        """Print the object as a string."""
        return "Index[{}]: {}".format(self._id, self._name)

    @property
    def change(self) -> float:
        """Get change."""
        return self._change

    @property
    def change_percent(self) -> float:
        """Get change percent."""
        return self._change_percent

    @property
    def currency(self) -> str:
        """Get currency."""
        return self._currency

    @property
    def description(self) -> str:
        """Get description."""
        return self._description

    @property
    def flag_code(self) -> str:
        """Get flag code."""
        return self._flag_code

    @property
    def highest_price(self) -> float:
        """Get highest price."""
        return self._highest_price

    @property
    def id(self) -> str:
        """Get id."""
        return self._id

    @property
    def last_price(self) -> float:
        """Get last price."""
        return self._last_price

    @property
    def last_price_updated(self) -> str:
        """Get last price updated."""
        return self._last_price_updated

    @property
    def lowest_price(self) -> float:
        """Get lowest price."""
        return self._lowest_price

    @property
    def name(self) -> str:
        """Get name."""
        return self._name

    @property
    def price_at_start_of_year(self) -> float:
        """Get price at start of year."""
        return self._price_at_start_of_year

    @property
    def price_five_years_ago(self) -> float:
        """Get price five years ago."""
        return self._price_five_years_ago

    @property
    def price_one_month_ago(self) -> float:
        """Get price one month ago."""
        return self._price_one_month_ago

    @property
    def price_one_week_ago(self) -> float:
        """Get price one week ago."""
        return self._price_one_week_ago

    @property
    def price_one_year_ago(self) -> float:
        """Get price one year ago."""
        return self._price_one_year_ago

    @property
    def price_six_months_ago(self) -> float:
        """Get price six months ago."""
        return self._price_six_months_ago

    @property
    def price_three_months_ago(self) -> float:
        """Get price three months ago."""
        return self._price_three_months_ago

    @property
    def price_three_years_ago(self) -> float:
        """Get price three years ago."""
        return self._price_three_years_ago

    @property
    def push_permitted(self) -> bool:
        """Get push permitted."""
        return self._push_permitted

    @property
    def quote_updated(self) -> str:
        """Get quote updated."""
        return self._quote_updated

    @property
    def title(self) -> str:
        """Get title."""
        return self._title
