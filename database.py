# from mysql.connector import connect, Error
# import config

# try: 
#     with connect(**config.configValue) as connection:
#         create_db_query = "CREATE DATABASE IF NOT EXISTS warehouse"
#         with connection.cursor() as cursor:
#             cursor.execute(create_db_query)
#             connection.commit()
#             print("Database created succesfully")

    
# # Create the table in the database if it doesn't exist

#     with connect(**config.configValue) as connection:
#         with connection.cursor() as cursor:        
#             cursor.execute("""
#                 CREATE TABLE IF NOT EXISTS products (
#                     id INT AUTO_INCREMENT PRIMARY KEY,
#                     name VARCHAR(100) NOT NULL,
#                     supplier VARCHAR(100) NOT NULL,
#                     color VARCHAR(50) NOT NULL,
#                     price DECIMAL(10,2) NOT NULL
#                 );
#             """)
#             connection.commit()
#             print("Table products created succesfully")
#             cursor.close()
#             connection.close()
            
#     with connect(**config.configValue) as connection:
#         insert_query = """
#             INSERT INTO products (name, supplier, color, price) 
#             VALUES ("%s", "%s")
#             """
#         products = [
#             ("table", "IKEA", "white", 499.99),
#             ("chair", "Actona", "brown", 99.89),
#             ("cabinet", "Simpo", "black", 389.99), 
#             ("table", "Alprom", "white", 299.79), 
#             ("chair", "Alprom", "brown", 119.5), 
#             ("dresser", "IKEA", "brown", 289.8), 
#         ]
#         with connection.cursor() as cursor:
#             cursor.executemany(insert_query, products)
#             connection.commit()
            
# except Error as e:
#     print(e)