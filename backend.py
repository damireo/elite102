import mysql.connector

db = mysql.connector.connect(
    user="root",
    password="Damire2007!",
    database="Elite102"
)
cursor = db.cursor()


#create account
def create_account(username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password)) #inserts parameters into users
    user_id = cursor.lastrowid 
    cursor.execute("INSERT INTO accounts (user_id) VALUES (%s)", (user_id,)) #inserts userid into accounts
    db.commit()
    return("Account successfully created.")

#get balance
def get_balance(username):
    cursor.execute("""
        SELECT a.balance FROM accounts a
        JOIN users u ON a.user_id = u.user_id
        WHERE u.username = %s
    """, (username,)) #selects balance where username is equal to user account 
    result = cursor.fetchone()
    return result[0] if result else None #returns balance if it exists

#deposit money
def deposit(username, amount):
    cursor.execute("""
        UPDATE accounts SET balance = balance + %s 
        WHERE user_id = (SELECT user_id FROM users WHERE username = %s)  
    """, (amount, username)) #adds to the balance on the parameter given for username
    db.commit()
    return("Deposit successful.")

#withdraw money
def withdraw(username, amount):
    current_balance = get_balance(username) #checks balance
    if(current_balance is not None and current_balance >= amount): #checks if balance is valid to withdraw from
        cursor.execute("""
            UPDATE accounts SET balance = balance - %s
            WHERE user_id = (SELECT user_id FROM users WHERE username = %s)
        """, (amount, username)) #same method as adding money except subtraction

        db.commit()
        return("Withdrawal successful.")
    else:
        return("Insufficient funds or user not found.")

#delete account
def delete_account(username):
    cursor.execute("DELETE FROM users WHERE username = %s", (username,)) #gets rid of specific usernmae in user table
    db.commit()
    return("Account deleted successfully.")

#modify stuff in account
def modify_account(old_username, new_username=None, new_password=None):
    if new_username: #update username
        cursor.execute("UPDATE users SET username = %s WHERE username = %s", (new_username, old_username))
    if new_password: #update passwrd
        cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, old_username if not new_username else new_username))
    db.commit()
    return("Account updated successfully.")




