class WeekDay:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Week:
    def __init__(self):
        self.__head = None

    def setHead(self, newdata):
        self.__head = WeekDay(newdata)

# Print the linked list
    def display(self):
        printval = self.__head
        while printval is not None:
            print (printval.data)
            printval = printval.next

        print "----------"

    def append(self, newdata):
        temp = self.__head
        while temp.next is not None:
            temp = temp.next

        newDay = WeekDay(newdata)
        temp.next = newDay

    def addAtBegining(self, newdata):
        newDay = WeekDay(newdata)

# Update the new nodes next val to existing node
        newDay.next = self.__head
        self.__head = newDay

def main():
    my_week = Week()

    my_week.setHead("Mon")

    my_week.append("Tue")
    my_week.append("Wed")
    my_week.append("Thr")
    my_week.append("Fri")
    my_week.append("Sat")

    my_week.addAtBegining("Sun")

    my_week.display()
