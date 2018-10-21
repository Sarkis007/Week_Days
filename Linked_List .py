class WeekDay:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Week:
    def __init__(self):
        self.__head = None

    def find(self, data):
        temp = self.__head
        while temp.data is not data:
            temp = temp.next
        return temp

    def display(self):
        printval = self.__head
        while printval is not None:
            print (printval.data)
            printval = printval.next

        print "----------"

    def append(self, newdata):
        newDay = WeekDay(newdata)
        if self.__head is None:
            self.__head = newDay
        else:
            temp = self.__head
            while temp.next is not None:
                temp = temp.next


            temp.next = newDay

    def addAtBegining(self, newdata):
        newDay = WeekDay(newdata)

        newDay.next = self.__head
        self.__head = newDay

    def appendAfter(self, prevDay, newDay):
        new_Day = WeekDay(newDay)
        prev_Day = self.find(prevDay)

        if prev_Day is None:
            print("This Day doesn't exist in the list")


        new_Day.next = prev_Day.next
        prev_Day.next = new_Day

    def delete(self, Day):
        temp = self.__head
        while temp is not None and temp.next.data != Day:
            temp = temp.next
        temp.next = temp.next.next

    def reverse(self):
        prev = None
        temp = self.__head
        while (temp is not None):
            next = temp.next

            temp.next = prev
            prev = temp

            temp = next
        self.__head = prev

def main():
    my_week = Week()
    my_week.append("Mon")
    my_week.append("Tue")
    my_week.append("Wed")
    my_week.append("Thr")
    my_week.append("Fri")
    my_week.append("Sat")
    my_week.append("Sun")
    my_week.appendAfter("Wed", "Test")
    my_week.delete("Test")
    my_week.reverse()
    my_week.display()

main()