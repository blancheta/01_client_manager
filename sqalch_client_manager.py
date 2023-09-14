from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

'''we create Base, which will return a class - to inherit from; the base for our first class (Client):'''
Base = declarative_base()


class Client(Base):
    __tablename__ = "clients"
    id = Column("id", Integer, primary_key=True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    address = Column("address", String)
    total_spent = Column("total_spent", Integer)

    '''we define a constructor'''

    def __init__(self, id, first, last, address, total_spent):
        self.id = id
        self.firstname = first
        self.lastname = last
        self.address = address
        self.total_spent = total_spent

    def __repr__(self):
        return f"({self.id}) {self.firstname} {self.lastname} ({self.address}, {self.total_spent})"


engine = create_engine("sqlite:///mydb_client.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

client1 = Client(1, "Mike", "Smith", "24 Main Street, NY", 12000)
client2 = Client(2, "Anna", "Blue", "15 Small St., London", 4000)
client3 = Client(3, "Bob", "Blue", "15 Small St., London", 3500)
client4 = Client(4, "Angela", "Cold", "78 New Road, Birmingham", 2200)

session.add(client1)
session.add(client2)
session.add(client3)
session.add(client4)

session.commit()


results = session.query(Client).filter(Client.lastname=="Blue").all()
results = session.query(Client).filter(Client.total_spent >= 3000).all()

for r in results:
    print(r)


