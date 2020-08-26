"""Representation of a Exchange Traded Fund."""
from typing import Any, Dict

from pyavanza.error import AvanzaParseError


class ExchangeTradedFund:
    """Exchange Traded Fund object."""

    def __init__(self, json_data: Dict[str, Any]) -> None:
        """Initialize exchange traded fund object using json data."""
        try:
            self._change: float = json_data["change"]
            self._change_percent: float = json_data["changePercent"]
            self._currency: str = json_data["currency"]
            self._flag_code: str = json_data["flagCode"]
            self._has_investment_fees: bool = json_data["hasInvestmentFees"]
            self._id: str = json_data["id"]
            self._isin: str = json_data["isin"]
            self._loan_factor: float = json_data["loanFactor"]
            self._market_place: str = json_data["marketPlace"]
            self._name: str = json_data["name"]
            self._push_permitted: bool = json_data["pushPermitted"]
            self._quote_updated: str = json_data["quoteUpdated"]
            self._ticker_symbol: str = json_data["tickerSymbol"]
            self._total_value_traded: float = json_data["totalValueTraded"]
            self._total_volume_traded: int = json_data["totalVolumeTraded"]
            self._tradable: bool = json_data["tradable"]
        except KeyError as exception:
            raise AvanzaParseError(exception.args[0]) from exception

        # Not all exchange traded funds have a category
        self._asset_root_category: str = json_data.get("assetRootCategory", None)
        self._asset_sub_category: str = json_data.get("assetSubCategory", None)
        self._asset_sub_sub_category: str = json_data.get("assetSubSubCategory", None)
        # Not all exchange traded funds have a direciton
        self._direction: str = json_data.get("direction", None)
        # Could be missing if no transactions have been made
        self._buy_price: float = json_data.get("buyPrice", None)
        self._highest_price: float = json_data.get("highestPrice", None)
        self._last_price: float = json_data.get("lastPrice", None)
        self._last_price_updated: str = json_data.get("lastPriceUpdated", None)
        self._lowest_price: float = json_data.get("lowestPrice", None)
        self._sell_price: float = json_data.get("sellPrice", None)
        self._underlying_orderbook: Dict[str, Any] = json_data.get(
            "underlyingOrderbook", None
        )
        # Not all exchange traded funds have and issuer
        self._issuer_name: str = json_data.get("issuerName", None)
        # Not all exchange traded funds have a leverage
        self._leverage: float = json_data.get("leverage", None)
        # Not all exchange traded funds have a management fee
        self._management_fee: float = json_data.get("managementFee", None)
        # Could be missing if exchange traded fund has not been on the market long enough
        self._price_at_start_of_year: float = json_data.get("priceAtStartOfYear", None)
        self._price_five_years_ago: float = json_data.get("priceFiveYearsAgo", None)
        self._price_one_month_ago: float = json_data.get("priceOneMonthAgo", None)
        self._price_one_week_ago: float = json_data.get("priceOneWeekAgo", None)
        self._price_one_year_ago: float = json_data.get("priceOneYearAgo", None)
        self._price_six_months_ago: float = json_data.get("priceSixMonthsAgo", None)
        self._price_three_months_ago: float = json_data.get("priceThreeMonthsAgo", None)
        self._price_three_years_ago: float = json_data.get("priceThreeYearsAgo", None)
        # Not all exchange traded fund have a priip document or prospectus
        self._priip_document_url: str = json_data.get("priipDocumentUrl", None)
        self._prospectus: str = json_data.get("prospectus", None)
        # Not all exchange traded funds have a start date
        self._start_date: str = json_data.get("startDate", None)
        # Not all exchange traded funds have a spread
        self._spread: float = json_data.get("spread", None)

    def __str__(self) -> str:
        """Print the object as a string."""
        return "Exchange Traded Fund[{}]: {}".format(self._id, self._name)

    @property
    def asset_root_category(self) -> str:
        """Get asset root category."""
        return self._asset_root_category

    @property
    def asset_sub_category(self) -> str:
        """Get asset sub category."""
        return self._asset_sub_category

    @property
    def asset_sub_sub_category(self) -> str:
        """Get asset sub sub category."""
        return self._asset_sub_sub_category

    @property
    def buy_price(self) -> float:
        """Get buy price."""
        return self._buy_price

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
    def direction(self) -> str:
        """Get direction."""
        return self._direction

    @property
    def flag_code(self) -> str:
        """Get flag code."""
        return self._flag_code

    @property
    def has_investment_fees(self) -> bool:
        """Get has investment fees."""
        return self._has_investment_fees

    @property
    def highest_price(self) -> float:
        """Get highest price."""
        return self._highest_price

    @property
    def id(self) -> str:
        """Get id."""
        return self._id

    @property
    def isin(self) -> str:
        """Get isin."""
        return self._isin

    @property
    def issuer_name(self) -> str:
        """Get issuer name."""
        return self._issuer_name

    @property
    def last_price(self) -> float:
        """Get last price."""
        return self._last_price

    @property
    def last_price_updated(self) -> str:
        """Get last price updated."""
        return self._last_price_updated

    @property
    def leverage(self) -> float:
        """Get leverage."""
        return self._leverage

    @property
    def loan_factor(self) -> float:
        """Get loan factor."""
        return self._loan_factor

    @property
    def lowest_price(self) -> float:
        """Get lowest price."""
        return self._lowest_price

    @property
    def management_fee(self) -> float:
        """Get management fee."""
        return self._management_fee

    @property
    def market_place(self) -> str:
        """Get market place."""
        return self._market_place

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
    def priip_document_url(self) -> str:
        """Get priip document url."""
        return self._priip_document_url

    @property
    def prospectus(self) -> str:
        """Get prospectus."""
        return self._prospectus

    @property
    def push_permitted(self) -> bool:
        """Get push permitted."""
        return self._push_permitted

    @property
    def quote_updated(self) -> str:
        """Get quote updated."""
        return self._quote_updated

    @property
    def sell_price(self) -> float:
        """Get sell price."""
        return self._sell_price

    @property
    def spread(self) -> float:
        """Get spread."""
        return self._spread

    @property
    def start_date(self) -> str:
        """Get start date."""
        return self._start_date

    @property
    def ticker_symbol(self) -> str:
        """Get ticker symbol."""
        return self._ticker_symbol

    @property
    def total_value_traded(self) -> float:
        """Get total value traded."""
        return self._total_value_traded

    @property
    def total_volume_traded(self) -> int:
        """Get total volume traded."""
        return self._total_volume_traded

    @property
    def tradable(self) -> bool:
        """Get tradable."""
        return self._tradable

    @property
    def underlying_orderbook(self) -> Dict[str, Any]:
        """Get underlying orderbook."""
        return self._underlying_orderbook
