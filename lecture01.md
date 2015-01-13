# Lecture 01

##C operators

The multiplication operators are left-associative

* operator in C is the same as Racket
* they are written in normal ways
* When working with integers, the division operator trunacates
any intermediate value and behaves the same as the Racket 
quotient funcion


Example:
```C
const int a = (4 * 5) / 2; //10
const int b = 4 * (5 / 2); //8!!
const int c = -5 / 2; //-2!!
```

##Function definations
*In C braces({})indecatest the beginning and end of the function body

*The return keyword is placed before the expression to be returned

```C
//C function:
int my_sqr(const int x){
	return x * x;
}
```
*In C, it is impossible to violate the contract type , and "type"runtime
errors do not exist.

```C
//C:
my_sqr("hello") //=> will not run!!!
