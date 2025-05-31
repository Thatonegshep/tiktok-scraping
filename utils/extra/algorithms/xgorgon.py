Q='utf-8'
P='UTF-8'
O='time'
N='X-Khronos'
M='X-Gorgon'
L=format
K=round
J=enumerate
H='gorgon'
F=str
E='0'
D=range
C=len
B=int
A=None
import hashlib as G,random as R,struct,json,time as I
class S:
	def __init__(A,params,data,cookies):A.params=params;A.data=data;A.cookies=cookies
	def hash(B,data):A=F(G.md5(data.encode()).hexdigest());return A
	def get_base_string(A):B=A.hash(A.params);B=B+A.hash(A.data)if A.data else B+F(E*32);B=B+A.hash(A.cookies)if A.cookies else B+F(E*32);return B
	def get_value(A):B=A.get_base_string();return A.encrypt(B)
	def encrypt(H,data):
		J=B(I.time());len=20;O=[223,119,185,64,185,155,132,131,209,185,203,209,247,194,185,133,195,208,251,195];C=[]
		for E in D(0,12,4):
			P=data[8*E:8*(E+1)]
			for K in D(4):A=B(P[K*2:(K+1)*2],16);C.append(A)
		C.extend([0,6,11,28]);A=B(hex(J),16);C.append((A&4278190080)>>24);C.append((A&16711680)>>16);C.append((A&65280)>>8);C.append((A&255)>>0);G=[]
		for(Q,R)in zip(C,O):G.append(Q^R)
		for E in D(len):S=H.reverse(G[E]);T=G[(E+1)%len];U=S^T;V=H.rbit_algorithm(U);A=(V^4294967295^len)&255;G[E]=A
		L=''
		for W in G:L+=H.hex_string(W)
		return{M:'0404b0d30000'+L,N:F(J)}
	def rbit_algorithm(H,num):
		F='';A=bin(num)[2:]
		while C(A)<8:A=E+A
		for G in D(0,8):F=F+A[7-G]
		return B(F,2)
	def hex_string(B,num):
		A=hex(num)[2:]
		if C(A)<2:A=E+A
		return A
	def reverse(C,num):A=C.hex_string(num);return B(A[1:]+A[:1],16)
