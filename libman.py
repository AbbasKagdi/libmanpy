"""
Project Name: Library Managemnet System
Language: Python
Author: Abbas Kagdi
"""

print("""
*******************************
*                             *
** LIBRARY MANAGEMENT SYSTEM **   
*                             *
*******************************
\n""")

import datetime
import mysql.connector as con
import creds

# edit creds.py to match your db settings
db = con.connect(host = creds.host, user = creds.user, password = creds.password, database = creds.database)
cursor = db.cursor()

#CREATING REQUIRED TABLES
"""
# replace comments with necessary details, if setting up on new device
cursor.execute("create database if not exists python; use python;")
cursor.execute("create table if not exists books")
cursor.execute("create table if not exists members")
cursor.execute("create table if not exists booking") 
db.commit() """

#starting main loop
status = True
while status:
    choice = int(input("""
    Welcome!
    Choose record to enter
    1. Enter Books Record
    2. Enter Members Record
    3. Enter Booking Record
    4. Exit Menu\n
    """))

    # Books Table
    if choice == 1:
        while True:
            choice = int(input("""
            Book Records
            Choose action on books record
            1. Show all Books
            2. Register a new book
            3. Delete a book
            4. Previous Menu
            5. Exit Program\n
            """))
            # user choices
            if choice == 1:
                cursor.execute("select * from books")
                rows = cursor.fetchall()
                print("book id\t\tname\t\tgenre\t\tauthor")
                for row in rows:
                    for cell in row:
                        print(cell, end='\t\t')
                    print("\n")
                continue

            elif choice == 2:
                book_name = str(input("Enter Book name\n"))
                genre = str(input("Enter Genre\n"))
                author = str(input("Enter Author's name\n"))
                sql = "insert into books values(NULL,%s,%s,%s)"
                val = (book_name, genre, author)
                cursor.execute(sql, val)
                db.commit()
                if cursor.rowcount == 1:
                    print("New book added\n")
                    cursor.execute("commit")
                else:
                    print("Error!")
                    status = False
                    break
                continue

            elif choice == 3:
                # show all book IDs
                cursor.execute("select book_id, name from books")
                print("\nList of all book IDs\n")
                rows = cursor.fetchall()
                for row in rows:
                    for cell in row:
                        print(cell, end="\t")
                    print("\n")
                book = str(input("\nEnter book ID to remove\n"))
                # check if book in use
                sql = "select name from members where member_id in (SELECT member_id from booking where book_id = "+ book +")"
                cursor.execute(sql)
                member = cursor.fetchall()
                if cursor.rowcount > 0:
                    print("\nCannot delete book, as it is issued by:")
                    for x in member:
                        for y in x:
                            print(y, end="\n")
                else:
                    sql = "delete from books where book_id = " + book
                    cursor.execute(sql)
                    print("Book deleted succesfully\n")
                    cursor.execute("commit")
                continue

            elif choice == 4:
                choice = 0
                break
            elif choice == 5:
                choice = 4
                break

    # Members Table
    if choice == 2:
        while True:
            choice = int(input("""
            Member Records
            Choose action on members record
            1. Show all members data
            2. Register a new member
            3. Delete a member record
            4. Previous Menu
            5. Exit Program\n
            """))
            # user choices
            if choice == 1:
                cursor.execute("select * from members")
                rows = cursor.fetchall()
                print("member id\tname\t\tcontact\n")
                for row in rows:
                    for cell in row:
                        print(cell, end='\t\t')
                    print("\n")
                continue

            elif choice == 2:
                member_name = str(input("Enter Member name\n"))
                contact = int(input("Enter contact number\n"))
                sql = "insert into members values(NULL,%s,%s)"
                val = (member_name, contact)
                cursor.execute(sql, val)
                if cursor.rowcount == 1:
                    print("New member record added\n")
                    cursor.execute("commit")
                else:
                    print("Error!")
                    status = False
                    break
                continue

            elif choice == 3:
                # show all mmeber IDs
                cursor.execute("select member_id, name from members")
                print("\nList of all member IDs\n")
                rows = cursor.fetchall()
                for row in rows:
                    for cell in row:
                        print(cell, end="\t")
                    print("\n")
                member = str(input("\nEnter member ID to remove\n"))
                # check if member issued a book
                sql = "select name from books where book_id in (SELECT book_id from booking where member_id = "+ member +")"
                cursor.execute(sql)
                book = cursor.fetchall()
                if cursor.rowcount > 0:
                    print("Cannot delete member record, as they have issued book(s):")
                    for x in book:
                        for y in x:
                            print(y, end="\t")
                else:
                    sql = "delete from members where member_id = " + member
                    cursor.execute(sql)
                    print("Member record deleted succesfully\n")
                    cursor.execute("commit")
                continue

            elif choice == 4:
                choice = 0
                break
            elif choice == 5:
                choice = 4
                break

    # Booking Table
    if choice == 3:
        while True:
            choice = int(input("""
            Booking Records
            Choose action on booking record
            1. Show all bookings
            2. Issue a book
            3. Return a book
            4. Show all books issued by a member
            5. Show all deafulting members 
            6. Previous Menu
            7. Exit Program\n
            """))
            # user choices
            if choice == 1:
                cursor.execute("SELECT booking.order_id, members.name as Member, books.name as Book, booking.issue_date FROM booking join members ON booking.member_id = members.member_id join books ON booking.book_id = books.book_id")
                rows = cursor.fetchall()
                print("Order id\tMember\t\tBook\t\tIssue date\n")
                for row in rows:
                    for cell in row:
                        print(cell, end='\t\t')
                    print("\n")
                continue

            elif choice == 2:
                # print all books
                print("List of all book IDs")
                cursor.execute("select book_id, name from books")
                rows = cursor.fetchall()
                print("\nBook id\t\tName\n")
                
                for row in rows:
                    for cell in row:
                        print(cell, end="\t\t")
                    print("\n")
                book = int(input("Enter Book ID\n"))
                
                # print all members
                print("\nList of all member IDs")
                cursor.execute("select member_id, name from members")
                rows = cursor.fetchall()
                print("Member id\tName")
                
                for row in rows:
                    for cell in row:
                        print(cell, end="\t\t")
                    print("\n")
                member = int(input("Enter Member ID\n"))
                
                # issue a book
                sql = "insert into booking values(NULL,%s,%s, curdate(), NULL)"
                val = (member, book)
                cursor.execute(sql, val)
                if cursor.rowcount == 1:
                    print("New transaction recorded.\n")
                    cursor.execute("commit")
                else:
                    print("Error!")
                    status = False
                    break
                continue

            elif choice == 3:
                # printing due records
                cursor.execute("SELECT booking.order_id, members.name as Member, books.name as Book, booking.issue_date FROM booking join members ON booking.member_id = members.member_id join books ON booking.book_id = books.book_id where booking.return_date is null")
                rows = cursor.fetchall()
                print("order id\tmember id\tbook id\t\tbook name\tissue date\n")
                for row in rows:
                    for cell in row:
                        print(cell, end="\t\t")
                    print("\n")
                
                # select booking id for returning book
                order = int(input("Enter Order ID\n"))

                # return a book
                sql = "update booking set return_date = curdate() where order_id = " + str(order)
                cursor.execute(sql)
                if cursor.rowcount > 0:
                    print("Order id: %s closed succesfully.\n" %order)
                    cursor.execute("commit")
                else:
                    print("Error!")
                continue

            elif choice == 4:
                # print all members
                print("List of all member IDs")
                cursor.execute("select member_id, name from members")
                rows = cursor.fetchall()
                print("Member ID\tName")
                for row in rows:
                    for cell in row:
                        print(cell, end="\t\t")
                    print("\n")
                member = int(input("\nEnter Member ID to preview\n"))
                # print all books issued by member ID
                sql = "select name from books where book_id in (SELECT book_id from booking where member_id = " + str(member) + ")"
                cursor.execute(sql)
                rows = cursor.fetchall()
                print("\nList of books under member id: %s" %member)
                for row in rows:
                    for cell in row:
                        print(cell)
                print("\n")
                continue

            elif choice == 5:
                # cursor.execute("select name from members where member_id in (select member_id from booking where return_date is null and datediff(curdate(), issue_date) > 30)")
                cursor.execute("select DISTINCT members.member_id, members.name, (datediff(curdate(), booking.issue_date) - 30) as dues from booking inner join members on booking.member_id = members.member_id where booking.return_date is null and datediff(curdate(), booking.issue_date) > 30")
                defaulters = cursor.fetchall()
                if cursor.rowcount == 0:
                    print("\nNo members have oustanding dues")
                else:
                    # printing names of all defaulters
                    print("List of all members with due records\n")
                    print("Member id\tName\t\tOustanding days\n")
                    # print dues of defaulting members
                    for row in defaulters:
                        for cell in row:
                            print(cell, end='\t\t')
                        print("\n")
                continue

            elif choice == 6:
                choice = 0
                break
            elif choice == 7:
                choice = 4
                break

    # Exit
    if choice == 4:
        print("*** Exiting Program ***")
        status = False

# close the connection
db.close()