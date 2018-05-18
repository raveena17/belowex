class Date:
    """ a user-defined data structure that
        stores and manipulates dates
    """

    def __init__(self, month, day, year):
        """ the constructor for objects of type Date """
        self.month = month
        self.day = day
        self.year = year


    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.
        """
        s =  "%02d/%02d/%04d" % (self.month, self.day, self.year)
        return s
    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise. """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def equals(self, d2):
        """ Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month and self.day == d2.day:
            return True
        else:
            return False
    def tomorrow(self):
        self.a=[1,3,5,7,8,10]
        if self.month in self.a:
            if self.day==31:
                self.day = 1
                self.month=self.month+1
                return self.month,self.day,self.year
            else:
                self.day = self.day+1
                return self.month,self.day,self.year
        self.a=[4,6,9,11]
        if self.month in self.a :
            if self.day==30:
                self.day = 1
                self.month=self.month+1
                return self.month,self.day,self.year
            else:
                self.day=self.day+1
                return self.month,self.day,self.year
        if self.month==2:
            if self.isLeapYear() == True:
                if self.day==29:
                 self.day = 1
                 self.month=self.month+1
                 return self.month,self.day,self.year
                else:
                  self.day=self.day+1
                  return self.month,self.day,self.year
            if self.isLeapYear() == False:
                 
                if self.day == 28:
                   self.day = 1
                   self.month=self.month+1
                   return self.month,self.day,self.year
                else:
                   self.day=self.day+1
                   return self.month,self.day,self.year
        if self.month == 12:
             if self.day == 31:
                self.day = 1
                self.month = 1
                self.year=self.year+1
                return self.month,self.day,self.year
             else:
                self.day=self.day+1
                self.year=self.year
                return self.month,self.day,self.year
    def yesterday(self):
        self.a=[5,7,8,10,12]
        if self.month in self.a:
            if self.day==1:
                self.day = 30
                self.month=self.month-1
                return self.month,self.day,self.year
            else:
                self.day=self.day-1
                return self.month,self.day,self.year
        self.a=[2,4,6,9,11]
        if self.month in self.a :
            if self.day==1:
                self.day = 31
                self.month=self.month-1
                return self.month,self.day,self.year
            else:
                self.day=self.day-1
                return self.month,self.day,self.year
        if self.month==3:
            if self.isLeapYear() == True:
                if self.day==1:
                 self.day = 29
                 self.month=self.month-1
                 return self.month,self.day,self.year
                else:
                  self.day=self.day-1
                  return self.month,self.day,self.year
            if self.isLeapYear() == False:
                 
                if self.day==1:
                   self.day = 28
                   self.month=self.month-1
                   return self.month,self.day,self.year
                else:
                   self.day=self.day-1
                   return self.month,self.day,self.year
        if self.month == 1:
             if self.day == 1:
                self.day = 31
                self.month = 12
                self.year=self.year-1
                return self.month,self.day,self.year
             else:
                self.day=self.day-1
                self.year=self.year
                return self.month,self.day,self.year
        
    def addndays(self,n):
        for i in range(n):
            print self.tomorrow
              
    def subnday(self,n):
      for i in range(n):
        self.a=[5,7,8,10,12]
        if self.month in self.a:
            if self.day==1:
                self.day = 30
                self.month=self.month-1
                print self.month,self.day,self.year
                #return self.month,self.day,self.year
            else:
                self.day=self.day-1
                print self.month,self.day,self.year
                #return self.month,self.day,self.year
        self.a=[2,4,6,9,11]
        if self.month in self.a :
            if self.day==1:
                self.day = 31
                self.month=self.month-1
                print self.month,self.day,self.year
                #return self.month,self.day,self.year
            else:
                self.day=self.day-1
                print self.month,self.day,self.year
                #return self.month,self.day,self.year
        if self.month==3:
            if self.isLeapYear() == True:
                if self.day==1:
                 self.day = 29
                 self.month=self.month-1
                 print self.month,self.day,self.year
                 #return self.month,self.day,self.year
                else:
                  self.day=self.day-1
                  print self.month,self.day,self.year
                  #return self.month,self.day,self.year
            if self.isLeapYear() == False:
                if self.day==1:
                   self.day = 28
                   self.month=self.month-1
                   print self.month,self.day,self.year
                   #return self.month,self.day,self.year
                else:
                   self.day=self.day-1
                   print self.month,self.day,self.year
                   #return self.month,self.day,self.year
        if self.month == 1:
             if self.day == 1:
                self.day = 31
                self.month = 12
                self.year=self.year-1
                print self.month,self.day,self.year
                #return self.month,self.day,self.year
             else:
                self.day=self.day-1
                self.year=self.year
                print self.month,self.day,self.year
                #return self.month,self.day,self.year
    def isbefore(self,d2):
        if self.month>d2.month and self.day>d2.day and self.year>d2.year:
            return True
        if self.month>d2.month and self.year>d2.year:
            return True
        if self.month>d2.month and self.year==d2.year:
            return True
        if self.month==d2.month and self.day>d2.day and self.year==d2.year:
            return True
        else:
            return False
    def isafter(self,d2):
        if self.month<d2.month and self.day<d2.day and self.year<d2.year:
            return True
        if self.month<d2.month and self.year<d2.year:
            return True
        if self.month<d2.month and self.year==d2.year:
            return True
        if self.month==d2.month and self.day<d2.day and self.year==d2.year:
            return True
        else:
            return False
    def dow(self):
        a=self.year%400
        if a>300:
          b=a%300
          c=b//4
          d=(c*2)+(b-c)+(1)
          e1=d%7
          if self.isLeapYear() == True:
            f=[30,29,31,30,31,30,31,31,30,31,30,31]
            f1=0
            for i in range(self.month):
             f1=f1+f[i]
             g=e1+f1+self.day
             e=g%7
             if e==0:
                return 'sunday'
             if e==1:
                return 'monday'
             if e==2:
                return 'tuesday'
             if e==3:
                return 'wednesday'
             if e==4:
                return 'thursday'
             if e==5:
                return 'friday'
             if e==6:
                return 'saturday'
          if self.isLeapYear() == False:
             f=[30,28,31,30,31,30,31,31,30,31,30,31]
             f1=0
             for i in range(self.month):
              f1=f1+f[i]
              g=e1+f[self.month-1]+self.day
              e=g%7
              if e==0:
                return 'sunday'
              if e==1:
                return 'monday'
              if e==2:
                return 'tuesday'
              if e==3:
                return 'wednesday'
              if e==4:
                return 'thursday'
              if e==5:
                return 'friday'
              if e==6:
                return 'saturday'
        if a>200 and a<300:
          b=a%200
          c=b//4
          d=(c*2)+(b-c)+(3)
          e1=d%7
          if self.isLeapYear() == True:
            f=[30,29,31,30,31,30,31,31,30,31,30,31]
            f1=0
            for i in range(self.month):
              f1=f1+f[i]
              g=e1+f1+self.day
              e=g%7
              if e==0:
                return 'sunday'
              if e==1:
                return 'monday'
              if e==2:
                return 'tuesday'
              if e==3:
                return 'wednesday'
              if e==4:
                return 'thursday'
              if e==5:
                return 'friday'
              if e==6:
                return 'saturday'
          if self.isLeapYear() == False:
             f=[30,28,31,30,31,30,31,31,30,31,30,31]
             f=0
             for i in range(self.month):
               f1=f1+f[i]
               g=e1+f1+self.day
               e=g%7
               if e==0:
                return 'sunday'
               if e==1:
                return 'monday'
               if e==2:
                return 'tuesday'
               if e==3:
                return 'wednesday'
               if e==4:
                return 'thursday'
               if e==5:
                return 'friday'
               if e==6:
                return 'saturday'
              
        if a>100 and a<200 and a<300:
         b=a%100
         c=b//4
         d=(c*2)+(b-c)+(5)
         e1=d%7
         if self.isLeapYear() == True:
            f=[30,29,31,30,31,30,31,31,30,31,30,31]
            f1=0
            for i in range(self.month):
              f1=f1+f[i]
              g=e1+f1+self.day
              e=g%7
              if e==0:
                return 'sunday'
              if e==1:
                return 'monday'
              if e==2:
                return 'tuesday'
              if e==3:
                return 'wednesday'
              if e==4:
                return 'thursday'
              if e==5:
                return 'friday'
              if e==6:
                return 'saturday'
         if self.isLeapYear() == False:
            f=[30,28,31,30,31,30,31,31,30,31,30,31]
            f1=0
            for i in range(self.month):
              f1=f1+f[i]
              g=e1+f1+self.day
              e=g%7
              if e==0:
                return 'sunday'
              if e==1:
                return 'monday'
              if e==2:
                return 'tuesday'
              if e==3:
                return 'wednesday'
              if e==4:
                return 'thursday'
              if e==5:
                return 'friday'
              if e==6:
                return 'saturday'
            
        if a<100:
         c=a//4
         d=(c*2)+(a-c)
         e1=d%7
         if self.isLeapYear()== True:
            f=[30,29,31,30,31,30,31,31,30,31,30,31]
            f1=0
            for i in range(self.month):
              f1=f1+f[i]
              g=e1+f1+self.day
              e=g%7
              if e==0:
                return 'sunday'
              if e==1:
                return 'monday'
              if e==2:
                return 'tuesday'
              if e==3:
                return 'wednesday'
              if e==4:
                return 'thursday'
              if e==5:
                return 'friday'
              if e==6:
                return 'saturday'
         if self.isLeapYear() == False:
            f=[30,28,31,30,31,30,31,31,30,31,30,31]
            f1=0
            for i in range(self.month):
              f1=f1+f[i]
              g=e1+f1+self.day
              e=g%7
              if e==0:
                return 'sunday'
              if e==1:
                return 'monday'
              if e==2:
                return 'tuesday'
              if e==3:
                return 'wednesday'
              if e==4:
                return 'thursday'
              if e==5:
                return 'friday'
              if e==6:
                return 'saturday'
    def diff(self,d2):
        counter = 0
        #counter = counter + 1
        while self.day != d2.day or self.month != d2.month or self.year != d2.year:
           #counter = 0
           counter = counter + 1
           if self.month > d2.month or self.day > d2.day or self.year > d2.year:
               d2.tomorrow()
           if self.month >= d2.month or self.day < d2.day or self.year > d2.year:
               d2.tomorrow()
           if self.month == d2.month or self.day > d2.day or self.year == d2.year:
               d2.tomorrow()
           if self.month == d2.month or self.day < d2.day or self.year > d2.year:
               d2.tomorrow()
           if self.month<d2.month or self.day<d2.day or self.year < d2.year:
               d2.yesterday()
           if self.month>d2.month or self.day<d2.day or self.year < d2.year:
               d2.yesterday()
           if self.month<d2.month or self.day>d2.day or self.year < d2.year:
               d2.yesterday()

        return counter
             
            
           
            
           
        
        
        
    

            
            
            
                
                
