"""Common code for unit testing pyavanza."""
import asyncio
import unittest


def sync(coro):
    """Use this wrapper to run a asynchronous test."""

    def wrapper(*args, **kwargs):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(coro(*args, **kwargs))

    return wrapper


class TestCase(unittest.TestCase):
    """Base test case class for all pyavanza unit test."""

    def shortDescription(self):
        """Disable printing of docstring in test runner."""
        return None


JSON_STOCK_DATA = {
    "priceOneWeekAgo": None,
    "priceOneMonthAgo": None,
    "priceSixMonthsAgo": None,
    "priceAtStartOfYear": None,
    "priceOneYearAgo": None,
    "priceThreeYearsAgo": None,
    "priceFiveYearsAgo": None,
    "priceThreeMonthsAgo": None,
    "marketPlace": None,
    "marketList": None,
    "morningStarFactSheetUrl": None,
    "name": None,
    "id": None,
    "country": None,
    "currency": None,
    "totalVolumeTraded": None,
    "lowestPrice": None,
    "highestPrice": None,
    "tradable": None,
    "shortSellable": None,
    "isin": None,
    "lastPrice": None,
    "lastPriceUpdated": None,
    "change": None,
    "changePercent": None,
    "totalValueTraded": None,
    "quoteUpdated": None,
    "tickerSymbol": None,
    "loanFactor": None,
    "flagCode": None,
    "hasInvestmentFees": None,
    "keyRatios": None,
    "numberOfOwners": None,
    "superLoan": None,
    "pushPermitted": None,
    "dividends": None,
    "relatedStocks": None,
    "company": None,
    "orderDepthLevels": None,
    "marketMakerExpected": None,
    "orderDepthReceivedTime": None,
    "latestTrades": None,
    "marketTrades": None,
    "annualMeetings": None,
    "companyReports": None,
    "brokerTradeSummary": None,
    "companyOwners": None,
    "buyPrice": None,
    "sellPrice": None,
}

JSON_STOCK_DATA_ALLOWED_MISSING_KEYS = [
    "buyPrice",
    "highestPrice",
    "lastPrice",
    "lastPriceUpdated",
    "lowestPrice",
    "orderDepthReceivedTime",
    "sellPrice",
    "company",
    "companyOwners",
    "keyRatios",
    "marketList",
    "morningStarFactSheetUrl",
    "priceAtStartOfYear",
    "priceFiveYearsAgo",
    "priceOneMonthAgo",
    "priceOneWeekAgo",
    "priceOneYearAgo",
    "priceSixMonthsAgo",
    "priceThreeMonthsAgo",
    "priceThreeYearsAgo",
]

JSON_FUND_DATA = {
    "NAV": None,
    "NAVLastUpdated": None,
    "administrators": None,
    "autoPortfolio": None,
    "buyFee": None,
    "buyable": None,
    "capital": None,
    "changeSinceFiveYears": None,
    "changeSinceOneDay": None,
    "changeSinceOneMonth": None,
    "changeSinceOneWeek": None,
    "changeSinceOneYear": None,
    "changeSinceSixMonths": None,
    "changeSinceTenYears": None,
    "changeSinceThreeMonths": None,
    "changeSinceThreeYears": None,
    "changeSinceTurnOfTheYear": None,
    "description": None,
    "domicile": None,
    "fundCompany": None,
    "hasInvestmentFees": None,
    "id": None,
    "isin": None,
    "loanFactor": None,
    "managementFee": None,
    "name": None,
    "normanAmount": None,
    "numberOfOwners": None,
    "otherFees": None,
    "prospectus": None,
    "rating": None,
    "relatedFunds": None,
    "risk": None,
    "riskLevel": None,
    "sellFee": None,
    "sellable": None,
    "sharpeRatio": None,
    "standardDeviation": None,
    "startDate": None,
    "subCategory": None,
    "tradingCurrency": None,
    "type": None,
}

JSON_FUND_DATA_ALLOWED_MISSING_KEYS = [
    "capital",
    "changeSinceFiveYears",
    "changeSinceOneDay",
    "changeSinceOneMonth",
    "changeSinceOneWeek",
    "changeSinceOneYear",
    "changeSinceSixMonths",
    "changeSinceTenYears",
    "changeSinceThreeMonths",
    "changeSinceThreeYears",
    "changeSinceTurnOfTheYear",
    "rating",
    "risk",
    "riskLevel",
    "sharpeRatio",
    "standardDeviation",
    "subCategory",
    "type",
]
