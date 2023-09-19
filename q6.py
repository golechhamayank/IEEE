import pandas as pd
df = pd.read_csv('accountdata.csv', index_col = 'acno')
while True:
    ch = int(input('''
    1. Create Account
    2. Deposit
    3. Withdraw
    4. Account Summary
    5. Exit

    Enter an Option: '''))

    if ch == 1:
        name = input('''
        Owner's Name: ''')
        acno = len(df) + 1000
        bal = 0
        print(f'''
        Owner's Name: {name}
        Account No.: {acno}
        Balance: 0
        
''')
        df.loc[acno] = [name,bal]
        df.to_csv('accountdata.csv')

    elif ch in (2,3):
        acno = int(input('''
        Account No.: '''))
        if acno in df.index:
            if ch == 2:
                amt = int(input('''
            Deposit: '''))
                df.loc[acno,'bal'] += amt
                print(f'''
            Balance: {df.loc[acno,'bal']}''')
            elif ch == 3:
                amt = int(input('''
            Withdraw: '''))
                df.loc[acno,'bal'] -= amt
                print(f'''
            Balance: {df.loc[acno,'bal']}''')
            df.to_csv('accountdata.csv')
        else:
            print('''
            Please enter a valid Account No.''')

    elif ch == 4:
        acno = int(input('''
        Account No.: '''))
        if acno in df.index:
            print(f'''
            Balance: {df.loc[acno,'bal']}''')
        else:
            print('''
            Please enter a valid Account No.''')
    elif ch == 5:
        print('''
            Thank You''')
        break
    else:
        print('''
            Please enter a valid option''')
