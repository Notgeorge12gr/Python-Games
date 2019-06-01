#Import is for the system to wait for a certent amount of time
import time
rq=0
end='''

    {}    {}


   |        |
   |________|

'''
print ('Hey and welcome to Da Quiz')
time.sleep(0.2)
print ('You will to anwser 10 math question')
time.sleep(0.2)
print ('But before we start')
time.sleep(0.2)
print ('What is your name?')
name=input()
print('Ok then',name,'lets start')
time.sleep(0.2)
print('What is 10+13?')
q1=input()
if (q1=='23'):
	rq=rq+1
	print ('Right',name,'10+13 is 23')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'10+13 is 23')
	time.sleep(0.2)
	print('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
print ('Question 2')
time.sleep(0.2)
print ('What is 26+62?')
q2=input()
if (q2=='88'):
	rq=rq+1
	print ('Right',name,'26+62 is 88')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'26+62 is 88')
	time.sleep(0.2)
	print('Lets move on')
print ('Question 3')
time.sleep(0.2)
print ('What is 135-87?')
q3=input()
if (q3=='48'):
	rq=rq+1
	print ('Right',name,'135-87 is 48')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'135-87 is 48')
	time.sleep(0.2)
	print('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
print ('Question 4')
time.sleep(0.2)
print ('What is the capital of Greece?')
q4=input()
if (q4=='Athens'):
	rq=rq+1
	print ('Right',name,'the capital of Greece is Athens')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'the capital of Greece is Athens')
	time.sleep(0.2)
	print('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
print ('Question 5')
time.sleep(0.2)
print ('What is the capital of Itali?')
q5=input()
if (q5=='Rome'):
	rq=rq+1
	print ('Right',name,'the capital of Itali is Rome')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'the capital of Rome')
	time.sleep(0.2)
	print('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
print ('Question 6')
time.sleep(0.2)
print ('What is the capital of United Kindom?')
q6=input()
if (q6=='London'):
	rq=rq+1
	print ('Right',name,'the capital of United Kindom is London')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'the capital of United Kindom is London')
	time.sleep(0.2)
	print('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
print ('Question 7')
time.sleep(0.2)
print ('What year did Greece won the Eurovision contest?')
q7=input()
if (q7=='2005'):
	rq=rq+1
	print ('Right',name,'Greece won the eurovion contest in 2005')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'Greece won the Eurovison contest in 2005')
	time.sleep(0.2)
	print('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
print ('Question 8')
time.sleep(0.2)
print ('What year was the Playstasion 2 released?')
q8=input()
if (q8=='2000'):
	rq=rq+1
	print ('Right',name,'the Playstation 2 was released in 2000')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'the Playstation 2 was released in 2000')
	time.sleep(0.2)
	print('Lets move on')
print ('Question 9')
time.sleep(0.2)
print ('What game is the most sold?')
q9=input()
if (q9=='tetris') or (q9=='Tetris'):
	rq=rq+1
	print ('Right',name,'Tetris is the most sold game 170 milion copies sold')
	time.sleep(0.2)
	print ('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
else:
	print ('Sorry',name,'Tetris is the most sold game with 170 milion copies sold')
	time.sleep(0.2)
	print('Lets move on')
	time.sleep(0.2)
	print ('Right questions =',rq)
print ('The last question')
time.sleep (0.2)
print ('Question 10')
time.sleep(0.2)
print ('When was the latest version of windows released?')
q10=input()
if (q10=='2015'):
	rq=rq+1
	print ('Right',name,'Windows 10 was released in 2015')
	time.sleep(0.2)
else:
	print ('Sorry',name,'Windows 10 was released in 2015')
	time.sleep(0.2)
print ('The test is done and here is your score')
time.sleep(0.2)
print ('You got',rq,'out of 10 right',name)
time.sleep(0.2)
if rq <=3:
	print ('Congrats',name,'did not pasted Da quiz')
elif rq ==4:
	print ('Sorry',name,'you barely did not pass Da quiz')
elif rq ==5:
	print ('Congrats',name,'you barely pasted Da quiz')
elif rq ==6:
	print ('Congrats',name,'you pasted Da quiz with a B')
elif rq ==7:
	print ('Congrats',name,'you pasted Da quiz with B+')
elif rq ==8:
	print ('Congrats',name,'you  pasted Da quiz with an A-')
elif rq ==9:
	print ('Congrats',name,'you pasted Da quiz with an A')
elif rq ==10:
	print ('Congrats',name,'you pasted Da quiz an A+')
print('Goodbye',name,'i hope is see you again')
print(end)
end = input ('Press enter to exit Da quiz')
