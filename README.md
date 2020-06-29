# pyavanza

![Version](https://img.shields.io/pypi/v/pyavanza)
![Downloads](https://pepy.tech/badge/pyavanza)
![License](https://img.shields.io/github/license/claha/pyavanza.svg)
![Test](https://github.com/claha/pyavanza/workflows/Test/badge.svg)
![Lint](https://github.com/claha/pyavanza/workflows/Lint/badge.svg)
![Build](https://github.com/claha/pyavanza/workflows/Build/badge.svg)

A Python wrapper around the Avanza mobile API

## Examples

### Search

```python
import pyavanza

query = "avanza"
limit = 5
instruments = pyavanza.search(query, limit=limit)
for instrument in instruments:
    print(instrument)

# Instrument[5361]: Avanza Bank Holding
# Instrument[1025150]: Avanza USA
# Instrument[878733]: Avanza Global
# Instrument[944976]: Avanza Emerging Markets
# Instrument[788394]: Avanza Auto 6
```

### Search (asynchronously)

```python
import asyncio
import aiohttp
import pyavanza

async def search():
    query = "avanza"
    limit = 5
    instrument = pyavanza.InstrumentType.FUND
    async with aiohttp.ClientSession() as session:
        instruments = await pyavanza.search_async(
            session, query, limit=limit, instrument=instrument
        )
        for instrument in instruments:
            print(instrument)

loop = asyncio.get_event_loop()
loop.run_until_complete(search())

# Instrument[1025150]: Avanza USA
# Instrument[878733]: Avanza Global
# Instrument[944976]: Avanza Emerging Markets
# Instrument[788394]: Avanza Auto 6
# Instrument[788398]: Avanza Auto 4
```
