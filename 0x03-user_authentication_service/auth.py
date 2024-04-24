#!/usr/bin/python3
"""
Authentication system
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Encrypt a password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode("utf-8"), salt)
