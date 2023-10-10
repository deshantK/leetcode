import asyncio
async def fn():
	#task=asyncio.create_task(fn2())
	print("one")
	#await asyncio.sleep(1)
	#await fn2()
    #asyncio.run(fn2())
	print('four')
	await asyncio.sleep(1)
	print('five')
	await asyncio.sleep(1)

async def fn2():
	#await asyncio.sleep(1)
	print("2two")
	await asyncio.sleep(1)
	print("2three")
	
asyncio.run(fn())
