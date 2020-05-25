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
