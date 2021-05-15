
# Bài 1:
"""
Lập trương trình để thực hiện các công việc sau:
Dung vòng lặp while hoặc do...while để tính số pi theo công thức sau:
pi/4 = 1 - 1/3 + 1/5 .... + (-1**n)/(2n+1)
Chương trình sẽ dừng khi 1/(2n+1)< epsilon.
 với epsilon là 1 số thực được nhập từ bàn phím trong khoảng (0,1)
 """
# Bài làm:
"""
epsilon = float(input("nhập epsilon ="))
if epsilon <= 0 or epsilon >= 1:
    print("bạn đã nhập sai giá trị của epsilon, vui lòng nhập lại.")
else:
    i = 0
    a = 0
    while 1/( 2*i + 1) >= epsilon :
        a += ((-1)**i) / (2*i + 1)
        i += 1
    print(f"giá trị của pi là: {4*a} ")"""

#Bài 2:
# Giai phương trình bậc 2 a*(x**2) + b*x + c = o
"""
import math
a = float(input(" nhập a = "))
b = float(input(" nhập b = "))
c = float(input(" nhập c = "))
if a == 0:
    if b == 0:
        print(" Phương trình vô nghiệm.")
    else:
        print(f"phương trình có một nghiệm x = {-c/ b}")
else:
    denta = b**2 - 4*a*c
    if denta == 0:
        print(f"phương trình có nghiệm kép x1 = x2 = {-b/(2*a)}")
    elif denta > 0:
        x1 = ((-b + math.sqrt(denta))/ (2 * a))
        x2 = ((-b - math.sqrt(denta))/(2 * a))
        print(f" Phương trình có 2 nghiêm x1 = {x1}, x2 = {x2}")
    else:
        j = math.sqrt(complex(-1))
        x1 = complex((-b + math.sqrt(-denta)*(j))/(2*a))
        x2 = complex((-b - math.sqrt(-denta)*j)/(2*a))
        print(f"phương trình có 2 nghiệm phức x1 = {x1}, x2 = {x2}")
"""

