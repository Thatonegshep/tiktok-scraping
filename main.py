_I=' to start'
_H='press '
_G=' Enter video link '
_F='proxies.txt'
_E=False
_D='clear'
_C=True
_B='(\\d{18,19})'
_A='nt'
import requests,ssl,re,cursor
cursor.hide()
from pystyle import*
from http import cookiejar
from urllib3.exceptions import InsecureRequestWarning
from utils.extra.algorithms.xgorgon import Gorgon
from utils.device_gen import*
import time
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context=ssl._create_unverified_context
class BlockCookies(cookiejar.CookiePolicy):return_ok=set_ok=domain_return_ok=path_return_ok=lambda self,*args,**kwargs:_E;netscape=_C;rfc2965=hide_cookie2=_E
class BytedanceFuck:
	def __init__(self,__aweme_id):self.__aweme_id=__aweme_id;self.__success=0;self.__errors=0;self.__devices=0;self.__device=0;self.__version='2.0';self.__lock=threading.Lock();self.__devices=['SM-G9900','SM-A136U1','SM-M225FV','SM-E426B','SM-M526BR','SM-M326B','SM-A528B','SM-F711B','SM-F926B','SM-A037G','SM-A225F','SM-M325FV','SM-A226B','SM-M426B','SM-A525F'];self.__domains=['api22-core-c-useast1a.tiktokv.com','api19-core-c-useast1a.tiktokv.com','api16-core-c-useast1a.tiktokv.com','api21-core-c-useast1a.tiktokv.com'];self.__versions=['190303','190205','190204','190103','180904','180804','180803','180802'];self.__client=requests.Session();self.__proxies=open(_F,'r').read().splitlines();self.__client.cookies.set_policy(BlockCookies())
	def __safe_print(self,arg):self.__lock.acquire();print(arg);self.__lock.release()
	def __send_request(self,__device_id,__install_id):
		try:
			proxy=random.choice(self.__proxies);params=urlencode({'device_id':__device_id,'iid':__install_id,'device_type':random.choice(self.__devices),'app_name':'musical_ly','host_abi':'armeabi-v7a','channel':'googleplay','device_platform':'android','version_code':random.choice(self.__versions),'device_brand':'samsung','os_version':random.randint(6,9),'aid':1233});payload=urlencode({'item_id':self.__aweme_id,'play_delta':1});sig=Gorgon(params,payload,None).get_value();response=self.__client.post(url='https://'+random.choice(self.__domains)+'/aweme/v1/aweme/stats/?'+params,headers={'x-gorgon':sig['X-Gorgon'],'x-khronos':sig['X-Khronos'],'user-agent':'okhttp/3.10.0.1'},data=payload,proxies={'http':f"http://{proxy}",'https':f"http://{proxy}"},verify=_E)
			if response.json()['status_code']==0:self.__success+=1;self.__safe_print(f"root@localhost ~ Views sent: {self.__success} @ {str(response.json()["log_pb"]["impr_id"]).lower()}")
			else:self.__errors+=1
		except Exception as e:self.__errors+=1;pass
	def __title_loop(self):
		while _C:print(f"title Viewbot ^| Success: {self.__success} ^| Fails: {self.__errors} ^| Devices: {self.__device} ^| Video: {self.__aweme_id} ^| {self.__version} by Tekky");time.sleep(.001)
	def __view_loop(self,__device_id,__install_id):
		__thread_contition=0
		while __thread_contition<2000:
			if threading.active_count()<1000:threading.Thread(target=self.__send_request,args=[__device_id,__install_id]).start();__thread_contition+=1
	def __device_loop(self):
		while _C:
			try:proxy=random.choice(self.__proxies);__start=time.time();device=Device().create_device();__device_id,__install_id=Applog(device,proxy).register_device();Xlog(__device_id,proxy).bypass();self.__device+=1;print(Col.purple+'{'+Col.reset+'*'+Col.purple+'}'+Col.reset+f"{Col.reset} Generated device {Col.blue}! {Col.purple}[{Col.blue}{__device_id} {Col.reset}|{Col.blue} {__install_id}{Col.purple}] {Col.purple}[{Col.reset}Execution time: {Col.blue}{round(time.time()-__start,1)}s{Col.purple}]{Col.reset}");threading.Thread(target=self.__view_loop,args=[__device_id,__install_id]).start()
			except Exception as e:print(e);self.__errors+=1;continue
	def start(self):
		for x in range(5):threading.Thread(target=self.__device_loop).start()
def init():os.system(f"title Viewbot v2.0 by Tekky"if os.name==_A else'');os.system(f"cls"if os.name==_A else _D);link=input(Col.purple+'{'+Col.reset+'?'+Col.purple+'}'+Col.reset+_G+Col.purple+'['+Col.reset+_H+Col.blue+'Enter'+Col.reset+_I+Col.purple+']'+Col.reset+' -> ');__aweme_id=str(re.findall(_B,link)[0]if len(re.findall(_B,link))==1 else re.findall(_B,requests.head(link,allow_redirects=_C,timeout=5).url)[0]);os.system('cls'if os.name==_A else _D);BytedanceFuck(__aweme_id).start()
def fetch_proxies():
	response=requests.get(url='https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxy-list/data.txt')
	if response.ok:
		os.unlink(_F)
		with open(_F,'w')as f:f.write(response.text);f.close();print('proxy list fetched :)')
	else:print('proxy list fetch error...');exit(1)
if __name__=='__main__':os.system(f"title Viewbot v2.0 by Tekky"if os.name==_A else'');os.system(f"cls"if os.name==_A else _D);link=input(Col.purple+'{'+Col.reset+'?'+Col.purple+'}'+Col.reset+_G+Col.purple+'['+Col.reset+_H+Col.blue+'Enter'+Col.reset+_I+Col.purple+']'+Col.reset+' -> ');__aweme_id=str(re.findall(_B,link)[0]if len(re.findall(_B,link))==1 else re.findall(_B,requests.head(link,allow_redirects=_C,timeout=5).url)[0]);os.system('cls'if os.name==_A else _D);BytedanceFuck(__aweme_id).start()
