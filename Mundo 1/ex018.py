import math
an = float (input(' Digite o angulo que deseja:'))
seno = math.sin (math.radians(an))
cosseno = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O angulo de {} tem o Seno de {:.2f}'.format (an,seno))
print('O angulo de {} tem o Coseno de {:.2f}'.format(an,cosseno))
print('O angulo de {} tem a Tangente de {:.2f}'.format(an, tan))
