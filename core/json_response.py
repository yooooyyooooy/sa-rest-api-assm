from typing import Any

from fastapi.responses import JSONResponse


class SuccessJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return super().render(content={"success": True, "data": content})


class FailureJSONResponse(JSONResponse):
    def render(self, content: Any) -> bytes:
        return super().render(content={"success": False, "err": content})
