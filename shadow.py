import requests as req
from time import sleep

print("\t\n\nCodeD bY mile_403")
print("\tProxy type :\n\t [ 1 ] HTTP/S\n\t [ 2 ] SOCKS4\n\t [ 3 ] SOCKS5")
type = input("\tEnter number : ")
if int(type) == 1:
  header = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
  res = req.get("https://doku.ga/proxy/?http", headers=header).text
  open('http.txt','w').write(str(res.replace("<br />", ""))+'\n')
  print("\tHTTP/S Proxy List Saved in : http.txt")
  sleep(5)
elif int(type) == 2:
  header = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
  res = req.get("https://doku.ga/proxy/?socks4", headers=header).text
  open('socks4.txt','w').write(str(res.replace("<br />", ""))+'\n')
  print("\tSOCKS4 Proxy List Saved in : socks4.txt")
  sleep(5)
elif int(type) == 3:
  header = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}
  res = req.get("https://doku.ga/proxy/?socks5", headers=header).text
  open('socks5.txt','w').write(str(res.replace("<br />", ""))+'\n')
  print("\tSOCKS4 Proxy List Saved in : socks5.txt")
  sleep(5)
else:
  print("\tPlease input a valid number")
  sleep(10)
