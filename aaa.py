rubin = 1
print(rubin)
rubin = "바보"
print(rubin)

kdt = {"305호" : "홀쭉",
"공욱재" : "미남"}

print(kdt)
kdt_order = {"우리는","개발자","입니다."}

for index in kdt_order:
  print(index)

def percent_calc(real_value , total_value):
  result = (real_value / total_value) * 100
  return result

calc = percent_calc(20,100)
print(calc)