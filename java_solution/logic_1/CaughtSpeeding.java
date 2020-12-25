package java_solution.logic_1;

public class CaughtSpeeding {
    public int caughtSpeeding(int speed, boolean isBirthday) {
        return isBirthday ? ((speed <= 65) ? 0 : (speed >= 66 && speed <= 85) ? 1 : 2) : ((speed <= 60) ? 0 : (speed >= 61 && speed <= 80) ? 1 : 2);
    }
}
