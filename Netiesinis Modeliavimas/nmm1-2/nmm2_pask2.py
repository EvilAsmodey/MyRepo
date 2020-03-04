import cmath
import random
import sys
import time

#----------------------globals-------------------------------------

I = complex(0, 1)
c = 1
d = 1
g = 1
a = 1
N = 10
h = 1/N
Tau = 1/N
delta = 1e-5
kappa = 1
gamma = 0
T = 0.5

t1 = 1
t2 = 0
t3 = 0
t4 = 0
debug = 0

#---------------------entry--------------------------------------

def entry_point():
	global debug
	global t1
	global t2
	global t3
	global t4

	if len(sys.argv) > 1:
		t1 = num(sys.argv[1])
	if len(sys.argv) > 2:
		t2 = num(sys.argv[2])
	if len(sys.argv) > 3:
		t3 = num(sys.argv[3])
	if len(sys.argv) > 4:
		t4 = num(sys.argv[4])
	if len(sys.argv) > 5:
		debug = num(sys.argv[5])

	if debug == 1:
		print_sep('...CMD arguments list start')
		print(sys.argv)
		print_sep('...CMD arguments list end')

	x = 0.39
	t = 1.17
	_round = 8
	_range = 6

	print_sep('Start...')

	if t1 == 1:
		print_sep('Test 1...Start...')
		startTime = time.time()
		test_1(Tau, x, t, c, d, _round, _range)
		endTime = time.time() - startTime
		print("Test 1 execution time: ", str(round(endTime * 1000)), " (ms)")
		print_sep('Test1...End...')
	if t2 == 1:
		print_sep('Test2...Start...')
		startTime = time.time()
		test_2(Tau, x, t, c, d, _round, _range)
		endTime = time.time() - startTime
		print("Test #2 execution time: ", str(round(endTime * 1000)), " (ms)")
		print_sep('Test2...End...')
	if t3 == 1:
		print_sep('Test3...Start...')
		startTime = time.time()
		test_3(_round)
		endTime = time.time() - startTime
		print("Test3 execution time: ", str(round(endTime * 1000)), " (ms)")
		print_sep('Test3...End...')
	if t4 == 1:
		print_sep('Test4...Start...')
		startTime = time.time()
		test_4(_round)
		endTime = time.time() - startTime
		print(endTime)
		str_p = " (ms)"
		if endTime < 1:
			endTime = round(endTime * 1000, 6)
			str_p = " (ms)"
		else:
			endTime = round(endTime, 4)
			str_p = " (s)"

		print("Test4 execution time: ", str(endTime), str_p)
		print_sep('Test4...End...')
	return 0

#-------------------------functions----------------------------------

def u_tikslus(x, t):
	return (t - 1) * (cmath.sin(2 * cmath.pi * x))

def f(x,t):
	return  cmath.sin(2*cmath.pi*x) - (a**2 + I) * (-4*cmath.pi**2*(t - I) * cmath.sin(2 * cmath.pi * x)) - I * g * cmath.log(1 + (t**2 + 1) * cmath.sin(2 * cmath.pi * x));

def f_prime(h, tau, uJ, uStogasJ, fStogasJ, fJ):
	p1 = 2* (cmath.pi) * x * cmath.sin
	p2 = 2* (cmath.pi) * x * cmath.sin - (t - i)
	p3 = 0
	#p4 = (uStogasJ + uJ) * pow(h, 2)
	#p5 = (fStogasJ + fJ) * I * pow(h, 2)

	res = p1 + p2 + (p3 * p4) - p5

	return res

#-------------------------tests----------------------------------

def test_1(Tau,x,t,c,d,_round,_range):
	print("1st TEST. Parameters c = ",c," d = ",d," Point coord x = ",x," Time value t = ",t,"\n")
	n_list = []

	n_list.append(run_test1(x, t, h, Tau))
	print("Algorithm discretization steps h = ", _fround(h, _round), " Tau = ", _fround(Tau, _round), " gaunama netikties reikšmė: ", round(n_list[0], 50), "\n")
	h_curr = h
	tau_curr = Tau
	for j in range(1, _range + 1): 
		h_curr = 0.1 * h_curr
		tau_curr = 0.1 * tau_curr
		n_list.append(run_test1(x, t, h_curr, tau_curr))
		print("If alg discretization steps [h] = ",_fround(h_curr, _round)," ir [Tau] = ",_fround(tau_curr, _round),", gaunama netikties reikšmė: " , round(n_list[j], 50) , ". Netiktis sumažėjo ", _fround((n_list[j - 1]/n_list[j]), _round), " kartų. \n")

	return 0

