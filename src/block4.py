import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from scipy.stats import t
def run():
    n, mean, std, sla = 60,95.0,12.0,100.0
    low, high = t.interval(.95,n-1,loc=mean,scale=std/n**.5)
    # Одностороння верхня межа відповідає перевірці μ ≤ SLA.
    upper = mean+t.ppf(.95,n-1)*std/n**.5
    print('Блок 4: 95% ДІ середнього:',low,high)
    print('Верхня одностороння межа:',upper,'SLA для середнього виконано:',upper<=sla)
    return {'low':float(low),'high':float(high),'upper':float(upper),'sla':sla}
if __name__ == '__main__': run()
