from dataclasses import dataclass

@dataclass
class Holiday():
    monthes = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    
    def __init__(self, name, day, month):
        self.name = name
        self.day = day
        self.month = month
        
    def str(self):
        return "Happy {} day!".format(self.name)
    
    def eq(self, other):
        if isinstance(other, Holiday):
            return self.month == other.month
        return False
    
    def lt(self, other):
        if isinstance(other, Holiday):
            self_index = Holiday.monthes.index(self.month)
            other_index = Holiday.monthes.index(other.month)
            if self_index < other_index:
                return True
            elif self_index == other_index:
                return self.day < other.day
            else:
                return False
        return False
    
    def le(self, other):
        if isinstance(other, Holiday):
            self_index = Holiday.monthes.index(self.month)
            other_index = Holiday.monthes.index(other.month)
            if self_index < other_index:
                return True
            elif self_index == other_index:
                return self.day <= other.day
            else:
                return False
        return False
    
    def gt(self, other):
        if isinstance(other, Holiday):
            self_index = Holiday.monthes.index(self.month)
            other_index = Holiday.monthes.index(other.month)
            if self_index > other_index:
                return True
            elif self_index == other_index:
                return self.day > other.day
            else:
                return False
        return False
    
    def ge(self, other):
        if isinstance(other, Holiday):
            self_index = Holiday.monthes.index(self.month)
            other_index = Holiday.monthes.index(other.month)
            if self_index > other_index:
                return True
            elif self_index == other_index:
                return self.day >= other.day
            else:
                return False
        return False

a = Holiday("среда", 1, "March")
b = Holiday("суббота", 2, "August")

print(a.gt(b))