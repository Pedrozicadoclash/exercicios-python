qt_par = 0
qt_impar = 0
nums = []
for n in range(1,11):
 nums.append(int(input(f"Digite o {n}° número: ")))
print(max(nums))
if (nums%2==0):
    print(f"Numeros pares: {qt_par}")
else:
    print(f"Numeros impares: {qt_impar}")