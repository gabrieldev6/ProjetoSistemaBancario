class Conta:
    def __init__(self, titular, numeroConta, saldo):
        self.__titular = titular
        self.__numeroConta = numeroConta
        self.__saldo = saldo

    def getTitular(self):
        return self.__titular
    
    def getTitular(self, titular):
        self.__titular = titular

    def getNumeroConta(self):
        return self.__numeroConta
    
    def getNumeroConta(self, numeroConta):
        self.__numeroConta = numeroConta

    def getSaldo(self):
        return self.__saldo
    
    def getSaldo(self, saldo):
        self.__saldo = saldo