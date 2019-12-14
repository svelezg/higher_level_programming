#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    query = session.query(City, State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id.asc()).all()

    for cities, states in query:
        print("{}: ({}) {}".format(states.name, cities.id, cities.name))
