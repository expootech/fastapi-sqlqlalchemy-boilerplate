from fastapi import HTTPException

class UserNotFoundException(HTTPException):
    def __init__(self, user_id: int):
        super().__init__(status_code=404, detail=f"User {user_id} not found")
