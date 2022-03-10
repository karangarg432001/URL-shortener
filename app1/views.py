from django.shortcuts import render
from django.db import connection
# Create your views here.
def xyz(request):
    return render(request, "index.html")

def signUp(request):
    email = request.POST['email']
    psw = request.POST['pswname']
    cursor = connection.cursor()
    query1 = "select * from users where email  ='" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchall()
    if len(data) > 0:
        data = {"email":"Already SignedUP" , "password":""}
        return render(request, "first.html", data)
    else:
        query2 = "insert into users (email, password) values (%s, %s)"
        value2 = (email, psw)
        cursor.execute(query2, value2)
        print(cursor.rowcount)
        data = {"email":email, "password":psw}
        return render(request, "first.html", data)

# Create your views here.
def signin(request):
    return render(request, "login.html")


def login(request):
    email = request.POST['email']
    psw = request.POST['psw']
    cursor = connection.cursor()
    query1 = "select * from users where email  ='" + email + "'"
    cursor.execute(query1)
    data = cursor.fetchone()
    if data is None:
        data = {"email": "Not SignedUP", "password": ""}
        return render(request, "first.html", data)
    else:
        if data[2] == 0:
            data = {"email": "You are not verified user", "password": ""}
            return render(request, "first.html", data)
        if data[1] == psw:
            data = {"email": "Login Success", "password": ""}
            return render(request, "first.html", data)
        else:
            data = {"email": "Password is not correct", "password": ""}
            return render(request, "first.html", data)


