/*

 */

public class BinarySearchTree < T extends Comparable>
{
    private TreeNode overallRoot;

    // Constructs an empty binary tree
    public BinarySearchTree()
    {
        overallRoot = null;
    }

    // Constructs a binary tree with the given node as its root.
    public BinarySearchTree(TreeNode overallRoot)
    {
        this.overallRoot = overallRoot;
    }

    //returns the element with the largest value
    public T getMax()
    {
        return getMax(overallRoot);
    }
    private T getMax(TreeNode root)
    {
        if (root == null)
            return null;
        else if (root.right == null)
            return (T)root.data;
        else
            return getMax(root.right);
    }

    //returns the element with the smallest value
    public T getMin()
    {
        return getMin(overallRoot);
    }
    private T getMin(TreeNode root)
    {
        if (root == null)
            return null;
        else if (root.left == null)
            return (T)root.data;
        else
            return getMin(root.left);
    }

    // returns the depth of the tree
    public int getDepth()
    {
        return getDepth(overallRoot);
    }
    private int getDepth(TreeNode root)
    {
        int depth = 0;
        if (root != null)
        {
            depth = 1;
            depth += Math.max(getDepth(root.left), getDepth(root.right));
        }
        return depth;
    }

    // returns the number of leaves in the tree
    public int getNumLeaves()
    {
        return getNumLeaves(overallRoot);
    }
    private int getNumLeaves(TreeNode root)
    {
        int numLeaves = 0;
        if (root != null)
        {
            if (root.left == null && root.right == null)
                numLeaves++;
            else
            {
                if (root.left != null)
                    numLeaves += getNumLeaves(root.left);
                if (root.right != null)
                    numLeaves += getNumLeaves(root.right);
            }
        }
        return numLeaves;
    }

    // returns a String of the elements “inOrder”
    public String toString()
    {
        return toString(overallRoot);
    }
    public String toString(TreeNode root)
    {
        StringBuffer s = new StringBuffer();
        if (root != null) {
            s.append(toString(root.left));	// append my left sub-tree
            s.append(root.data + " ");	        // append myself
            s.append(toString(root.right));	// append my right sub-tree
        }
        return s.toString();
    }

    // prints tree sideways
    public void printSideways()
    {
        printSideways(overallRoot, 0);
    }
    public void printSideways(TreeNode root, int indent)
    {
        if (root != null)
        {
            String indentS = "";
            for (int i = 0; i < indent; i++)
                indentS += "    ";
            indent++;
            printSideways(root.right, indent);
            System.out.println(indentS + "(" + root.data + ")");
            printSideways(root.left, indent);
        }
    }

    // Prints all elements of this tree in left to right order.
    public void print()
    {
        print(overallRoot);
        System.out.println();
    }

    // Prints a portion of the overall tree
    private void print(TreeNode root)
    {
        // implicit base case: if null, do nothing
        if (root != null)
        {
            print(root.left);			// print my left sub-tree
            System.out.print(root.data + " ");	// print myself
            print(root.right);			// print my right sub-tree
        }
    }

    // Returns true if the overall tree contains the given target value,
    // false otherwise
    public boolean contains(T target)
    {
        return contains(overallRoot, target);
    }

    // Returns true if a portion of the overall tree contains the given
    // target value, false otherwise.
    private boolean contains(TreeNode root, T target)
    {
        if (root == null)
            return false;
        else if (root.data == target)
            return true;
        else if (target.compareTo(root.data) < 0)
            return contains(root.left, target);
        else
            return contains(root.right, target);
    }

    // Adds the value to the tree such that sorted BST order is maintained
    public void add(T value)
    {
        overallRoot = add(overallRoot, value);
    }

    // Adds the value to the given subtree.  Does not add duplicates.
    // A node's initial state is passed in and its modified
    // state is returned.  This is the x = change(x) pattern and
    // it allows attaching new nodes to the tree.
    private TreeNode add(TreeNode root, T value)
    {
        if (root == null)
            root = new TreeNode(value);
        else if (value.compareTo(root.data) < 0)
            root.left = add(root.left, value);
        else if (value.compareTo(root.data) > 0)
            root.right = add(root.right, value);
        return root;
    }
} // end BinarySearchTree