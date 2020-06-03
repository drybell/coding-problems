/*
* Daniel Ryaboshapka
* Coding Problems 
* February 2nd 2019
*
* Problem 3: The prime factors of 13195 are 5, 7, 13 and 29.
* 	What is the largest prime factor of the number 600851475143 ?
*
* Language Chosen: C++
*
* Time Designing: 
* Time Coding: 
* Time Documenting: 
* Total Time Spent on Problem: 
*
*/


int checkPrime(int carry, int prev)
{
	int divisible = carry % prev; 
	if(divisible != 0){
		checkPrime(carry, prev - 1)
	}
}



int* generatePrimes(int* hold)
{
	for(int i = 0; i < 100000; i++){
		
	}
}

int main(int argc, char const *argv[])
{
	
	int* prime_array = malloc(100000 * sizeof(int));
	prime_array = generatePrimes(prime_array);
	return 0;
}