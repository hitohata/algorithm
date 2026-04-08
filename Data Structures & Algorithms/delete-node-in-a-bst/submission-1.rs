// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//     pub val: i32,
//     pub left: Option<Rc<RefCell<TreeNode>>>,
//     pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//     #[inline]
//     pub fn new(val: i32) -> Self {
//         TreeNode {
//             val,
//             left: None,
//             right: None,
//         }
//     }
// }

use std::rc::Rc;
use std::cell::RefCell;

impl Solution {
    pub fn delete_node(root: Option<Rc<RefCell<TreeNode>>>, key: i32) -> Option<Rc<RefCell<TreeNode>>> {
        let Some(root) = root else {
            return None
        };

        let root = root.brrow_mut();

        if key < root.val {
            root.left = Self::delete_node(root.left, key);
        };
        if root.val < key {
            root.right = Self::delete_node(root.right, key);
        };

        if root.val == key {
            let min_node = find_min_node(root.right); 
            root.val = min_node.val;
            root.right = Self::delete_node(root.right, key);
        }
        return root
    }
}

fn find_min_node(root: Option<Rc<RefCell<TreeNode>>>) {
    let mut min_node = None;

    while min_node.is_some() && min_node.left.is_some() {
        min_node = min_node.left;
    } 
    return min_node
}