import asyncio


class ExecutionPortal:
    def __init__(self):
        self._loop = asyncio.get_event_loop()
        self._s2a_queue = asyncio.Queue()
        self._a2s_queue = asyncio.Queue()

    def pass_to_async(self, item, wait=True):
        if wait:
            asyncio.run_coroutine_threadsafe(self._s2a_queue.put(item), self._loop).result()
        else:
            self._loop.call_soon(self._s2a_queue.put_nowait, item)
 
    def get_from_async(self):
        return asyncio.run_coroutine_threadsafe(self._a2s_queue.get(), self._loop).result()

    async def pass_to_sync(self, item, wait=True):
        if wait:
            await self._a2s_queue.put(item)
        else:
            self._a2s_queue.put_nowait(item)

    async def get_from_sync(self):
        return await self._s2a_queue.get()
