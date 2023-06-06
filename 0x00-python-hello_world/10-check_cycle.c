#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - a function that checks if a singly linked list has a cycle in it
 * @list: the linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *s = list, *f = list;

	while (s != NULL && f != NULL && f->next != NULL)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}
	return (0);
}
