use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn postorder_traversal(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut ans: Vec<i32> = Vec::new();

        fn dfs(root: Option<Rc<RefCell<TreeNode>>>, ans: &mut Vec<i32>) {
            if let Some(node) = root {
                let node_borrow = node.borrow();
                
                dfs(node_borrow.left.clone(), ans);
                dfs(node_borrow.right.clone(), ans);

                ans.push(node_borrow.val);
            }
        }
        dfs(root, &mut ans);
        ans
    }
}