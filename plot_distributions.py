#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 20 17:36:59 2018

@author: armandkapllani
"""

import os 
os.getcwd()  
import numpy as np
from scipy.special import factorial
from scipy.special import gamma
import matplotlib.pyplot as plt

#----------------------#
# Poisson distribution #
#----------------------#

# Use the lambda operator to create a small anonymous function. 
poisson_pmf = lambda mu, x: np.exp(-mu) * mu**x / factorial(x)
x = range(0,20)

fig, ax = plt.subplots(figsize=(8, 6))

mu_list = [1,2,3,4,5]
for mu in mu_list:
    dist = []
    for x_i in x:
        dist.append(poisson_pmf(mu, x_i))
    ax.plot(x,
            dist,
            label=f'$\mu$={mu}',
            alpha=0.5,
            marker='o',
            markersize=8)
        
ax.grid()
ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$f(x \mid \mu)$', fontsize=16)
ax.axis(xmin = 0, ymin = 0)
ax.legend(fontsize = 16)

plt.show()

#----------------------#
# Pareto distribution  #
#----------------------#

pareto_pmf = lambda alpha, x_m, x: alpha * x_m**alpha / x**(alpha+1)

fig, ax = plt.subplots(figsize=(8, 6))

x = range(1,6)
x_m = 1
list_alpha = [1, 2, 3, 4]

for alpha in  list_alpha:
    dist = []
    for x_i in x:
        dist.append(pareto_pmf(alpha, x_m, x_i))
    ax.plot(x,
            dist,
            label=f'$\\alpha$={alpha}',
            marker='o',
            markersize=8)
        
ax.grid()
ax.set_xlabel('$x$ and $x_m = 1$', fontsize=14)
ax.set_ylabel('$P(X=x)$', fontsize=16)
ax.axis(xmin = 0, ymin = 0)

plt.show()

#---------------------#
# Normal Distribution #
#---------------------#

normal_pdf = lambda mu, sigma, x: 1/(np.sqrt(2*np.pi) * sigma) * np.exp((-1/2)*(((x-mu)/sigma)**2))

fig, ax = plt.subplots(figsize=(8,6))
x = np.linspace(-5,5)

list_mu = [0]
list_sigma = [0.2,1,3]

for mu in list_mu:
    for sigma in list_sigma:
        dist = []
        for x_i in x:
            dist.append(normal_pdf(mu,sigma, x_i))
        ax.plot(x,
        dist,
        label=f'$\simga$={sigma}, $\mu={mu}$',
        alpha=0.5,
        marker='o',
        markersize=8)

ax.grid()
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('$\phi_{\mu, \sigma^2}(x)$', fontsize=16)
ax.axis(xmin = -5, ymin = 0)

plt.show()

#--------------------------#
# Chi-squared distribution #
#--------------------------#

chi_squared = lambda k, x: 1/(np.power(2,(k/2))*gamma(k/2)) * np.power(x,(k/2-1))*np.exp(-x/2)

fig, ax = plt.subplots(figsize=(8,6))
x = np.linspace(0,8)

list_k = [1,2,3,4,6,9]

for k in list_k:
    dist=[]
    for x_i in x:
        dist.append(chi_squared(k,x_i))
    ax.plot(x,
        dist,
        label=f'$\alpha={alpha}',
        marker='o',
        markersize=4)

ax.grid()
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('$\chi^2(k)$', fontsize=16)
ax.axis(xmin = 0, ymin = 0)

plt.show()      


#-----------------------------#
# Weibull distribution pdf    #
#-----------------------------#

weibull = lambda k, mu, x: (k/mu) * (x/mu)**(k-1) * np.exp((-x/mu)**k)

fig, ax = plt.subplots(figsize=(8,6))
x = np.arange(0, 2.5, 0.05)

list_mu = [1]
list_k = [0.5,1,1.5,5]

for k in list_k:
    for mu in list_mu:
        dist=[]
        for x_i in x:
            dist.append(weibull(k,mu,x_i))
    ax.plot(x,
        dist,
        label=f'$\mu$={mu}',
        markersize=4)

ax.grid()
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('Weibull pdf', fontsize=16)
ax.axis(xmin = 0, ymin = 0)

plt.show()      
        

#-----------------------------#
# Weibull distribution cdf    #
#-----------------------------#

weibull_cdf = lambda k, mu, x: 1 - np.exp((-x/mu)**k)

fig, ax = plt.subplots(figsize=(8,6))
x = np.arange(0, 2.5, 0.05)

list_mu = [1]
list_k = [0.5,1,1.5,5]

for mu in list_mu:
    for k in list_k:
        dist=[]
        for x_i in x:
            dist.append(weibull_cdf(k,mu,x_i))
    ax.plot(x,
        dist,
        label=f'$\\alpha$={alpha}$, $\mu = {mu}$',
        marker='o',
        markersize=4)

ax.grid()
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('Weibull cdf', fontsize=16)
ax.axis(xmin = 0, ymin = 0)

plt.show()      
   
#-----------------------------#
# Beta distribution           #
#-----------------------------#

beta_pdf = lambda alpha, beta, x: x**(alpha-1)*(1-x)**(beta-1)*gamma(alpha+beta)/(gamma(alpha)*gamma(beta))

fig, ax = plt.subplots(figsize=(8,6))
x = np.linspace(0,1)

list_alpha = [0.5, 5, 1, 2]
list_beta = [0.5, 1, 3, 2]

for alpha, beta in zip(list_alpha, list_beta):
    dist = []
    for x_i in x:
        dist.append(beta_pdf(alpha,beta,x_i))
    ax.plot(x,
            dist,
            label=f'$\\alpha={alpha}$, $\\beta={beta}$',
            marker = 'o',
            markersize=4)

ax.grid()
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('$Beta$', fontsize=16)
ax.axis(xmin = 0, ymin = 0)
ax.legend(fontsize = 16)

plt.show()  












