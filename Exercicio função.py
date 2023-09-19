def fatorial(num):
	for i in range(num - 1, 0, -1):
		num *= i
	return num

def calc_combinacao(n, m):
	combinacoes = fatorial(n)/(fatorial(m) * fatorial(n - m))
	return combinacoes

n, m = map(int, input().split())
combinacao = calc_combinacao(n, m)
print(combinacao)
