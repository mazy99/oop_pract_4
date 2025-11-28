from typing import Literal


def set_status(status: Literal["new", "in_progress", "completed"]) -> None:
    print(f"Текущий статус: {status}")


set_status("new")
set_status("in_progress")
set_status("completed")
