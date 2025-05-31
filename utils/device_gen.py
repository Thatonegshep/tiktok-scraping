_e='armeabi-v7a'
_d='offset'
_c='googleplay'
_b='os_version'
_a='channel'
_Z='Keep-Alive'
_Y='login=0;ct=0'
_X='user-agent'
_W='connection'
_V='x-tt-dm-status'
_U='x-ss-req-ticket'
_T='accept-encoding'
_S='wifi'
_R='dpi'
_Q='cdid'
_P='timezone_name'
_O='update_version_code'
_N='manifest_version_code'
_M='openudid'
_L='os_api'
_K='language'
_J='X-Khronos'
_I='X-Gorgon'
_H=None
_G='region'
_F='resolution'
_E='device_brand'
_D='aid'
_C='device_model'
_B='version_code'
_A='os'
import random,json,time,hashlib,requests,curlify,base64,sys,colorama,datetime,urllib.parse,threading,uuid,binascii,os
from urllib.parse import*
from utils.extra.constants import*
from utils.extra.algorithms.ttencrypt import TTEncrypt
from utils.extra.algorithms.xgorgon import Xgorgon
from utils.extra.device import Device
class Applog:
	def __init__(self,device,proxy):self.__device=device;self.__host='log-va.tiktokv.com';self.proxies={'http':f"http://{proxy}",'https':f"http://{proxy}"}
	def __headers(self,params,payload=_H):sig=Xgorgon().calculate(params,payload,_H);headers={'x-ss-stub':str(hashlib.md5(str(payload).encode()).hexdigest()).upper(),_T:'gzip','passport-sdk-version':'19','sdk-version':'2',_U:str(int(time.time()))+'000',_V:_Y,'host':self.__host,_W:_Z,'content-type':'application/octet-stream',_X:f"com.zhiliaoapp.musically/{application[_B]} "+f"(Linux; U; Android {self.__device[_A]}; pt_BR; {self.__device[_C]}; "+f"Build/{self.__device["build"]}; "+'Cronet/TTNetVersion:5f9640e3 2021-04-21 QuicVersion:47946d2a 2020-10-14)',_I:sig[_I],_J:str(sig[_J])};return headers
	def __params(self):G='locale';F='build_number';E='op_region';D='app_language';C='sys_region';B='ab_version';A='version_name';__base_params={'ac':_S,_a:_c,_D:application[_D],'app_name':'musical_ly',_B:application[_B],A:application[A],'device_platform':'android',B:application[B],'ssmix':'a','device_type':self.__device[_C],_E:self.__device[_E],_K:self.__device[_K],_L:self.__device[_L],_b:self.__device[_A],_M:self.__device[_M],_N:application[_N],_F:str(self.__device[_F]).split('x')[1]+'*'+str(self.__device[_F]).split('x')[0],_R:self.__device[_R],_O:application[_O],'_rticket':round(time.time()*1000),'app_type':'normal',C:self.__device[C],_P:self.__device[_P],D:self.__device[D],'ac2':_S,'uoo':'0',E:self.__device[E],'timezone_offset':self.__device[_d],F:application[F],G:self.__device[G],_G:self.__device[_G],'ts':int(time.time()),_Q:self.__device[_Q],'cpu_support64':'true','host_abi':_e};return urlencode(__base_params)
	def __payload(self):K='req_id';J='clientudid';I='google_aid';H='sig_hash';G='rom_version';F='rom';E='timezone';D='display_density';C='release_build';B='git_hash';A='app_version';payload={'magic_tag':'ss_app_log','header':{'display_name':'TikTok',_O:application[_O],_N:application[_N],'app_version_minor':'',_D:application[_D],_a:_c,'package':'com.zhiliaoapp.musically',A:application[A],_B:application[_B],'sdk_version':'2.12.1-rc.17','sdk_target_version':29,B:application[B],_A:'Android',_b:str(self.__device[_A]),_L:self.__device[_L],_C:self.__device[_C],_E:self.__device[_E],'device_manufacturer':self.__device[_E],'cpu_abi':_e,C:application[C],'density_dpi':self.__device[_R],D:self.__device[D],_F:self.__device[_F],_K:self.__device[_K],E:self.__device[E],'access':_S,'not_request_sender':0,F:self.__device[F],G:self.__device[G],_Q:self.__device[_Q],H:application[H],'gaid_limited':0,I:self.__device[I],_M:self.__device[_M],J:self.__device[J],_G:self.__device[_G],'tz_name':f"{self.__device[_P].split("/")[0]}\\/{self.__device[_P].split("/")[1]}",'tz_offset':self.__device[_d],K:self.__device[K],'custom':{'is_kids_mode':0,'filter_warn':0,'web_ua':f"Dalvik\\/2.1.0 (Linux; U; Android {self.__device[_A]}; {self.__device[_C]} Build\\/{self.__device["build"]})",'user_period':0,'user_mode':-1},'apk_first_install_time':self.__device['install_time'],'is_system_app':0,'sdk_flavor':'global'},'_gen_time':round(time.time()*1000)};return payload
	@staticmethod
	def __tt_encryption(data):ttencrypt=TTEncrypt();data_formated=json.dumps(data).replace(' ','');return ttencrypt.encrypt(data_formated)
	def register_device(self):
		A='device_id';params=self.__params();payload=self.__payload();r=requests.post(url='http://'+self.__host+'/service/2/device_register/?'+params,headers=self.__headers(params),data=bytes.fromhex(self.__tt_encryption(payload)),proxies=self.proxies)
		if r.json()[A]==0 or r.json()[A]=='0':self.register_device()
		if r.ok:print('registered....')
		return r.json()[A],r.json()['install_id']
class Xlog:
	def __init__(self,__device_id,proxy):self.__device_id=__device_id;self.proxies={'http':f"http://{proxy}",'https':f"http://{proxy}"}
	def bypass(self):params=urlencode({_A:'0','ver':'0.6.11.29.19-MT','m':'2','app_ver':'19.1.3',_G:'en_US',_D:'1233','did':self.__device_id});sig=Xgorgon().calculate(params,_H,_H);headers={_T:'gzip','cookie':'sessionid=',_U:str(''.join(str(time.time()).split('.')))[:13],_V:_Y,_I:sig[_I],_J:str(sig[_J]),'host':'xlog-va.tiktokv.com',_W:_Z,_X:'okhttp/3.10.0.1'};url='https://xlog-va.tiktokv.com/v2/s/?'+params;response=requests.get(url,headers=headers,proxies=self.proxies)
