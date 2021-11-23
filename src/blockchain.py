import hashlib
import json
import datetime
import random

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []
        self.difficulty = 4
        self.minerRewards = 50
        self.blockSize = 10

    def getLastBlock(self):
        return self.chain[-1]

    def addBlock(self, block):
        if(len(self.chain) > 0):
            block.prev = self.getLastBlock().hash
        else:
            block.prev = "none"
        self.chain.append(block)
    

    def getChainInfo(self):
        info = []

        for block in self.chain:
            info.append(block.getBlockInfo())


class Block:
    def __init__(self,index,time, transactions):
        self.index = index
        self.transactions = transactions
        self.time = time
        self.prev = ''
        self.hash = self.CalculateHash()
        

    def CalculateHash(self):
        self.nonse = int(0)
        hashTrasaction = ''

        for tran in self.transactions:
            hashStr = str(self.time) + hashTrasaction + self.prev + str(self.index) + str(self.nonse)
            hash_encoded = json.dumps(hashStr,sort_keys=True).encode()
            return hashlib.sha256(hash_encoded).hexdigest()

    def getBlockInfo(self):
        info = []

        info.append(self.hash)

	def mineBlock(self, difficulty):
        arr = []

		
		#compute until the beginning of the hash = 0123..difficulty
		arrStr = map(str, arr);  
		hashPuzzle = ''.join(arrStr)
		#print(len(hashPuzzle));
		while self.hash[0:difficulty] != hashPuzzle:
			self.nonse += 1
			self.hash = self.calculateHash()
		print("Block Mined!")
		return True

class Transaction:
    def __init__(self,sender,reciever,amt):
        self.sender = sender
        self.reciever = reciever
        self.amt = amt
        self.time = datetime.date.today()
        self.hash = self.calculateHash()
    def calculateHash(self):
        hashString = self.sender + self.reciever + str(self.amt) + str(self.time)
        hashEncoded = json.dumps(hashString, sort_keys=True).encode()
        return hashlib.sha256(hashEncoded).hexdigest()

