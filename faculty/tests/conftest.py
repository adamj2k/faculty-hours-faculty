import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from faculty.main import app
from faculty.models.database import Base, engine, get_db
from faculty.models.models import Teacher

TEST_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    TEST_DATABASE_URL, connect_args={"check_same_thread": False}, poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    """Test base in memory."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    """Create a test client that uses the override_get_db fixture to return a session."""

    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def create_sample_teacher(db_session):
    """Create a sample teacher for testing."""
    teacher = Teacher(id=1, name="John", last_name="Doe", email="john.doe@faculty.com")
    db_session.add(teacher)
    db_session.commit()
    db_session.refresh(teacher)
    return teacher


@pytest.fixture(autouse=True)
def disable_send_message(monkeypatch):
    """Disable send_message function to be used in tests"""

    def dummy_send_message(message, queue, teacher_id=None):
        """Dummy send_message for RabbitMQ function to be used in tests"""
        print(
            f"[TEST] Dummy send_message invoked: message={message}, queue={queue}, teacher_id={teacher_id}"
        )

    class MockChannel:
        def basic_publish(self, exchange, routing_key, body):
            print(
                f"[TEST] Mock publish: exchange={exchange}, routing_key={routing_key}, body={body}"
            )

        def queue_declare(self, queue):
            print(f"[TEST] Mock queue declare: queue={queue}")

    def dummy_producer_connection():
        """Dummy producer_connection that returns a mock channel"""
        return MockChannel()

    def dummy_declare_queue(queue):
        """Dummy declare_queue that returns a mock channel"""
        channel = MockChannel()
        channel.queue_declare(queue)
        return channel

    monkeypatch.setattr("faculty.services.producer.declare_queue", dummy_declare_queue)
    monkeypatch.setattr(
        "faculty.services.producer.producer_connection", dummy_producer_connection
    )
    monkeypatch.setattr("faculty.services.producer.send_message", dummy_send_message)
