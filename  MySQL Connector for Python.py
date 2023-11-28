import mysql.connector

class MysqlIO:
    """Connect to MySQL server with python and excecute SQL commands."""
    def __init__(self, database='test'):
        try:
            
            # Change the host, user and password as needed
            
            connection = mysql.connector.connect(host='localhost',
                                                 database=database,
                                                 user='Zhou',
                                                 password='jojojo',
                                                 use_pure=True
                                                 )
            if connection.is_connected():
                db_info = connection.get_server_info()
                print("Connected to MySQL Server version", db_info)
                print("Your're connected to database:", database)
                self.connection = connection
        except Exception as e:
            print("Error while connecting to MySQL", e)
            
    def execute(self, query, header=False):
        """Execute SQL commands and return retrieved queries."""
        cursor = self.connection.cursor(buffered=True)
        cursor.execute(query)
        try:
            record = cursor.fetchall()
            if header:
                header = [i[0] for i in cursor.description]
                return {'header': header, 'record': record}
            else:    
                return record
        except:
            pass
        
    def to_df(self, query):
        """Return the retrieved SQL queries into pandas dataframe."""
        res = self.execute(query, header=True)
        df = pd.DataFrame(res['record'])
        df.columns = res['header']
        return df
    
    # Create a connection instance
    
db = MysqlIO()

# Call .to_df method to execute the query and make dataframe from the results.

query = """
    select *
    from Loan join Account using(account_id);
    """
df = db.to_df(query)
view raw
