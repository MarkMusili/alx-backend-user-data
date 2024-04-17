#!/usr/bin/env python3
"""
Session based authentication
"""
from .auth import Auth
from uuid import uuid4

class SessionAuth(Auth):
    """
    Class implimentation for session authentication
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Create a session id for user_id
        """
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id