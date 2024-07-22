drop table EMP;

create table EMP (
     empid   integer     primary key,
     fname   varchar(30)   not null,
     lname   varchar(30)   not null,
     email   varchar(100)  not null,
     phone   varchar(15)   not null,
     hdate   date          not null,
     jobid   varchar(20)   not null,
     sal     integer       not null,
     comm    decimal(5,2),
     mgrid   integer,
     deptid  integer
);

-- 데이터 입력
insert into emp(empid, fname, lname, email, phone,
                hdate, jobid, sal, comm, mgrid, deptid)
VALUES (100,'Steven','King','SKING','515.123.4567','2003-06-17','AD_PRES',24000,null,null,90);


select * from EMP;

-- 데이터 조회 1 - 리스트
select empid, fname, email, jobid, deptid from EMP;

-- 데이터 조회 2 - 상세 조회
select * from EMP where empid = 100;

-- 사원데이터 총 수 조회
select count(empid) total from EMP;