# Bài 3:
"""
1. Nhập một số nguyên N (0<N<1000) từ bàn phím.

2. Tìm và in ra các số hoàn thiện trong khoảng (0;N).

3. Tính tổng các số vừa tìm được và thông báo ra màn hình.

Chú ý: Số hoàn thiện (số hoàn chỉnh, số hoàn hảo)
 là số nguyên dương mà tổng các ước (khác nó) bằng chính nó.
"""
# Bài làm:
"""
n = int(input('nhập n ='))
i = 2
uoc = 1
sum_uoc = 0
Tổng_các_số_hoàn_thiện = 0
while i <= n:
    while uoc < i:
        if i % uoc == 0:
            sum_uoc = sum_uoc + uoc
        uoc += 1
    if sum_uoc == i:
        print(f"{i} là số hoàn thiện")
        Tổng_các_số_hoàn_thiện = Tổng_các_số_hoàn_thiện + i
    i += 1
print("tổng các số hoàn thiện từ 1 đến {n} là: {Tổng_các_số_hoàn_thiện}")
"""
"""
i = int(input('nhập i ='))
uoc = 1
sum_uoc = 0
Tổng_các_số_hoàn_thiện = 0
while uoc < i:
    if i%uoc == 0:
        sum_uoc = sum_uoc + uoc
    uoc += 1
if sum_uoc == i:
    print(f"{i} là số hoàn thiện")
    Tổng_các_số_hoàn_thiện = Tổng_các_số_hoàn_thiện + i
print(f'{Tổng_các_số_hoàn_thiện}')
"""
# Bài 4:
"""
Lập chương trình thực hiện các công việc sau:

1. Nhập 2 số nguyên M, N (1 < M, N < 2000) từ bàn phím

2. Kiểm tra xem M, N có phải cặp số thân thiết không. In kết qủa ra màn hình.
"""
# Bài làm:
"""
n = int(input("nhập n ="))
m = int(input("nhập m ="))
if n <= 1 or n >= 2000:
    print("Bạn đã nhập sai, vui lòng nhập lại n")
else:
    if m <= 1 or m >= 2000:
        print("Bạn đã nhập sai, vui lòng nhập lại")
uoc_n = 1
uoc_m = 1
sum_uoc_n = 0
sum_uoc_m = 0
while uoc_n < n:
    if n % uoc_n == 0 :
        sum_uoc_n = sum_uoc_n + uoc_n
    uoc_n += 1
while uoc_m < m :
    if m % uoc_m == 0:
        sum_uoc_m = sum_uoc_m + uoc_m
    uoc_m += 1
if n == sum_uoc_m and m == sum_uoc_n:
    print(f"{m}, {n} là 2 số thân thiết")
"""
# Bài 5:
"""
Lập trương trình thực hiện các công việc sau
  1 Nhập 2 số nguyên M,N (1< N,M < 2000) từ bàn phím
  2 Kiểm tra xem M, N có phải cặp số hứa hôn hay không,in kết quả ra màn hình
Lưu ý: cặp số hứa hôn là cặp số mà tổng các ước của số này lớn hơn số kia 1 đơn vị và ngược lại
Ví dụ: cặp 48 và 75 là cặp số hứa hôn
"""
# Bài làm:
"""
n = int(input("nhập n ="))
m = int(input("nhập m ="))
if n <= 1 or n >= 2000:
    print("Bạn đã nhập sai, vui lòng nhập lại n")
else:
    if m <= 1 or m >= 2000:
        print("Bạn đã nhập sai, vui lòng nhập lại m")
uoc_n = 1
uoc_m = 1
sum_uoc_n = 0
sum_uoc_m = 0
while uoc_n < n:
    if n % uoc_n == 0:
        sum_uoc_n = sum_uoc_n + uoc_n
    uoc_n += 1
print(sum_uoc_n)
while uoc_m < m:
    if m % uoc_m == 0:
        sum_uoc_m = sum_uoc_m + uoc_m
    uoc_m += 1
print(sum_uoc_m)
if sum_uoc_n == m + 1 and sum_uoc_m == n + 1:
    print(f'{n}, {m} là cặp số hứa hôn')
"""
# Bài 6:
"""
1. Nhập 1 số nguyên M (0 < M < 10000) từ bàn phím.

2. Liệt kê các số tự mãn trong khoảng từ 0 đến N.

Chú ý: Số tự mãn là một số dương mà tổng lập phương các chữ số của nó bằng chính nó. Ví dụ: 153 = 1^3+5^3+3^3 
"""
# Bài làm:
"""m = int(input("nhập m ="))
if m <= 0 or m >= 1000:
    print("Bạn đã nhập sai, vui lòng nhập lại giá trị của m")
a = int (m / 100)
b = int((m - 100*a)/10)
c = m - 100*a - 10*b
if a**3 + b**3 + c**3 == m:
    print(f"{m} là số tự mãn")
"""
# Bài 8:
"""
Lập chương trình thực hiện các công việc sau:
  1. Nhập 2 số nguyên dương M, N từ bàn phím. 
  2. Tìm tổng các ước chung của M, N.
  3. Đếm xem chúng có bao ước chung. In kết qủa ra màn hình
"""
# Bài làm:
"""
n = int(input("nhập n ="))
m = int(input("nhập m ="))
if n <= 0 or m <= 0:
    print("Bạn đã nhập sai, vui lòng nhập lại.")
if m < n:
    m, n = n, m
uoc = 1
số_ước_chung = 0
sum_uoc = 0
while uoc < n:
    if n % uoc == 0 and m % uoc == 0:
        số_ước_chung = số_ước_chung + 1
        sum_uoc = sum_uoc + uoc
    uoc += 1
print(f"số ước chung của m và n là {số_ước_chung}")
print(f"Tổng các ước chung của m, n là {sum_uoc}")
"""











