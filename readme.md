## Introduction
This is a simple console app for customer. 2 mode: Run by directly interact with customer and run by read file for testing. This console app with colorful written by `Python3`



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

#### Application
At first, we see on structure and function of `Export Factory`, for example the class `PrinterFactory`, we just only use this instace of class to indirectly generate the `PrinterStrategy` and doesn't have any responsibilities for stroing some special attributes for each instance, so that we need only create one instance in its lifecycle. This is the big chance we can apply the **Singleton Design Pattern** to this class. In addition, we can do the same with other classes `TelegramFactory`, `MessenerFactory`,...


## WorkFlow
Flowchart của người dùng 


## Naming Convention
In computer programming, a naming covention is the set of rules for choosing the character sequence to be used for identifiers which denote variables, types, functions, and other entities in source code and documentation.

The reason why 

## Demo => Video

Convention of code:
danh từ, động từ
cách đặt tên file

Documentation

## Unittest => Unit-test + Coverage-python
Test tổng tiền
Input nhập vào -> ValueError(out of rangec  )
data còn lại

Nhược điểm
Thiếu tương tác với người dùng, trong thực thi vẫn chưa cho khách hàng hủy đơn + thay đổi liều lượng + Xem các Instruction nâng cao như thoat thoátthoát khỏi hệ thống, 

Timer

Payment

Dataset is fixed => Not test 
Not test => Print true or false

Chưa check phone number

Cai Id phải là int 


## References
+ https://refactoring.guru/design-patterns
+ https://peps.python.org/pep-0008/#function-and-variable-names
+ https://en.wikipedia.org/wiki/Naming_convention_(programming)