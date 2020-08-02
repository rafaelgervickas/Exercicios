Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nome = input (' Qual é o seu nome?')
 Qual é o seu nome? Rafael
>>> print ('Óla,'Nome', Prazer em te conhecer!)
       
SyntaxError: invalid syntax
>>> print ('Óla,'nome', Prazer em te conhecer!)
       
SyntaxError: invalid syntax
>>> print('Olá',nome,'Prazer em conhece-lo(a)')
Olá  Rafael Prazer em conhece-lo(a)
>>> print ('Óla',nome,'Prazer em te conhecer')
Óla  Rafael Prazer em te conhecer
>>> 
>>> dia = 07
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
>>> dia = input (' Em que dia você nasceu?')
 Em que dia você nasceu? 07
>>> mes = input (' Em que mês você nasceu?')
 Em que mês você nasceu? Jul
>>> ano = input (' Em que ano você nasceu?')
 Em que ano você nasceu? 2001
>>>  print ('Você nasceu',dia,'de',mes,'no',ano,'.Correto?')
 
SyntaxError: unexpected indent
>>> print ('Você nasceu',dia,'de',mes,'no',ano,'.Correto?')
Você nasceu  07 de  Jul no  2001 .Correto?
>>>  print ('Você nasceu',dia,'de',mes,'de',ano,'.Correto?')
 
SyntaxError: unexpected indent
>>> print ('Você nasceu',dia,'de',mes,'de',ano,'.Correto?')
Você nasceu  07 de  Jul de  2001 .Correto?
>>> 