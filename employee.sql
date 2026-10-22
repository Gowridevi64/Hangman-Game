delimiter $$
create trigger employee_insert
after insert on employee
for each row
begin
insert into employee_log(emp_name,action_time)
values(New.name,now());
end $$
delimiter ;