import pytest
from application import create_app, db as database

# prepare app
@pytest.fixture(scope='session')
def app():
    app = create_app('test_settings')
    return app

# Prepare the db, session means that this fixuture is only created once at the beginning of all tests
@pytest.fixture(scope='session')
def db(app, request):
    database.app = app
    database.create_all()

    # Destroy methods after test execution is complete
    def teardown():
        database.drop_all()

    request.addfinalizer(teardown)
    return database

# Prepare the database session
@pytest.fixture(scope='function')
def session(db, request):
    session = db.create_scoped_session()
    db.session = session

    def teardown():
        session.remove()

    request.addfinalizer(teardown)
    return session





