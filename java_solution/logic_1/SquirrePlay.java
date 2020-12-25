package java_solution.logic_1;

public class SquirrePlay {
    public boolean squirrelPlay(int temp, boolean isSummer) {
        return isSummer ? (temp >= 60 && temp <= 100) ? true : false : (temp >= 60 && temp <= 90) ? true : false;
    }      
}
