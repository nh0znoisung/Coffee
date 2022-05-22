from dataclasses import dataclass
from export_strategy import *

@dataclass
class ExportFactory:
    @staticmethod
    def getInstance(): pass
    def createStrategy(self): pass

@dataclass
class PrinterFactory(ExportFactory):
    __instance = None

    # Singleton
    @staticmethod
    def getInstance():
        if PrinterFactory.__instance == None:
            PrinterFactory.__instance = PrinterFactory()
        return PrinterFactory.__instance
    
    def createStrategy(self):
        return PrinterStrategy()

@dataclass
class ChatappFactory(ExportFactory): pass    

@dataclass
class TelegramFactory(ChatappFactory):
    __instance = None
    # Singleton
    @staticmethod
    def getInstance():
        if TelegramFactory.__instance == None:
            TelegramFactory.__instance = TelegramFactory()
        return TelegramFactory.__instance

    def createStrategy(self, phone_number: str):
        return TelegramStrategy(phone_number)

@dataclass
class ZaloFactory(ChatappFactory):
    __instance = None
    # Singleton
    @staticmethod
    def getInstance():
        if ZaloFactory.__instance == None:
            ZaloFactory.__instance = ZaloFactory()
        return ZaloFactory.__instance
    
    def createStrategy(self, phone_number: str):
        return ZaloStrategy(phone_number)

@dataclass
class MessengerFactory(ChatappFactory):
    __instance = None
    # Singleton
    @staticmethod
    def getInstance():
        if MessengerFactory.__instance == None:
            MessengerFactory.__instance =  MessengerFactory()
        return MessengerFactory.__instance
    
    def createStrategy(self, id: str):
        return MessengerStrategy(id)


