import httpx
async def grafana_health(base_url="http://localhost:3000"):
    async with httpx.AsyncClient(timeout=5) as c:
        r=await c.get(f"{base_url}/api/health")
        return r.json()
