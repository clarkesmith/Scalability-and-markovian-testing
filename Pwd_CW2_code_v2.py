"""Phase 1
"""
import random


def participation_matrix(a):
    blist = []
    for i in range(a):
        blist.append([])
    for i in range(a):
        for j in range(a):
            blist[i].append(0)

    for i in range(a):
        for j in range(a):
            blist[i][j] = round(random.uniform(0, 1), 1)

    for i in range(0, len(blist)):
        for j in range(0, len(blist)):
            if i == j:
                blist[i][j] = 0
    return blist


def make_markovian(blist):
    for i in range(0, len(blist)):
        a = True
        while a:
            total = 0
            for j in range(0, len(blist)):
                total += blist[j][i]
            if total > 1:
                x = random.randint(0, (len(blist)-1))
                if blist[x][i] >= 0:
                    if blist[x][i] > 0.5:
                        blist[x][i] -= 0.1
                    elif blist[x][i] < 0.2:
                        blist[x][i] = 0
                    else:
                        blist[x][i] -= (blist[x][i] / 2)
                    blist[x][i] = round(blist[x][i], 1)
                elif blist[x][i] < 0:
                    blist[x][i] = 0
            elif total < 1:
                x = random.randint(0, (len(blist)-1))
                if blist[x][i] > 0:
                    blist[x][i] += (blist[x][i] / 2)
                    blist[x][i] = round(blist[x][i], 1)
                elif blist[x][i] < 0:
                    blist[x][i] = 0
                else:
                    d = random.uniform(0, 0.1)
                    blist[x][i] = round(d, 1)
            else:
                a = False
    return blist


"""Phase 2
"""


def corp_control(seed, companies):
    direct_control = []
    for i in range(0, len(companies)):
        if companies[seed][i] >= 0.5:
            direct_control.append(i)
    if len(direct_control) == 0:
        print("The Seed company does not directly control any companies")
    else:
        print("Seed company directly controls company number:", end=' ')
        for items in direct_control:
            print(items, end=" ")
        print()

    indirect_control = []
    for j in range(0, len(companies)):
        indirect_index = 0
        indirect_index += companies[seed][j]
        for k in range(0, len(direct_control)):
            co = direct_control[k]
            indirect_index += companies[co][j]
        if indirect_index >= 0.5 and j not in direct_control and j not in indirect_control and j != seed:
            indirect_control.append(j)
    if len(indirect_control) == 0:
        print("The seed company does not indirectly control any companies")
    else:
        print("Seed company indirectly controls company number:", end=' ')
        for items in indirect_control:
            print(items, end=" ")
        print()

    return direct_control, indirect_control


"""
# Manual inputs:
ncompanies = random.randint(2, 10)  # max number of companies
company_ownership = participation_matrix(ncompanies)
print(company_ownership)
print("Make Markovian? Y/N")
markovian = input()
if markovian == "Y" or markovian == "y":
    company_ownership = make_markovian(company_ownership)
    print(company_ownership)
print("which is the seed company?")
s = int(input())
corp_control(s, company_ownership)
"""


"""Phase 3
"""
from matplotlib import pyplot as plt

import time
startTime = time.time()
k = [2,3,4]
k_list = []
for i in range(0, 10):
    k_list.append(random.choice(k))
k_list.sort()
print(k_list)
nm_times = []
nm_times_ave = []

def scalability_testing(n):
    nm_times = []
    s = random.randint(0, n-1)
    startTime = time.time()
    corp_control(s, participation_matrix(n))
    endTime = time.time()
    elapsed = endTime - startTime
    nm_times.append(elapsed)
    n_ave = sum(nm_times) / float(len(nm_times))
    return n_ave

for i in range(0, 10):
    if k_list[i] == 2:
        n = 10**(k_list[i])
        n2_ave = scalability_testing(n)
    if k_list[i] == 3:
        n = 10**(k_list[i])
        n3_ave = scalability_testing(n)
    if k_list[i] == 4:
        n = 10**(k_list[i])
        n4_ave = scalability_testing(n)

nm_times_ave.append(n2_ave)
nm_times_ave.append(n3_ave)
nm_times_ave.append(n4_ave)

print("Non-Markovian times:", nm_times_ave)

x_axis = k
y_axis = nm_times_ave
plt.plot(x_axis, y_axis, color='green', marker='o', linestyle='solid')

plt.title("Non-Markovian phase 3 test")

plt.xlabel('value of k')
plt.ylabel('time (s)')

plt.show()

# For Markovian testing
"""
for i in range(0, 10):
    n = 10**(k_list[i]/2)
    s = random.randint(0, n-1)
    startTime = time.time()
    dc, ic = corp_control(s, make_markovian(participation_matrix(n)))
    endTime = time.time()
    elapsed = endTime - startTime
    m_times.append(elapsed)
print("Markovian times:", m_times)
"""