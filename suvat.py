import math
from rounding import round_up

suvat_table = {
    's': None,
    'u': None,
    'v': None,
    'a': None,
    't': None
}



print('SUVAT SOLVER')
print('For unknown value, leave blank')
for variable in suvat_table.keys():
    inp = input(f'[{variable.capitalize()}] > ')
    try:
        suvat_table[variable] = float(inp)
    except (ValueError, TypeError):  # Catch invalid conversions
        suvat_table[variable] = None


s = suvat_table['s']
u = suvat_table['u']
v = suvat_table['v']
a = suvat_table['a']
t = suvat_table['t']

# FINAL VELOCITY

# v = u + at
if v == None and (None not in [u, a, t]):
    suvat_table['v'] = suvat_table['u'] + (suvat_table['a'] * suvat_table['t'])

# v = (2s / t) - u
if t != 0:
    if v == None and (None not in [s, t, u]):
        suvat_table['v'] = (2 * suvat_table['s'] / suvat_table['t']) - suvat_table['u']

# v = sqrt(u^2 + 2as)
if v == None and (None not in [u, a, s]):
    suvat_table['v'] = (suvat_table['u']**2 + 2 * suvat_table['a'] * suvat_table['s'])**0.5


# INITIAL VELOCITY

# u = v - at
if u == None and (None not in [v, a, t]):
    suvat_table['u'] = suvat_table['v'] - (suvat_table['a'] * suvat_table['t'])

# u = (2s / t) - v
if t != 0:
    if u == None and (None not in [s, t, v]):
        suvat_table['u'] = (2 * suvat_table['s'] / suvat_table['t']) - suvat_table['v']

# u = sqrt(v^2 - 2as)
if u == None and (None not in [v, a, s]):
    suvat_table['u'] = (suvat_table['v']**2 - 2 * suvat_table['a'] * suvat_table['s'])**0.5


# DISPLACEMENT

# s = ut + 0.5at^2
if s == None and (None not in [u, a, t]):
    suvat_table['s'] = (suvat_table['u'] * suvat_table['t']) + (0.5 * suvat_table['a'] * suvat_table['t']**2)

# s = ((u + v) / 2) * t
if t != 0:
    if s == None and (None not in [u, v, t]):
        suvat_table['s'] = ((suvat_table['u'] + suvat_table['v']) / 2) * suvat_table['t']

# s = vt - 0.5at^2
if s == None and (None not in [v, a, t]):
    suvat_table['s'] = (suvat_table['v'] * suvat_table['t']) - (0.5 * suvat_table['a'] * suvat_table['t']**2)

# s = (v^2 - u^2) / (2a)
if a != 0:
    if s == None and (None not in [v, u, a]):
        suvat_table['s'] = (suvat_table['v']**2 - suvat_table['u']**2) / (2 * suvat_table['a'])


# ACCELERATION

# a = (v - u) / t
if t != 0:
    if a == None and (None not in [v, u, t]):
        suvat_table['a'] = (suvat_table['v'] - suvat_table['u']) / suvat_table['t']

# a = (2(s - ut)) / t^2
if t != 0:
    if a == None and (None not in [s, u, t]):
        suvat_table['a'] = (2 * (suvat_table['s'] - (suvat_table['u'] * suvat_table['t']))) / (suvat_table['t']**2)

# a = (v^2 - u^2) / (2s)
if s != 0:
    if a == None and (None not in [v, u, s]):
        suvat_table['a'] = (suvat_table['v']**2 - suvat_table['u']**2) / (2 * suvat_table['s'])


# TIME

# t = (v - u) / a
if a != 0:
    if t == None and (None not in [v, u, a]):
        suvat_table['t'] = (suvat_table['v'] - suvat_table['u']) / suvat_table['a']

# t = (-u + sqrt(u^2 + 2as)) / a
if a != 0:
    if t == None and (None not in [u, a, s]):
        suvat_table['t'] = (-suvat_table['u'] + (suvat_table['u']**2 + 2 * suvat_table['a'] * suvat_table['s'])**0.5) / suvat_table['a']

# t = (2s) / (u + v)
try:
    if u+v != 0:
        if t == None and (None not in [s, u, v]):
            suvat_table['t'] = (2 * suvat_table['s']) / (suvat_table['u'] + suvat_table['v'])
except:
    pass
print('\nResults')
print(f"[m]\tDisplacement:\t\t{round_up(suvat_table['s'], 3)}")
print(f"[ms^-1]\tInitial Velocity:\t{round_up(suvat_table['u'], 3)}")
print(f"[ms^-1]\tFinal Velocity:\t\t{round_up(suvat_table['v'], 3)}")
print(f"[ms^-2]\tAcceleration:\t\t{round_up(suvat_table['a'], 3)}")
print(f"[s]\tTime:\t\t\t{round_up(suvat_table['t'], 3)}")