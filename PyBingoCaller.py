import random
import readchar



class BingoBalls():
    def __init__(self):
        self.availableballs=[]
        self.pulledBalls=[]
        bingo='BINGO'
        num=1
        i=1
        for letter in bingo:
            i=1
            while i < 16:
                self.availableballs.append(f'{letter}-{num}')
                i+=1
                num+=1

    def pullball(self):
        if len(self.availableballs)==0:
            print('All Balls have been called.')
            return
        pull=random.randint(0,len(self.availableballs)-1)
        #print (f'Will pull #{pull} out of {len(self.availableballs)}.')
        currentball=self.availableballs[pull]
        self.pulledBalls.append(currentball)
        self.availableballs.remove(currentball)
        print(f'\nBall #{len(self.pulledBalls)} is {currentball}')

    def numofballscalled(self):
        print (f'\n{len(self.pulledBalls)} ball(s) called\n')
    
    def listBalls(self,balllist):
        b=1
        tb=len(balllist)
        cb=1
        print('\n')
        for ball in balllist:
            if len(ball)==3: ball=ball+' '
            print(f'{ball}', end='')
            if tb!=cb:
                print(f', ',end='')
            if b==10:
                print('')
                b=0
            b+=1
            cb+=1

    def listPulledBalls(self):
        self.listBalls(self.pulledBalls)    
        self.numofballscalled()

    def listAvailableBalls(self):
        self.listBalls(self.availableballs)
     

if __name__=='__main__':

    game=BingoBalls()
    print ('\nPyBingoCaller by Jarrett McAlicher\n')
    while True:
        print ("\nMenu: 'C' call new number, 'L' List called numbers,\n      'A' Available numbers, 'N' Number of balls called,'S' Stop Game... ",end='')
        
        key=readchar.readkey()
        if key.upper()=='S' or key.upper()=='X':
            game.listPulledBalls()
            print('\nGame Completed.')
            break
        elif key.upper()=='L':
            game.listPulledBalls()
        elif key.upper()=='A':
            game.listAvailableBalls()
        elif key.upper()=='C':
            game.pullball()
        elif key.upper()=='N':
            game.numofballscalled()
        
    

