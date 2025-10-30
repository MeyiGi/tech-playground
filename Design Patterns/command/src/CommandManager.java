import java.util.Stack;

// invoker
public class CommandManager {
    private Stack<Command> undoCommands = new Stack<>();
    private Stack<Command> redoCommand = new Stack<>();

    public void executeCommand(Command command) {
        undoCommands.add(command);
        command.execute();
        redoCommand.clear();
    }

    public void undo() {
        if (!undoCommands.isEmpty()) {
            Command command = undoCommands.pop();
            command.undo();
            redoCommand.add(command);
        }
    }

    public void redo() {
        if (!redoCommand.isEmpty()) {
            Command command = redoCommand.pop();
            command.execute();
            undoCommands.add(command);
        }
    }
}
