"""
Модуль с классом для общения с базой данных
"""

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    String,
    Integer,
    MetaData,
    inspect,
    select,
    update,
    insert,
    func,
)
from .models import GenerateResultInfo, GenerateMethodCount


class DBException(Exception):
    """
    Класс исключения, связанного с базой данных
    """

    pass


class Database:
    """
    Класс с логикой для взаимодействия с базой данных MariaDB/MySQL
    """

    def __init__(self, user, password, database, port, host):
        self.database_uri = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4"
        self.engine = create_engine(self.database_uri)

        self.meta = MetaData()

        self.generated_data = Table(
            "generated_data",
            self.meta,
            Column(
                "id",
                Integer,
                primary_key=True,
                nullable=False,
                autoincrement=True,
            ),
            Column("user_id", Integer, nullable=False),
            Column("method", String(128), nullable=False),
            Column("query", String(4096), nullable=False),
            Column(
                "text",
                String(4096),
                nullable=False,
                default="",
            ),
            Column("rating", Integer, nullable=False),
            Column("unix_date", Integer, nullable=False),
            Column("group_id", Integer, nullable=False),
            Column("status", Integer, nullable=False),
            Column(
                "gen_time",
                Integer,
                nullable=False,
                default=0,
            ),
            Column("platform", String(128), nullable=False),
            Column("published", Integer, nullable=False),
            Column("hidden", Integer, nullable=False),
        )

    def get_all(self) -> list[GenerateResultInfo]:
        try:
            with self.engine.connect() as connection:
                select_query = select(self.generated_data)

                response = connection.execute(select_query).fetchall()

                result = []
                for row in response:
                    result += [
                        GenerateResultInfo(
                            post_id=row[0],
                            user_id=row[1],
                            method=row[2],
                            hint=row[3],
                            text=row[4],
                            rating=row[5],
                            date=row[6],
                            group_id=row[7],
                            status=row[8],
                            gen_time=row[9],
                            platform=row[10],
                            published=row[11],
                            hidden=row[12],
                        )
                    ]
                return result

        except Exception as exc:
            raise DBException(f"Error in get_all: {exc}") from exc
