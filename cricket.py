p=input('Enter player name:')
print('                             Welcome ',p,'!!!!')
import sys
i=[0,1]
j=[0,1]
k=[0,1]
import random

def ball(i,j,k,a):
  if a==5:
        a=1
        print('This ball:',a)
        i[0]+=1
        print('BALLS :',i[0])
        j[0]+=a
        print('Total score :',j[0],'/',k[0])
        
    
     
  elif a==7:
        a=0
        print('You\'re out')
        print('This ball:',a)
        i[0]+=1
        print('BALLS:',i[0])
        j[0]+=a
        print('Total score:',j[0],'/',k[0])
        k[0]+=1
        if k[0]==5:
           sys.exit('Se you later')
  elif a==8:
          a=0
          print('This ball :',a)
          i[0]+=1
          print('BALLS:',i[0])
          j[0]+=a
          print('Total score:',j[0],'/',k[0])
  elif a==9:
          a=1
          print('This ball :',a)
          i[0]+=1
          print('BALLS:',i[0])
          j[0]+=a
          print('Total score:',j[0],'/',k[0])
  elif a==10:
          a=1
          print('This ball :',a)
          i[0]+=1
          print('BALLS:',i[0])
          j[0]+=a
          print('Total score:',j[0],'/',k[0])
  else:
         print('This ball :',a)
         i[0]+=1
         print('BALLS:',i[0])
         j[0]+=a
         print('Total score:',j[0],'/',k[0])
#0.1
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play your first ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#0.2
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)
  
#0.3
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball'''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#0.4
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball'''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#0.5
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#1.0
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play last ball of the over'''))
if x>=10 and x<=99:
  ball(i,j,k,a)

print('                                   Toatal score=',j[0],'/',k[0],'after one Over')
print('                                   Run rate=',j[0]/1)

#1.1
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#1.2
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball'''))
if x>=10 and x<=99:
  ball(i,j,k,a)
  
#1.3
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#1.4
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#1.5
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball  '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#2
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play last ball of the over'''))
if x>=10 and x<=99:
  ball(i,j,k,a)

print('                                   Toatal score=',j[0],'/',k[0],'after two Overs')
print('                                   Run rate=',j[0]/2)

#2.1
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#2.2
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball'''))
if x>=10 and x<=99:
  ball(i,j,k,a)
  
#2.3
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#2.4
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#2.5
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball  '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#3
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play last ball of the over'''))
if x>=10 and x<=99:
  ball(i,j,k,a)

print('                                   Total score=',j[0],'/',k[0],'after three Overs')
print('                                   Run rate=',j[0]/3)

#3.1
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#3.2
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball'''))
if x>=10 and x<=99:
  ball(i,j,k,a)
  
#3.3
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#3.4
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#3.5
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball  '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#4
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play last ball of the over'''))
if x>=10 and x<=99:
  ball(i,j,k,a)

print('                                   Toatal score=',j[0],'/',k[0],'after four Overs')
print('                                   Run rate=',j[0]/4)

#4.1
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#4.2
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball'''))
if x>=10 and x<=99:
  ball(i,j,k,a)
  
#4.3
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#4.4
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#4.5
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play the next ball  '''))
if x>=10 and x<=99:
  ball(i,j,k,a)

#5
a=random.randint(0,10)
x=int(input('''

  Enter a two digit integer to play last ball of the over'''))
if x>=10 and x<=99:
  ball(i,j,k,a)

print('                                   Toatal score=',j[0],'/',k[0],'after five Overs')
print('                                   Run rate=',j[0]/5)

