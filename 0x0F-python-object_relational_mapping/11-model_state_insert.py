#!/usr/bin/python3
""" Write script to add State object “Louisiana” to database """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ Print the new states.id after creation """
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    lou_state = State(name='Louisiana')
    session.add(lou_state)
    session.commit()
    print('{0}'.format(lou_state.id))
    session.close()
