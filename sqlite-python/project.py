import sqlite3

def add_project(conn, project):
    sql = ''' INSERT INTO projects(name,begin_date,end_date) VALUES(?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, project)

    conn.commit()

    return cur.lastrowid

def add_task(conn, task):
    sql = ''' INSERT INTO tasks(name,priority,status_id,begin_date,end_date) VALUES(?,?,?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, task)

    conn.commit()

    return cur.lastrowid

def main():

    try:
        with sqlite3.connect('my.db') as conn:
            project = ('Nadia', '2020-02-14', '2024-08-04')
            project_id = add_project(conn, project)
            print(f"Berhasil bikin project dengan ID {project_id}")

            tasks = [
                ('Analys the requirements of the app', 1, 1, project_id, '2026-07-28', '2026-07-31'),
                ('Confirm with user about the top requirements', 1, 1, project_id, '2026-07-29', '2026-08-01')
            ]

            for task in tasks:
                task_id = add_task(conn, task)
                print(f"Membuat tugas dengan ID {task_id}")

    except sqlite3.Error as e:
        print(e)

if __name__ == '__main__':
    main()