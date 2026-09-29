import httpx
async def query_prometheus(query,base_url="http://localhost:9090"):
    async with httpx.AsyncClient(timeout=5) as c:
        r=await c.get(f"{base_url}/api/v1/query",params={"query":query})
        r.raise_for_status()
        return r.json()
