import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

from parser import getGDPandPopulationData

country_data = getGDPandPopulationData()

country_names = []
country_gdps = []
country_populations = []
country_gdp_per_caps = []

largest_gdp_per_cap = 0
for i in range(0, len(country_data)):
    country_data[i][2] = country_data[i][2] / 1000000

    country_names.append(country_data[i][0])
    country_gdps.append(country_data[i][1])
    country_populations.append(country_data[i][2])
    country_gdp_per_caps.append(country_data[i][3])

    if largest_gdp_per_cap < country_gdp_per_caps[i]:
        largest_gdp_per_cap = country_gdp_per_caps[i]

colors = np.asarray(country_gdp_per_caps)
area = np.pi * (50.0 * np.asarray(country_gdp_per_caps) / largest_gdp_per_cap)**2

plt.ion()
fig, ax = plt.subplots()
plt.scatter(country_populations, country_gdps, s=area, c=colors, alpha=0.5)

for i, txt in enumerate(country_names):
    plt.annotate(txt, (country_populations[i], country_gdps[i]))

z = np.polyfit(country_populations, country_gdps, 1)
p = np.poly1d(z)
plt.plot(country_populations, p(country_populations), "r--")

slope, intercept, r_value, p_value, std_err = stats.linregress(country_populations,country_gdps)
rsq = r_value**2

textstr = '$r^2=%.2f$'%(rsq)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.xlabel('Country Population (Millions)')
plt.ylabel('Country GDP (PPP)')
plt.title('Country GDP (PPP) vs Country Population')
plt.show()

country_names = []
country_gdps = []
country_populations = []
country_gdp_per_caps = []

largest_gdp_per_cap = 0
new_set_index = -1
population_cap = 300

for i in range(0, len(country_data)):
    if country_data[i][2] > population_cap:
        continue

    country_names.append(country_data[i][0])
    country_gdps.append(country_data[i][1])
    country_populations.append(country_data[i][2])
    country_gdp_per_caps.append(country_data[i][3])

    new_set_index = new_set_index + 1

    if largest_gdp_per_cap < country_gdp_per_caps[new_set_index]:
        largest_gdp_per_cap = country_gdp_per_caps[new_set_index]

colors = np.asarray(country_gdp_per_caps)
area = np.pi * (50.0 * np.asarray(country_gdp_per_caps) / largest_gdp_per_cap)**2

fig, ax = plt.subplots()
plt.scatter(country_populations, country_gdps, s=area, c=colors, alpha=0.5)

for i, txt in enumerate(country_names):
    plt.annotate(txt, (country_populations[i], country_gdps[i]))

z = np.polyfit(country_populations, country_gdps, 1)
p = np.poly1d(z)
plt.plot(country_populations, p(country_populations), "r--")

slope, intercept, r_value, p_value, std_err = stats.linregress(country_populations,country_gdps)
rsq = r_value**2

textstr = '$r^2=%.2f$'%(rsq)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.xlabel('Country Population (Millions)')
plt.ylabel('Country GDP (PPP)')
plt.title('Country GDP (PPP) vs Country Population (Population Cap: ' + str(population_cap) + ' Million)')
plt.show()

country_names = []
country_gdps = []
country_populations = []
country_gdp_per_caps = []

largest_gdp_per_cap = 0
new_set_index = -1
population_cap = 150

for i in range(0, len(country_data)):
    if country_data[i][2] > population_cap:
        continue

    country_names.append(country_data[i][0])
    country_gdps.append(country_data[i][1])
    country_populations.append(country_data[i][2])
    country_gdp_per_caps.append(country_data[i][3])

    new_set_index = new_set_index + 1

    if largest_gdp_per_cap < country_gdp_per_caps[new_set_index]:
        largest_gdp_per_cap = country_gdp_per_caps[new_set_index]

colors = np.asarray(country_gdp_per_caps)
area = np.pi * (50.0 * np.asarray(country_gdp_per_caps) / largest_gdp_per_cap)**2

