"""Representation of a Stock."""
from typing import Any, Dict, List

from pyavanza.error import AvanzaParseError


class Stock:
    """Stock object."""

    def __init__(self, json_data: Dict[str, Any]) -> None:
        """Initialize stock object using json data."""
        try:
            self._annual_meetings: List[Dict[str, Any]] = json_data["annualMeetings"]
            self._broker_trade_summary: Dict[str, Any] = json_data["brokerTradeSummary"]
            self._change: float = json_data["change"]
            self._change_percent: float = json_data["changePercent"]
            self._company_reports: List[Dict[str, str]] = json_data["companyReports"]
            self._country: str = json_data["country"]
            self._currency: str = json_data["currency"]
            self._dividends: List[Dict[str, Any]] = json_data["dividends"]
            self._flag_code: str = json_data["flagCode"]
            self._has_investment_fees: bool = json_data["hasInvestmentFees"]
            self._id: str = json_data["id"]
            self._isin: str = json_data["isin"]
            self._latest_trades: List[Dict[str, Any]] = json_data["latestTrades"]
            self._loan_factor: float = json_data["loanFactor"]
            self._market_maker_expected: bool = json_data["marketMakerExpected"]
            self._market_place: str = json_data["marketPlace"]
            self._market_trades: bool = json_data["marketTrades"]
            self._name: str = json_data["name"]
            self._number_of_owners: int = json_data["numberOfOwners"]
            self._order_depth_levels: List[Dict[str, Any]] = json_data[
                "orderDepthLevels"
            ]
            self._push_permitted: bool = json_data["pushPermitted"]
            self._quote_updated: str = json_data["quoteUpdated"]
            self._related_stocks: List[Dict[str, Any]] = json_data["relatedStocks"]
            self._short_sellable: bool = json_data["shortSellable"]
            self._super_loan: bool = json_data["superLoan"]
            self._ticker_symbol: str = json_data["tickerSymbol"]
            self._total_value_traded: float = json_data["totalValueTraded"]
            self._total_volume_traded: int = json_data["totalVolumeTraded"]
            self._tradable: bool = json_data["tradable"]
        except KeyError as exception:
            raise AvanzaParseError(exception.args[0]) from exception

        # Could be missing if no transactions have been made
        self._buy_price: float = json_data.get("buyPrice", None)
        self._highest_price: float = json_data.get("highestPrice", None)
        self._last_price: float = json_data.get("lastPrice", None)
        self._last_price_updated: str = json_data.get("lastPriceUpdated", None)
        self._lowest_price: float = json_data.get("lowestPrice", None)
        self._order_depth_received_time: str = json_data.get(
            "orderDepthReceivedTime", None
        )
        self._sell_price: float = json_data.get("sellPrice", None)
        # Company information is not available for all stocks
        self._company: Dict[str, Any] = json_data.get("company", None)
        self._company_owners: Dict[str, Any] = json_data.get("companyOwners", None)
        # Not available for all stocks
        self._key_ratios: Dict[str, float] = json_data.get("keyRatios", None)
        # Not all market places has a market list
        self._market_list: str = json_data.get("marketList", None)
        # Not available for all stocks
        self._morning_star_fact_sheet_url: str = json_data.get(
            "morningStarFactSheetUrl", None
        )
        # Could be missing if stock has not been on the market long enough
        self._price_at_start_of_year: float = json_data.get("priceAtStartOfYear", None)
        self._price_five_years_ago: float = json_data.get("priceFiveYearsAgo", None)
        self._price_one_month_ago: float = json_data.get("priceOneMonthAgo", None)
        self._price_one_week_ago: float = json_data.get("priceOneWeekAgo", None)
        self._price_one_year_ago: float = json_data.get("priceOneYearAgo", None)
        self._price_six_months_ago: float = json_data.get("priceSixMonthsAgo", None)
        self._price_three_months_ago: float = json_data.get("priceThreeMonthsAgo", None)
        self._price_three_years_ago: float = json_data.get("priceThreeYearsAgo", None)

    def __str__(self) -> str:
        """Print the object as a string."""
        return "Stock[{}]: {}".format(self._id, self._name)

    @property
    def annual_meetings(self) -> List[Dict[str, Any]]:
        """Get annual meetings."""
        return self._annual_meetings

    @property
    def broker_trade_summary(self) -> Dict[str, Any]:
        """Get broker trade summary."""
        return self._broker_trade_summary

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
    def company(self) -> Dict[str, Any]:
        """Get company."""
        return self._company

    @property
    def company_owners(self) -> Dict[str, Any]:
        """Get company owners."""
        return self._company_owners

    @property
    def company_reports(self) -> List[Dict[str, str]]:
        """Get company reports."""
        return self._company_reports

    @property
    def country(self) -> str:
        """Get country."""
        return self._country

    @property
    def currency(self) -> str:
        """Get currency."""
        return self._currency

    @property
    def dividends(self) -> List[Dict[str, Any]]:
        """Get dividends."""
        return self._dividends

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
    def key_ratios(self) -> Dict[str, Any]:
        """Get key ratios."""
        return self._key_ratios

    @property
    def last_price(self) -> float:
        """Get last price."""
        return self._last_price

    @property
    def last_price_updated(self) -> str:
        """Get last price updated."""
        return self._last_price_updated

    @property
    def latest_trades(self) -> List[Dict[str, Any]]:
        """Get latest trades."""
        return self._latest_trades

    @property
    def loan_factor(self) -> float:
        """Get loan factor."""
        return self._loan_factor

    @property
    def lowest_price(self) -> float:
        """Get lowest price."""
        return self._lowest_price

    @property
    def market_list(self) -> str:
        """Get market list."""
        return self._market_list

    @property
    def market_maker_expected(self) -> bool:
        """Get market maker expected."""
        return self._market_maker_expected

    @property
    def market_place(self) -> str:
        """Get market place."""
        return self._market_place

    @property
    def market_trades(self) -> bool:
        """Get market trades."""
        return self._market_trades

    @property
    def morning_star_fact_sheet_url(self) -> str:
        """Get morning star fact sheet url."""
        return self._morning_star_fact_sheet_url

    @property
    def name(self) -> str:
        """Get name."""
        return self._name

    @property
    def number_of_owners(self) -> int:
        """Get number of owners."""
        return self._number_of_owners

    @property
    def order_depth_levels(self) -> List[Dict[str, Any]]:
        """Get order depth levels."""
        return self._order_depth_levels

    @property
    def order_depth_received_time(self) -> str:
        """Get order depth received time."""
        return self._order_depth_received_time

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
    def related_stocks(self) -> List[Dict[str, Any]]:
        """Get related stocks."""
        return self._related_stocks

    @property
    def sell_price(self) -> float:
        """Get sell price."""
        return self._sell_price

    @property
    def short_sellable(self) -> bool:
        """Get short sellable."""
        return self._short_sellable

    @property
    def super_loan(self) -> bool:
        """Get super loan."""
        return self._super_loan

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