def run_test1(x, t, h, tau):
	uJ = u_tikslus(x, t)
	uStogasJ = u_tikslus(x, t + tau)
	fJ = f(x, t)
	fStogasJ = f(x, t + tau)
	utAproksimacija = (uStogasJ - uJ) / tau
	uxxAproksimacija = 0.5*(a**2 + I)
	netiesinioNarioAproksimacija = I*g*(cmath.log(1 + abs((uStogasJ + uJ) / 2)))
	fAproksimacija = 0.5*(fJ + fStogasJ)
	netiktis = abs(utAproksimacija - fAproksimacija - netiesinioNarioAproksimacija - I * uxxAproksimacija)
	return netiktis
#---------------------------------------------------------------------------------------------
def test_2(Tau,x,t,c,d,_round,_range):
	print("2-as TEST. Parametres c = ",_fround(c, _round)," d = ",_fround(d, _round)," Taško koordinatė x = ",_fround(x, _round)," Laiko momento reikšmė t = ",_fround(t, _round),"\n")
	n_list = []

	n_list.append(run_test2(x, t, h, Tau))
	print("If algorithm discret steps h = ", _fround(h, _round), " Tau = ", _fround(Tau, _round), " gaunama netikties reikšmė: ", round(n_list[0], 50), "\n")

	h_curr = h
	tau_curr = Tau

	for j in range(1, _range + 1): 
		h_curr /= 10
		tau_curr /= 10
		n_list.append(run_test2(x, t, h_curr, tau_curr))

		print("Algorithm discretization steps [h] = ",_fround(h_curr, _round)," ir [Tau] = ",_fround(tau_curr, _round),", gaunama netikties reikšmė: " , round(n_list[j], 50) , ". Netiktis sumažėjo " , _fround((n_list[j - 1]/n_list[j]), _round) , " kartų. \n")
	return 0

def run_test2(x, t, h, tau):
	uJ = u_tikslus(x, t)

	uStogasJ = u_tikslus(x, t + tau)
	fJ = f(x, t)
	fStogasJ = f(x, t + tau)
	#constC = 2 - I*((2*(h**2))/tau) - c*(h**2)
	
	fnRes = f_prime(h, tau, uJ, uStogasJ, fStogasJ, fJ)
	
	netiktis = abs(uStogasJPliusVienas - (constC*uStogasJ) + uStogasJMinusVienas + fnRes)
	return netiktis

def test_3(_round):
	f3_list = [complex(0, 0)] * (N+1)
	u_list_rand = [complex(0, 0)] * (N+1)
	
	constC = 2 - I*((2*(h**2))/Tau) - c*(h**2)

	for j in range(1,N):
		u_list_rand[j] = random.randrange(0,10) + I * random.randrange(-10,10)
	
	u_list_rand[0] = u_list_rand[1] # - * 1 (kappa)
	u_list_rand[N] = u_list_rand[N-1]

	for j in range(1,N):
		f3_list[j] = constC * u_list_rand[j] - u_list_rand[j-1] - u_list_rand[j+1]

	tRes = Thomas_alg(f3_list, constC)

	testRes = ret_max(u_list_rand, tRes)

	print("3 TEST. Parameters h = {0}, Tau = {1}".format(round(h, _round), round(Tau, _round)))
	print("Netiktis=",round(testRes, 50), " [",_fround(testRes, 20),"]", "\n")

	return 0

def Thomas_alg(f, constC, n = N):
	alpha = [complex(0, 0)] * (n+1)
	beta = [complex(0, 0)] * (n+1)
	alpha[1] = kappa
	beta[1] = gamma

	res = [complex(0, 0)] * (n+1)

	for j in range(2,n+1):
		alpha[j] = 1 / (constC - alpha[j-1])
		beta[j] = (beta[j-1]+f[j-1]) * alpha[j]

	res[n] = (kappa*beta[n]) / (1-kappa*alpha[n])

	for j in reversed(range(n)):
		res[j] = alpha[j+1] * res[j+1] + beta[j+1]

	return res

