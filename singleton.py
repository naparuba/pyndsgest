#!/usr/bin/python
# -*- coding: utf8 -*-


#on en fait un singleton, plus simple
#en plus avec une seule connexion ca va plus vite, merci http1.1
class Singleton(object):
    _ref = None
    
    def __new__(cls, *args, **kw):
        if cls._ref is None:
            cls._ref = super(Singleton, cls).__new__(cls, *args, **kw)
        return cls._ref

