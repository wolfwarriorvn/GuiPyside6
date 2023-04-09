from PySide6 import QtWidgets, QtSql


class Data:
    def __init__(self) -> None:
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('database.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False
        
        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS accounts (ID integer primary key AUTOINCREMENT, UID VARCHAR(20), "
            "Pass VARCHAR(20), Proxy VARCHAR(20))")
        return True
    
    def execute_query(self, sql_query, values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if values is not None:
            for value in values:
                query.addBindValue(value)

        query.exec()
    
    def add_usernick_query(self, uid, pw):
        sql_query = "INSERT INTO accounts (UID,Pass) VALUES (?, ?)"
        self.execute_query(sql_query, [uid, pw])
    
    def update_user_query(self, uid, pw, id):
        sql_query = "UPDATE accounts SET UID=?, Pass=? WHERE ID=?"
        self.execute_query(sql_query, [uid, id])
    
    def delete_user_query(self, id):
        sql_query = "DELETE FROM accounts WHERE ID=?"
        self.execute_query(sql_query, [id])
