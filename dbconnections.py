import pymysql

def get_connection():
    try:
        con = pymysql.connect(
            host="localhost",
            user="root",                  # your MySQL username
            passwd="riddhi282005",        # your MySQL password
            database="student_record_management"  # your DB name
        )
        print("✅ Database connection established")
        return con
    except Exception as e:
        print("❌ Database connection failed:", e)
        return None
    
if __name__ == "__main__":
    connection = get_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print("📂 Connected to database:", db_name[0])
        except Exception as e:
            print("❌ Error running test query:", e)
        finally:
            connection.close()
            print("🔒 Connection closed")