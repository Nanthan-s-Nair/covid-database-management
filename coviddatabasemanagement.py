print()
# connecting to mysql
import datetime
import mysql.connector as mysql
sql=mysql.connect(host='localhost',user='root',passwd='nanthan@493')
cur=sql.cursor()
sql.autocommit=True

# creating database if not exist

try :
    cur.execute('create database covid')
except:
    pass
cur.execute('use covid')
# creating table if not exist

try:
    cur.execute("""create table vaccinated(name varchar(50) not null,gender varchar(2),age int(3) not null,
date_of_birth date not null,aadhar_no bigint(12) primary key,phonenumber bigint(10) not null,
vaccine_name varchar(20) not null,vaccinated_at varchar(30) not null,vac_date_1 date not null,dose int(1) not null,vac_date_2 date)""")
except :
    pass

# inserting values if not exist

try:
    cur.execute('''insert into vaccinated values('akshya','F',21,'2000.08.23',923456789868,9283148564,'covishield','ambattur','2022-01-13',1,null),
('mahesh','M',34,'1987-04-01',912232673823,9283596538,'covaxin','avadi','2021-05-03',2,'2021-06-09'),
('raghuram','M',24,'1997-07-03',945675342139,8610600922,'covaxin','perambur','2022-01-30',1,null),
('babu','M',54,'1967-01-27',945695678231,8072129163,'covishield','paruthipet','2022-01-19',1,null),
('venugopal','M',41,'1980-11-08',911134532234,7092010579,'covishield','thirupathi','2021-03-23',2,'2021-07-01')''')
except:
    pass

# Main menu

print(' '*50+'COVID VACCINIATION')
print(' '*50+'-----------------------------------------')
print('''1.Sign in as user
2.Sign in as admin''')
try:
    sign=int(input('Enter your choice:'))
except:
    sign=None
if sign==1:
    print('''
    RISE TOETHER TO STOP COVID-19.
    GET YOUR WEAPON AGAINST THE PANDEMIC-THE VACCINE.
    so take your vaccine protect yourself and protect the society.
    STAY HOME STAY SAFE.    GET VACCINATED !!!!
    ''')
    while True:
        print('='*100)
        print('''\t\tMAIN MENU
        1.Vaccine Registration
        2.Vaccine Certificate
        3.Exit''')
        try:
            ch=int(input('\nEnter your choice :'))

            # Vaccine Registration
            
            if ch==1:
                addch='y'
                while True:
                    if addch in ('y','Y'):
                        print('='*100)
                        print('\t\tVaccine Registration')
                        print('''
            You are going to register for :
            1. First dose 
            2. Second dose''')
                        choice=int(input('Enter your choice:'))
                        if choice==1:
                            try:
                                print('Your First dose registration form')
                                print('-----------------------------------\n')
                                name=input('Enter your name:')
                                gender=input('Enter your gender(M/F):').upper()
                                if gender not in 'MF':
                                    print("Gender should be 'M' or 'F'")
                                    raise
                                age=int(input('Enter your age:'))
                                dob=input('Enter your date_of_birth (in yyyy-mm-dd format):')
                                aadhar1=int(input('Enter your aadharcard no.:'))
                                aadhar2=int(input('re-enter your aadhar no.:'))
                                if aadhar1==aadhar2:
                                    aadhar=aadhar1
                                else :
                                    print('re-entered aadhar is not same as first entered aadhar')
                                    break
                                cur.execute('select * from vaccinated where aadhar_no={}'.format(aadhar))
                                info=cur.fetchall()
                                if len(info)!=0:
                                        raise EOFError
                                ph_no=int(input('Enter your phone number:'))
                                vaccine=input('Enter the vaccine name:')
                                if vaccine not in ('covaxin','covishield'):
                                    raise NameError
                                place=input('Enter the place of vaccination:')
                                dt=datetime.date.today()
                                dose=1
                                querry="insert into vaccinated values('{}','{}',{},'{}',{},{},'{}','{}','{}',{},null)".format(name,gender,age,dob,aadhar,ph_no,vaccine,place,dt,dose)
                                cur.execute(querry)
                                print('\nYou have been registered for 1st dose of vaccination !...')
                                if vaccine=='covaxin':
                                    due2=dt+datetime.timedelta(30)
                                elif vaccine=='covishield':
                                    due2=dt+datetime.timedelta(90)
                                print('your next dose is due on',due2)
                                print('Thank you for registeration :-)')
                            except EOFError:
                                print('You have already taken your 1st dose of vaccine')
                                print('Please login for 2nd dose')
                            except NameError:
                                print('vaccine name should be covaxin or covishield ')
                            except :
                                print('Value that you have given is incorrect :-(  ')
                        elif choice==2:
                            try:
                                aadhar=int(input('Enter your aadhar no.:'))
                                cur.execute('select * from vaccinated where aadhar_no={}'.format(aadhar))
                                info=cur.fetchall()
                                if len(info)==0:
                                    raise
                                for i in info:
                                    for j in i:
                                        print(j, end='  ')
                                    print()
                                confirm=input('\nIs this your details(y/n):')
                                now=datetime.date.today()
                                if confirm in 'yY':
                                    if info[0][6]=='covaxin':
                                        due2=info[0][8]+datetime.timedelta(30)
                                    elif info[0][6]=='covishield':
                                        due2=info[0][8]+datetime.timedelta(90)
                                
                                    if info[0][9]==2:
                                        raise EOFError
                                    elif now < due2:
                                        raise NameError
                                    else:
                                        cur.execute('Update vaccinated set dose=2 where aadhar_no={}'.format(aadhar))
                                        dt_2=datetime.date.today()
                                        cur.execute("update vaccinated set vac_date_2='{}'".format(dt_2))
                                        print('\nYou have been registered for second dose !')
                                        print('Thanks for registeration :-)')
                                else:
                                    raise
                            except EOFError:
                                print(' \nYou have already vaccinated  2nd dose')
                            except NameError:
                                print('\nyou have',(due2-now).days,' days left for your 2nd dose')
                            except:
                                print('\nYour data is not available !')
                                print('Please put 1st dose for registering for 2nd dose')
                        else:
                            print('Enter a valid input(1/2)')
                        addch=input('Do you wish to register for more person(s) ? (y/n):')
                    else :
                        break

            # Vaccine Certificate
            
            elif ch==2:
                try:
                    aadhar=int(input('Enter your aadhar no:'))
                    cur.execute('select * from vaccinated where aadhar_no={}'.format(aadhar))
                    va=cur.fetchall()
                    if len(va)==0:
                        print('No details available')
                        raise
                    val=va[0]
                    name=val[0]
                    gender=val[1]
                    age=val[2]
                    dob=val[3]
                    aadhar=val[4]
                    phone=val[5]
                    vaccine=val[6]
                    place=val[7]
                    dt=val[8]
                    dose=val[9]
                    dt2=val[10]
                    print('='*50)
                    print()
                    print(' '*25,end='')
                    print('CERTIFICATE')
                    print('''
        name\t\t:{}
        gender\t:{}
        age\t\t:{}
        date of birth\t:{}
        aadhar no.\t:{}
        phone number\t:{}
        vaccine name\t:{}
        place\t\t:{}
        dose\t\t:{}
        1st dose\t:{}
        2nd dose\t:{}'''.format(name,gender,age,dob,aadhar,phone,vaccine,place,dose,dt,dt2))
                    print('='*50)
                except:
                    print('You have not been vaccinated')

                
            # Breaking the loop
            
            elif ch==3:
                print('Exiting program....')
                break
            else:
                raise
        except:
            print('Your choice is invalid :-(')
