import socket,threading,sys;

clients=[]
name=[]
dict={"A1":'123456','A2':'123456','A3':'123456','A4':'123456','A5':'123456'}
#接收连接则创建线程执行
class myThread (threading.Thread):   #继承父类threading.Thread
    def __init__(self, threadID, name, counter, client):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.client=client
        clients.append(client)#添加客户端
        self.flag=False#判断下线
        print(name+"已运行")
        self.usrinfo=""

    #给各个客户端发消息
    def sendmess(self,message):
        for st in clients:
            st.send(message.encode())

    #处理接收消息
    def receive(self):
        str=self.client.recv(1024).decode()#接收消息
        print(str)
        if str=="/exitmeplease":#如果消息为/exitmeplease，执行停止处理
            self.client.send("exit".encode())
            self.stop()
            return
        self.sendmess(str)#给各个客户端发消息

    #处理停止请求
    def stop(self):
        clients.remove(self.client)#移除客户端
        name.remove(self.usrinfo[0])
        self.flag=True#将下线标志设为TRUE
        self.client.close()  # 下线，终止socket
        print(self.usrinfo[0]+"已经下线")
        self.sendmess(self.usrinfo[0]+"已经下线")#发送下线信息

    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        self.usrinfo=self.client.recv(1024).decode().split("&")#获取信息
        print(self.usrinfo)
        #验证
         #验证是否已登录
        if self.usrinfo[0] in name:
            self.client.send("2".encode())
            print("345")
            return
         #验证用户名密码
        if self.usrinfo[0] in dict:#验证用户名
            if dict[self.usrinfo[0]]==self.usrinfo[1]:#验证密码
                name.append(self.usrinfo[0])
                self.client.send("1".encode())
                while True:
                    if self.flag:#监听下线消息
                        break
                    self.receive()
                return#返回

        #此处代表验证失败,发送错误消息并终止socket
        self.client.send("4".encode())
        print(self.usrinfo[0]+"验证失败")
        self.client.close()
        clients.remove(self.client)




def conn():#创建服务
    host=socket.gethostname()
    port=8888
    addr=(host,port)
    s=socket.socket()#创建套接字
    s.bind(addr)#绑定地址
    s.listen(5)#等待连接，最大数量5
    print("running")
    return s

def startUp():
    s=conn()
    x=0

    while True:
        client,add=s.accept()#建立连接，连接为client，地址add
        x+=1
        thread1=myThread(x,"thread"+str(x),x,client)#将连接转到线程处理
        thread1.start()

if __name__ == '__main__':
    startUp()