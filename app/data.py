from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient

class Database:
    def __init__(self):
        # Connect to database using credentials from .env
        load_dotenv()
    
        uri = "mongodb+srv://sunilaryal22:U8RB9wujjap20ePJ@cluster0.3wzj6yk.mongodb.net/"

        self.database = MongoClient(uri, tlsCAFile=where())["Bandersnatch"]
        self.collection = self.database.get_collection("Monsters")
        
    def dataframe(self) -> DataFrame:
        documents = list(self.collection.find({}, {"_id":False}))
        return DataFrame(documents)
        
    def seed(self, amount):
       monsters = [Monster().to_dict() for _ in range(amount)]
       self.collection.insert_many(monsters)
        
    def reset(self):
       self.collection.delete_many({})

    def count(self) -> int:
       return self.collection.count_documents({})

    def html_table(self) -> str:
        # add a base case for dataframe being empty
        df = self.dataframe()
        return df.to_html(index=False)
    

if __name__ == "__main__":
    print('this is a run file')
    db = Database()
    db.seed(10)
    