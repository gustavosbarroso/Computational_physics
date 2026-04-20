from numpy import array
a= array([1,2,3,4],int)
b = array([2,4,6,8] ,int)
print(b/a+1)
print(b/(a+1))
print(1/a)
#No caso (b/a + 1), divide-se o elemento b[1] por a[1] e assim por diante e depois soma 1 em todos os elementos do array.#
#No caso 2,o parênteses prioriza a soma a+1 em relação a multiplicação. a+1 é feito e a divisão de elemento por elemento é feita.#
#No caso 3, 1 divide cada elemento do array individualmente. #
