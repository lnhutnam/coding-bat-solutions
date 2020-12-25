package java_solution.logic_1;

public class CigarParty {
    public boolean cigarParty(int cigars, boolean isWeekend) {
        return (cigars >= 40 && cigars <= 60) ? true : ((isWeekend && cigars >= 40) ? true : false);
    } 
}
