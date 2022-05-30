#include "lists.h"

/**
 * check_cycle - check if a singly linked list contains a cycle in it
 * @list: pointer to a node in the list
 *
 * pseudocode
 * use two pointers to transverse the list, one increases by 1 step and another
 * by 2 steps. If they happen to point to the same node, there exists a cycle
 *
 * Return: 0(no cycle) and (1) if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	a = b = list;
	while (b != NULL && b->next != NULL)
	{
		a = a->next;
		b = b->next->next;
		if (a == b) /* loop exists */
			return (1);
	}
	return (0);
}
