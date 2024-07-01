import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS InventoryManagement(
            id Integer Primary Key,
            shirt text,
            size text,
            price text,
            pant text,
            psize text,
            pprice text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function


    def insert(self, shirt, size, price, pant, psize, pprice):
        self.cur.execute("insert into InventoryManagement values (NULL,?,?,?,?,?,?)",
                         (shirt, size, price, pant, psize, pprice))
        self.con.commit()

    # Fetch All Data from DB


    def fetch(self):
        self.cur.execute("SELECT * from InventoryManagement")
        rows = self.cur.fetchall()
        return rows

    # Delete a Record in DB


    def remove(self, id):
        self.cur.execute("delete from InventoryManagement where id=?", (id,))
        self.con.commit()

    # Update a Record in DB

    def update(self, id, shirt, size, price, pant, psize, pprice):
        self.cur.execute("update employees set shirt=?, size=?, price=?, pant=?, psize=?, pprice=? where id=?",
            (shirt, size, price, pant, psize, pprice, id))
        self.con.commit()