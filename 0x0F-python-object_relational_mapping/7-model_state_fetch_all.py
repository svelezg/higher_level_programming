#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

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

    selection = select('*').select_from(State).order_by(State.id)
    result = session.execute(selection).fetchall()
    for _row in result:
        print('{}: {}'.format(_row.id, _row.name))

"""
    print("----> order_by(id):")
    query = session.query(State).order_by(State.id)
    for _row in query.all():
        print('{}: {}'.format(_row.id, _row.name))
"""
