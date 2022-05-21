from dataclasses import dataclass
from ExportStrategy import *

@dataclass
class ExportFactory:
    @staticmethod
    def getInstance(): pass
    def createStrategy(self): pass

@dataclass
class PrinterFactory(ExportFactory):
    instance = None

    # Singleton
    @staticmethod
    def getInstance():
        if PrinterFactory.instance == None:
            PrinterFactory.instance = PrinterFactory()
        return PrinterFactory.instance
    
    def createStrategy(self):
        return PrinterStrategy()

@dataclass
class ChatappFactory(ExportFactory): pass    

@dataclass
class TelegramFactory(ChatappFactory):
    instance = None
    # Singleton
    @staticmethod
    def getInstance():
        if TelegramFactory.instance == None:
            TelegramFactory.instance = TelegramFactory()
        return TelegramFactory.instance

    def createStrategy(self, phone_number: str):
        return TelegramStrategy(phone_number)

@dataclass
class ZaloFactory(ChatappFactory):
    instance = None
    # Singleton
    @staticmethod
    def getInstance():
        if ZaloFactory.instance == None:
            ZaloFactory.instance = ZaloFactory()
        return ZaloFactory.instance
    
    def createStrategy(self, phone_number: str):
        return ZaloStrategy(phone_number)

@dataclass
class MessengerFactory(ChatappFactory):
    instance = None
    # Singleton
    @staticmethod
    def getInstance():
        if MessengerFactory.instance == None:
            MessengerFactory.instance =  MessengerFactory()
        return MessengerFactory.instance
    
    def createStrategy(self, id: str):
        return MessengerStrategy(id)


