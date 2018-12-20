import pyb
import micropython
micropython.alloc_emergency_exception_buf(100)

from pyb import USB_VCP

class Controller(object):
    def __init__(self):
        self.vs = USB_VCP()
        self.direction = 0
        self.speed = 0
        self.select_dir = 0
        self.select_speed = 0
        #self.vs.setinterrupt(-1)
        
    def dir_menu(self):
        print('please input your instructions')
        print('1. set the direction ')
        print('2. set the speed ')
        print('3. send the instruction ')
        
    def get_instrcution(self):
        print('please input your instructions ')
        print('1. set the direction ')
        print('2. set the speed ')
        print('3. send the instruction ')
        while True:
            if self.vs.any():
                pyb.delay(2000)
                self.instrcution = self.vs.readline()
                if (self.select_dir == 1):
                    if (self.instrcution == b'1'):
                        self.select_dir = 0
                        print('forward')
                        self.dir_menu()
                    elif(self.instrcution == b'2'):
                        self.select_dir = 0
                        print('back')
                        self.dir_menu()
                    elif(self.instrcution == b'3'):
                        self.select_dir = 0
                        print('leftforward')
                        self.dir_menu()
                    elif(self.instrcution == b'4'):
                        self.select_dir = 0
                        print('leftback')
                        self.dir_menu()
                    elif(self.instrcution == b'5'):
                        self.select_dir = 0
                        print('rightforward')
                        self.dir_menu()
                    elif(self.instrcution == b'6'):
                        self.select_dir = 0
                        print('rightback')
                        self.dir_menu()
                    elif(self.instrcution == b'7'):
                        self.select_dir = 0
                        print('stop')
                        self.dir_menu()
                    elif(self.instrcution == b'8'):
                        self.select_dir = 0
                        print('MotorA-F')
                        self.dir_menu()
                    elif(self.instrcution == b'9'):
                        self.select_dir = 0
                        print('MotorA-R')
                        self.dir_menu()
                    elif(self.instrcution == b'10'):
                        self.select_dir = 0
                        print('MotorB-F')
                        self.dir_menu()
                    elif(self.instrcution == b'11'):
                        self.select_dir = 0
                        print('MotorB-R')
                        self.dir_menu()
                    elif(self.instrcution == b'12'):
                        self.select_dir = 0
                        print('RUN')
                        self.dir_menu()
                    else:
                        print('please set the diretion')
                elif (self.select_speed == 1):
                    self.select_speed == 0
                    print('speed is ',int(self.instrcution))
                    print('please input your instructions')
                    print('1. set the direction ')
                    print('2. set the speed ')
                    print('3. send the instruction ')
                elif (self.instrcution == b'1'):
                    self.select_dir = 1
                    print('please set the diretion ')
                    print('1. forward')
                    print('2. back')
                    print('3. leftforward')
                    print('4. leftback')
                    print('5. rightforward')
                    print('6. rightback')
                    print('7. stop')
                    print('8. MotorA-F')
                    print('9. MotorA-R')
                    print('10.MotorB-F')
                    print('11.MotorB-R')
                    print('12.RUN')
                elif (self.instrcution == b'2'):
                    self.select_speed = 1
                    print('set the speed ')
                elif (self.instrcution == b'3'):
                    print('send the instruction ')
                else:
                    print ('test',self.instrcution)
                    print('please input your instructions')
                    print('1. set the direction ')
                    print('2. set the speed ')
                    print('3. send the instruction ')

                
if __name__ == "__main__":
    red = Controller()
    red.get_instrcution()