fig, ax = plt.subplots()
plt.scatter(country_populations, country_gdps, s=area, c=colors, alpha=0.5)

for i, txt in enumerate(country_names):
    plt.annotate(txt, (country_populations[i], country_gdps[i]))

z = np.polyfit(country_populations, country_gdps, 1)
p = np.poly1d(z)
plt.plot(country_populations, p(country_populations), "r--")

slope, intercept, r_value, p_value, std_err = stats.linregress(country_populations,country_gdps)
rsq = r_value**2

textstr = '$r^2=%.2f$'%(rsq)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.xlabel('Country Population (Millions)')
plt.ylabel('Country GDP (PPP)')
plt.title('Country GDP (PPP) vs Country Population (Population Cap: ' + str(population_cap) + ' Million)')
plt.show()

country_names = []
country_gdps = []
country_populations = []
country_gdp_per_caps = []

largest_gdp_per_cap = 0
new_set_index = -1
population_cap = 1

for i in range(0, len(country_data)):
    if country_data[i][2] > population_cap:
        continue

    country_names.append(country_data[i][0])
    country_gdps.append(country_data[i][1])
    country_populations.append(country_data[i][2])
    country_gdp_per_caps.append(country_data[i][3])

    new_set_index = new_set_index + 1

    if largest_gdp_per_cap < country_gdp_per_caps[new_set_index]:
        largest_gdp_per_cap = country_gdp_per_caps[new_set_index]

colors = np.asarray(country_gdp_per_caps)
area = np.pi * (50.0 * np.asarray(country_gdp_per_caps) / largest_gdp_per_cap)**2

fig, ax = plt.subplots()
plt.scatter(country_populations, country_gdps, s=area, c=colors, alpha=0.5)

for i, txt in enumerate(country_names):
    plt.annotate(txt, (country_populations[i], country_gdps[i]))

z = np.polyfit(country_populations, country_gdps, 1)
p = np.poly1d(z)
plt.plot(country_populations, p(country_populations), "r--")

slope, intercept, r_value, p_value, std_err = stats.linregress(country_populations,country_gdps)
rsq = r_value**2

textstr = '$r^2=%.2f$'%(rsq)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.xlabel('Country Population (Millions)')
plt.ylabel('Country GDP (PPP)')
plt.title('Country GDP (PPP) vs Country Population (Population Cap: ' + str(population_cap) + ' Million)')
plt.show()

country_names = []
country_gdps = []
country_populations = []
country_gdp_per_caps = []

largest_gdp_per_cap = 0
new_set_index = -1
population_cap = 0.2

for i in range(0, len(country_data)):
    if country_data[i][2] > population_cap:
        continue

    country_names.append(country_data[i][0])
    country_gdps.append(country_data[i][1])
    country_populations.append(country_data[i][2])
    country_gdp_per_caps.append(country_data[i][3])

    new_set_index = new_set_index + 1

    if largest_gdp_per_cap < country_gdp_per_caps[new_set_index]:
        largest_gdp_per_cap = country_gdp_per_caps[new_set_index]

colors = np.asarray(country_gdp_per_caps)
area = np.pi * (50.0 * np.asarray(country_gdp_per_caps) / largest_gdp_per_cap)**2

fig, ax = plt.subplots()
plt.scatter(country_populations, country_gdps, s=area, c=colors, alpha=0.5)

for i, txt in enumerate(country_names):
    plt.annotate(txt, (country_populations[i], country_gdps[i]))

z = np.polyfit(country_populations, country_gdps, 1)
p = np.poly1d(z)
plt.plot(country_populations, p(country_populations), "r--")

slope, intercept, r_value, p_value, std_err = stats.linregress(country_populations,country_gdps)
rsq = r_value**2

textstr = '$r^2=%.2f$'%(rsq)
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

plt.xlabel('Country Population (Millions)')
plt.ylabel('Country GDP (PPP)')
plt.title('Country GDP (PPP) vs Country Population (Population Cap: ' + str(population_cap) + ' Million)')
plt.show()

input('Press enter when done')
