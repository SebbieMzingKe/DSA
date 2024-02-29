import java.util.Scanner;

public class Circular_queue_arr {
    private static final int MAX = 5;
    private int[] queue = new int[MAX];
    private int rear = 0;
    private int front = 0;
    private int count = 0;
    private int j = 1;
    private int x = 1;

    void insertion() {
        if (count == MAX) {
            System.out.println("\n Queue is Full");
        } else {
            Scanner scanner = new Scanner(System.in);
            System.out.printf("\n Enter no %d:", j++);
            queue[rear++] = scanner.nextInt();
        }
    }


    void deletion() {
        if (front == rear) {
            System.out.println("\n Queue is empty");
        } else {
            System.out.printf("\n Deleted Element is %d", queue[front++]);
            x++;
            front = (front + 1) % MAX;
            count--;
        }
    }

    void display() {
        if (front == rear) {
            System.out.println("\n Queue is empty");
        } else {
            for (int i = front; i < rear; i++) {
                System.out.println(queue[i]);
            }
        }
    }

    public static void main(String[] args) {
        Circular_queue_arr queueExample = new Circular_queue_arr();


        for (int i = 0; i < MAX; i++) {
            queueExample.insertion();

        }


        queueExample.deletion();
        queueExample.display();

    }
}

