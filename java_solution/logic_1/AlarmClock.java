package java_solution.logic_1;

public class AlarmClock {
    public String alarmClock(int day, boolean vacation) {
        return vacation ? (day == 0 || day == 6) ? "off" : "10:00" : (day == 0 || day == 6) ? "10:00" : "7:00";
    }
}
