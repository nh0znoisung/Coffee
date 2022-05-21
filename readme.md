## Introduction
This is a simple `console app` for customer in order to use the Coffee System service (such as buy coffee with more topping, print bill, send order status,...) by Code with Me. This colorful console app written by `Python3` and run well on `Linux` OS. The system is designed with 2 mode. The first one is normal when the user (customer) can interact directly with program via the command line instruction and the second one is read the already file for testing. Due to the simple of this app, there is no `Database System` at all, the data just initializes manually and store in a json file. Hope you enjoy and have fun :).

## Usage
### Requirements
+ `Python` >= 3.8.10
+ `Pip` >= 20.0.2
+ **OS**: `Linux` 

### Install dependencies
``` sh
pip install -r requirements.txt
```

### Run program
``` sh
python3 CoffeeSystem.py
```

### Testing
``` sh
coverage run -m unittest TestCoffeeSystem
coverage report -m
coverage html
```

Watch `htmlcov/index.html`

## Design Pattern
In this assignment, I will try to integrate 4 Design Pattern in order to make my code easier to promote, make changes in the future and object reusability. They include **Singleton, Visitor, Factory, Strategy**. 
### Singleton

#### Introduction
`Singleton` is a **creational design** pattern that lets us ensure that a class has only one instance and it will be initialized only when it's requested for the first time, while providing a global access point to this instance.


#### How to implement
+ Create an attribute which have **private static field** into the class for storing the *Singleton instance*.
+ Define a **public static creation method** for getting the *singleton instance*. Inside the method, if singleton instance is `NULL`, initialize with new instance and then we just return the instance.
+ Make the access modifier of method `Constructor` of this class is `private` so that other class cannot create object and just the creation static method in this class can.
+ The client code cannot invoke the contructor of this class and only get instance by call the static creation method. 
![](/images/singleton-structure.png)

#### Application
At first, we see on structure and function of `Export Factory`, for example the class `PrinterFactory`, we just only use this instace of class to indirectly generate the `PrinterStrategy` and doesn't have any responsibilities for stroing some special attributes for each instance, so that we need only create one instance in its lifecycle. This is the big chance we can apply the **Singleton Design Pattern** to this class. In addition, we can do the same with other classes `TelegramFactory`, `MessenerFactory`,...
![](/images/singleton-code.png)

## Flowchart
![](/images/Flowchart.png) 


## Naming Convention
In computer programming, a naming covention is the set of rules for choosing the character sequence to be used for **identifiers** which denote **variables, types, functions**, and other **entities** in **source code** and **documentation.

The reasons why we need to use a naming convention include the following:
- To reduce the effort needed to read and understand source code.
- To enable code reviews to focus on issues more important than syntax and naming standards.
- To enable code quality review tools to focus their reporting mainly on significant issues other than syntax and style preferences.

In Python case, these are some recommendation about naming covention for this programming language:
- **Class names** need to write as `UpperCamelCase`
- **Constants** need to write as `CAPITALIZED_WITH_UNDERSCORES`
- **Other names** need to write as `lowercase_separated_by_underscores`
- **Private attributes** need to write with the prefix is 1 or 2 underscores such as `__instance`, `_instance`,... Prefix with double underscores or more changes the behaviour in classes regarding to [Name mangling](https://en.wikipedia.org/wiki/Name_mangling#Python). Moreover, prefix and postfix with double underscores are indented as `Magic names` which fulfill special behaviour in Python object, *for example*, `__add__` can use by syntax **obj1.__add__(obj2)** or **obj1 + obj2**.
- Always use `self` for first argument to instance methods. While we always use `cls` for first argument to class methods.

## Demo => Video

Convention of code:
danh từ, động từ
cách đặt tên file

Documentation

Coverage > 80%

## Unittest => Unit-test + Coverage-python
Test tổng tiền
Input nhập vào -> ValueError(out of rangec  )
data còn lại

Nhược điểm
Thiếu tương tác với người dùng, trong thực thi vẫn chưa cho khách hàng hủy đơn + thay đổi liều lượng + Xem các Instruction nâng cao như thoat thoátthoát khỏi hệ thống, 

Timer

## Future improvement
+ We can extend the instruction, such as enter `Q` to quit the program instantly, enter `H` for showing the instruction, enter `C` to show all the customer's cart up to now,...
+ Interact with real application, call API of Messenger, Telegram, Zalo to send order status when it complete or prinNot test => Print true or false

Chưa check phone number

Cai Id phải là int 
t bill.
+ Add the payment function, check and call API for thrid party or bank for paying the cart 
+ Data is can fetch/update from the Database Management System.


## References
+ https://refactoring.guru/design-patterns
+ https://peps.python.org/pep-0008/#function-and-variable-names
+ https://en.wikipedia.org/wiki/Naming_convention_(programming)