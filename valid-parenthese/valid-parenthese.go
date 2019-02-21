package parenthese

func isValid(s string) bool {
	var stack []string
	paren_map := map[string]string{
		")": "(",
		"]": "[",
		"}": "{",
	}
	for i := range s {
		if _, ok := paren_map[string(s[i])]; !ok {
			stack = append(stack, string(s[i]))
		} else if stack == nil || paren_map[string(s[i])] != stack[len(stack)-1] {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}
	return true
}
