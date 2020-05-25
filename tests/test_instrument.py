"""Test instrument."""
import pyavanza
import tests.common as common


class TestInstrument(common.TestCase):
    """Test that creates an instrument."""

    def test_instrument_no_data(self):
        """Test create Instrument without data."""
        with self.assertRaises(pyavanza.AvanzaParseError):
            pyavanza.Instrument(pyavanza.InstrumentType.STOCK, {})

    def test_instrument_missing_id(self):
        """Test create instrument without id."""
        with self.assertRaises(pyavanza.AvanzaParseError) as context:
            pyavanza.Instrument(
                pyavanza.InstrumentType.STOCK,
                {"name": "Test", "tickerSymbol": "TEST", "tradable": True},
            )
        self.assertEqual(context.exception.args[0], "id")

    def test_instrument_missing_name(self):
        """Test create instrument without name."""
        with self.assertRaises(pyavanza.AvanzaParseError) as context:
            pyavanza.Instrument(
                pyavanza.InstrumentType.STOCK,
                {"id": "1234", "tickerSymbol": "TEST", "tradable": True},
            )
        self.assertEqual(context.exception.args[0], "name")

    def test_instrument_missing_ticker_symbol(self):
        """Test create instrument without ticker symbol."""
        with self.assertRaises(pyavanza.AvanzaParseError) as context:
            pyavanza.Instrument(
                pyavanza.InstrumentType.STOCK,
                {"id": "1234", "name": "Test", "tradable": True},
            )
        self.assertEqual(context.exception.args[0], "tickerSymbol")

    def test_instrument_missing_tradable(self):
        """Test create instrument without tradable."""
        with self.assertRaises(pyavanza.AvanzaParseError) as context:
            pyavanza.Instrument(
                pyavanza.InstrumentType.STOCK,
                {"id": "1234", "name": "Test", "tickerSymbol": "TEST"},
            )
        self.assertEqual(context.exception.args[0], "tradable")

    def test_instrument_string(self):
        """Test string representation of an instrument."""
        instrument = pyavanza.Instrument(
            pyavanza.InstrumentType.STOCK,
            {"id": "1234", "name": "Test", "tickerSymbol": "TEST", "tradable": True},
        )
        self.assertEqual(str(instrument), "Instrument[1234]: Test")
