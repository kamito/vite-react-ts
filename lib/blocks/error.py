#!/usr/bin/env python

class UrlInvalidError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "UrlInvalidError"

class ApiTokenInvalidError(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "UrlInvalidError"
