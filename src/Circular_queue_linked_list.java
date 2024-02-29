import java.util.Scanner;

public class Circular_queue_linked_list {
    private static final int MAX = 5;
    private int[] cq = new int[MAX];
    private int front = 0;
    private int rear = 0;
    private int count = 0;

    void insertCQ() {
        int data;
        if (count == MAX) {
            System.out.println("\n Circular Queue is Full");
        } else {
            Scanner scanner = new Scanner(System.in);
            System.out.print("\n Enter data: ");
            data = scanner.nextInt();
            cq[rear] = data;
            rear = (rear + 1) % MAX;
            count++;
            System.out.println("\n Data Inserted in the Circular Queue ");
        }
    }

    void deleteCQ() {
        if (count == 0) {
            System.out.println("\n\nCircular Queue is Empty..");
        } else {
            System.out.printf("\n Deleted element from Circular Queue is %d ", cq[front]);
            front = (front + 1) % MAX;
            count--;
        }
    }


    void displayCQ() {
        int i, j;
        if (count == 0) {
            System.out.println("\n\n\t Circular Queue is Empty ");
        } else {
            System.out.println("\n \nElements in Circular Queue are:\n");
            j = count;
            for (i = front; j != 0; j--) {
                System.out.print(cq[i] + "\t");
                i = (i + 1) % MAX;
            }
            System.out.println();
        }
    }

    // Add other methods or functions as needed

    public static void main(String[] args) {
        Circular_queue_linked_list circularQueue = new Circular_queue_linked_list();

        for (int i = 0; i < MAX; i++){
        circularQueue.insertCQ();
        }
        //circularQueue.displayCQ();
        circularQueue.deleteCQ();
        circularQueue.displayCQ();
    }
}
