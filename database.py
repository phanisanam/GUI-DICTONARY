import sqlite3
word_list=[]
def connect():  
   con=sqlite3.connect("data.db")
   cur=con.cursor()
   cur.execute("create table  IF NOT EXISTS dictonary(word text,meaning text)")
   con.commit()
   con.close()


def insert(word,meaning):
    con=sqlite3.connect("data.db")
    cur=con.cursor()
    cur.execute("insert into dictonary values(?,?)",(word,meaning))
    con.commit()
    con.close()

def search(word):
    con=sqlite3.connect("data.db")
    cur=con.cursor()
    cur.execute("select meaning from dictonary where word=?",[word])
    rows=cur.fetchall();
    con.close()
    return rows



def view():
    con=sqlite3.connect("data.db")
    cur=con.cursor()
    cur.execute("select word from dictonary")
    rows=cur.fetchall();
    con.close()
    for keys in rows:
       word_list.append(keys)
    return word_list
       


    





connect()

#insert("heart","a human organ")
#insert("gold","an ornament")
#insert("sandals","a type of foot wear")
#insert("ground","a place where childrens plays ")
#insert("state","part of a countty")
#insert("mouse","a living organism")
#insert("computer","a device which contains Cpu and ram")
#insert("fan","a electronic device")
#insert("potatto","a type of vegetable which grows inside the soil")

#print(search("rod"))
#delete("potatto")

