import java.util.Scanner;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class StackLinkedList {
    private Node top;
    private static final int maxElements = 5; // Maximum number of elements allowed

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        StackLinkedList stack = new StackLinkedList();

        //  push
        System.out.println("enter elements to be pushed :");
        int count = 0;
        while (count < maxElements) {
            int element = scanner.nextInt();
            stack.push(element);
            count++;
        }

        // pop
        stack.pop();
        // display
        stack.display();
    }

    public void push(int data) {
        if (getSize() >= maxElements) {
            System.out.println(" Stack is full.");
            return;
        }
        Node newNode = new Node(data);
        if (top == null) {
            top = newNode;
        } else {
            newNode.next = top;
            top = newNode;
        }
        System.out.println("Data Pushed into the stack: " + data);
    }

    public void pop() {
        if (top == null) {
            System.out.println("Stack is Underflow");
        } else {
            System.out.println("Deleted Element is: " + top.data);
            top = top.next;
        }
    }

    public void display() {
        if (top == null) {
            System.out.println("Stack is Underflow");
        } else {
            Node temp = top;
            System.out.println("Display elements are:");
            while (temp != null) {
                System.out.print(temp.data + " ");
                temp = temp.next;
            }
            System.out.println();
        }
    }

    public int getSize() {
        int count = 0;
        Node temp = top;
        while (temp != null) {
            count++;
            temp = temp.next;
        }
        return count;
    }
}