elif sign==2:
    ad=input('Enter your user name:')
    passcode=input('Enter your passcode:')
    print()
    if ad.lower()=='pavan adhish' and passcode=='Beckham':
        print('Welcome Mr. Pavan Adhish')
        access='granted'
    elif ad.lower()=='vishnu abiram' and passcode=='ilbforever':
        print('Welcome Mr. Vishnu Abiram')
        access='granted'
    elif ad.lower()=='nanthan' and passcode=='nandynandy':
        print('Welcome Mr. Nanthan S Nair')
        access='granted'
    elif ad.lower()=='veeramani' and passcode=='password':
        print('Welcome Mr. Veera manikandan')
        access='granted'
    else :
        print('Access Denied')
        access='denied'
    if access=='granted':
        while True:
            print('\n\t\tMAIN MENU')
            print('1. Update people profile')
            print('2.Access details of people who are vaccinated')
            print('3.Exit')
            val=input('\nEnter your choice:')
            if val=='2':
                while True:
                    print('''
------------------------------------------------------------------
\t\tACCESS MENU
1. Details of all people who are vaccinated
2. Total number of people vaccinated
3. Number of females who are vaccinated
4. Number of males who are vaccinated
5. Number of people vaccinated whose age is above or of 18
6. Number of people vaccinated who are below age of 18
7. Number of people vaccinated at a given date
8. Number of people vaccinated at a given place
9. Main menu
-----------------------------------------------------------------''')
                    try:
                        ch=int(input('\nEnter your choice:'))
                        if ch==1:
                            q='select * from vaccinated'
                            cur.execute(q)
                            info=cur.fetchall()
                            print('Details of all people who are vaccianted')
                            print('-'*175)
                            print('Name\tGender \tAge\tDOB\t\tAadhar_no.\tphone_no.\t\tvaccine\tplace\tdose_1\t\tdose\tdose_2')
                            print('-'*175)
                            for i in info:
                                for j in i:
                                    print(j,end='\t')
                                print()
                            print('-'*175)
                        elif ch==2:
                            q='select count(aadhar_no) from vaccinated'
                            cur.execute(q)
                            info=cur.fetchone()
                            for i in info:
                                print('Total number of people vaccinated=',i)
                        elif ch==3:
                            q="select count(gender) from vaccinated where gender='F'"
                            cur.execute(q)
                            info=cur.fetchone()
                            for i in info :
                                print('Number of females who are vaccinated=',i)
                        elif ch==4:
                            q="select count(gender) from vaccinated where gender='M'"
                            cur.execute(q)
                            info=cur.fetchone()
                            for i in info :
                                print('Number of males who are vaccinated=',i)
                        elif ch==5:
                            q="select count(age) from vaccinated where age>=18"
                            cur.execute(q)
                            info=cur.fetchone()
                            for i in info :
                                print('Number of people vaccinated whose age is above or of 18=',i)
                        elif ch==6:
                            q="select count(age) from vaccinated where age<18"
                            cur.execute(q)
                            info=cur.fetchone()
                            for i in info :
                                print('Number of people vaccinated who are below age of 18=',i)
                        elif ch==7:
                            dt=input('Enter a date(yyyy-mm-dd):')
                            q="select count(aadhar_no) from vaccinated where vac_date_1='{}' or vac_date_2='{}'".format(dt,dt)
                            cur.execute(q)
                            info=cur.fetchone()
                            for i in info :
                                print('Number of people vaccinated at {}='.format(dt),i)
                        elif ch==8:
                            try:
                                place=input('Enter the palce:')
                                q="select count(aadhar_no) from vaccinated where vaccinated_at='{}'".format(place)
                                cur.execute(q)
                                info=cur.fetchone()
                                for i in info :
                                    print('Number of people vaccinated at {}='.format(place),i)
                            except:
                                print('No one vaccinated at {}'.format(place))
                        elif ch==9:
                            break
                        else:
                            print('Enter a valid input...')
                    except:
                        print('Invalid input...')
            elif val=='1':
                # Updating a record

                try:
                    aadhar=int(input('Enter the Aadhar card no.:'))
                    # Checking weather their record is present

                    cur.execute('select aadhar_no from vaccinated')
                    k=cur.fetchall()
                    out='no'
                    for i in k:
                        if aadhar in i:
                            out='yes'
                            break
                        else:
                            out='no'
                    if out=='no':
                        raise EOFError
                    else:
                        pass
                    cur.execute('select * from vaccinated where aadhar_no={}'.format(aadhar))
                    items=cur.fetchall()
                    for i in items:
                        for j in i:
                            print(j,end='   ')
                    confirm=input('\nIs this is the person whose detail you want to update(y/n):')
                    if confirm in 'yY':
                        # Asking for which information to be updated
                        
                        print('Which information you want to update:')
                        print('''
1. Name
2. Age
3. Date of Birth
4. Phone number
5. Vaccine name''')
                        try:
                            ch=int(input('\nEnter your choice:'))
                            if ch==1:
                                name=input('Enter your name(without error):')
                                q="update vaccinated set name='{}' where aadhar_no={}".format(name,aadhar)
                                cur.execute(q)
                                print('Name is updated as {}'.format(name))
                            elif ch==2:
                                age=int(input('Enter your correct Age:'))
                                q="update vaccinated set age={} where aadhar_no={}".format(age,aadhar)
                                cur.execute(q)
                                print('Age is updated as {}'.format(age))
                            elif ch==3:
                                date=input('Enter your Date of Birth (yyyy-mm-dd format):')
                                q="update vaccinated set date_of_birth='{}' where aadhar_no={}".format(date,aadhar)
                                cur.execute(q)
                                print('Date of birth is updated as {}'.format(date))
                            elif ch==4:
                                ph=int(input('Enter the phone number:'))
                                q="update vaccinated set phonenumber={} where aadhar_no={}".format(ph,aadhar)
                                cur.execute(q)
                                print('Phone number is updated as {}'.format(ph))
                            elif ch==5:
                                vaccine=input('Enter the vaccine_name:')
                                if vaccine not in ('covaxin','covishield'):
                                    print('vaccine name should be covaxin or covishield')
                                    raise
                                q="update vaccinated set vaccine_name='{}' where aadhar_no={}".format(vaccine,aadhar)
                                cur.execute(q)
                                print('Vaccine name is updated as {}'.format(vaccine))
                            else:
                                raise
                        except:
                            print('Enter a valid input')
                    else:
                        raise
                except:
                    print('Sorry your data not found')
                    print('Take your vaccine to update your record')
            elif val=='3':
                print('exiting program..')
                break
            else:
                print('Enter a valid input...')

else :
    print('Invalid Choice')
