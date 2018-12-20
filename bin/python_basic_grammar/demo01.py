import datetime
import time

class Activity:
    __decription = "This is private attr for Activity class inner use!"
    _location = 'Asia'
    country = 'China'

    def __init__(self, **kwargs):
        print(self.__decription)
        self.activity_attrs = kwargs
    
    @staticmethod
    def checkActivity(self):
        if self is None:
            raise Exception('no activity instance!')
        if self.activity_attrs['activity_begin_date'] is None or self.activity_attrs['activity_end_date'] is None:
            raise Exception("activity_begin_date or activity_end_date is None!")
        activity_begin_date = time.mktime(time.strptime(self.activity_attrs['activity_begin_date'], '%Y-%M-%d'))
        activity_end_date = time.mktime(time.strptime(self.activity_attrs['activity_end_date'], '%Y-%M-%d'))
        if activity_begin_date >= activity_end_date:
            raise Exception('activity_begin_date >= activity_end_date')
    
    def get_act_time(self):
        return {'activity_begin_date':self.activity_attrs['activity_begin_date'],
                'activity_end_date':self.activity_attrs['activity_end_date']}
        
        

act2 = Activity(activity_name='注册送积分', activity_begin_date='2018-11-02', activity_end_date='2018-12-30')
print(act2.activity_attrs)
print(type(act2.activity_attrs))

act2.activity_attrs['activity_name'] = '注册送电影票'
print(act2.activity_attrs)

print(act2.__getattribute__('activity_attrs'))

print("创建活动3!")
act_attrs = {'activity_name':'购买VIP会员参与抽奖','activity_begin_date':'2018-12-11', 'activity_end_date':'2018-12-30'}
act3 = Activity(**act_attrs)

Activity.checkActivity(act3)

print(act3.get_act_time())

print(act3.country)
print(act3._location)

