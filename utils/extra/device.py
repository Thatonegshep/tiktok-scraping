_C='offset'
_B='timezone_name'
_A='timezone'
import os,random,time,base64,datetime,pytz,uuid,binascii,curlify
from utils.extra.constants import*
class Device:
	def __init__(self):0
	@staticmethod
	def __setup_timezone(country_code):timezone_name=random.choice(pytz.country_timezones[country_code]);timezone=round(int(datetime.datetime.now(pytz.timezone(timezone_name)).utcoffset().seconds/3600));offset=round(datetime.datetime.now(pytz.timezone(timezone_name)).utcoffset().total_seconds());return{_B:timezone_name,_A:timezone,_C:offset}
	@staticmethod
	def __setup_locale(country_code):
		try:search_country=[country for country in locales if country_code in country.keys()];return search_country[0][country_code]
		except Exception as e:raise ValueError(e)
	@staticmethod
	def __set_gmt(timezone):
		A='GMT+{}:00'
		if 0<timezone<10:result='GMT+0{}:00'.format(str(timezone))
		if 0>timezone>-10:result='GMT-0{}:00'.format(str(timezone))
		if 0<timezone and timezone>=10:result=A.format(str(timezone))
		if timezone<0 and timezone<=-10:result=A.format(str(timezone))
		return result
	@staticmethod
	def __guuid():return str(uuid.uuid4())
	@staticmethod
	def __openudid():return binascii.hexlify(os.urandom(8)).decode()
	@staticmethod
	def __detect_api_level(os_version):
		if os_version==7.:return 24
		if os_version==8.:return 26
		if os_version==9.:return 28
		if os_version==1e1:return 29
		if os_version==11.:return 30
	@staticmethod
	def __security_path():
		paths=[]
		for i in range(2):random_bytes=os.urandom(16);encoded_path=base64.urlsafe_b64encode(random_bytes).decode();paths.append(encoded_path)
		return f"/data/app/~~{paths[0]}/com.zhiliaoapp.musically-{paths[1]}/base.apk"
	def create_device(self,country_code='us'):J='dpi';I='display_density';H='resolution';G='product';F='board';E='core';D='rom';C='build';B='os';A='device';simple_device=random.choice(devices);timezone_params=self.__setup_timezone(country_code);locales_params=self.__setup_locale(country_code);gmt=self.__set_gmt(timezone_params[_A]);build=random.choice(simple_device[C]);rom=random.choice(simple_device[D]);core=random.choice(simple_device[E]);model=random.choice(simple_device['model']);product_info=random.choice(simple_device[A]);board=random.choice(simple_device[F]);device_i=product_info[A];product=product_info[G];device={'device_brand':simple_device['brand'],'device_model':model,'google_aid':self.__guuid(),'cdid':self.__guuid(),'clientudid':self.__guuid(),'req_id':self.__guuid(),C:build,D:rom,'rom_version':build+'.'+rom,H:simple_device[H],_B:timezone_params[_B],_A:timezone_params[_A],_C:timezone_params[_C],'locale':locales_params,B:simple_device[B],'os_api':self.__detect_api_level(simple_device[B]),'openudid':self.__openudid(),I:simple_device[I],J:simple_device[J],A:device_i,G:product,'install_time':int(round(time.time()*1000))-random.randint(5000,30000),'region':country_code.upper(),'language':'en'if country_code=='us'else country_code,'app_language':'en'if country_code=='us'else country_code,'op_region':country_code.upper(),'sys_region':country_code.upper(),E:core,F:board,'gmt':gmt,'ut':random.randint(100,500),'cba':hex(random.randint(1000000000,5900000000)),'ts':random.randint(-1414524480,-1014524480),'uid':random.randrange(10000,10550,50),'dp':random.randint(100000000,999999999),'hc':f"0016{random.randint(500000,999999)}",'bas':random.randint(10,100),'bat':random.randrange(3500,4900,500),'path':self.__security_path(),'dbg':random.randint(-100,0),'token_cache':base64.urlsafe_b64encode(os.urandom(108)).decode().replace('=','_')};return device
