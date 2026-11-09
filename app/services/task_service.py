from app.database import get_connection


def get_all_tasks():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT * FROM tasks ORDER BY id"
        ).fetchall()

        return [dict(row) for row in rows]


def get_task(task_id: int):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()

        return dict(row) if row else None


def create_task(data):
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO tasks (title, description)
            VALUES (?, ?)
            """,
            (data.title, data.description)
        )

        conn.commit()
        return get_task(cursor.lastrowid)


def update_task(task_id: int, data):
    with get_connection() as conn:
        existing = get_task(task_id)

        if not existing:
            return None

        updates = data.model_dump(exclude_unset=True)

        title = updates.get("title", existing["title"])
        description = updates.get(
            "description", existing["description"]
        )
        completed = updates.get(
            "completed", existing["completed"]
        )

        conn.execute(
            """
            UPDATE tasks
            SET title = ?, description = ?, completed = ?
            WHERE id = ?
            """,
            (title, description, int(completed), task_id)
        )

        conn.commit()
        return get_task(task_id)


def delete_task(task_id: int):
    with get_connection() as conn:
        conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        conn.commit()

        return True