class T:
	digits={B:A for(A,B)in J('0123456789abcdefghijklmnopqrstuvwxyz')};HEX_STRS=[[30,0,224,220,147,69,1,200],[30,0,224,236,147,69,1,200],[30,0,224,228,147,69,1,208],[30,60,224,244,147,69,0,216],[30,64,224,228,147,69,0,216],[30,0,224,227,147,69,1,213],[30,64,224,210,147,69,0,160],[30,64,224,203,147,69,0,150],[30,64,224,211,147,69,0,167],[30,64,224,228,147,69,0,156],[30,64,224,216,147,69,0,216],[30,64,224,226,147,69,0,205],[30,64,224,214,147,69,0,176],[30,64,224,217,147,69,0,180],[30,64,224,240,147,69,0,213],[30,64,224,210,147,69,0,216],[30,64,224,235,147,69,0,192],[30,64,224,234,147,69,0,193],[30,64,224,234,147,69,0,186],[30,64,224,171,147,69,0,136],[30,64,224,103,147,69,0,166],[30,64,224,167,147,69,0,15],[30,64,224,139,147,69,0,182],[30,64,224,194,147,69,0,84],[30,64,224,183,147,69,0,170],[30,64,224,205,147,69,0,125],[30,64,224,138,147,69,0,175],[30,64,224,229,147,69,0,12],[30,64,224,163,147,69,0,26],[30,64,224,105,147,69,0,35],[30,64,224,167,147,69,0,24]];LEN=20
	def calculate(A,params,cookie=A,body=A):
		A.hex_str=R.choice(A.HEX_STRS);hash=A.getGorgonHash(params,body,cookie);C=A.encryption();D=A.__init_hash(hash,C);B='';E=A.__handle(D[H])
		for G in E:B+=A.__hex2str(G)
		I=A.__hex2str(A.hex_str[7]);J=A.__hex2str(A.hex_str[3]);K=A.__hex2str(A.hex_str[1]);L=A.__hex2str(A.hex_str[6]);return{M:'0404{}{}{}{}{}'.format(I,J,K,L,B),N:F(hash[O])}
	def charCodeAt(A,str,i):return A.get_bianma(str[i:1])
	def encryption(H):
		F=C=I=G=J=A;E=[]
		for B in D(256):E.append(B)
		for B in D(256):
			if B==0:C=0
			elif F is not A:C=F
			else:C=E[B-1]
			I=H.hex_str[B%8]
			if(C==85)&(B!=1)&(F!=85):C=0
			G=H.ensureMax(C+B+I);F=G if G<B else A;J=E[G];E[B]=J
		return E
	def ensureMax(B,val,max=256):
		A=val
		while A>=256:A=A-256
		return A
	def epoch(A):return B(K(I.time()))
	def convert_base(A,hex,base):return sum(A.digits[C]*base**B for(B,C)in J(reversed(hex.lower())))
	def fromHex(A,hex):return A.convert_base(hex,B(16))
	def getGorgonHash(C,url,data=A,cookie=A,encoding=P):
		F=encoding;A=[];J=B(K(I.time()));L=C.__to_hex(J);M=G.md5(url.encode(P)).hexdigest();E=C.__ranges(start=4)
		for D in E:A.append(C.fromHex(M[D*2:2*D+2]))
		A=A+C.__xgorgon_data(data,F);A=A+C.__xgorgon_cookie(cookie,F)
		for D in E:A.append(0)
		for D in E:A.append(C.fromHex(L[D*2:2*D+2]))
		return{H:A,O:J}
	def __handle(A,gorgonHash):
		D=gorgonHash;G=A.__ranges(A.LEN)
		for F in G:
			H=D[F];I=A.__reverse(H);J=B(D[(F+1)%A.LEN]);K=I^J;L=A.__rbit(K);M=L^A.LEN;E=~M
			while E<0:E+=4294967296
			N=A.__to_hex(E);O=C(N)-2;P=A.fromHex(A.__to_hex(E)[O:]);D[F]=P
		return D
	def __hex2str(B,num):
		A=B.__to_hex(num)
		if C(A)<2:A=E+A
		return A
	def __init_hash(D,gorgonHash,hexEncryption):
		L=hexEncryption;G=gorgonHash;I=[];J=[]+L;M=N=K=E=O=P=Q=A;R=D.__ranges(D.LEN)
		for F in R:M=G[H][F];N=0 if C(I)==0 else I[-1];K=D.ensureMax(L[F+1]+B(N));I.append(K);E=J[K];J[F+1]=E;O=D.ensureMax(E+E);P=J[O];Q=M^P;G[H][F]=Q
		return G
	def __ranges(H,start=0,stop=A,step=1):
		E=step;C=stop;B=start
		if C is A:C=B;B=0
		if(E>0)&(B>=C)or(E<0)&(B<=C):return[]
		F=[]
		for G in D(B,C,E):F.append(G)
		return F
	def __rbit(F,num):
		D='';A=L(num,'b')
		while C(A)<8:A=E+A
		G=F.__ranges(8)
		for H in G:D+=A[7-H]
		return B(D,2)
	def __reverse(B,num):
		A=B.__to_hex(num)
		if C(A)<2:A=E+A
		return B.fromHex(A[1:10]+A[0:1])
	def __to_hex(A,num):return L(B(num),'x')
	def __xgorgon_cookie(F,cookie,encoding=Q):
		B=cookie;D=[];H=F.__ranges(4)
		if B is A or C(B)==0:
			for E in H:D.append(0)
		else:
			I=G.md5(B.encode()).hexdigest()
			for E in H:D.append(F.fromHex(I[E*2:2*E+2]))
		return D
	def __xgorgon_data(D,data,encoding=Q):
		B=data;E=[];F=A
		if B is A or C(B)==0:
			H=D.__ranges(4)
			for I in H:E.append(0)
		else:
			F=B
			if encoding=='octet':F=G.md5(B.encode()).hexdigest()
			H=D.__ranges(4)
			for I in H:E.append(D.fromHex(F[I*2:2*I+2]))
		return E
