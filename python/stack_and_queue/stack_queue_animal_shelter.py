class Dog:

    def __init__(self,data):

        self.data = data
        self.type = 'Dog'
        self.next = None

class Cat:

    def __init__(self,data):

        self.data = data
        self.type = 'Cat'
        self.next = None


class Animalshelter():

    def __init__(self):
        self.first = None
        self.second = None
    
    def enqueue(self,animal):

        node =  animal
        if self.second:
            
            self.second.next = node
            self.second = node
        else:
            self.first = node
            self.second = node
            
    def dequeue(self,pref):
        
        if self.first:
            temp=self.first

            while temp:

                if temp.type==pref:
                    self.first=temp.next
                    temp.next=None

                    if self.second.data==temp.data:
                        self.first=None
                    return temp.data
                else:
                    temp=temp.next
                    if self.first==self.second:
                        break

        else:
            return "Null"
  


if __name__ == "__main__":

    animal=Animalshelter()   
    cat1=Cat('Cat')
    cat2=Cat('Cat')
    dog1=Dog('Dog')
    dog2=Dog('Dog')
    animal.enqueue(cat1)
    animal.enqueue(cat2)
    animal.enqueue(dog1)
    animal.dequeue('Cat')
    animal.dequeue('Cat')
    animal.dequeue('Dog')
    animal.dequeue('Dog')
    animal.dequeue('Dog')
