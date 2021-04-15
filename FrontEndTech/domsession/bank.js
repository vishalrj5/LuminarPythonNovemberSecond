class Bank {

    static getData() {
        var users = {
            userone: { username: "userone", password: "test", mpin: 201348, acno: 1000, balance: 1000 },
            usertwo: { username: "usertwo", password: "test1", mpin: 201345, acno: 1001, balance: 2000 },
            userthree: { username: "userthree", password: "test2", mpin: 2020, acno: 1002, balance: 3000 },
        }
        return users

    }

    //authenticate user("userone","test")
    static authenticateUser(username, password) {

        alert("authentication")

        var data = Bank.getData()
        if (username in data) {
            let pwd = data[username]["password"]
            if (pwd == password) {


                return 0
            }
            else {
                return -1
            }
        }
        else {
            return 1
        }

    }

    static login() {
        alert("inside login")
        let uname = document.querySelector("#uname").value
        let pwd = document.querySelector("#pwd").value
        var user = Bank.authenticateUser(uname, pwd)
        if (user == 1) {
            alert("User doesnot Exists")

        }
        else if (user == -1) {
            alert("invalid password")
        }
        else if (user == 0) {
            alert("login success")
            window.location.href="log2.html"
        }
    }
    static deposit(username,balance) {

        alert("inside deposit")
        let uname = document.querySelector("#u1name").value
        var newamount = document.querySelector("#dep").value
        var acc = document.querySelector("#acc").value
        var user = Bank.authenticateUser(uname, pwd)
        var data=Bank.getData()
        if(uname in data){
            let dep=data[uname]["balance"]
            
            alert(data[uname][amount])
        }
        else{
            alert("Invalid Account number")
        }
        

    }

    static withdraw() {

    }
}

