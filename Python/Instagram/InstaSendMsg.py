from Instagram import Instagram

if __name__ == "__main__":

    instance = Instagram()
    try:
        login_status = True
        while login_status:
            username = input("Enter username... ")
            password = input("Enter password... ")
    
            login_status = instance.login(username, password)
    
        while True:

            receiver = input("Enter receiver username... ")
            receiver_status = instance.selectUser(receiver)

            if receiver_status:
                message = input("Enter message to send... ")
                count = int(input("Enter how many times to send..."))
                for c in range(count):
                    instance.sendMsg(message)
                    print(f"count:{c+1}")
                if (c+1) == count:
                    print(f"Message({message}) sending complete.(Times:{c+1})")

    except Exception as e:
        print(e)
    finally:
        print("Closing all windows...")
        instance.closeBrowser()
