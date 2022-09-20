import os
import shutil
import time as timer1
import sqlite3
from typing import Any
from time import  time as epochTime
from pathlib import Path


def encode(a):
    a = a.replace("\\", "$")
    a = a.replace("/", "$")
    a = a.replace(":", "___")
    # print(a)
    return a


#############function to encode & decode############

def decode(a):
    a = a.replace("$", "\\")
    a = a.replace("___", ":")
    # print(a)
    return a

def create_DB(input_right,input_left):
    global connection
    connection = sqlite3.connect(os.path.join(os.getcwd(), 'oddb.db'))
    global mycursor
    mycursor = connection.cursor()
    start=epochTime()

############## generate data base ################################

    mycursor.execute(" CREATE TABLE IF NOT EXISTS previous_dir (id integer primary key AUTOINCREMENT ,dir VARCHAR(255),"
                     "lastCheck timestamp) ")
    
    #input_right,input_left=input(" ").split()
    right=encode(input_right)
    left=encode(input_left)
    
    
    
  
    
    
    for i in range(2):
        
        stmt="select id  from previous_dir where dir=?"
        args=(encode(input_right)  ,)
        
        mycursor.execute(stmt,args)
        input_exists=mycursor.fetchall()
        zz="{}".format(encode(input_right))
        if(len(input_exists)) ==0:
            sql="insert into previous_dir (dir,lastcheck) values (?,?)"
            val = (encode(input_right),epochTime() )
            mycursor.execute(sql, val)
            connection.commit()
            
            #hg=input_exists[1][0]
            #print(decode(encode(input_right)))
            
           
            mycursor.execute(" CREATE TABLE IF NOT EXISTS {}(id  AUTO_INCREMENT ,name VARCHAR(255)"
                         ",path VARCHAR(255),rank integer ,created timestamp ,modified timestamp ,"
                         "size_file float ,flag integer ,copied integer,isFolder integer )".format(zz))
    
            for root ,dirs,files in os.walk(input_right):
                #print(root)
                #print(files)
                sql = "INSERT INTO {}(name,path,rank,created,modified,size_file" \
                                                 ",flag,copied,isFolder ) VALUES (?,?,?,?,?,?,?,?,?)".format(zz)
                cc=root[len(input_right):]
                dd=str(cc.count("\\")   )
                ee=os.path.abspath(os.path.join(root,os.pardir))
                ee=ee[len(input_right):]
                os.chdir(root)            
                val = [(cc,ee,dd,os.path.getctime(root),0,0,0,0,1)]
                #print(val)
                mycursor.executemany(sql, val)
                connection.commit()
                
                for x in files:
                    #print (root)
                    cc=root[len(input_right):]
                    #print(x)
                    #print(cc)
                    dd=str(cc.count("\\")   )
                    #print(dd)	
                    #os.chdir(root)   
                    val = [(x, cc,dd,os.path.getctime(x),os.path.getmtime(x),os.path.getsize(x),0,0,0)]
                    #print(val)
                    mycursor.executemany(sql, val)
                    connection.commit()
        
                    
        
