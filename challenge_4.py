n = int(input('enter number of scores: '))
scores = [0] * n
for i in range(n):
    scores[i] = int(input())
print(scores)
low_count = 0
medium_count = 0
high_count = 0
critical_count = 0
valid_count = 0
invalid_count = 0
for i in range(n):
    if scores[i] < 0:
        invalid_count =invalid_count+ 1
    elif scores[i] <= 30:
        low_count =low_count+1
        valid_count =valid_count+1
    elif scores[i] <= 60:
        medium_count =medium_count+ 1
        valid_count = valid_count+1
    elif scores[i] <= 100:
        high_count =high_count+ 1
        valid_count =valid_count+ 1
    else:
        critical_count += 1
        valid_count += 1
low_risk = [0] * low_count
medium_risk = [0] * medium_count
high_risk = [0] * high_count
critical_risk = [0] * critical_count
l = m = h = c = 0
for i in range(n):
    if scores[i] < 0:
        pass
    elif scores[i] <= 30:
        low_risk[l] = scores[i]
        l =l+ 1
    elif scores[i] <= 60:
        medium_risk[m] = scores[i]
        m =m+ 1
    elif scores[i] <= 100:
        high_risk[h] = scores[i]
        h =h+ 1
    else:
        critical_risk[c] = scores[i]
        c =c+ 1
print('Low risk =', low_risk)
print('Medium risk =', medium_risk)
print('High risk =', high_risk)
print('Critical risk =', critical_risk)
removed_entries = 0
D = int(input('Register Digit: '))
if D % 2 == 0:
    removed_entries = len(low_risk)
    low_risk = []
else:
    removed_entries = len(critical_risk)
    critical_risk = []
print('After Personalized Filtering:')
print('Low risk =', low_risk)
print('Medium risk =', medium_risk)
print('High risk =', high_risk)
print('Critical risk =', critical_risk)
print('Total valid entries =', valid_count)
print('Ignored entries =', invalid_count)
print('Removed Due to Personalization:', removed_entries)
