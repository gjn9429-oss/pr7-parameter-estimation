import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
import numpy as np
from scipy import stats
def run():
    rng = np.random.default_rng(43)
    sample = rng.normal(142.5,18.2,50)
    n = len(sample)
    mean = float(np.mean(sample))
    variance = float(np.var(sample,ddof=1))
    std = variance**0.5
    rows = []
    for confidence in [0.95,0.99]:
        alpha = 1-confidence
        low, high = stats.t.interval(confidence,n-1,loc=mean,scale=std/n**0.5)
        variance_low = (n-1)*variance/stats.chi2.ppf(1-alpha/2,n-1)
        variance_high = (n-1)*variance/stats.chi2.ppf(alpha/2,n-1)
        rows.append([confidence,float(low),float(high),float(variance_low),float(variance_high),float(variance_low**0.5),float(variance_high**0.5)])
    print('Блок 2: середнє, S², S:',mean,variance,std)
    for row in rows: print(row)
    return {'mean':mean,'variance':variance,'std':std,'rows':rows}
if __name__ == '__main__': run()
