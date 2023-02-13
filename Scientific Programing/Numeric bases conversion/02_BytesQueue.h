#include <iostream>
using namespace std;

class BytesQueue
{
    //
    public:
    
        BytesQueue();

        struct Node
        {
            char value;
            Node *next;
        };

        Node *queue;

        void add(char data);
        void pop();
        void show();
    //
};


/// Constructor de la clase cola.
BytesQueue::BytesQueue(){queue = NULL;}

/// Para agregar un dato a la cola.
void BytesQueue::add(char data)
{
    // Se crea un nuevo nodo y se le agrega el dato //
    Node *node = new Node;
    node -> value = data;

    // Si la cola NO está vacía //
    if (queue != NULL)
    {
        Node *current;
        Node *step = queue;
        for(current = queue; current != NULL; current = current -> next)
        {
            step = current;
        }
        step -> next = node;
        node -> next = current;
    }
    else
    {
        node -> next = queue;
        queue = node;
    }
}

/// Para remover un elemento de la cola.
void BytesQueue::pop()
{
    // Si la cola NO está vacía //
    if (queue != NULL)
    {
        char first = queue -> value;
        queue = queue -> next;
        cout<<"\nSe eliminó el dato "<<first;
    }
    else
    {
        cout<<"\n| Cola vacía |";
    }
}

/// Para mostrar la cola.
void BytesQueue::show()
{
    // Si la cola NO está vacía //
    if(queue != NULL)
    {
        for(Node *current = queue; current != NULL; current = current -> next)
        {
            printf("%i", current -> value);
        }
    }
    else
    {
        cout<<"Cola vacía |";
    }
}