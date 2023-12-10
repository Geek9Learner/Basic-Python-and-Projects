"""
With the help of object oriented approach we will make an ATM functionality.
We will use simply class concept.
Functionality:  1. Creating PIN for existing Account/ATM
                2. Make an deposit to existing Account
                3. Proceed with Withdrawal process
                4. Checking the balance for existing account
                5. Update the 4 digit PIN for already existing ATM
"""
import mysql.connector

class ATM:
    def __init__(self) -> None:
        self.balance=0
        self.loginID=0
        self.password=None
        self.logIN()
        
    def db_connection(self):
        connection=mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='root',
                                   database='mydata'
                                   )
        return connection
        
    def logIN(self):
        self.loginID  = int(input('Enter your customerID: '))
        self.password = input('Enter the login password: ')
        
        connection=self.db_connection()
        mycursor= connection.cursor()
        mycursor.execute('select ID,customer from user_account where ID=%s and user_password=%s',[self.loginID,self.password])
        user_exist=mycursor.fetchall()
        
        if len(user_exist):
            user_id,user_name=user_exist[0]
            print('\n\t Welcome {user}'.format(user=user_name),', Please proceed with menu.')
            self.menu()
        else:
            print('\n\t No user exist in our system...Please create an account')
            self.menu()
        connection.commit()
        connection.close()
        
        return user_id,user_name

    def menu(self) -> None:
        user_choice=int(input("""
              0.Press 0 if you don't have account in SBI to create account.
              1.Press 1 to create PIN for Existing account.
              2.Press 2 to make deposit.
              3.Press 3 to withdraw an amount.
              4.Press 4 to check balance for existing account.:\t"""))
        
        if user_choice == 0:
            self.create_account()
        if user_choice == 1:
            self.create_PIN()
        elif user_choice == 2:
            self.deposit_amount()
        elif user_choice == 3:
            self.withdraw_amount()
        elif user_choice == 4:
            self.check_balance()
        else:
            print('Thanks for Using SBI ATM')
            
    def create_account(self):
        connection=self.db_connection()
        name=input('Enter your name:')
        account=input('Enter account starting with 208400:')
        balance=int(input('Enter the starting amount to deposit:'))
        user_password=input('Enter your user password:')
        atm_facility=input('Press Y or N for atm facility:')
        atm_number=input('Enter atm number xxxx-yyyy-zzzz format:')
        atm_pin=int(input('Please choose four digit PIN:'))
        
        #New customer account creation.. data insertion to the table
        insert_cursor=connection.cursor()
        SQL_statement='INSERT INTO user_account(CUSTOMER,ACCOUNT,BALANCE,USER_PASSWORD,ATM_FACILITY,ATM_NO,ATM_PIN) VALUES(%s,%s,%s,%s,%s,%s,%s)'
        value=(name,account,balance,user_password,atm_facility,atm_number,atm_pin)
        insert_cursor.execute(SQL_statement,value)
        
        
        #show the user newly created ID
        show_cursor=connection.cursor()
        show_cursor.execute('SELECT CUSTOMER,ID FROM USER_ACCOUNT WHERE ACCOUNT=%s',[account])
        new_user_info=show_cursor.fetchall()
        cust_name,id=new_user_info[0]
        print('Heyy {name} your account ID is {cust_id}'.format(name=cust_name,cust_id=id))
        connection.commit()
        connection.close()
            
    
    def deposit_amount(self):
        deposit_balance=int(input('Enter the balance for deposit:'))
        connection=self.db_connection()
        
        update_cursor=connection.cursor()
        update_cursor.execute('UPDATE USER_ACCOUNT SET BALANCE = BALANCE + %s WHERE ID=%s',[deposit_balance,self.loginID])
        connection.commit()
        connection.close()
        print('Succesful deposit of {} amount.'.format(deposit_balance))
        
    def withdraw_amount(self):
        withdrawal_amount=int(input('Enter the withdrawal amount:'))
        connection=self.db_connection()
        
        withdraw_cursor=connection.cursor()
        
        withdraw_cursor.execute('UPDATE USER_ACCOUNT SET BALANCE = BALANCE - %s WHERE ID=%s',[withdrawal_amount,self.loginID])
        connection.commit()
        connection.close()
        print('Withdrawal of {} successful'.format(withdrawal_amount))
        
    def check_balance(self):
        connection=self.db_connection()
        check_cursor=connection.cursor()
        check_cursor.execute('SELECT ID,CUSTOMER,BALANCE FROM USER_ACCOUNT WHERE ID=%s',[self.loginID])
        check_balance_output=check_cursor.fetchall()
        print('your balance info is: ',check_balance_output)
        connection.commit()
        connection.close()
        
        
if __name__=="__main__":
    atm=ATM()
        

    