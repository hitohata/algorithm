impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = vec![];

        for b in s.chars() {
            if b == '(' || b == '{' || b == '[' {
                stack.push(b);
                continue
            };
            
            if let Some(last) = stack.pop() {
                if last == '(' && b == ')' || last == '{' && b == '}' || last == '[' && b == ']' {
                    continue
                }
            }

            return false
        }

        return stack.len() == 0
    }
}