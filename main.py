# Functional Prompt

def flat_sort(array):
    result = list()
    for i in array:
        if type(i) == list:
            for j in i:
                result.append(j)
        else:
            result.append(i)
    return sorted(result)

print(flat_sort([4,1,3,9, [2,3], [5, 6, 8, 0 ,1]]))

"""
- How does this solution ensure data immutability?
It doesn't have any side effects, so no data is being changed outside of this function, so given the same input it will always produce the same output.

- Is this solution a pure function? Why or why not?
This is a pure function as because as mentioned earlier it has no side effects.

- Is this solution a higher order function? Why or why not?
This solution is not a higher order function because it does not take a function as an argument.

- Would it have been easier to solve this problem using a different programming style?
I think having access to a global array would have made it easier for me personally as I am still inexperienced, but I can certainly see the benefits of this style of programming.

- Why in particular is functional programming a helpful paradigm when solving this problem?
I can see functional programming being useful in solving this problem because there would be no fear of the lists or the data therein being changed in any way. It is simply used for a specific reason and the original data is preserved.

"""

# Object Oriented Prompt

class Podracer:
    def __init__(self, max_speed, condition, price): 
        self.max_speed = max_speed
        self.condition = condition
        self.price = price
    
    def repair(self):
        self.condition = "Repaired"
        print(f"Successfully repaired!")

class AnakinsPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def boost(self):
        self.max_speed *= 2
        print("Speed boost active!")

class SebulbasPod(Podracer):
    def __init__(self, max_speed, condition, price):
        super().__init__(max_speed, condition, price)
    
    def flame_jet(self, podracer):
        podracer.condition = "Trashed"
        print("Critical hit!")

pod = Podracer(1, "Trashed", 10)
pod.repair()
print(pod.condition)

new_pod = AnakinsPod(2, "Perfect", 50)
new_pod.boost()
print(new_pod.max_speed)
print(new_pod.condition)

third_pod = SebulbasPod(5, "Perfect", 100)
third_pod.flame_jet(new_pod)
print(new_pod.condition)

"""
- How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
    - Encapsulation
    - Abstraction
    - Inheritance
    - Polymorphism
This solution encapsulates information within different classes (Podracer, AnakinsPod & SebulbasPod), and it also uses inheritance when creating both subclasses which derive from the main Podracer superclass.

- Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
I personally think this coding style is suited perfectly for this problem because of all of the benefits that we get from using OOP programming, such as the potential use of the four pillars ans the use of classes in general.

- How in particular did Object Oriented Programming assist in the solving of this problem?
Being able to create a superclass along with other derivative subclasses, as well as simply being able to use the methods defined in those classes as intended to change the state of a specific object assisted in solving this problem an incredible amount.

"""