#!/usr/bin/env python3
"""
Filtering log information
"""

import logging
import re
import os
import mysql.connector
from typing import List


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str],
                 redaction: str, message: str, seperator: str) -> str:
    """Returns the log message obsfuscated"""
    for field in fields:
        message = re.sub(rf"{field}=.+?{seperator}",
                         f"{field}={redaction}{seperator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the record
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Return a logging object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Return an instance of mysql-connector connection
    """
    connector = mysql.connector.connect(
        user = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password = os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database = os.getenv('PERSONAL_DATA_DB_NAME')
    )
    return connector


def main():
    """
    Main function
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        message = ""
        for i in range(len(row)):
            message += f"{PII_FIELDS[i]}={row[i]};"
        logger.info(message)
    cursor.close()
    db.close()