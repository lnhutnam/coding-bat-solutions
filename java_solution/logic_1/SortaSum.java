package java_solution.logic_1;

public class SortaSum {
    public int add(int a, int b) {
        while (b != 0) {
            int carry = a & b;
            a ^= b;
            b = carry << 1;
        }
        return a;
    }

    public int sortaSum(int a, int b) {
        int sum = add(a, b);
        return (sum < 20 && sum >= 10) ? 20 : sum;
    }

}
