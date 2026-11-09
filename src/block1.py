import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
GRAPHICS = Path(__file__).resolve().parent.parent / 'graphics'
def save(fig, name):
    GRAPHICS.mkdir(exist_ok=True)
    fig.tight_layout()
    fig.savefig(GRAPHICS / name, dpi=180)
    plt.close(fig)
def run():
    rng = np.random.default_rng(42)
    rate = 0.04
    sizes = [5,10,20,50,100,500,1000,5000,10000]
    rows = []
    # Для кожного n генеруємо 1000 окремих незалежних вибірок.
    for n in sizes:
        estimates = []
        for repeat in range(1000):
            sample = rng.exponential(1 / rate, n)
            estimates.append(1 / np.mean(sample))
        estimates = np.array(estimates)
        bias = np.mean(estimates) - rate
        mse = np.mean((estimates - rate)**2)
        rows.append([n, float(np.mean(estimates)), float(bias), float(mse)])
    print('Блок 1: n, середня оцінка, Bias, MSE')
    for row in rows: print(row)
    fig, axes = plt.subplots(1,2,figsize=(9,3.6))
    for ax, column, label in zip(axes,[2,3],['Bias','MSE']):
        ax.plot(sizes,[r[column] for r in rows],'o-',label='Експеримент')
        if column == 2: theory = [rate/(n-1) for n in sizes]
        else: theory = [rate**2*(n+2)/((n-1)*(n-2)) for n in sizes]
        ax.plot(sizes,theory,'--',label='Теорія')
        ax.set(xscale='log',xlabel='Обсяг n',ylabel=label)
        ax.grid(alpha=.25)
        ax.legend()
    save(fig,'block1_bias_mse.png')
    return rows
if __name__ == '__main__': run()
