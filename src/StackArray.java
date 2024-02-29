import java.util.Scanner;

public class StackArray {
    private static final int size = 6; //size of the stack
    private static final int[] stack = new int[size];
    private static int top = -1;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // push
        System.out.println("Enter elements to push onto the stack  " );
        while (top < size - 1) {
            int element = scanner.nextInt();
            push(element);
        }

        //  pop
        pop();


        // display
        display();
    }

    static void push(int x) {
        if (top >= size - 1) {
            System.out.println("Stack Overflow");
        } else {
            top = top + 1;
            stack[top] = x;
            System.out.println("Data Pushed into the stack is: " + x);
        }
    }

    static void pop() {
        if (top == -1) {
            System.out.println("Stack  Underflow");
        } else {
            System.out.println("Deleted Element is: " + stack[top]);
            top = top - 1;
        }
    }

    static void display() {
        if (top == -1) {
            System.out.println("Stack is Underflow");
        } else {
            System.out.println("Displayed elements are:");
            for (int i = top; i >= 0; i--) {
                System.out.print(stack[i] + " ");
            }
            System.out.println();
        }
    }
}
