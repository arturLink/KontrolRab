
#task1 ne sdelano
#Ќапишите программу, котора€ по данному числу n от 1 до 9 выводит на экран n скворечников. ћежду двум€ соседними скворечниками также имеетс€ пустой (из пробелов) столбец. –азрешаетс€ вывести пустой столбец после последнего скворечника. ƒл€ упрощени€ рисовани€ скопируйте скворечник из примера в среду разработки.
#i=int(input("Skolko skvoresknikov ot 1 do 9? - "))
#for i in range(1,9):
#	if i==1:
#		print(" -----")
#		print("|  O  |")
#		print("!  -  !")
#		print(" -----")

#task2
#¬ывести степени натуральных чисел, не превосход€щие данного числа n. ѕользователь задает показатель степени и число n.
#n=int(input("Number: "))
#s=int(input("Stepen: "))
#count=0
#for i in range(n):
#	if (i**s)<n:
#		count+=1
#		print("stepeni "+str(count))

	
	

#task3
#from random import *
#from math import *
#students=randint(1,30)
#print("Amount of students == "+str(students))
#A=0
#for i in range(students):
	#mark=randint(1,5)
	#print("mark == "+str(mark))
	#if mark>0:
		#A+=mark
#average=students/A
#print("Average == "+str(average))

#task4
#ћой богатый д€дюшка подарил мне один доллар в мой первый день рождени€. ¬ каждый день рождени€ он увеличивал свой подарок и прибавл€л к нему столько долларов, сколько лет мне исполнилось. Ќаписать программу, указывающую, к какому дню рождени€ подарок превысит 100$.
#age=0
#gift=0
#for age in range(1,100):
	#gift+=age
	#print(gift)
	#if gift>100:
		#print("Age when gift is more than 100$ - "+str(age))
		#break

#task5
#for stroka in range(1,9):
	#if stroka==1:
		#print("1",end=" ")
	#elif stroka==2:
		#print("1",end=" ")
	#elif stroka==3:
		#print("2",end=" ")
	#elif stroka==4:
		#print("3",end=" ")
	#elif stroka==5:
		#print("5",end=" ")
	#elif stroka==6:
		#print("8",end=" ")
	#elif stroka==7:
		#print("13",end=" ")
	#elif stroka==8:
		#print("21",end=" ")