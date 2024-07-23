import sqlite3

# 사원 데이터 총 갯수 조회
def getTotalEmp():
    sql = 'select count(empid) + 1 total from emp'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    rs = cursor.fetchone()
    cnt = rs[0]
    cursor.close()
    conn.close()
    return cnt

def newEmp(emp):
    sql = "insert into emp values (?,?,?,?,?,?,?,?,"\
           "?, nullif(?,'null'), nullif(?,'null'))"
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (emp[0], emp[1], emp[2],emp[3], emp[4],emp[5],emp[6], emp[7], emp[8],emp[9],emp[10])
    cursor.execute(sql, params)
    print(cursor.rowcount, '건의 데이터 추가됨!')
    conn.commit()
    cursor.close()
    conn.close()

# 사원 데이터 전체 조회
def readAllEmp():
    sql = 'select empid, fname, email, jobid, deptid from emp'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    emps = cursor.fetchall()
    cursor.close()
    conn.close()
    return emps

# 사원 한명 상세 조회
def readOneEmp(empid):
    sql = 'select *  from emp where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (empid,)
    cursor.execute(sql, params)
    emp = cursor.fetchone()
    cursor.close()
    conn.close()
    return emp

#
def deleteEmp(empid):
    sql = 'delete from emp where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (empid,)
    cursor.execute(sql, params)
    cnt = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return cnt

#
def updateEmp(emp):
    sql = 'update emp set email=?, phone=?, jobid=?, sal=?, '\
            'comm=?, mgrid=?, deptid=? where empid = ?'
    conn = sqlite3.connect('db/python.db')
    cursor = conn.cursor()
    params = (emp[3], emp[4],emp[6], emp[7], emp[8],emp[9],emp[10],emp[0])
    cursor.execute(sql, params)
    cnt = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return cnt