import pickle
import Employee as emp
#creating obj of Employee class
e=emp.Employee(100,'AAA',5000,'Daund')
#now save state of an obj to file-pickling
with open("employees.txt","wb") as f:
    pickle.dump(e,f)
    print("obj successfully stored")
#now read state of an obj from file--unpickling
with open("employees.txt","rb") as f:
    obj=pickle.load(f)
    print("obj read succssfully ")
    obj.display()