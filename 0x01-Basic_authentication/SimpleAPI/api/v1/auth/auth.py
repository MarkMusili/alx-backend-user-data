#!/usr/bin/env python3
"""
Authentication class to manage API
"""
from flask import request
from typing import TypeVar, List


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Require authentication method
        """
        if path is None or \
                excluded_paths is None or excluded_paths == []:
            return True
        
        if not path.endswith('/'):
            path += '/'
        
        if path in excluded_paths:
            return False
        
        return True
    

    def authorization_header(self, request=None) -> str:
        """"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"""
        return None