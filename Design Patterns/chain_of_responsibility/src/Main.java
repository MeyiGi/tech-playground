public class Main {
    public static void main(String[] args) {
        Handler level1Handler = new Level1Handler();
        Handler level2Handler = new Level2Handler();
        Handler level3Handler = new Level3Handler();

        level1Handler.setNext(level2Handler);
        level2Handler.setNext(level3Handler);

        level1Handler.process_request("reset password");
        level1Handler.process_request("software issue");
        level1Handler.process_request("billing issue");
        level3Handler.process_request("fuck you bitch");
    }
}