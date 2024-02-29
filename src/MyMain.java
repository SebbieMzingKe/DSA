//package main;

//import MyQueue;

public class MyMain {
    public static void main(String[]args)
    {
        MyQueue queue = new MyQueue(10);
        System.out.println(queue.enqueue(1575));
        System.out.println(queue.enqueue(75897));
        System.out.println(queue.enqueue(87995));
        System.out.println(queue.enqueue(5000));
        System.out.println(queue.enqueue(64586));
        System.out.println(queue.enqueue(65000));
        System.out.println(queue.enqueue(886588));
        System.out.println(queue.enqueue(9087754));
        System.out.println(queue.enqueue(868698));
        System.out.println(queue.enqueue(868686));
        System.out.println("Size of the elements in the array is::" + queue.getSize());
        System.out.println("The element at the top of the Queue is::"+ queue.top());
        System.out.println("Is the Queue Empty?"+"  "+ queue.isEmpty());
        System.out.println(  "Popped element from the Queue is::"+"  "+queue.dequeue());
    }
}