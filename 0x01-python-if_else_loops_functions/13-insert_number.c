#include "lists.h"

 /**
 * insert_node - inserts a number into a sorted linked list
 * @head: the first node in the linked list
 * @number: the number to be inserted
 *
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp2;
	listint_t *temp1 = *head;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;

	if (!temp1 || temp1->n >= number)
	{
		new->next = temp1;
		*head = new;
		return (new);
	}

	temp2 = temp1->next;
	while (temp1 && temp2 && (temp2->n < number))
	{
		temp1 = temp1->next;
		temp2 = temp1->next;
	}

	temp1->next = new;
	new->next = temp2;
	return (new);
}
