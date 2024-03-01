use std::{cell::RefCell, iter::successors, rc::Rc};

use crate::definitions::tree_node::TreeNode;

pub fn find_bottom_left_value(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
    let top_row = vec![root.unwrap()];
    let bottom_row = successors(Some(top_row), |row| {
        let next_row = row
            .iter()
            .map(|node| node.borrow())
            .flat_map(|node| [node.left.clone(), node.right.clone()])
            .flatten()
            .collect::<Vec<_>>();
        if next_row.is_empty() {
            None
        } else {
            Some(next_row)
        }
    })
    .last()
    .unwrap();
    let bottom_left = bottom_row[0].borrow();
    bottom_left.val
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        let input = TreeNode::from_vec(&[Some(2), Some(1), Some(3)]);
        let output = 1;
        assert_eq!(find_bottom_left_value(input), output);
    }

    #[test]
    fn test_2() {
        let input = TreeNode::from_vec(&[
            Some(1),
            Some(2),
            Some(3),
            Some(4),
            None,
            Some(5),
            Some(6),
            None,
            None,
            Some(7),
        ]);
        let output = 7;
        assert_eq!(find_bottom_left_value(input), output);
    }
}
