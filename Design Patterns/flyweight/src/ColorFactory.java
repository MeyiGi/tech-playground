import java.util.HashMap;
import java.util.Map;

public class ColorFactory {
    private static final Map<String, Color> cache = new HashMap<>();

    public static Color getColor(String name) {
        if (!cache.containsKey(name)) {
            cache.put(name, new Color(name));
        }
        return cache.get(name);
    }
}
