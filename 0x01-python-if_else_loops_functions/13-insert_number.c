#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: the first node in the linked list
 * @number: the number to be inserted
 *
 * Return: address of the new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, temp2;
	listint_t *temp1 = *head;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new_mode)
		return (NULL);

	new->n = number;

	if (!tmp1 || tmp1->n >= number)
	{
		new->next = tmp1;
		*head = new;
		return (new);
	}

	tmp2 = tmp1->next;
	while (tmp1 && tmp2 && (tmp2->n < number))
	{
		tmp1 = tmp1->next;
		tmp2 = tmp1->next;
	}

	tmp1->next = new;
	new->next = tmp2;
	return (new);
}
