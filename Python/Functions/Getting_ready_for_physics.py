print('Celsius Calculator')
def f_to_c(f_temp):
    c_temp= (f_temp-32) * 5/9
    return c_temp

f_100_in_celsius= print(f_to_c(100))
print()
print('Farenheit Calculator')
def c_to_f(c_temp):
    f_temp= c_temp*(9/5) + 32   
    return f_temp

c_0_in_farenheit= print(c_to_f(0))
print()
print("Mass and Acceleration")
def get_force(mass, acceleration):
    train_mass= mass
    train_acceleration= acceleration
    train_force = train_mass*train_acceleration
    return "The GE train supplies "+str(train_force)+" Newtons of force."

print(get_force(22680, 10))
print()
print('Energy')
def get_energy(mass):
    c = 3*10**8
    e= mass*(c*c)   
    bomb_energy = e
    return "A 1kg bomb supplies "+str(bomb_energy)+" Joules."

print(get_energy(1))
print()
print('MAD')
def get_work(mass, acceleration, distance):
    force = mass*acceleration
    work= force*distance
    train_distance= distance
    train_work= work
    return "The GE train does "+str(train_work)+" Joules over "+ str(train_distance)+" meters."

print(get_work(22680, 10, 10))