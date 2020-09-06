"""Representation of a Fund."""
from typing import Any, Dict, List

from pyavanza.error import AvanzaParseError


class Fund:
    """Fund object."""

    def __init__(self, json_data: Dict[str, Any]) -> None:
        """Initialize fund object using json data."""
        try:
            self._nav: float = json_data["NAV"]
            self._nav_last_updated: str = json_data["NAVLastUpdated"]
            self._administrators: str = json_data["administrators"]
            self._auto_portfolio: bool = json_data["autoPortfolio"]
            self._buy_fee: float = json_data["buyFee"]
            self._buyable: bool = json_data["buyable"]
            self._description: str = json_data["description"]
            self._domicile: str = json_data["domicile"]
            self._fund_company: Dict[str, str] = json_data["fundCompany"]
            self._has_investment_fees: bool = json_data["hasInvestmentFees"]
            self._id: str = json_data["id"]
            self._isin: str = json_data["isin"]
            self._loan_factor: float = json_data["loanFactor"]
            self._management_fee: float = json_data["managementFee"]
            self._name: str = json_data["name"]
            self._norman_amount: float = json_data["normanAmount"]
            self._number_of_owners: int = json_data["numberOfOwners"]
            self._other_fees: str = json_data["otherFees"]
            self._prospectus: str = json_data["prospectus"]
            self._related_funds: List[Dict[str, Any]] = json_data["relatedFunds"]
            self._sell_fee: float = json_data["sellFee"]
            self._sellable: bool = json_data["sellable"]
            self._start_date: str = json_data["startDate"]
            self._trading_currency: str = json_data["tradingCurrency"]
        except KeyError as exception:
            raise AvanzaParseError(exception.args[0]) from exception

        # Could be missing if fund has not been on the market long enough
        self._change_since_five_years: float = json_data.get(
            "changeSinceFiveYears", None
        )
        self._change_since_one_day: float = json_data.get("changeSinceOneDay", None)
        self._change_since_one_month: float = json_data.get("changeSinceOneMonth", None)
        self._change_since_one_week: float = json_data.get("changeSinceOneWeek", None)
        self._change_since_one_year: float = json_data.get("changeSinceOneYear", None)
        self._change_since_six_months: float = json_data.get(
            "changeSinceSixMonths", None
        )
        self._change_since_ten_years: float = json_data.get("changeSinceTenYears", None)
        self._change_since_three_months: float = json_data.get(
            "changeSinceThreeMonths", None
        )
        self._change_since_three_years: float = json_data.get(
            "changeSinceThreeYears", None
        )
        self._change_since_turn_of_the_year: float = json_data.get(
            "changeSinceTurnOfTheYear", None
        )
        # Might not be available for all funds
        self._capital: float = json_data.get("capital", None)
        self._rating: int = json_data.get("rating", None)
        self._risk: int = json_data.get("risk", None)
        self._risk_level: str = json_data.get("riskLevel", None)
        self._sharpe_ratio: float = json_data.get("sharpeRatio", None)
        self._standard_deviation: float = json_data.get("standardDeviation", None)
        # Not all funds specify this
        self._sub_category: str = json_data.get("subCategory", None)
        self._type: str = json_data.get("type", None)

    def __str__(self) -> str:
        """Print the object as a string."""
        return "Fund[{}]: {}".format(self._id, self._name)

    @property
    def nav(self) -> float:
        """Get nav."""
        return self._nav

    @property
    def nav_last_updated(self) -> str:
        """Get nav last updated."""
        return self._nav_last_updated

    @property
    def administrators(self) -> str:
        """Get administrators."""
        return self._administrators

    @property
    def auto_portfolio(self) -> bool:
        """Get auto portfolio."""
        return self._auto_portfolio

    @property
    def buy_fee(self) -> float:
        """Get buy fee."""
        return self._buy_fee

    @property
    def buyable(self) -> bool:
        """Get buyable."""
        return self._buyable

    @property
    def capital(self) -> float:
        """Get capital."""
        return self._capital

    @property
    def change_since_five_years(self) -> float:
        """Get change since five years."""
        return self._change_since_five_years

    @property
    def change_since_one_day(self) -> float:
        """Get change since one day."""
        return self._change_since_one_day

    @property
    def change_since_one_month(self) -> float:
        """Get change since one month."""
        return self._change_since_one_month

    @property
    def change_since_one_week(self) -> float:
        """Get change since one week."""
        return self._change_since_one_week

    @property
    def change_since_one_year(self) -> float:
        """Get change since one year."""
        return self._change_since_one_year

    @property
    def change_since_six_months(self) -> float:
        """Get change since six months."""
        return self._change_since_six_months

    @property
    def change_since_ten_years(self) -> float:
        """Get change since ten years."""
        return self._change_since_ten_years

    @property
    def change_since_three_months(self) -> float:
        """Get change since three months."""
        return self._change_since_three_months

    @property
    def change_since_three_years(self) -> float:
        """Get change since three years."""
        return self._change_since_three_years

    @property
    def change_since_turn_of_the_year(self) -> float:
        """Get change since turn of the year."""
        return self._change_since_turn_of_the_year

    @property
    def description(self) -> str:
        """Get description."""
        return self._description

    @property
    def domicile(self) -> str:
        """Get domicile."""
        return self._domicile

    @property
    def fund_company(self) -> Dict[str, str]:
        """Get fund company."""
        return self._fund_company

    @property
    def has_investment_fees(self) -> bool:
        """Get has investment fees."""
        return self._has_investment_fees

    @property
    def id(self) -> str:
        """Get id."""
        return self._id

    @property
    def isin(self) -> str:
        """Get isin."""
        return self._isin

    @property
    def loan_factor(self) -> float:
        """Get loan factor."""
        return self._loan_factor

    @property
    def management_fee(self) -> float:
        """Get management fee."""
        return self._management_fee

    @property
    def name(self) -> str:
        """Get name."""
        return self._name

    @property
    def norman_amount(self) -> float:
        """Get norman amount."""
        return self._norman_amount

    @property
    def number_of_owners(self) -> int:
        """Get number of owners."""
        return self._number_of_owners

    @property
    def other_fees(self) -> str:
        """Get other fees."""
        return self._other_fees

    @property
    def prospectus(self) -> str:
        """Get prospectus."""
        return self._prospectus

    @property
    def rating(self) -> int:
        """Get rating."""
        return self._rating

    @property
    def related_funds(self) -> List[Dict[str, Any]]:
        """Get related funds."""
        return self._related_funds

    @property
    def risk(self) -> int:
        """Get risk."""
        return self._risk

    @property
    def risk_level(self) -> str:
        """Get risk level."""
        return self._risk_level

    @property
    def sell_fee(self) -> float:
        """Get sell fee."""
        return self._sell_fee

    @property
    def sellable(self) -> bool:
        """Get sellable."""
        return self._sellable

    @property
    def sharpe_ratio(self) -> float:
        """Get sharpe ratio."""
        return self._sharpe_ratio

    @property
    def standard_deviation(self) -> float:
        """Get standard deviation."""
        return self._standard_deviation

    @property
    def start_date(self) -> str:
        """Get start date."""
        return self._start_date

    @property
    def sub_category(self) -> str:
        """Get sub category."""
        return self._sub_category

    @property
    def trading_currency(self) -> str:
        """Get trading currency."""
        return self._trading_currency

    @property
    def type(self) -> str:
        """Get type."""
        return self._type
