//This problem was asked by Google.

// An XOR linked list is a more memory efficient doubly linked list.
// Instead of each node holding next and prev fields, it holds a field named both, 
// which is an XOR of the next node and the previous node. Implement an XOR linked list; 
// it has an add(element) which adds the element to the end, 
// and a get(index) which returns the node at index.

// If using a language that has no pointers (such as Python), 
// you can assume you have access to get_pointer and dereference_pointer 
// functions that converts between nodes and memory addresses.

/* Need a refresher of c and pointers, will be good practice */

// XOR is valid if and only if one of the inputs is high

/* FROM WIKIPEDIA: 
algebraic laws: 
	X⊕X = 0
	X⊕0 = X
	X⊕Y = Y⊕X
	(X⊕Y)⊕Z = X⊕(Y⊕Z) */

// An XOR linked list compresses the same information into one address field by storing the bitwise XOR 
// (here denoted by ⊕) of the address for previous and the address for next in one field:

// uintptr_t xor_ptr = (uintptr_t)p1 ^ (uintptr_t)p2;
// (void *)(xor_ptr ^ (uintptr_t)p2)
// from https://stackoverflow.com/questions/26569728/using-xor-with-pointers-in-c

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// typedef struct XORList *XORList;
typedef uintptr_t $;

typedef struct Node Node;
typedef Node* NodePtr;

struct Node { 
	NodePtr both; 
	int value;
};

void print (NodePtr root);
void add (NodePtr root, int elem);
NodePtr get (NodePtr root, int index);


// struct XORList {
// 	Node root;
// 	// void (*add);
// 	// void (*get);
// 	// void (*print);
// };

void print (NodePtr root){
	printf("Printing... \n");
	NodePtr prev = NULL;
	NodePtr temp = root;
	NodePtr next; 
	while (root != NULL){
		printf("%d ", temp->value);
		next = (NodePtr)(($)temp->both ^ ($)prev);
		prev = temp;
		temp = next;
	}
	printf("\n");
}

void add (NodePtr root, int elem){
	while (root != NULL){
		root = (void *)(($)root->both ^ ($)root);
	}
	// Node newnode = malloc()


}

NodePtr get (NodePtr self, int index){
	return NULL;
}


int main(int argc, char const *argv[]){

	(void) argc; 
	(void) argv; 

	// initialize some nodes
	NodePtr x = malloc(sizeof(Node));
	NodePtr y = malloc(sizeof(Node));
	NodePtr z = malloc(sizeof(Node));

	x->value = 5; 
	y->value = 7; 
	z->value = 10; 

	// bitwise XOR is ^, $ is uintptr_t
	// $ x_ptr = ($)y ^ ($)NULL;
	x->both = (NodePtr)(($)y ^ ($)NULL);
	y->both = (NodePtr)(($)x ^ ($)z);
	z->both = (NodePtr)(($)y ^ ($)NULL);
	// Node test = (void *)(x_ptr ^ ($)NULL);
	// printf("%d ",(int)test->value);

	print(x);
	return 0;
}

/* Definitely needed to brush up on a lot of C stuff here, but learned a lot.
   uintptr_t allows for easy manipulation of addresses with XOR
   and syntax of typedef and struct pointers. */