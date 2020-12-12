package communication;

public class Message {

    public String tree_print;
    public int player;
    public int id;
    public int new_node;
    public int challenge;
    public boolean win;
    public boolean checkeo;
    public boolean exit;

    public void setTree_print(String tree_print)
    {
        this.tree_print = tree_print;
    }

    public String getTree_print()
    {
        return this.tree_print;
    }
}
