from optn import Overpartition

pi = [-8, 7, -5, 5, 5, 4, -3, 3, 1]

a = Overpartition.from_neg_list(pi)
print(a)
print("weight: {}".format(a.weight()))
print("Dyson rank: {}".format(a.d_rank()))
print("first residual crank: {}".format(a.res1crank()))
f = a.frob_rep_1()
print("first Frobenius representation:")
print(f[0].str(separator=" "))
print(f[1].str(separator=" "))
