from sqlmodel import create_engine, Session

from app.core.config import settings


# 创建数据库引擎
engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)


# 创建 Session 依赖
def get_session():
    with Session(engine) as session:
        yield session
