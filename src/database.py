import oracledb


def get_database_connection():
    dsn = oracledb.makedsn("orion.javeriana.edu.co", 1521, service_name="LAB")
    return oracledb.connect(user="is819912", password="HVqqfgDQZ3wIebj", dsn=dsn)
