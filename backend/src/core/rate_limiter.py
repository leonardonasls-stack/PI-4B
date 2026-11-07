import time
from collections import defaultdict
from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

class RateLimiterMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 5, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        # Armazena timestamps por IP: { ip: [timestamp1, timestamp2, ...] }
        self.requests_log = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        # Aplicar Rate Limit estrito no endpoint de login
        if request.url.path.endswith("/auth/login") and request.method == "POST":
            # Captura IP do cliente (considerando proxies reversos Nginx via X-Forwarded-For)
            forwarded_for = request.headers.get("x-forwarded-for")
            if forwarded_for:
                client_ip = forwarded_for.split(",")[0].strip()
            else:
                client_ip = request.client.host if request.client else "unknown"

            now = time.time()
            cutoff = now - self.window_seconds

            # Limpa timestamps antigos para esse IP
            timestamps = [ts for ts in self.requests_log[client_ip] if ts > cutoff]
            
            if len(timestamps) >= self.max_requests:
                retry_after = int(self.window_seconds - (now - timestamps[0]))
                return JSONResponse(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    content={
                        "detail": f"Muitas tentativas consecutivas de login detectadas. Por segurança, tente novamente em {max(1, retry_after)} segundos."
                    },
                    headers={"Retry-After": str(max(1, retry_after))}
                )

            timestamps.append(now)
            self.requests_log[client_ip] = timestamps

        return await call_next(request)

