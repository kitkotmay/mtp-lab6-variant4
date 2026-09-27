from sqlalchemy import String, create_engine, select
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


class Student(Base):
    """Модель студента."""

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )
    full_name: Mapped[str] = mapped_column(String(100))
    group_name: Mapped[str] = mapped_column(String(20))
    variant: Mapped[int]

    def __repr__(self):
        return (
            f"Student(id={self.id}, "
            f"full_name='{self.full_name}', "
            f"group='{self.group_name}', "
            f"variant={self.variant})"
        )


def main():
    engine = create_engine(
        "sqlite:///students.db",
        echo=False,
    )

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        students = [
            Student(
                full_name="Ковалевич Александра Андреевна",
                group_name="221141р",
                variant=4,
            ),
            Student(
                full_name="Иванов Иван Иванович",
                group_name="221141р",
                variant=2,
            ),
            Student(
                full_name="Петров Пётр Петрович",
                group_name="221141р",
                variant=7,
            ),
        ]

        session.add_all(students)
        session.commit()

    with Session(engine) as session:
        statement = select(Student)
        students = session.scalars(statement).all()

        print("Записи из базы данных:")

        for student in students:
            print(student)


if __name__ == "__main__":
    main()
