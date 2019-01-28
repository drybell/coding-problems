/*
* Daniel Ryaboshapka
* Coding Problems 
* January 28th 2019
*
* Problem 1: If we list all the natural numbers below 10 
* that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
* The sum of these multiples is 23.
* Find the sum of all the multiples of 3 or 5 below 1000.
*
* FIRST LANGUAGE CHOSEN: C 
* ON DECK: C++
* IN THE HOLE: C#
*
* Time Designing: 5 minutes
* Time Coding: 15 minutes
* Time Documenting: 5 minutes
* Total Time Spent on Problem: ~20 minutes
*
*/


//BRUTE FORCE APPROACH
//in my initial design notes I quickly thought of a for loop to be the fastest
//way to code up. I had thoughts of recursion as well but I haven't thought 
//of a more efficient solution as "total" increases

#import <stdio.h>

int multiple_3_5(int total)
{
	int counter = 0;

	for (int i = 0; i < total; i++) {
		int flag = 0;
		if(i % 3 == 0){
			flag = 1;     //FLAG IS FOR DOUBLE COUNTING MULTIPLES OF 3 AND 5
			counter += i;
		}
		if(i % 5 == 0){
			if(flag == 1){
				counter += 0; 
			}
			else{
				counter += i;
			}
		}
	}

	return counter;
}

int main(int argc, char const *argv[])
{
	(void) argc;
	(void) argv;
	int total = 1000;
	int sum = multiple_3_5(total);
	printf("The sum of all the multiples of 3 and 5 below %d is %d\n", 
		total, sum);
	return 0;
}