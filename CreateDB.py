import sqlite3

# Drop the GEEK table if already exists.
#csr_obj.execute("DROP TABLE IF EXISTS GEEK")

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)

    return conn

# =================================================================================

def createTable() :

    # Creating table
    table = """
        CREATE TABLE "menucmd_tbl" (
        -- table of commands for menu item - lvl is the foreign key with menu_tbl
        "lvl"	INTEGER,
        "lvln"	INTEGER,
        "cmdtype"	TEXT, -- command type C for command , P for print , I for input
        "cmd"	TEXT
        );
    """
    csr_obj.execute(table)
    print("Created menucmd_tbl table ")

    table = """
        CREATE TABLE "menu_tbl" (
        "lvl"	INTEGER,
        "lvln"	INTEGER,
        "descrizione"	TEXT
    );"""
    csr_obj.execute(table)
    print("Created menu_tbl table ")
    print("Tables are created")

# =================================================================================

def insert_rows() :

    multiple_columns = [(1, 1, 'Ebay Delivery address'),
                        (1, 2, 'Cartoleria Cigola'),
                        (1, 3, 'NFS'),
                        (1, 4, ''),
                        (1, 5, ''),
                        (1, 6, ''),
                        (1, 7, ''),
                        (1, 8, ''),
                        (1, 9, ''),
                        (1, 10, ''),
                        (1, 11, ''),
                        (1, 12, ''),
                        (1, 13, ''),
                        (1, 14, ''),
                        (1, 15, ''),
                        (1, 16, ''),
                        (1, 17, ''),
                        (1, 18, ''),
                        (1, 19, ''),
                        (1, 20, ''),
                        (1, 21, ''),
                        (1, 50, 'Mount NFS disks'),
                        # --------------------------------------------- Menu level 3
                        (3, 31, 'restart NFS'),
                        (3, 32, 'show NFS status'),
                        (3, 33, ''),
                        (3, 34, ''),
                        (3, 35, ''),
                        (3, 36, ''),
                        (3, 37, ''),
                        (3, 38, ''),
                        (3, 39, ''),
                        # --------------------------------------------- Menu level 5
                        (5, 51, 'mount /media/Rpi3B+Download') ,
                        (5, 52, 'umount /media/Rpi3B+Download') ,
                        (5, 53, 'mount /media/Qnap'),
                        (5, 54, 'umount /media/Qnap'),
                        (5, 55, 'mount /media/Qnap2'),
                        (5, 56, 'umount /media/Qnap2'),
                        (5, 57, 'mount /media/FreeNas'),
                        (5, 58, 'umount /media/FreeNas'),
                        (5, 59, 'mount /media/nfs-low'),
                        (5, 60, 'umount /media/nfs-low'),
                        (5, 61, 'mount media/Phenom'),
                        (5, 62, 'umount /media/Phenom'),
                        (5, 63, ''),
                        (5, 64, ''),
                        (5, 65, ''),
                        (5, 66, ''),
                        (5, 67, 'mount ram disk'),
                        (5, 68, 'umount ram disk'),
                        (5, 69, 'list NFS mounted')
                        ]

    count = csr_obj.executemany("INSERT INTO menu_tbl VALUES (?,?,?)", multiple_columns)
    conn_obj.commit()
    print("Record inserted successfully into menu_tbl table ", csr_obj.rowcount)


    multiple_columns = [(1, 1, 'C', 'xed /media/1TbF/320Gb/Varie/Ebay/Indirizzo.txt &'),
                        (2, 1, 'P', 'Press a key to continue'),
                        (1, 2, 'P', 'xed /media/1TbF/320Gb/Varie/CartoleriaCigola.txt &'),
                        (2, 2, 'P', 'Press a key to continue'),
                        (4, 1, 'P', 'Type a word')
                        ]

    count = csr_obj.executemany("INSERT INTO menucmd_tbl VALUES (?,?,?,?)", multiple_columns)

    conn_obj.commit()
    print("Record inserted successfully into menucmd_tbl table ", csr_obj.rowcount)


# =================================================================================

try:
    conn_obj = create_connection('/home/riky60/PycharmProjects/Prj01/Menu.db')
    # cursor object
    csr_obj = conn_obj.cursor()
    createTable()
    insert_rows()

except sqlite3.Error as error:
    print("Error on sqlite create/insert table " , error)

finally:
    if conn_obj:
        # Close the connection
        conn_obj.close()
        print("The SQLite connection is closed")

#=============================================================================================


