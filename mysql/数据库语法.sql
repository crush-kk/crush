-- 1、想一想如下命令怎么写？
-- （1）查看所有数据库
show databases;
-- （2）删除数据库
drop <数据库名>;
-- （3）创建数据库
create <数据库名>;
-- （4）使用数据库
use <数据库名>
-- （5）查看所有表
show tables;
-- （6）查看表结构
 desc tables;
-- 2、sql数据类型有哪些？
数值型 tinyint/smallint/int/bigint/float/double/decimal 
字符串型char/varchar/text 
日期时间型 date/time/timestamp

-- 3、sql约束有哪些？
非空约束 not null
唯一约束 unique key 数据允许为空，如果不为空，则数据不能重复。
主键约束primary key 数据不允许为空，且数据不能重复。系统会为主键约束生成索引，一个表的主键约束只能有一个，主键约束可以有多个字段
外键约束 foreign key
-- 4、char(长度)和varchar(长度)的区别？
char 定长字符串，所以存取速度比varchar快很多，但是当插入数据长度小于固定长度，用空格填充，是一种空间换时间的做法。最多存放255个字符。
varchar 可变长字符串，所以存取速度慢，是一种时间换空间的做法。最多存放65532个字符。
-- 5、修改表结构语法有哪些？
添加字段
alter table <表名> add <新字段> <数据类型>;
-- 修改字段名和数据类型
alter table <表名> change/modify <旧字段> <新字段> <数据类型>;
-- 只修改数据类型
alter table <表名> modify  <新字段> <数据类型>;
-- 删除字段
alter table <表名> drop <字段>;
-- 修改表名
alter table <表名> rename to  <新表名>;
-- 添加唯一约束
alter table <表名> add constraint <约束名> unique(字段名);
-- 删除唯一约束
alter table <表名> drop index <约束名>;
-- 添加外键约束
alter table <表名> add constraint <外键约束名> foreign key (字段名) references <主表名> (字段名) [ on update | delete no xxxx];
no action 不允许主键表执行操作
cascade 主键随着外键操作
set null 
-- 添加索引
alter table <表名> add index 索引名(字段名);
-- 删除索引
alter table <表名> drop index 索引名;

-- 6、分组查询的完整语法？
select <分组字段名> from <表名> group by <分组字段>;
-- 7、子查询的结果可以有哪些？怎么用？

-- 子查询练习：
-- student 表中有sno,sname,sage,ssex字段
-- teacher 表中有tno,tname字段
-- course 表中有cno,cname,tno字段
-- sc 表中有sno,cno,score字段
-- 求：
-- 1.查询王华的所有课程成绩；
select cname, score from student s ,sc,course c where s.sno=sc.sno and sc.cno=c.cno;
-- 2.查询所有课程成绩小于60 分的同学的学号、姓名；
selct s.sno, sname, from student s, sc, course c where c.cno=sc.cno and sc.sno=s.sno and score < 60;
-- 3.查询平均成绩大于85 的所有学生的学号、姓名和平均成绩
selct s.sno, sname,avg(score) from student s, sc, course c where c.cno=sc.cno and sc.sno=s.sno group by s.sno having avg(score) > 85;
-- 8、左连接、右连接和全连接的区别？
左连接 以左表作为基础，结果集包括左表的所有行。若右表有匹配的记录则直接匹配，否则补空值。
右连接 以右表作为基础，结果集包括右表的所有行。若左表有匹配的记录则直接匹配，否则补空值。 
全连接 结果集包括左表和右表的所有行。当某行在另一表中没有匹配行，补空值。
-- 9、删除drop truncate delete 的区别：
-- 1.语法
drop table <表名>;
truncate <表名>;
delete * from <表名>;
-- 2.速度
从快到慢： drop > truncate > delete
-- 3.语言类型
drop、truncate 是DDL数据定义语言
delect 是DML数据操纵语言
-- 4.日志

-- 5.表中如果有自增变量
delect 不会删除索引。下次插入数据保持下一个索引。
-- 10、索引的创建与作用？
加快查询速度
-- 11、sql语言分为哪几类？
DDL、DQL、DML、DCL


#存储过程

CREATE DEFINER=`root`@`localhost` PROCEDURE `generate_student`(v_left int, v_right int, account_prefix varchar(20), v_password varchar(20))
BEGIN
  declare v_age int;
  declare v_gender char(1);
  declare v_i int default v_left;
  
  lp: loop
    if v_i > v_right then
      leave lp;
    end if;
    #设置随机年龄段在20 ~ 40岁之间
    set v_age = 20 + floor(rand() * 21);
    #随机设置性别 F男 M女
    set v_gender = elt(1 + floor(rand() * 2),'F', 'M');
    insert into student(sid, account, `password`, sname, age, gender) values(v_i, concat(account_prefix, v_i), v_password,  concat(account_prefix, v_i), v_age, v_gender);
    set v_i = v_i + 1;
  end loop;
END

#游标的使用
-- 1.定义一个游标
-- 2.定义游标退出机制
-- 3.开启游标
-- 4.做一个死循环
-- 5.使用游标
-- 6.关闭游标
CREATE DEFINER=`root`@`localhost` PROCEDURE `change_age`()
BEGIN
declare v_sid int;
declare v_age int;
declare done tinyint default false;
-- 1. 定义一个游标
 declare stu_cs cursor for select sid, age from student;
 -- 2. 定义游标退出机制
 declare continue handler for not found set done = true;
 -- 3. 开启游标
 open stu_cs;
-- 4. 定义一个死循环
lp: loop
  if done then 
    leave lp;
  end if;
-- 5.使用游标
  fetch stu_cs into v_sid, v_age;
  if v_age % 2 = 1 then
    update student set age = age + 1 where sid = v_sid;
  end if;
end loop;
-- 6. 关闭游标
close stu_cs;
 
END


