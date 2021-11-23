import blockchain
import time

chain = blockchain.Blockchain()

chain.addBlock(blockchain.Block(1,time.time(),[blockchain.Transaction("someonar","somedf",100)]))
chain.addBlock(blockchain.Block(2,time.time(),[blockchain.Transaction("someonar","somedf",100)]))
chain.addBlock(blockchain.Block(3,time.time(),[blockchain.Transaction("someonar","somedf",100)]))


# def CalculateHash(self):
#         hashTransaction = ''

#         for transaction in self.transactions:
#             hashTransaction += transaction.hash

#             hashString = str(self.time) + hashTransaction + self.prev + str(self.index) + str(self.nonse)
#             hashEncoded = json.dumps(hashString, sort_keys=True).encode()
#             return hashlib.sha256(hashEncoded).hexdigest()