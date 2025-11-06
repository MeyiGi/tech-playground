// fighter want to use wizard abilities also

public class Fighter implements WizardAdapter {
    private final Wizard legacyImplementationOfWizardLogic = new Wizard();

    public void createShield() {
        System.out.println("Metal Shield created successfully!");
    }

    @Override
    public void attack() {
        legacyImplementationOfWizardLogic.attackOfWizard();
    }
}
