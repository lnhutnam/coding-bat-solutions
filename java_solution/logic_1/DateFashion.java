package java_solution.logic_1;

public class DateFashion {
    public int dateFashion(int you, int date) {
        return (you <= 2 || date <= 2) ? 0 : (you >= 8 || date >= 8) ? 2 : 1;
    }
}
