#include <iostream>
using namespace std;

class BytesStack
{
    //
    public:
    
        BytesStack();

        struct Node
        {
            char value;
            Node *next;
        };

        Node *stack;

        void add(char data);
        void pop();
        void show();
    //
};


/// Constructor de la clase cola.
BytesStack::BytesStack(){stack = NULL;}

/// Para agregar un dato a la pila.
void BytesStack::add(char data)
{
    // Se crea el nuevo nodo y se le almacena el dato //
    Node *node = new Node();
    node -> value = data;

    // Se guarda el inicio de la lista //
    Node *start = stack;

    // Se inserta el nodo al principio //
    if (stack == start)
    {
        stack = node;
    }
    node -> next = start;
}

/// Para remover un dato de la pila.
void BytesStack::pop()
{
    /// Implementación pendiente ///
}

/// Para mostrar la pila.
void BytesStack::show()
{
    // Si la cola NO está vacía //
    if (stack != NULL)
    {
        for(Node *current; current != NULL; current = current -> next)
        {
            printf("%i", current -> value);
        }
    }
}