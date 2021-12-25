
# ExPortal

ExPortal is a simple tool that allows you to pass data between synchronous and asynchronous executions in Python.

# features
- **zero** dependencies

# requirements

- Python 3.6^

# install

```bash
$ pip3 install exportal
```

# example


```python
import asyncio
from threading import Thread

from exportal import ExecutionPortal


exportal = ExecutionPortal()


async def async_func():
    value = await exportal.get_from_sync()
    print(f"async:\trecieved value '{value}' from sync")
    print("async:\tpassing value + 1 back to sync")
    await exportal.pass_to_sync(value + 1, wait=False)


def sync_func():
    value = 1
    print(f"sync:\tpassing value '{value}' to async")
    exportal.pass_to_async(value, wait=False)
    value = exportal.get_from_async()
    print(f"sync:\trecieved value '{value}' from async")


Thread(target=sync_func).start()
asyncio.get_event_loop().run_until_complete(async_func())
```
```
>>> sync:   passing value '1' to async
>>> async:  recieved value '1' from sync
>>> async:  passing value + 1 back to sync
>>> sync:   recieved value '2' from async
```