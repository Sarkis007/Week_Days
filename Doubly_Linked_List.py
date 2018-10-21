class WeekDay:
    def __init__(self, data=None,  next=None, prev=None):
        self.next = next
        self.prev = prev
        self.data = data

class Week:
    def __init__(self):
        self.__head = None

    def find(self, data):
        temp = self.__head
        while temp.data is not data:
            temp = temp.next
        return temp

    def append(self, newdata):
        newDay = WeekDay(newdata)
        newDay.next = None
        if self.__head is None:
            newDay.prev = None
            self.__head = newDay

        else:
            temp = self.__head
            while temp.next is not None:
                temp = temp.next

            temp.next = newDay
            newDay.prev = temp

    def appendAfter(self, prevDay, newDay):
        new_Day = WeekDay(newDay)


        prev_Day = self.find(prevDay)

        if prev_Day is None:
            print("This Day doesn't exist in the list")


        new_Day.next = prev_Day.next
        prev_Day.next = new_Day
        new_Day.prev = prev_Day

        if new_Day.next is not None:
            new_Day.next.prev = new_Day

    def display(self):
        temp = self.__head
        while temp is not None:
            print temp.data
            temp = temp.next

    def delete(self, Day):
        deletedata = self.find(Day)

        if self.__head == deletedata:
            self.__head = deletedata.next
        if deletedata.next is not None:
            deletedata.next.prev = deletedata.prev
        if deletedata.prev is not None:
            deletedata.prev.next = deletedata.next

    def reverse(self):
        current = None
        temp = self.__head

        while temp is not None:
            current = temp.prev
            temp.prev = temp.next
            temp.next = current
            temp = temp.prev

        if current is not None:
            self.__head = current.prev



def main():
    my_week = Week()

    my_week.append("Mon")
    my_week.append("Tue")
    my_week.append("Wed")
    my_week.append("Thr")
    my_week.append("Fri")
    my_week.append("Sat")
    my_week.append("Sun")
    my_week.appendAfter("Sat","Test")
    my_week.delete("Test")
    my_week.reverse()
    my_week.display()


main()