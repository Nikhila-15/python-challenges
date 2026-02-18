n=int(input('enter number of requests:'))
s=[0]*n
for i in range(n):
    s[i]=int(input())
print(s)
invalid_requests=[]
low_demand=[]
moderate_demand=[]
high_demand=[]
valid_count=0
removed_count=0
for i in range(n):
    if s[i]<0:
        invalid_requests.append(s[i])
    elif s[i]==0:
        pass
        valid_count += 1
    elif s[i]>=1 and s[i]<=20:
        low_demand.append(s[i])
        valid_count += 1
    elif s[i]>=21 and s[i]<50:
        moderate_demand.append(s[i])
        valid_count += 1
    else:
        high_demand.append(s[i])
        valid_count += 1
print("Before personalisation:")
print('invalid requests=',invalid_requests)
print('low demand=',low_demand)
print('moderate demand=',moderate_demand)
print('high demand=',high_demand)

name=input('enter your name:')
L=len(name.replace(" ",""))
print('Length of name:',L)
PLI=L%3
if PLI == 0:
    removed_count = len(low_demand)
    low_demand = []
elif PLI == 1:
    removed_count= len(high_demand)
    high_demand = []
elif PLI == 2:
    removed_count= len(high_demand)+len(low_demand)
    low_demand = []
    high_demand = []
else:
    print('invalid input')

print("After personalisation:")
print('invalid requests=',invalid_requests)
print('low demand=',low_demand)
print('moderate demand=',moderate_demand)
print('high demand=',high_demand)
print('valid requests=',valid_count)
print('removed count due to PLI=',removed_count)


