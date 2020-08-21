from math import radians, sin, cos, tan
an = float (input(' Digite o angulo que deseja:'))
seno = sin (radians(an))
cosseno = cos(radians(an))
tan = tan(radians(an))
print('O angulo de {} tem o Seno de {:.2f}'.format (an,seno))
print('O angulo de {} tem o Coseno de {:.2f}'.format(an,cosseno))
print('O angulo de {} tem a Tangente de {:.2f}'.format(an, tan))
