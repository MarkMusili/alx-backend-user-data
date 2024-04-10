#!/usr/bin/env python3
"""
Filtering log information
"""
import re

def filter_datum(fields, redaction, message, seperator):
    """
    ARGS:
        fields: a list of strings representing all fields to obfuscate
        redaction: a string representing by what the field will be obfuscated
        message: a string representing the log line
        separator: a string representing by which character 
            is separating all fields in the log line (message)
    Returns the log message obsfuscated
    """
    for field in fields:
        message = re.sub(rf'{field}=.*?{seperator}',
                         f'{field}={redaction}{seperator}', message)
    return message