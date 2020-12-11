package communication;

import java.util.logging.Level;
import java.util.logging.Logger;
import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;

public class Jason {

    private final static Logger logger = Logger.getLogger( Logger.GLOBAL_LOGGER_NAME );
    private static ObjectMapper objectMapper = new ObjectMapper();

    /**
     * It converts a communication.Message Object into a String to send it as a message.
     *
     * @param message
     * @return message_string
     */
    public static String objectToString(Message message){
        String message_string = null;
        try {
            message_string = objectMapper.writeValueAsString(message);
        }
        catch (JsonProcessingException e){
            logger.log(Level.SEVERE, "Error converting communication.Message object to string");
        }
        return message_string;
    }

    /**
     * It converts a received message string into a communication.Message object.
     *
     * @param message_string
     * @return message
     */
    public static Message stringToObject(String message_string){
        Message message = null;
        try {
            JsonNode messageNode = objectMapper.readTree(message_string);
            message = objectMapper.treeToValue(messageNode, Message.class);
        }
        catch (JsonProcessingException e){
            logger.log(Level.SEVERE, "Error converting message to Card Object");
        }
        return message;
    }
}
