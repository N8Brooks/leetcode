pub mod tree_node {
    use std::{cell::RefCell, rc::Rc};

    #[derive(Debug, PartialEq, Eq)]
    pub struct TreeNode {
        pub val: i32,
        pub left: Option<Rc<RefCell<TreeNode>>>,
        pub right: Option<Rc<RefCell<TreeNode>>>,
    }

    impl TreeNode {
        #[inline]
        pub fn new(val: i32) -> Self {
            TreeNode {
                val,
                left: None,
                right: None,
            }
        }

        pub fn from_vec(vec: &[Option<i32>]) -> Option<Rc<RefCell<TreeNode>>> {
            let mut vec = vec.iter().map(|x| x.map(TreeNode::new));
            let root = match vec.next() {
                Some(Some(root)) => Rc::new(RefCell::new(root)),
                _ => return None,
            };
            let mut queue = std::collections::VecDeque::new();
            queue.push_back(Rc::clone(&root));
            while let Some(node) = queue.pop_front() {
                if let Some(Some(left)) = vec.next() {
                    let left = Rc::new(RefCell::new(left));
                    node.borrow_mut().left = Some(Rc::clone(&left));
                    queue.push_back(Rc::clone(&left));
                }
                if let Some(Some(right)) = vec.next() {
                    let right = Rc::new(RefCell::new(right));
                    node.borrow_mut().right = Some(Rc::clone(&right));
                    queue.push_back(Rc::clone(&right));
                }
            }
            Some(root)
        }
    }
}
