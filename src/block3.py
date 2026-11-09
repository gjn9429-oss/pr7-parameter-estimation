import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import math
import numpy as np
from scipy.stats import norm
from statsmodels.stats.proportion import proportion_confint
from block1 import save
import matplotlib.pyplot as plt
def run():
    n, m = 500, 35
    p = m/n
    z = norm.ppf(0.975)
    error = z*math.sqrt(p*(1-p)/n)
    wald = [p-error,p+error]
    wilson = list(proportion_confint(m,n,alpha=0.05,method='wilson'))
    required = math.ceil(z*z*p*(1-p)/0.01**2)
    sizes = np.arange(50,5001)
    widths = 2*z*np.sqrt(p*(1-p)/sizes)
    fig,ax = plt.subplots(figsize=(8,3.7))
    ax.plot(sizes,widths)
    ax.axhline(.02,linestyle='--',color='tab:red',label='Ширина 0,02')
    ax.axvline(required,linestyle=':',label=f'n = {required}')
    ax.set(xlabel='Обсяг n',ylabel='Ширина інтервалу Волда',title='Частка помилок p̂ = 0,07; γ = 0,95')
    ax.legend();ax.grid(alpha=.25)
    save(fig,'block3_interval_width.png')
    print('Блок 3: p̂, Волд, Вілсон, мінімальний n:',p,wald,wilson,required)
    return {'p':p,'wald':wald,'wilson':[float(x) for x in wilson],'required':required}
if __name__ == '__main__': run()