##########################################3fdgsfdgmh############################
        
        if (len(input_exists)) != 0:
            
            stmt="select lastcheck,id  from previous_dir where dir=?"
            args=(encode(input_right),)
            mycursor.execute(stmt,args)
            input_exists=mycursor.fetchall()
            
            ''' find last time of sync'''
            timer=input_exists[-1][0]
        
            sql = "UPDATE  previous_dir SET lastcheck=? WHERE dir=?"
    
            val = (epochTime(),encode(input_right))
            mycursor.execute(sql, val)
            connection.commit()
            
            
            for root, dirs, files in os.walk(input_right):
                
                                    
                sql = "INSERT INTO {}(name,path,rank,created,modified,size_file" \
                                                 ",flag,copied,isFolder ) VALUES (?,?,?,?,?,?,?,?,?)".format(zz)
                cc=root[len(input_right):]
                dd=str(cc.count("\\")   )
                
                os.chdir(root)
                ctime=os.path.getctime(root)
                
                #print(val)
                if timer<ctime:
                    ee=os.path.abspath(os.path.join(root,os.pardir))
                    ee=ee[len(input_right):]
                    val = [(cc,ee,dd,ctime,0,0,0,0,1)]
                    mycursor.executemany(sql, val)
                    connection.commit()
    
    
                for x in files:
                    #os.chdir(root)
                    ctime=os.path.getctime(x)
                    mtime=os.path.getmtime(x)
                    
                    if timer<ctime :
                        sql = "INSERT INTO {}(name,path,rank,created \
                        ,modified,size_file,flag,copied,isFolder) VALUES \
                        (?,?,?,?,?,?,?,?,?)".format(zz)
                        
                        cc=root[len(input_right):]
                        dd=str(cc.count("\\")   )
                        #print(dd)            	      
                        val = [(x, cc,dd,ctime,mtime,os.path.getsize(x),5,8,0)]
                        mycursor.executemany(sql, val)
                        connection.commit()
                        
                    if timer<mtime and timer>ctime :
                        cc=root[len(input_right):]
                        dd=str(cc.count("\\")   )

                        print(f'{x}')            	      
                        ''' delete item befor modified '''
                        drg="DELETE FROM {} WHERE name='{}' and \
                        (path ='{}' and created='{}' )".format(zz,x,cc,ctime)
                        
                        
                        mycursor.execute(drg)
                        connection.commit()
                        
                        ''' insert modified item '''
                        val = [(x, cc,dd,ctime,mtime,os.path.getsize(x),5,8,0)]
                        mycursor.executemany(sql, val)
                        connection.commit()
                        
                        if encode(input_right) == right:
                            tempu=left
                        else:
                            tempu=right
                        ''' to delete in destination '''
                        upd="UPDATE {} SET flag='-5', copied ='8'\
                        where  name='{}' and path='{}'\
                         ".format(tempu,x,cc)
                        
                        mycursor.execute(upd)
                        connection.commit()
    
    
                        
        #print(input_right)
        input_right=input_left
        #print(input_right)
    
    #####################End of generate table#################################
    print("end task")
    print(epochTime()-start)

######################### SYNCK  #######################################

