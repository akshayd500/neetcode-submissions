class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_whites = blocks[:k].count('W')
        min_ops = current_whites
        for i in range(k, len(blocks)):
            if blocks[i] == 'W':
                current_whites += 1
            if blocks[i - k] == 'W':
                current_whites -= 1
                
            min_ops = min(min_ops, current_whites)
            
        return min_ops