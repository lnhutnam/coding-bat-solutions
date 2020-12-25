package java_solution.logic_1;

public class Love6 {
    public int add(int a, int b) {
        while (b != 0) {
            int carry = a & b;
            a ^= b;
            b = carry << 1;
        }
        return a;
    }

    public int _abs(int a) {
        return (a > 0) ? a : -a;
    }

    public boolean love6(int a, int b) {
        return add(a, b) == 6 || a == 6 || b == 6 || _abs(add(a, -b)) == 6 ? true : false;
    }
}