def test_4(_round):
	print("Global test \n")
	print("Parameters d = {0}, c = {1}\n".format(d, c))
	h_curr = h
	n_curr = N
	tau_curr = Tau

	res = []
	for j in range(3):
		constC = 2 - I*((2*(h_curr**2))/tau_curr) - c*(h_curr**2)

		res.append(run_test_4_2(h_curr, n_curr, tau_curr, constC))
		#res.append(run_test4(h_curr, n_curr, tau_curr, constC))
		
		lw = '-'
		if j != 0:
			lw = _fround(res[j-1]/res[j], _round)
		print("h = {0}, Tau = {1}, netikties reikšmė = {2}, netiktis sumažėjo {3} kartų".format(h_curr, tau_curr, res[j], lw))
		
		h_curr /= 10
		n_curr *= 10
		tau_curr /= 10
	paklaida_max = max(res)
	print("Viso algoritmo paklaida (didziausia) = {0}".format(paklaida_max))
	return 0

def run_test_4_2(h_curr, n_curr, tau_curr, constC):
	t = 0.0

	n_list = []

	u = []
	
	for j in range(0,n_curr+1):
		x = j*h_curr
		u.append(u_tikslus(x,t))

	while t < T:
		paklaida = 1
		uStogai = u[:]

		while paklaida > delta:
			u_next = []
			for j in range(1,n_curr):
				x = j * h_curr
				fStogas = f(j*h_curr, t + tau_curr)
				fJ = f(j*h_curr, t)
				u_next.append(f_prime(h_curr, tau_curr, u[j], u[j+1], u[j-1], uStogai[j], fStogas, fJ))
			uStogasNew = Thomas_alg(u_next, constC, n_curr)
			paklaida = ret_max(uStogai,uStogasNew)
			uStogai = uStogasNew
		t = t + tau_curr
		u_t = []
		for j in range(0,n_curr+1):
			u_t.append(u_tikslus(x,t))
		pakl2 = ret_max(u_t, uStogasNew)
		n_list.append(pakl2)

		paklMax = -1

		for j in range(0, len(n_list) - 1):
			if abs(n_list[j]) > paklMax:
				paklMax = n_list[j];

	return paklMax

def run_test4(h_curr, n, tau, constC):
	t = 0.0
	u = [complex(0, 0)] * (n+1)
	uStogai = [complex(0, 0)] * (n+1)
	n_list = []

	for j in range(0,n+1):
		u[j] = u_tikslus(j*h_curr,t)
	
	while t <= T:
		u_next = get_u_next(h_curr, tau, t, u, n, constC)
		t += tau

		for j in range(0,n+1):
			uStogai[j] = u_tikslus(j*h_curr,t)

		netiktis = ret_max(u_next,uStogai)
		n_list.append(netiktis)
		u = u_next[:]

	return max([abs(j) for j in n_list])

def get_u_next(h_curr, tau, t, u, n, constC):
	f_prime_list = [complex(0, 0)] * (n+1)
	uStogas_old = u[:]

	stop = False

	while stop == False:
		for j in range(1,n):
			# f_prime(h_curr, tau, uJ, uJPliusVienas, uJMinusVienas, uStogasJ, fStogasJ, fJ)
			# uStogasJ = u_tikslus(h_curr*j, t + tau)
			f_prime_list[j] = f_prime(h_curr, tau, u[j], u[j+1], u[j-1], uStogas_old[j], f(j*h_curr, t + tau), f(j*h_curr, t))
			# f_prime_list[j] = f_prime(h_curr, tau, u[j], u[j + 1], u[j - 1], u_tikslus(h_curr*j, t + tau), f(j * h_curr, t + tau), f(j * h_curr, t))

		uStogas_new = Thomas_alg(f_prime_list, constC, n)

		if ret_max(uStogas_new,uStogas_old) < delta:
			stop = True
		else:
			uStogas_old = uStogas_new[:]

	return uStogas_new
#----------------------helper functions-------------------------------------

def _fround(value, _round):
	return format(value, '.'+str(_round)+'f')

def print_sep(val):
	print('-------------------------------------------------------------------------------------------------------------------------------------------')
	print(val)
	print('-------------------------------------------------------------------------------------------------------------------------------------------\n')
	return None

def ret_max(u_tikslus, u_thomas):
	return max([abs(u_tikslus[j] - u_thomas[j]) for j in range(0, len(u_tikslus))])

def num(s):
	try:
		return int(s)
	except ValueError:
		return float(s)

#----------------------start script-------------------------------------

entry_point()