############## ALGORITHM ###########################################
def Sync( r ,l):
    right=encode(r)
    left=encode(l)
    for RR in range(2):
        stmt="select max(rank) from {} ".format(right)
        mycursor.execute(stmt)
        connection.commit()
        max=mycursor.fetchall()
        print(max[0][0])
        
            ##################file 0##############
        for k in range(max[0][0]):
            stmt = "select name from {} where rank='{}' and isFolder='0'\
                    and copied !='8' and name  not in \
                    (select name from {} where \
                    rank='{}' and isFolder='0' )".format(right,k,left,k)
            
            
            mycursor.execute(stmt)
            connection.commit()
            out=mycursor.fetchall()
            print(out)
            
            stmt="update {} set flag='5', copied='8' where  rank ='{}' and \
                  name in ( select name from {} where rank='{}' and isFolder='0'\
                  and copied !='8' and name not in \
                (select name from {} \
                  where rank ='{}' and isFolder='0'))".format(right,k,right,k,left,k)
            
            mycursor.execute(stmt)
            connection.commit()
            out=mycursor.fetchall()
            #print(out)
            
            ####################folder 0 ##################################
            
            stmt1 = "select name from {} where rank='{}' and isFolder='1' \
                    and copied !='8' and name  not in \
                    (select name from {} where \
                    rank='{}' and isFolder='1' )".format(right,k+1,left,k+1)
            
            mycursor.execute(stmt1)
            connection.commit()
            out=mycursor.fetchall()
            print(out)
            #print(out[0][0])
            
            stmt1="update {} set flag='5', copied='8' where \
                  name in ( select name from {} where rank='{}' and isFolder='1' and\
                  copied !='8' and name not in \
                  (select name from {} \
                  where rank ='{}' and \
                  isFolder='1' ))".format(right,right,k+1,left,k+1)
            
            mycursor.execute(stmt1)
            connection.commit()
            #out1=mycursor.fetchall()
            #print(out)
            
            #################### Ckeck point  ################################
            
            
            for i in range(len(out)):
                a=out[i][0]
                print("adfs")
                stmt1="select path from {} where path LIKE\
                '{}' or path LIKE '{}\\%' ".format(right,a,a)
                mycursor.execute(stmt1)
                connection.commit()
                out2=mycursor.fetchall()
                stmt2="update {} set copied = '8' where path LIKE \
                '{}' or path LIKE '{}\\%'".format(right,a,a)
                mycursor.execute(stmt2)
                connection.commit()
                print(out2)
            
        
        
        right,left=left,right
    
    ########### END OF ALGORITHM ###################################
    
    
    ##################  SYNC SYNC SYNC ############################
    
    for yyy in range(2):
        
        ###################### DELETE ############################
        stmt="select path, name  from {} where flag='-5'".format(left)
        mycursor.execute(stmt)
        connection.commit()
        rm=mycursor.fetchall()
        for i in range(len(rm)):
            rm1="\\".join(rm[i])
            rm1=decode(left)+rm1
            if os.path.exists(rm1):
                os.remove(rm1)
                print(rm1)
        
         
        stmt="update {} set flag='0', copied='0' where flag='-5' ".format(left)
        
        mycursor.execute(stmt)
        connection.commit()
        out=mycursor.fetchall()
        #print(out)
        right, left = left, right
        ###################### COPY FOLDER COPY ############################
    for hhh in range(2):
        cfo="select name  from {} where \
                flag='5' and isFolder='1' ".format(left)
            
        mycursor.execute(cfo)
        connection.commit()
        cfo=mycursor.fetchall()
        print(cfo)
        
        
        for i in range(len(cfo)):
            #print(cfo)
            ahd="\\".join(cfo[i])
            ah=decode(left)+ahd
            bh=decode(right)+ahd
            print(bh)
            print(ah)
            if not os.path.isdir('{}'.format(bh)):
                shutil.copytree(ah,bh)
        
        
        
        stmt="update {} set flag='0', copied='0' \
              where  flag='5' and isFolder='1' ".format(left)
        
        mycursor.execute(stmt)
        connection.commit()
        out=mycursor.fetchall()
        #print(out)
        
        
        stmt="update {} set flag='0', copied='0' \
              where  flag='0' and copied='8' and isFolder='0' ".format(left)
        
        mycursor.execute(stmt)
        connection.commit()
        out=mycursor.fetchall()
        #print(out)
        right, left = left, right
        ###################### COPY FILE COPY ############################
    for kkk in range(2):
        gfo="select path,name  from {} where \
                flag='5' and isFolder='0' ".format(left)
            
        mycursor.execute(gfo)
        connection.commit()
        gf=mycursor.fetchall()
        print(gf)
        print(len(gf))
        for i in range(len(gf)):
            gf_temp="\\".join(gf[i])
            gf1=decode(left)+gf_temp
            gf2=decode(right)+gf_temp
            if not os.path.exists(gf2):
                shutil.copy(gf1,gf2)
                print(gf1)
                print(gf2)
            
        
        stmt="update {} set flag='0', copied='0' where \
                flag='5' and copied='8' and isFolder='0' ".format(left)
        
        mycursor.execute(stmt)
        connection.commit()
        out=mycursor.fetchall()
        #print(out)
    
        right,left=left,right
    


############## END SYNC END SYNK ##########################


#create_DB('C:\\Users\\asus\\Desktop\\N00600000','C:\\Users\\asus\\Desktop\\N00300000')
#Sync('C:\\Users\\asus\\Desktop\\N00600000','C:\\Users\\asus\\Desktop\\N00300000')

    #sql = "DROP TABLE G___$asd "
    #mycursor.execute(sql)
    #sql = "DROP TABLE G___$asf "
    #mycursor.execute(sql)

    #mycursor.execute(" CREATE TABLE IF NOT EXISTS file_dir (id  AUTO_INCREMENT ,name VARCHAR(255)"
    #                 ",path VARCHAR(255),rank integer ,created timestamp ,modified timestamp ,"
    #                 "size_file float ,flag integer ,copied integer )")

    #sql = "DELETE FROM previous_dir WHERE dir='G___$asd' "
    #mycursor.execute(sql)
    #connection.commit()
    #sql = "DELETE FROM G___$asd WHERE name='dfdngfm.txt'\
    #         and created='1561901351.12795' "
    #mycursor.execute(sql)
    #connection.commit()










