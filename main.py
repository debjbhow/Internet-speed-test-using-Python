import speedtest

s= speedtest.Speedtest()

option= int(input('''What do you want to know   :
1) Upload Speed
2) Download Speed
3) Ping '''))

if option==1:
    print(s.upload())

elif option==2:
    print(s.download())
elif option==3:
    server=[]
    s.get_servers(server)
    print(s.results.ping)

else:
    print("Invalid option")